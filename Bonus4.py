import csv
import pandas as pd
# from collections import OrderedDict
# import operator

filename = 'Countries.csv'
choice = input("How would you like to sort? :")
df1 = pd.read_csv(filename, header=0)
df2 = df1.sort_values(by=[choice], ascending=True)
df2.to_csv('my_new_csv.csv')
print(df2)

with open('my_new_csv.csv') as csvfile:
    readfile = csv.reader(csvfile)
    for row in readfile:
        print(row)
