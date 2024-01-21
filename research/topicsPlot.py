import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd


#read data 
topics_df = pd.read_csv("../myData/topicsData.csv")
print(topics_df)

#plot data using sn
sn.set_style("darkgrid")
sn.barplot(x="Year", y="Sexeducation", data=topics_df )
plt.show()