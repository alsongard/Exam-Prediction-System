import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

#read data from csv file
data_df = pd.read_csv("./myData/topicsData.csv")
print(data_df)
print(type(data_df))


#accessing column data_df through dot notation or column value
print(data_df.Sexeducation)
print(data_df.Sexeducation.max())

year = list(range(2000,2009))
#use plt.bar() to plot data
plt.bar(year, Sexeducation, data=data_df)
plt.title = "pattern of the exam."
plt.show()

#
