import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

from analyze import *

distinct_titles = query_db("SELECT DISTINCT normTitle FROM jobs")
test_vals = query_db(f"SELECT estimatedSalary from jobs limit 500000")
print(test_vals.mean())
print(test_vals.std())
random_sals = np.random.normal(test_vals.mean(), test_vals.std(), 500000)


def classify(title, salary):
    matches = test_data
    matches = matches[matches["normTitle"] == title]
    matches = matches[(matches["estimatedSalary"] >= (salary - 50000)) & (matches["estimatedSalary"] <= (salary + 50000))]
    match = matches[matches["clicks"] == matches["clicks"].max()]
    print(match)
    sys.stdout.flush()
    return match


match_list = pd.DataFrame()
test_data = random_n(1000000)

for sal in random_sals:
    match_list.append(classify(distinct_titles.sample(n=1), sal))
    print(sal)
    sys.stdout.flush()

print(match_list.head())
print(match_list.tail())
