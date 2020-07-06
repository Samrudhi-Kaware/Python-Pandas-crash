# import the pandas package
import pandas as pd
import numpy as np

# Series
# - one dimensional array

def function1():
    # list
    l1 = [10, 20, 30, 40, 50]
    print(f"l1 = {l1}, type = {type(l1)}")

    # array
    a1 = np.array([10, 20, 30, 40, 50])
    print(f"a1 = {a1}, type = {type(a1)}")

    # series
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(f"s1 = {s1}, type = {type(s1)}")


# function1()


def function2():
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(f"s1 = {s1}, type = {type(s1)}")
    print(f"dtype = {s1.dtype}")
    print(f"ndim = {s1.ndim}")
    print(f"shape = {s1.shape}")
    # ----
    print(f"index = {s1.index}")
    print(f"values = {s1.values}")

    print("-" * 40)

    s2 = pd.Series(['india', 'usa', 'uk', 'japan'])
    print(s2)
    print(f"dtype = {s2.dtype}")
    print(f"ndim = {s2.ndim}")
    print(f"shape = {s2.shape}")
    # ----
    print(f"index = {s2.index}")
    print(f"values = {s2.values}")


# function2()


def function3():
    countries = np.array(['india', 'usa', 'uk', 'japan', 'australia'])
    population = np.array([130, 100, 80, 50, 70])

    # for index in range(len(countries)):
    #     print(f"{countries[index]} has population {population[index]}")

    countries_series_1 = pd.Series(countries)
    print(countries_series_1)
    print(f"values = {countries_series_1.values}")
    print(f"index = {countries_series_1.index}")
    print(f"value at 0 = {countries_series_1[0]}")
    print(f"value at 4 = {countries_series_1[4]}")

    print("-" * 40)

    countries_series_2 = pd.Series(countries, index=population)
    print(countries_series_2)
    print(f"values = {countries_series_2.values}")
    print(f"index = {countries_series_2.index}")
    print(f"value at 130 = {countries_series_2[130]}")
    print(f"value at 70 = {countries_series_2[70]}")
    print("-" * 40)

    countries_series_3 = pd.Series(population, index=countries)
    print(countries_series_3)
    print(f"values = {countries_series_3.values}")
    print(f"index = {countries_series_3.index}")
    print(f"value at india = {countries_series_3['india']}")
    print(f"value at australia = {countries_series_3['australia']}")
    print("-" * 40)
function3()
def function4():
    # dictionary
    employee = {"name": "Douglas", "Gender": "Male", "Salary": 97303, "Team": "Marketing"}
    # series
    s1 = pd.Series(employee)
    print(s1)
    print(f"name = {s1['name']}")
function4()