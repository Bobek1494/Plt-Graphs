import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a = input("Which graph do you want? Linegraph,Bargraph,Histogram,Scatter")
a=a.lower()
df = pd.read_csv("database.csv")
plt.figure(figsize=(10,10))
if a == "bar":
    plt.bar(df["Date"],df["Sales"],color="b")
    plt.title("Sales Graph")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.show()
elif a == "linegraph":
    plt.plot(df["Date"],df["Sales"],color="b",linewidth="2",marker="o")
    plt.title("Sales Graph")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.show()
elif a=="hist":
    plt.hist(df["Sales"],bins=5,color="blue",edgecolor="black")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.show()
elif a =="scatter":
    plt.scatter(df["Date"],df["Sales"],color="b")
    plt.title("Sales Graph")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Wrong graph type")