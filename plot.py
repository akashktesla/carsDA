import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
from mpl_toolkits import mplot3d

class car:
    def __init__(self,name,ts,mvsold,avsold,leprice,heprice,mwp,tdv):
        self.name = name
        self.totalsales = ts
        self.leprice = leprice 
        self.heprice = heprice
        self.mvsold = mvsold
        self.avsold = avsold
        self.mwp = mwp
        self.tdv = tdv


def plot1(cars):
    #sorting based on total sales
    plot1_cars = sorted(cars, key=lambda x: x.totalsales)
    print(f'plot1_cars: {plot1_cars}')
    x = [var.name for var in plot1_cars ]
    y = [var.totalsales for var in plot1_cars ]
    plt.xlabel("car model")
    plt.ylabel("cars sold in a year")
    plt.title("yearly car sales for each model")
    plt.bar(x,y)
    plt.show()

#plot 2
def plot2(aki):
    x = ["Aug-22","Jul-22","Jun-22","May-22","Apr-22","Mar-22","Feb-22","Jan-22","Dec-21","Nov-21","Oct-21","Sep-21"]
    # print(aki.iloc[12,1])
    y = []
    for i in range(1,len(x)+1):
        y.append(aki.iloc[12,i])

    plt.xlabel("Months")
    plt.ylabel("Number of cars sold")
    plt.title("Monthly cars sales")
    x.reverse()
    y.reverse()
    plt.plot(x,y,"g*-")
    plt.show()

def plot3(cars):
    x = [var.name for var in cars ]
    y1 = [var.mvsold for var in cars ]
    y2 = [var.avsold for var in cars ]
    plt.xlabel("car model")
    plt.ylabel("cars sold")
    plt.title("sales of manual variants VS automatic variant")
    plt.plot(x,y1,"*-",label = "manual variant")
    plt.plot(x,y2,"*-",label = "automatic variant")
    plt.legend()
    plt.show()

def plot4(cars):
    x = [var.name for var in cars ]
    y1 = [var.leprice for var in cars ]
    y2 = [var.heprice for var in cars ]
    plt.xlabel("Car model")
    plt.ylabel("Price(lakhs)")
    plt.title("Price of low-end vs high-end variant")
    plt.plot(x,y1,"*-",label = "low-end variant")
    plt.plot(x,y2,"*-",label = "high-end variant")
    plt.legend()
    plt.show()

def plot5(cars):
    x = [var.name for var in cars]
    y = [var.totalsales for var in cars]
    plt.pie(y,labels = x)
    plt.title("yearly sales variation amoung models")
    plt.show()
    

def plot6(cars):
    x = [var.name for var in cars]
    plot1_cars = sorted(cars, key=lambda x: x.mwp)
    y = [var.mwp for var in plot1_cars ]
    plt.bar(x,y)
    plt.title("maximum waiting period for each model")
    plt.yticks(range(0,100,10))
    plt.ylabel("maximum waiting period(days)")
    plt.xlabel("car models")
    plt.show()

def plot7(cars):
    ax = plt.axes(projection = "3d")
    x1 = [var.name for var in cars]
    # print(x) 
    # plt.xticks(x)
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [var.tdv for var in cars]
    xpos = [1,2,3,4,5,6,7,8,9,10] 
    ypos = [2,4,6,8,10,12,14,16,18,20] 
    ypos = [3,24,5,2,34,4,2,1,4,3]
    zpos = np.zeros(10)
    # zpos = [1,2,3,4,5,6,7,8,9,10]
    plt.title("availability of number of test drive vechicles VS annual sales for each model")
    plt.yticks([2,1,0])
    plt.xticks([1,2,3,4,5,6,7,8,9,10])

    xsize = np.ones(10)*0.6
    ysize = np.ones(10)*0.6
    zsize = [var.totalsales for var in cars]
    print(f'totalsales: {zsize}')
    # zsize = [124,132,234,3,34,43,3,21,234,23]
    # zsize = [10,9,8,7,6,5,4,3,2,1]
    # zsize = np.ones(10)
    ax.bar3d(x,y,zpos,xsize,ysize,zsize,color = "#E02050")
    ax.set_xticklabels(x1)

    plt.show()




def main():
    aki = pd.read_excel("data.xlsx")
    _len = len(aki)
    cars = []
    for i in range(1,_len-2):
        name = aki.iloc[i,0]
        ts = aki.iloc[i,13]
        mvsold = aki.iloc[i,14]
        avsold = aki.iloc[i,15]
        leprice = aki.iloc[i,16]
        heprice = aki.iloc[i,18]
        mwp = aki.iloc[i,20]
        tdv = aki.iloc[i,21]
        cars.append(car(name,ts,mvsold,avsold,leprice,heprice,mwp,tdv))
    # plot1(cars)
    # plot2(aki)
    # plot3(cars)
    # plot4(cars)
    # plot5(cars)
    # plot6(cars)
    plot7(cars)

main()
