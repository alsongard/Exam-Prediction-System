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

#trying on pie chart for 3 topics
sexCounts = topics_df.Sexeducation.sum()
plantCounts = topics_df.Plants.sum()
DigestiveSystemCounts = topics_df.DigestiveSystem.sum()
BreathingSystemCounts = topics_df.BreathingSystem.sum()
DiseasesCounts = topics_df.Diseases.sum()
explodes = (0.02,0.02,0.02,0.02,0.02)
data = [sexCounts, plantCounts, DigestiveSystemCounts, BreathingSystemCounts, DiseasesCounts]
print(f"the length is {len(data)}")
print(f"sexCounts : {sexCounts} and plantCounts : {plantCounts}")
plt.pie(data,labels=["sex","plant","digestive system", "breathing system", "diseases"], startangle=90, colors=["red","green","black","yellow","purple"],explode=explodes, autopct="%1.1f%%")
plt.title("Exam Prediction")
plt.show()

#plot together with bars
x1 = [i - 0.2 for i in range(len(topics_df.Year))]
x2 = [i + 0.2 for i in range(len(topics_df.Year))]
plt.bar(x1, topics_df.Sexeducation, width=0.4, color="black")
plt.bar(x2, topics_df.Plants, width=0.4, color="blue")
plt.legend(["sexEducation","plants"])
plt.title("Exam Prediction")
plt.show()
print(x1)
print(x2)






# years = []
# years = topics_df.Year
# print(years)
# print("\n")
# print(topics_df.Sexeducation)
# # sn.barplot(data=topics_df, x=topics_df.Year, y=topics_df.Sexeducation, color="blue",width=0.7)
# plt.bar(topics_df.Year, topics_df.Sexeducation, color="blue", width=0.4)
# # plt.xticks(topics_df.Year)
# plt.gca().set_xticks(topics_df.Year)
# plt.show()

