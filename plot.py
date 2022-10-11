import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  

class car:
    def __init__(self,name,ts,mvsold,avsold,leprice,heprice):
        self.name = name
        self.totalsales = ts
        self.leprice = leprice 
        self.heprice = heprice
        self.mvsold = mvsold
        self.avsold = avsold


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
        cars.append(car(name,ts,mvsold,avsold,leprice,heprice))
    # plot1(cars)
    # plot2(aki)
    # plot3(cars)
    plot4(cars)

main()
