# 6 Pandas explore

## Slide 1
- Pandas Explore

- 2025-2026

## Slide 2
- Pandas explore

- Adding 1 row to DataFrame
- Combining datasets
- Reformat data
- Overview in graphs
- Boxplots, skewing and distributions

- 2

## Slide 3
- Data exploration

- We’ve done data import and data selection in pandas in the previous chapter.
- Those were the tools, in this chapter we’re talking about how to use these tools when confronted with a new dataset.
- And just a warning: in the course “Data visualisation” you will learn which graphs are appropriate in which case
- E.g. You can only use a line graph when plotting continuous variables
- We’ll try not to break those rules, but we may stray from the correct path

- 3

## Slide 4
- Adding 1 row to DataFrame

- Using “.concat”

- 4

- #Example DataFrame
- data = {"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
- "Age": [25, 30, 35, 40, 45]}
- df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])
- print(df)
- # new row to add
- new_row = {"Name": "Frank", "Age": 50}
- # adding the new row
- df = pd.concat([df, pd.DataFrame([new_row], index=['f'])])
- print("\nDataFrame after adding new row:")
- print(df)

## Slide 5
- Adding 1 row to DataFrame

- Using .loc
- new label  new entry
- existing label  overwrite entry

- 5

- #alternative method using loc
- df.loc['g'] = {"Name": "Grace", "Age": 55}
- print("\nDataFrame after adding new row using loc:")
- print(df)
- # alternative method using loc with existing index
- df.loc['f'] = {"Name": "Hank", "Age": 60}
- print("\nDataFrame after adding new row using existing index loc:")
- print(df)

## Slide 6
- Adding 1 row to DataFrame

- Using iloc throws error  only works with existing rows

- 6

- #adding a new row using iloc will raise an IndexError
- df.iloc[7] = {"Name": "Ivy", "Age": 65}

- #using an existing index will overwrite the row
- df.iloc[3] = {"Name": "Ivy", "Age": 65}

## Slide 7
- Combining multiple datasets

- Real-world data often comes in multiple pieces. You need to know how to grab those pieces and combine them into one dataset and make it ready for analysis.
- What the pieces are (pandas Series or DataFrames) may differ
- We start with 2 Series:				to create 1 DataFrame:

- 7

- city_2022_population

- city_rank

- city_data

## Slide 8
- Combining multiple datasets

- Next up is combining 2 DataFrames with identical columns
- In this example we concatenate 2 DataFrames into a new one

- 8

- city_data

- further_city_data

- all_city_data

## Slide 9
- Combining multiple datasets

- What happens when they share a key, but have different columns?

- 9

- All rows are kept.NaN appears when no data available

- all_city_data

- city_countries

- cities

## Slide 10
- Combining multiple datasets

- We can prevent the Na’s by using datasets with combinable data (~key)

- 10

- all_city_data

- capital_countries

- capitals

## Slide 11
- Merge

- Merging means that you combine two datasets that don’t share a key column
- You choose a column in one DataFrame to link with the key of the other DataFrame

- 11

- cities

- countries

## Slide 12
- Merge syntax

- In the example:
- DataFrame countries contains the index
- DataFrame cities contains a column ‘country’
- Begin by selecting both DataFrames. The order is important!
- With “left_index” or “right_index” you decide which of the 2 DataFrames contains the index
- pd.merge (countries, cities)  left_index = True
- pd.merge (cities, countries)  right_index = True
- With “left_on” or “right_on” you decide with which column in the other DataFrame (right of left) the index column must merge
- pd.merge (countries, cities, left_index = True)  right_on = country’
- pd.merge (cities, countries, right_index = True)  left_on = ‘country’

- 12

## Slide 13
- Merge example

- 13

- cities

- countries

- Notice how “Belgium” is not retained as it doesn’t have a corresponding row in cities
- Same for Algiers, Kabul, … they don’t exist in countries

## Slide 14
- Merge as inner join

- Do watch out: we merged two DataFrames with 4 and 10 rows, and got a 4 row DataFrame as result!
- This is because we inner joined. You’ll lose rows that don’t have a match in the other DataFrame’s key column.
- Also note: all columns were kept, even those that now only contain NaN-values.

- 14

## Slide 15
- Merge left and right

- By default, merge() always performs an inner join.
- However, by using the attribute ‘how’ you can indicate the  type of join you want to perform

- 15

## Slide 16
- Reformat data

- Data isn’t always nice and rectangular
- Or it is, but it’s the wrong type of rectangle
- Or in two rectangles (aka files) that need to be combined
- You can reformat your data into the form you need
- Another example of reshaping is a pivot table
- Pivoting allows you to summarize your data based on certain properties
- Helps a lot to get a quick overview of what is going on

- 16

## Slide 17
- DataFrame reshaping

- melt():
- make wide data long
- pivot():
- make long data wide
- pivot_table():
- same as .pivot() but can handle multiple indexes
- crosstab()

- 17

- https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter8-wrangling-basics.html

## Slide 18
- Melt

- 18

- https://pandas.pydata.org/docs/_images/reshaping_melt.png

- Used to collapse a DataFrame so that every column becomes a new row
- There are some id_vars, they will be copied
- The names of the columns are kept as values

## Slide 19
- Melt example

- 19

## Slide 20
- Melt, other example

- Suppose you were given the following DataFrame
- Can you (easily) calculate the average score for every student?
- No, because they are in different columns
- df["avg"] = (df["Math"] + df["English"] + df["Science"]) / 3
-  Not maintainable code!

- 20

## Slide 21
- Melt, other example

- Solution: melt!
- The average per student can now be calculated using group by

- 21

## Slide 22
- Pivot

- 22

- Pivot is basically the opposite of melt
- It combines multiple rows and uses one of the values as column name and the other as value
- Watch out, other columns may be dropped in the process
- Like “zoo” in the example

## Slide 23
- The simple example would be to un-melt the DataFrame we made before

- Pivot example

- 23

## Slide 24
- Pivot usage

- A lot of numerical data is stored in SQL-databases
- SQL-databases are normalized, so that would look like this:
- It’s impossible to write a SQL-query where the rows of the table “Course” become the column names
- But when you want to use the grades of students to do machine learning, you need all the grades on one line
- Pivot!

- 24

## Slide 25
- Pivot and summarize

- Up until now we only used pivot to copy values
- The example: every combination of “Name” and “Year”was unique
- But pivot can also create summaries
- What is the average number of courses per student?
- What is the total number of courses per student?
- What is the standard deviation of the number of courses students took per year?
- That is when we start using a pivot table
- You have this in Excel as well

- 25

## Slide 26
- Pivot table

- 26

- https://www.lumeer.io/pivot-tables-cheatsheet/

- A Pivot table:
- is used to summarize, sort, reorganize, group, count, total or average data stored in a table.
- allows us to transform columns into rows and rows into columns.
- allows grouping by any field (column) and performing advanced calculations on them.

## Slide 27
- What we start with: Minimum and maximum temperatures for some cities
- The cities we have:
- ['Brussels', 'Amsterdam', 'London’, 'Berlin', 'Madrid', 'Sydney’]

- Pivot table: pivot()

- 27

- https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html

## Slide 28
- Pivot table: pivot()

- “Unfold” the table by using pivot()
- Cities vs months or the other way around

- 28

- The order of the months is wrong!

- We lose the maximum temperature!

- df_pivot = df.pivot(index="City",columns="Month",values="Minimum_temperature")

- df_pivot = df.pivot(index="Month",columns="City",values="Minimum_temperature")

## Slide 29
- Pivot table - revisited

- “Unfold” the table using pivot()
- Cities vs months or the other way around
- Months appear chronologically
- Average temperature in cells instead of min or max temperatures

- 29

- What did we do to arrange the months chronologically?

## Slide 30
- Pivot table with aggregations: pivot_table()

- What is the average (mean) temperature per city or per month?

- 30

- table = pd.pivot_table(df, values='Average_temperature', index=['City'], aggfunc="mean")
- table = pd.pivot_table(df, values='Average_temperature', index=['Month'], aggfunc="mean")

## Slide 31
- Pivot table with aggregations: pivot_table()

- What are the average minimum and maximum temperatures per city?

- 31

- table = pd.pivot_table(df, values=['Minimum_temperature','Maximum_temperature’],    	index=['City'], aggfunc={'Minimum_temperature’:["mean"], 	'Maximum_temperature':["mean"]})

## Slide 32
- Pivot table with aggregations: pivot_table()

- Could we add the sum for the minimum temperatures and the standard deviation for the maximum temperatures?

- 32

- table = pd.pivot_table(df, values=['Minimum_temperature','Maximum_temperature’], 	index=['City'], aggfunc={'Minimum_temperature': ["mean","sum"], 	'Maximum_temperature':["mean","std"]})

## Slide 33
- Crosstabulation

- Look at the data on the right
- We see some numbers (units and sales), but a lot of categorical data (date, region and type)
- What possible questions on grouped data might there be:
- More children’s clothing sold in the East?
- More women’s clothing sold in April?
- Low sales in the South in winter months?
- Cross tabulation will help us investigate this

- 33

## Slide 34
- Crosstab: region vs type

- pd.crosstab(df.Region, df.Type)

- 34

- By default, in each cell the number of records in the DataFrame per region and type are shown
- So, in each region the most sales registrations are for women’s clothing.

## Slide 35
- Crosstab: region vs type

- This is the same crosstab as on the previous slide, but now we’re displayingthe mean of sales revenue
- So now we know that:
- In women’s clothing we have the lowest sales revenue. When women buy something, they buy less items or less expensive items. (From before we knew they made more sales though, so they might just like to go shopping.)
- Sales revenues are smaller in the East

- 35

- pd.crosstab(index = df_pivot.Region, columns = df_pivot.Type, 		values = df_pivot.Sales, aggfunc = 'mean')

## Slide 36
- An overview in graphs

- As people we like our numbers in graphs
- Unless you’re him:
- When doing data science, which implies you have no or limited domain knowledge, you explore the data by making graphs
- These graphs raise questions, that spark more graphs
- Repeat until you understand the data

- 36

## Slide 37
- The pie chart

- Pie charts are great. They not only have many colors, but they also remind us it’s time for a break. We need more pie!
- But seriously, don’t use pie charts unless you respect the rules:
- Max 6 slices
- In descending order
- Percentages printed

- 37

## Slide 38
- Scatter plot

- Scatter plot:
- Data visualisation technique to show the relationship  between two numerical variables.
- DataFrame.plot.scatter(x, y, s = none, c = none)
- x: column name to be used as horizontal coordinates for each point
- y: column name to be used as vertical coordinates for each point
- s: size of dots
- c: color of dots
- BTW, we’re using the cars dataset ‘MPG’ here
- The MPG dataset contains 234 cars and their mileage (~ chapter 5)
- https://ggplot2.tidyverse.org/reference/mpg.html

- 38

## Slide 39
- Scatter plot

- The easiest plot possible: plot highway miles per gallon vs engine displacement
- How far you can drive vs how big your engine is

- 39

## Slide 40
- Pandas vs matplotlib

- Pandas uses matplotlib under the hood, but you can use it separately
- You get the same graph, but the labels on the axes are gone

- 40

## Slide 41
- Scatter with factors

- Maybe the class of the car has an impact on this graph. Could we color the dots according to the class?

- 41

- Code also in notebook.

## Slide 42
- A trendline: ax+b

- We’ve seen the trend in the data (bigger engines are less economical), but can we show it?

- 42

## Slide 43
- A trendline: ax²+bx+c

- Maybe the relationship is of the second order?

- 43

## Slide 44
- Trendline

- The trendline shows there is a relationship between engine displacement and highway miles per gallons
- In statistical terms, this is called a covariance
- It’s a number you can calculate by using some cool formula
- But it doesn’t mean anything, as it will greatly depend on the actual numbers
- Big number: between number of ants and number of blades of grass
- Small number: between number of kids and number of cars
- The strength of a covariance is expressed as the correlation
- Can also be calculated using another cool formula
- Is always between -1 and +1 -> can be compared

- 44

## Slide 45
- 45

- https://www.youtube.com/watch?v=mG__Wpp9dns&ab_channel=zedstatistics

## Slide 46
- The cool formulas

- 46

## Slide 47
- Correlation = measure of strength

- 47

## Slide 48
- Extremes of correlation

- 48

- Correlation = 1Perfect positive relationship

- Correlation = 0
- No pattern

- Correlation = -1
- Perfect negative relationship

## Slide 49
- Covariance does not imply causation

- 49

## Slide 50
- Correlation in DataFrames

- A scatter plot is a very useful plot to check if there is correlation between two variables in a dataset
- But which variables correlate well, and which don’t? You have 2 options:
- Check numerically: calculate correlation matrix
- Check visually: plot a scatter matrix

- 50

## Slide 51
- Correlation matrix

- 51

- Calculate the correlation between all columns
- Or all numerical columns, to be precise
- Gives you a number showing how much they are related
- 0:  No correlation
- 1:  One goes up, other goes up
- -1: One goes up, other goes down
- The closer the number is to +1/-1, the better the correlation

## Slide 52
- Scatter matrix

- 52

- The same as a correlation matrix, but instead of numbers you get a scatter plot
- Some plots stand out:
- cty vs hwy: near perfect correlation
- year vs …: Only 2 distinct values for year are present
- cyl: few distinct values, but some correlation with displ

## Slide 53
- Scatter matrix

- Did we see that correctly?
- cty vs hwy: near perfect correlation
- cty: Miles per gallon in the city
- hwy: Miles per gallon on the highway
- cyl: few distinct values, but some correlation with displ
- cyl: the number of cilinders
- displ: the size of the engine (in liters)
- So yes, what we saw in the graphs is also true in real life

- 53

## Slide 54
- Boxplots, skewing and distributions

- When investigating it’s important to recognize certain patterns in the distribution of data
- Fortunately, there’s a whole field of knowledge concerning itself with just that:
- And we’d like very much to prep you for a couple of weeks in just the theoretical background of analysis of distributions, correlations, covariations, …
- But that would be a step too far...
- But what you do need to understand is the normal distribution

- 54

- Statistics!

## Slide 55
- Normal distribution

- Most data will have a “normal” distribution
- This means:
- A lot of datapoints in the center (red part)
- Some datapoints to the side (blue part)
- Leftovers left and right (green and ... part)
- Standard deviation is a measurefor the steepness of the curve

## Slide 56
- Normal distribution in boxplot

- A normal distribution is a plot of 1 variable, with varying standard deviation
- The smaller your stddev, the steeper the curve, the easier to predict
- The bigger your stddev, the flatter and widen the curve, the more spread your data, the more difficult to predict
- In case you want to compare 2 variables like prices of fiction vs prices of non-fiction books, you need a more compact way of showing a distribution
- Enter: The Boxplot

## Slide 57
- The yellow line: the median
- The box: the red part
- The lines: the blue part
- The dots: the green part
- IQR: Interquartile Range The difference between Q1 and Q3 which measures the spread of the middle 50% of the data.

## Slide 58
- Dataset skewing

- All data is ‘normal’, but some is more normal than others

## Slide 59
- skew()

- Skewness is a measure of the asymmetry of a distribution. A distribution is asymmetrical when its left and right side are not mirror images.
- Describes the distribution of a variable alongside other descriptive statistics
- Determines if a variable is normally distributed. A normal distribution has zero skew and is an assumption of many statistical procedures.

- 59

- https://www.scribbr.com/statistics/skewness/

## Slide 60
- Example: age of mother when giving birth

- Some mothers are only 15, but these are exceptions
- Most women give birth in their 20’s
- School is finished, found life-long partner, …
- There are still quite a few women giving birth in their 30’s
- Enjoyed life first, settled later
- Some exceptions are in their 40’s
- You’ll be 60 by the time the kid graduates, which is not ideal
- Conception becomes difficult after that age

- 60

## Slide 61
- More baby-examples

- 61

## Slide 62
- Negative skew or left skewed

- Distribution of Age of Deaths
- The distribution of the age of deaths in most populations is negatively skewed. Most people live to be between 70 and 80 years old, with fewer and fewer living less than this age.
- Distribution of Olympic Long Jumps
- In most years, the distribution of long jump lengths for competitors in the Olympics is negatively skewed because most competitors land a jump around 7.5-8 meters, with a few landing a jump of just 5-6 meters.
- Distribution of Scores on Easy Exams
- The distribution of scores on easy exams or tests tend to be negatively skewed because most students score very high, while a few students score much lower than the average.

## Slide 63
- Positive skew or right skewed

- Distribution of Income
- The distribution of individual incomes in the U.S. is right-skewed, with most individuals earning between $20k and $40k per year but with a long right tail of households that earn much more.
- Distribution of Pet Ownership
- The distribution of the number of pets that households own in any particular city is likely to be right skewed because most households have either 0 or 1 pet, but there are many outlier households that have 7, 8, 9+ pets that cause the distribution to be right skewed.
- Distribution of Scores on Difficult Exams
- The distribution of scores on any particularly difficult exam will be positively skewed with most students scoring around some mean value with a few outlier students scoring much higher.

## Slide 64
- Boxplot skewing

- How does a boxplot show skewing?
- The middle line is always the center of your data (median)
- If that is a perfect mirror-line, your data is perfectly symmetrical and perfectly normal
- But if the box is smaller on one side of the line, the data is “steeper” there
- Less different values, but they occur more
- Usually, a small box on one side also means a shorter line

## Slide 65
- Basic boxplot

- Compare the distribution of 4 categories
- 1 variable
- In 4 categories
- You see how
- A is very spread out (unsteep bell curve)
- D is very compact (pointy bell curve)
- All are pretty ‘normal’ or symmetrical distributed

## Slide 66
- Advanced boxplot

- You see all the above and:
- C doesn’t have a lot of datapoints
- B has two peaks

## Slide 67
- Violin plot

- Comparable to a boxplot, but the numbers are no longer there
- Prettier, but not always better
- Because it doesn’t compare: are there more A’s than D’s? Or C’s? How much steeper is A’s curve compared to C?
- You can use a violin-plot to raise questions, but rarely to answer them
- Example: is there a property in the B-dataset that splits the two bumps?

## Slide 68
- Once again: Mean (average), standard deviation

- 68

## Slide 69
- Mean (average), standard deviation

- 69

- https://www.youtube.com/watch?v=wpY9o_OyxoQ&ab_channel=zedstatistics

## Slide 70
- Mean (average), standard deviation

- 70

- https://www.youtube.com/watch?v=wpY9o_OyxoQ&ab_channel=zedstatistics

## Slide 71
- Mean (average), standard deviation

- Why square stuff for calculating variance and standard deviation?

- 71

- From learning that s = 9.18, you can say that on average, each score deviates from the mean by 9.18 points.

## Slide 72
- Back to the babies

- On the right are 2 graphs: the weight of a baby at birth and the duration of the pregnancy (gestation)
- To be comparable they were normalised
- Recalculated to be between 0 and 1 in stead of 150 and 350 or 52 and 72
- [For more information on normalisation see chapter 4]
- The top graph is wider, the bottom one slimmer
- Top standard deviation: 0.13
- Bottom standard deviation: 0.08

- 72

## Slide 73
- Distributions in mpg

- Before we go into deep analysis, let’s start practically:
- Create a simple plot of the distribution for highway miles per gallons in the MPG-dataset
- It’s a continuous variable, so we can’t count it
- Solution: binning
- Take some of the values together
- Which? Size of the bin
- In this case: let pandas decide on the bin size

- 73

## Slide 74
- Binning

- Maybe more bins? Or less bins?
- Depends on the data…

- 74

## Slide 75
- Truly normal data

- Mpg doesn’t have truly normal data(doesn’t have enough records)
- But we can generate it!

- 75

## Slide 76
- Comparing histograms

- The entire hwy-column isn’t normal, but maybe when we divide it by class of car?
- Can we show all histograms inone graph?
- Sure!
- But it looks really bad…

- 76

## Slide 77
- All hail the boxplot

- Boxplots will fix that mess quickly
- Remember: boxplots simplify data. Sometimes that is bad, but mostly it helps making data understandable and comparable.
- The graph shown here is clear and tells a story. That is what we need.

- 77

## Slide 78
- Violins are nice too

- They look better but contain way more information making them harder to understand.
- Violins are good to raise questions (why is purple such an ugly blob?) but never to answer them.

- 78

## Slide 79
- Exercises

- 79
