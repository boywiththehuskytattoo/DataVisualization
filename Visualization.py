import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np
import squarify

# Line chart showing the number of Marriages and Divorces per capita in the US between 1867 - 2014

us_marriage_divorce = pd.read_csv('us-marriages-divorces-1867-2014.csv')
year = us_marriage_divorce["Year"].values
marriage = us_marriage_divorce["Marriages_per_1000"].values
divorces = us_marriage_divorce["Divorces_per_1000"].values

sns.lineplot(year, marriage, label="Marriages")
sns.lineplot(year, divorces, label="Divorces")
plt.xlabel("Year")
plt.ylabel("Value per 1000")
plt.title("US Marriages and Divorces between 1867 - 2014")
plt.legend()
plt.show()
plt.gcf().clear()

# Vertical Bar chart showing the number of Marriages and Divorces per capita in the US in 1900, 1950 and 2000
df_us_marriage_divorce = DataFrame(us_marriage_divorce)
df_us_marriage_divorce = df_us_marriage_divorce.loc[df_us_marriage_divorce["Year"].isin([1900, 1950, 2000])]
df_year = df_us_marriage_divorce["Year"].values
df_marriages = df_us_marriage_divorce["Marriages_per_1000"].values
df_divorces = df_us_marriage_divorce["Divorces_per_1000"].values

barWidth = 0.25
r1 = np.arange(len(df_marriages))
r2 = [x + barWidth for x in r1]

plt.bar(r1, df_marriages, label="Marriages", width=barWidth)
plt.bar(r2, df_divorces, label="Divorces", width=barWidth)
plt.xticks([r + barWidth / 2 for r in range(len(df_marriages))], df_year)
plt.xlabel("Year")
plt.ylabel("Value per 1000")
plt.title("US Marriages and Divorces in 1900, 1950 and 2000")
plt.legend()
plt.show()
plt.gcf().clear()

# Horizontal bar chart showing the deadliest Hollywood actors by their kill count
df_Actor_kills = DataFrame(pd.read_csv("actor_kill_counts.csv"))
sns.barplot(x="Count", y="Actor", data=df_Actor_kills)
plt.xlabel("Kill Count")
plt.ylabel("Actors")
plt.yticks(rotation=45)
plt.show()
plt.gcf().clear()

# Pie chart showing the fraction of all roman emperors who were assassinated
df_Roman = DataFrame(pd.read_csv("roman-emperor-reigns.csv"))
assassinated_emp = df_Roman.loc[df_Roman["Cause_of_Death"] == "Assassinated"]
assassinated_count = len(assassinated_emp)
other_deaths = len(df_Roman) - assassinated_count
death_counts = [assassinated_count, other_deaths]
plt.pie(death_counts, labels=["Assassinated", "Other deaths"], autopct='%1.0f%%')
plt.legend()
plt.show()
plt.gcf().clear()

# Scatter plot showing the relationship between total revenue earned by arcades and the # of Computer Science PhDs
# awarded in the US between 2000 and 2009

df_arcade_CS: DataFrame = DataFrame(pd.read_csv("arcade-revenue-vs-cs-doctorates.csv"))
df_arcade_revenue = df_arcade_CS["Total Arcade Revenue (billions)"]
df_arcade_CS_Awards = df_arcade_CS["Computer Science Doctorates Awarded (US)"]
df_arcade_CS_year = df_arcade_CS["Year"]
plt.scatter(df_arcade_revenue, df_arcade_CS_Awards, c=df_arcade_CS_year,)
plt.xlabel("Total Arcade Revenue (billions)")
plt.ylabel("Computer Science Doctorates Awarded (US)")
plt.show()
plt.gcf().clear()

# Histogram showing the distribution of reign lengths of the Roman emperors
roman_emp_length_of_reigns = df_Roman["Length_of_Reign"]
plt.hist(roman_emp_length_of_reigns, bins=5)
plt.show()
plt.gcf().clear()

# Box plot to compare the the earnings of recent college graduates
df_college_grads = DataFrame(pd.read_csv("recent-college-grads-earnings.csv"))
major_women = df_college_grads.loc[df_college_grads["ShareWomen"] > 0.5]['Median'].values
major_men = df_college_grads.loc[df_college_grads["ShareWomen"] < 0.5]['Median'].values
data = [major_women, major_men]
ax = plt.boxplot(data, notch=True, patch_artist=True, boxprops=dict(facecolor="C0"))
plt.xticks([1, 2], ['Women', 'Men'])
plt.title("Earnings of recent college grad (Women vs Men)")
plt.ylabel("Earnings")
plt.xlabel("Gender")
plt.show()
plt.gcf().clear()


# Sub plots
fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
sns.lineplot(year, marriage, label="Marriages", ax=ax1)
sns.lineplot(year, divorces, label="Divorces", ax=ax2)
ax1.set_title("US Marriages and Divorces between 1867 - 2014")
ax1.set_ylabel("Value per 1000")
ax2.set_ylabel("Value per 1000")
ax2.set_xlabel("Year")
plt.legend()
plt.show()
plt.gcf().clear()

# Multiple plots
degree_gender_ratio = pd.read_csv('percent-degrees-conferred-women-usa.csv')
years = degree_gender_ratio['Year'].values
fig = plt.figure(figsize=(24, 12))
ax = fig.add_subplot(111)
plt.style.use('seaborn-darkgrid')
palette = plt.get_cmap('Paired')
num = 0
colorNum = 0
for column in degree_gender_ratio.drop("Year", axis=1):
    num += 1
    colorNum += 1
    if colorNum > len(palette.colors):
        colorNum = 0
    plt.subplot(6, 3, num)
    plt.ylim([0, 100])
    data = degree_gender_ratio[column].values
    sns.lineplot(years, data, color=palette(colorNum))
    plt.title(column, fontsize=7)
plt.suptitle("Gender Ratio of 17 US College Majors \nbetween 1970-2011?", fontsize=12, fontweight=0, color='black',
             style='italic')

plt.xlabel('Years', ha='center', va='center')
plt.text(0.06, 0.5, 'Percentage', ha='center', va='center', rotation='vertical', transform=fig.transFigure)
plt.show()
plt.gcf().clear()

# Tree map of the Actors and their kills
cmap = matplotlib.cm.Reds
mini = min(df_Actor_kills["Count"])
maxi = max(df_Actor_kills["Count"])
norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in df_Actor_kills["Count"]]
squarify.plot(sizes=df_Actor_kills["Count"], label=df_Actor_kills["Actor"], color=colors, alpha=0.7)
plt.axis('off')
plt.show()
plt.gcf().clear()
