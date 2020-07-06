import pandas as pd
import numpy as np


def function1():
    employees = [
        {"name": "Douglas", "Gender": "Male", "Salary": 97303, "Team": "Marketing"},
        {"name": "Maria", "Gender": "Female", "Salary": 107303, "Team": "HR", "email": "maria@test.com"},
        {"name": "Jerry", "Gender": "Male", "Salary": 88303, "Team": "Development"}
    ]

    df = pd.DataFrame(employees)
    print(df)
    print(f"type of df = {type(df)}")


# function1()


def function2():
    # df = pd.read_csv('./customers.csv')
    # print(df)

    # df = pd.DataFrame([10, 20, 30, 40, 50])
    # print(df)

    df1 = pd.DataFrame([
        [10, 20, 30, 40, 50],
        [60, 70, 80, 90, 100]
    ])
    print(df1)

    print("-" * 40)

    df2 = pd.DataFrame([
        [10, 60],
        [20, 70],
        [30, 80],
        [40, 90],
        [50, 100]
    ])
    print(df2)


# function2()

#Exploratory Data Analysis (EDA)
def function3():
    df = pd.read_csv('I:/Python Sunbeam/exercise/ML/customers.csv')
    # print(df)
    #attributes
    # print(f"values = {df.values}, type = {type(df.values)}") #data values
    # print(f"dtypes = {df.dtypes}") #data types
    #print(f"columns = {df.columns}")#column heads
    #print(f"is empty = {df.empty}")#is data is empty
    #print(f"shape = {df.shape}")#check shape
    #print(f"ndim = {df.ndim}")#check diamension also can say series
    #print(f"index = {df.index}")#indexs


    #methods
    #print(df.head(10))
    #print(df.tail(10))
    #print(df.info()) #info of data
    #print("--"*40)
    #print(df.describe())#statistical data
#function3()