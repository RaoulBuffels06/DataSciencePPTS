# 5 Pandas introduction

## Slide 1
- Chapter 5 – Intro Pandas

- 2025-2026

## Slide 2
- Overview

- Introduction
- Data structures in pandas: Series and DataFrame
- Extracting and assigning data
- Reading/writing data (CSV, JSON and SQLite)
- Basic DataFrame operations
- Missing values
- Conditional selections, sorting, grouping & counting
- Cleaning a dataset (using an example)

- 2

## Slide 3
- The most popular Python library for data analysis
- Through pandas, you get acquainted with your data
- Pandas helps you
- calculate statistics and answer questions about the data, like
- What's the average, median, max, or min of each column?
- Does column A correlate to column B?
- What does the distribution of data in column C look like?
- clean the data by doing things like removing missing values and filtering rows or columns
- visualize the data with help from Matplotlib (plot bars, lines, histograms, bubbles, …)
- store the cleaned, transformed data back into a CSV, other file or database

- 3

- pandas is derived from the term “panel data” which are data sets that include observations over multiple time periods for the same individuals   [Wikipedia]

## Slide 4
- The pandas library is a central component of the data science toolkit, but it is used in conjunction with other libraries.
- Pandas is built on top of the NumPy package, meaning a lot of the structure of NumPy is used or replicated in pandas.
- Data in pandas is often used to feed statistical analysis in SciPy, plotting functions in Matplotlib and SeaBorn, and machine learning algorithms in Scikit-learn.

- 4

## Slide 5
- Install and import pandas

- Run the install command in a terminal window:
- pip install pandas
- In Jupyter you must use a preceding ! to force the code cell to be executed in a terminal window:  	!pip install pandas
- To import pandas we usually import it with a shorter name since it's used so much:	import pandas as pd

- 5

## Slide 6
- About dirty data

- 6

## Slide 7
- Same data, different formats

- 7

- country      year  cases population
- <chr>       <int>  <int>      <int>
- 1 Afghanistan  1999    745   19987071
- 2 Afghanistan  2000   2666   20595360
- 3 Brazil       1999  37737  172006362
- 4 Brazil       2000  80488  174504898
- 5 China        1999 212258 1272915272
- 6 China        2000 213766 1280428583

- country      year type            count
- <chr>       <int> <chr>           <int>
- 1 Afghanistan  1999 cases             745
- 2 Afghanistan  1999 population   19987071
- 3 Afghanistan  2000 cases            2666
- 4 Afghanistan  2000 population   20595360
- 5 Brazil       1999 cases           37737
- 6 Brazil       1999 population  172006362
- 7 Brazil       2000 cases           80488
- 8 Brazil       2000 population  174504898
- 9 China        1999 cases          212258
- 10 China        1999 population 1272915272
- 11 China        2000 cases          213766
- 12 China        2000 population 1280428583

- country      year rate
- * <chr>       <int> <chr>
- 1 Afghanistan  1999 745/19987071
- 2 Afghanistan  2000 2666/20595360
- 3 Brazil       1999 37737/172006362
- 4 Brazil       2000 80488/174504898
- 5 China        1999 212258/1272915272
- 6 China        2000 213766/1280428583

- country     `1999` `2000`
- * <chr>        <int>  <int>
- 1 Afghanistan    745   2666
- 2 Brazil       37737  80488
- 3 China       212258 213766

- country         `1999`     `2000`
- * <chr>            <int>      <int>
- 1 Afghanistan   19987071   20595360
- 2 Brazil       172006362  174504898
- 3 China       1272915272 1280428583

- 1

- 2

- 3

- 4

## Slide 8
- 3 rules for data files

- Each variable must have its own column.
- Each observation must have its own row.
- Each value must have its own cell.

- 8

## Slide 9
- Does each variable have its own column?

- 9

- country      year  cases population
- <chr>       <int>  <int>      <int>
- 1 Afghanistan  1999    745   19987071
- 2 Afghanistan  2000   2666   20595360
- 3 Brazil       1999  37737  172006362
- 4 Brazil       2000  80488  174504898
- 5 China        1999 212258 1272915272
- 6 China        2000 213766 1280428583

- country      year type            count
- <chr>       <int> <chr>           <int>
- 1 Afghanistan  1999 cases             745
- 2 Afghanistan  1999 population   19987071
- 3 Afghanistan  2000 cases            2666
- 4 Afghanistan  2000 population   20595360
- 5 Brazil       1999 cases           37737
- 6 Brazil       1999 population  172006362
- 7 Brazil       2000 cases           80488
- 8 Brazil       2000 population  174504898
- 9 China        1999 cases          212258
- 10 China        1999 population 1272915272
- 11 China        2000 cases          213766
- 12 China        2000 population 1280428583

- country      year rate
- * <chr>       <int> <chr>
- 1 Afghanistan  1999 745/19987071
- 2 Afghanistan  2000 2666/20595360
- 3 Brazil       1999 37737/172006362
- 4 Brazil       2000 80488/174504898
- 5 China        1999 212258/1272915272
- 6 China        2000 213766/1280428583

- country     `1999` `2000`
- * <chr>        <int>  <int>
- 1 Afghanistan    745   2666
- 2 Brazil       37737  80488
- 3 China       212258 213766

- country         `1999`     `2000`
- * <chr>            <int>      <int>
- 1 Afghanistan   19987071   20595360
- 2 Brazil       172006362  174504898
- 3 China       1272915272 1280428583

- 1

- 2

- 3

- 4

## Slide 10
- Each variable must have its own column

- 10

- country      year  cases population
- <chr>       <int>  <int>      <int>
- 1 Afghanistan  1999    745   19987071
- 2 Afghanistan  2000   2666   20595360
- 3 Brazil       1999  37737  172006362
- 4 Brazil       2000  80488  174504898
- 5 China        1999 212258 1272915272
- 6 China        2000 213766 1280428583

- country      year type            count
- <chr>       <int> <chr>           <int>
- 1 Afghanistan  1999 cases             745
- 2 Afghanistan  1999 population   19987071
- 3 Afghanistan  2000 cases            2666
- 4 Afghanistan  2000 population   20595360
- 5 Brazil       1999 cases           37737
- 6 Brazil       1999 population  172006362
- 7 Brazil       2000 cases           80488
- 8 Brazil       2000 population  174504898
- 9 China        1999 cases          212258
- 10 China        1999 population 1272915272
- 11 China        2000 cases          213766
- 12 China        2000 population 1280428583

- country      year rate
- * <chr>       <int> <chr>
- 1 Afghanistan  1999 745/19987071
- 2 Afghanistan  2000 2666/20595360
- 3 Brazil       1999 37737/172006362
- 4 Brazil       2000 80488/174504898
- 5 China        1999 212258/1272915272
- 6 China        2000 213766/1280428583

- country     `1999` `2000`
- * <chr>        <int>  <int>
- 1 Afghanistan    745   2666
- 2 Brazil       37737  80488
- 3 China       212258 213766

- country         `1999`     `2000`
- * <chr>            <int>      <int>
- 1 Afghanistan   19987071   20595360
- 2 Brazil       172006362  174504898
- 3 China       1272915272 1280428583

- One column contains two variables

- 1999 and 2000 are not variables, they are values!

- type and count are no true variables (= characteristics of the observation object)

## Slide 11
- Does each observation have its own row?

- 11

- country      year  cases population
- <chr>       <int>  <int>      <int>
- 1 Afghanistan  1999    745   19987071
- 2 Afghanistan  2000   2666   20595360
- 3 Brazil       1999  37737  172006362
- 4 Brazil       2000  80488  174504898
- 5 China        1999 212258 1272915272
- 6 China        2000 213766 1280428583

- country      year type            count
- <chr>       <int> <chr>           <int>
- 1 Afghanistan  1999 cases             745
- 2 Afghanistan  1999 population   19987071
- 3 Afghanistan  2000 cases            2666
- 4 Afghanistan  2000 population   20595360
- 5 Brazil       1999 cases           37737
- 6 Brazil       1999 population  172006362
- 7 Brazil       2000 cases           80488
- 8 Brazil       2000 population  174504898
- 9 China        1999 cases          212258
- 10 China        1999 population 1272915272
- 11 China        2000 cases          213766
- 12 China        2000 population 1280428583

- country      year rate
- * <chr>       <int> <chr>
- 1 Afghanistan  1999 745/19987071
- 2 Afghanistan  2000 2666/20595360
- 3 Brazil       1999 37737/172006362
- 4 Brazil       2000 80488/174504898
- 5 China        1999 212258/1272915272
- 6 China        2000 213766/1280428583

- country     `1999` `2000`
- * <chr>        <int>  <int>
- 1 Afghanistan    745   2666
- 2 Brazil       37737  80488
- 3 China       212258 213766

- country         `1999`     `2000`
- * <chr>            <int>      <int>
- 1 Afghanistan   19987071   20595360
- 2 Brazil       172006362  174504898
- 3 China       1272915272 1280428583

- 1

- 2

- 3

- 4

## Slide 12
- Each observation must have its own row

- 12

- country      year  cases population
- <chr>       <int>  <int>      <int>
- 1 Afghanistan  1999    745   19987071
- 2 Afghanistan  2000   2666   20595360
- 3 Brazil       1999  37737  172006362
- 4 Brazil       2000  80488  174504898
- 5 China        1999 212258 1272915272
- 6 China        2000 213766 1280428583

- country      year type            count
- <chr>       <int> <chr>           <int>
- 1 Afghanistan  1999 cases             745
- 2 Afghanistan  1999 population   19987071
- 3 Afghanistan  2000 cases            2666
- 4 Afghanistan  2000 population   20595360
- 5 Brazil       1999 cases           37737
- 6 Brazil       1999 population  172006362
- 7 Brazil       2000 cases           80488
- 8 Brazil       2000 population  174504898
- 9 China        1999 cases          212258
- 10 China        1999 population 1272915272
- 11 China        2000 cases          213766
- 12 China        2000 population 1280428583

- country      year rate
- * <chr>       <int> <chr>
- 1 Afghanistan  1999 745/19987071
- 2 Afghanistan  2000 2666/20595360
- 3 Brazil       1999 37737/172006362
- 4 Brazil       2000 80488/174504898
- 5 China        1999 212258/1272915272
- 6 China        2000 213766/1280428583

- country     `1999` `2000`
- * <chr>        <int>  <int>
- 1 Afghanistan    745   2666
- 2 Brazil       37737  80488
- 3 China       212258 213766

- country         `1999`     `2000`
- * <chr>            <int>      <int>
- 1 Afghanistan   19987071   20595360
- 2 Brazil       172006362  174504898
- 3 China       1272915272 1280428583

- Observations spread across two tables

- 2 rows per observation

## Slide 13
- Does each value have its own cell?

- 13

- country      year  cases population
- <chr>       <int>  <int>      <int>
- 1 Afghanistan  1999    745   19987071
- 2 Afghanistan  2000   2666   20595360
- 3 Brazil       1999  37737  172006362
- 4 Brazil       2000  80488  174504898
- 5 China        1999 212258 1272915272
- 6 China        2000 213766 1280428583

- country      year type            count
- <chr>       <int> <chr>           <int>
- 1 Afghanistan  1999 cases             745
- 2 Afghanistan  1999 population   19987071
- 3 Afghanistan  2000 cases            2666
- 4 Afghanistan  2000 population   20595360
- 5 Brazil       1999 cases           37737
- 6 Brazil       1999 population  172006362
- 7 Brazil       2000 cases           80488
- 8 Brazil       2000 population  174504898
- 9 China        1999 cases          212258
- 10 China        1999 population 1272915272
- 11 China        2000 cases          213766
- 12 China        2000 population 1280428583

- country      year rate
- * <chr>       <int> <chr>
- 1 Afghanistan  1999 745/19987071
- 2 Afghanistan  2000 2666/20595360
- 3 Brazil       1999 37737/172006362
- 4 Brazil       2000 80488/174504898
- 5 China        1999 212258/1272915272
- 6 China        2000 213766/1280428583

- country     `1999` `2000`
- * <chr>        <int>  <int>
- 1 Afghanistan    745   2666
- 2 Brazil       37737  80488
- 3 China       212258 213766

- country         `1999`     `2000`
- * <chr>            <int>      <int>
- 1 Afghanistan   19987071   20595360
- 2 Brazil       172006362  174504898
- 3 China       1272915272 1280428583

- 1

- 2

- 3

- 4

## Slide 14
- Each value must have its own cell

- 14

- country      year  cases population
- <chr>       <int>  <int>      <int>
- 1 Afghanistan  1999    745   19987071
- 2 Afghanistan  2000   2666   20595360
- 3 Brazil       1999  37737  172006362
- 4 Brazil       2000  80488  174504898
- 5 China        1999 212258 1272915272
- 6 China        2000 213766 1280428583

- country      year type            count
- <chr>       <int> <chr>           <int>
- 1 Afghanistan  1999 cases             745
- 2 Afghanistan  1999 population   19987071
- 3 Afghanistan  2000 cases            2666
- 4 Afghanistan  2000 population   20595360
- 5 Brazil       1999 cases           37737
- 6 Brazil       1999 population  172006362
- 7 Brazil       2000 cases           80488
- 8 Brazil       2000 population  174504898
- 9 China        1999 cases          212258
- 10 China        1999 population 1272915272
- 11 China        2000 cases          213766
- 12 China        2000 population 1280428583

- country      year rate
- * <chr>       <int> <chr>
- 1 Afghanistan  1999 745/19987071
- 2 Afghanistan  2000 2666/20595360
- 3 Brazil       1999 37737/172006362
- 4 Brazil       2000 80488/174504898
- 5 China        1999 212258/1272915272
- 6 China        2000 213766/1280428583

- country     `1999` `2000`
- * <chr>        <int>  <int>
- 1 Afghanistan    745   2666
- 2 Brazil       37737  80488
- 3 China       212258 213766

- country         `1999`     `2000`
- * <chr>            <int>      <int>
- 1 Afghanistan   19987071   20595360
- 2 Brazil       172006362  174504898
- 3 China       1272915272 1280428583

- One cell contains two values

## Slide 15
- Pandas – Data Structures

- 15

## Slide 16
- Core components of pandas: Series & DataFrame

- A Series is essentially a column
- A DataFrame is a multi-dimensional table made up of a collection of Series

- 16

## Slide 17
- Creating DataFrames from scratch

- There are many ways to create a DataFrame from scratch, but a great option is to use a simple dictionary.
- Let's say we have a fruit stand that sells apples and oranges. We want to have a column for each fruit and a row for each customer purchase. Organized as a dictionary this looks like:
- The data dictionary counts 2 key-value pairs
- Keys: apples + oranges 	Values: lists with the corresponding purchases

- 17

- data = {
- 'apples': [3, 2, 0, 1],
- 'oranges': [0, 3, 7, 2]
- }

## Slide 18
- Creating DataFrames from scratch

- Next the dictionary can be passed to the DataFrame constructor
- Each (key, value) pair in the dictionary now corresponds to a column in the resulting DataFrame. The index of this DataFrame is generated on creation as the numbers 0-3.

- 18

- purchases = pd.DataFrame(data)purchases

## Slide 19
- Creating DataFrames from scratch

- Instead of the default numeric indexing, each row can get a custom index label: e.g. customer names
- A datarow of a specific customer can then be located based on their name

- 19

- purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', ‘David'])
- purchases

- purchases = purchases.loc[ 'Lily']

- To extract rows based on the index label, you use: .loc[‘label’]

## Slide 20
- Reset index

- You can always go back from the labeled indices (e.g. index=['June', 'Robert', 'Lily', ‘David’])  to the default numerical ones (e.g. 0-3) by using reset_index()
- Use the drop parameter to avoid the old index being added as a column:

- 20

- purchases =purchases.reset_index()

- purchases =purchases.reset_index(drop = True)

## Slide 21
- Pandas – Extracting and assigning data

- 21

## Slide 22
- Extracting data

- A datarow can also be extracted based on index number with iloc[index]
- By specifying a list of indexes multiple rows are retrieved

- 22

- purchases = purchases.iloc[2]

- purchases = purchases.iloc[[2,3]]

- purchases = purchases.iloc[[0,2,3]]

## Slide 23
- Extracting data

- 23

- https://files.realpython.com/media/iloc_vs_loc_80_border20.d5280f475f4e.png

## Slide 24
- Extracting data

- Extracting rows from a DataFrame can also be done by slicing

- 24

## Slide 25
- Extracting data

- Slicing works with index labels
- Note that if using labels (loc) the end-element is included in the result, which is not true in case of normal index-based slicing (iloc)

- 25

## Slide 26
- Extracting data

- Extracting 1 column from a dataframe results in a Series
- To extract columns as a DataFrame, you need to pass a list[] of column names

- 26

- Note that purchases.apples will also work

## Slide 27
- Assigning data

- a constant value:

- or an iterable of values:

- 27

- purchases['bananas']=3

- purchases['bananas’]=[2,0,5,7]

- purchases['lemons'] = range(1,len(purchases)+1,+1)

- Going the other way, assigning data to a DataFrame is easy.
- You can insert/update a column with either:

## Slide 28
- Pandas – Read and write data

- 28

## Slide 29
- Read and Write

- 29

- https://pandas.pydata.org/docs/getting_started/index.html

## Slide 30
- Reading data from CSVs

- With CSV files all you need is a single line to load in the data:
- CSVs don't have indexes like our DataFrames, so you need to designate the index_col when reading:

- 30

- df = pd.read_csv('purchases.csv')

- df = pd.read_csv('purchases.csv', index_col=0)

## Slide 31
- Reading data from JSON

- If you have a JSON file pandas can read this just as easily.
- Notice this time the index came correctly since JSON allows indexes to work through nesting.
- JSON isn't a tabular format. When pandas cannot deduce the JSON structure, set the orient parameter. (https://www.roelpeters.be/pandas-read-json-orient)

- 31

- df = pd.read_json('purchases.json')

## Slide 32
- Reading data from databases

- You can use any database, but we’ll be using SQLite
- No installation required, the entire database is contained in a file that you can open using portable software
- https://sqlitebrowser.org/
- We’re using 2 tables and yes, they are badly normalized

- 32

## Slide 33
- Reading data from databases

- The resulting dataframe is different from what we got from a CSV-file
- That’s because of how normalized data works
- We could fix this using the techniques that follow in this and the next chapter
- But for now it’s a good enough proof of concept

- 33

- import sqlite3
- con = sqlite3.connect("purchases.db")
- df = pd.read_sql_query("SELECT c.name, p.quantity, p.fruit FROM customers c join purchases p on c.customerID = p.customerID", con)
- df

## Slide 34
- Storing DataFrame in CSV, JSON or Excel

- After extensive work on cleaning data in a DataFrame, the result can be saved as a file of your choice.
- Similar to the ways we read in data, pandas provides intuitive commands to save it:

- 34

- df.to_csv('new_purchases.csv')
- df.to_json('new_purchases.json’)
- df.to_excel('new_purchases.xlsx’)

## Slide 35
- Pandas – DataFrame basic operations

- 35

## Slide 36
- Basic DataFrame operations

- Load the IMDB movies dataset from csv using the movie titles as index.
- To get an overview of the first or last records in the DataFrame, use the head() or tail() methods.  Both accept a number as argument to indicate how many records should be retrieved.

- 36

- df_movies = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")

- df_movies.head(3)

- df_movies.tail(2)

## Slide 37
- To customize the number of rows or columns to be displayed:

- set_option("display.max_...")

- 37

- pd.set_option('display.max_columns', 4)
- pd.set_option('display.max_rows', 6)
- df_movies

## Slide 38
- Getting info about the data

- The method .info() provides the essential details about the dataset, such as the number of rows and columns, the number of non-null values, what type of data is in each column, and how much memory the DataFrame is using.

- 38

- df_movies.info()

- Missing values!

- The dataframe counts 1000 rows and 11 columns This information can also be retrieved with the property shape.

- df_movies.shape

## Slide 39
- Getting info about the data

- You can use the .describe() method to find basic statistical characteristics:
- Count: number of non-missing values
- Mean
- Standard deviation
- Median (0,50)
- Quartiles (0,25/0,75)
- Range: min-max

- 39

- df_movies.describe()

## Slide 40
- Getting info about the data

- 40

- When using parameter “include” you can select columns of a certain type

- df_movies.describe(include="int")

- df_movies.describe(include=“object")

- ! Notice the characteristics change with the datatype

## Slide 41
- Column names cleanup

- Best practice for column names is to lowercase them, remove special characters, and replace spaces with underscores
- Here's how to get the column names of our dataset:
- Use the .rename() method to rename certain or all columns via a dictionary.

- 41

- df_movies.columns

- df_movies.rename(columns={
- 'Runtime (Minutes)': 'Runtime',
- 'Revenue (Millions)': 'Revenue_millions'
- }, inplace=True)

- Inplace = true is an alternative way to code df_movies = df_movies.rename(….)

## Slide 42
- Column names cleanup

- You can also set the columns property to a list of appropriate names:
- The above solution is a long way to lowercase each column.  Instead of just renaming each column manually we can do a list comprehension:

- 42

- df_movies.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime',
- 'rating', 'votes', 'revenue_millions', 'metascore']

- df_movies.columns = [col.lower() for col in df_movies]

## Slide 43
- Pandas – Missing values

- 43

## Slide 44
- Missing values

- When exploring data, you’ll most likely encounter missing or null values, which are essentially placeholders for non-existent values.
- Most commonly you'll see Python's None or NumPy's np.nan
- There are two options in dealing with nulls:
- Get rid of rows or columns with nulls (amputation)
- Replace nulls with non-null values (imputation)
- Data scientists regularly face the dilemma of dropping or imputing null values. This decision requires profound knowledge of the data and its context. Overall, removing null data is only suggested if you have a small amount of missing data.

- 44

## Slide 45
- Missing values

- .isnull() returns for every data cell whether a value is present.
- To count the number of nulls in each column use an aggregate function for summing.

- 45

- df_movies.isnull().sum()

- We can see now that our data has 128 missing values for revenue_millions and 64 missing values for metascore.

## Slide 46
- Missing values: remove rows or columns

- Remove rows with missing elements:
- 162 rows are deleted with missing revenue_millions and/or metascore
- This obviously seems like a waste since there's perfectly good data in the other columns of those dropped rows
- Other than just dropping rows, you can also drop columns with null values by setting the parameter axis=1:
- Now the columns revenue_millions and metascore are gone

- 46

- df_movies.dropna(inplace=True)df_movies. shape

- df_movies.dropna(axis = 1, inplace=True)df_movies. shape

## Slide 47
- What's with this axis=1 parameter?

- It's not immediately obvious where axis comes from and why is must be 1 to affect columns. To understand, just look at the .shape output:
- This is a tuple that represents the shape of the DataFrame, i.e. 1000 rows and 11 columns. Note that the rows are at index 0 of this tuple and columns are at index 1.
- Therefore axis=1 affects columns. This comes from NumPy and is a great example of why learning NumPy is worth your time.

- 47

- df_movies.shape

## Slide 48
- Missing values: imputation

- Imputation is a conventional technique used to keep valuable data that have null values.
- There may be instances where dropping every row with a null value removes too big a chunk from your dataset, so instead we can impute that null with another value, usually the mean or the median of that column.

- 48

## Slide 49
- Missing values: imputation

- Let's look at imputing the missing values in the revenue_millions column. First extract that column into its own variable:
- revenue now contains a Series:

- 49

- revenue = df_movies['revenue_millions']

- revenue.head()

## Slide 50
- Missing values: imputation

- Impute the missing values of revenue using the mean.
- First calculate the mean value:
- Next fill the nulls using .fillna() :

- 50

- revenue_mean = revenue.mean()
- revenue_mean

- revenue.fillna(revenue_mean, inplace=True)

- We have now replaced all nulls in revenue with the mean of the column.
- Notice that by using inplace=True we have actually affected the original df_movies and not only the series.

- df_movies.isnull().sum()

## Slide 51
- Pandas – Data manipulation techniquesConditional Selection Sorting GroupingCounting

- 51

## Slide 52
- Conditional selections

- We’ve gone over how to select columns and rows, but what if we want to make a conditional selection?
- For example, what if we want to filter our movies DataFrame to show only films directed by Ridley Scott?

- 52

- df_movies[df_movies['director'] == 'Ridley Scott']

- This instruction can be read as SQL:Select df_movies where df_movies director equals Ridley Scott.

## Slide 53
- Conditional selections

- Conditions can be combined by using logical operators:
- | for "or"
- & for "and“
- Each condition is written between ()
- E.g. movies directed by Ridley Scott with a rating above 7.0

- 53

- df_movies[(df_movies['director'] == 'Ridley Scott') & (df_movies['rating'] > 7.0 ) ]

## Slide 54
- Conditional selections

- Frequently used in selection making is the isin() method (~ OR)
- E.g. movies directed by Ridley Scott OR James Gunn

- 54

- df_movies[df_movies['director'].isin(['Ridley Scott','James Gunn'] )]

## Slide 55
- Sorting

- In case you want to sort the movies by director, you can use the method sort_values()

- 55

- df_movies[df_movies['director'].isin(['Ridley Scott','James Gunn'] )].sort_values(by='director',ascending=False)

## Slide 56
- Grouping

- 56

- The output “movies directed by Ridley Scot” can also be retrieved by using the methods groupby() and get_group()

- grouped = df_movies.groupby('director')
- grouped.get_group('Ridley Scott')

## Slide 57
- Counting

- To retrieve the number of movies directed by Ridley Scot, just use the function len()
- To retrieve the number of movies directed per director, use the method size()

- 57

- grouped = df_movies.groupby('director')
- len(grouped.get_group('Ridley Scott’))

- df_movies.groupby('director').size().sort_values(ascending=False)

## Slide 58
- Counting

- To count the number of movies directed by each director, you can immediately - without grouping - use the method value_counts()

- 58

- df_movies['director’].value_counts()

## Slide 59
- Pandas – Cleaning a dataset using an example

- 59

## Slide 60
- Cleaning a dataset

- Open the cars_cleaning notebook
- Part 1 contains a detailed description of the opening and cleaning of some random dataset
- We’ll go over the highlights in the following slides.

- 60

## Slide 61
- Create a calculated column

- The cars dataset has mileage in miles per gallon, not in liters per 100 km
- We can create a new column!
- The formula is something you know (or lookup)
- Note how we used a list comprehension
- By going over a column we created a list of the same number of rows as the dataframe
- This ensures the data is stored nicely

- 61

## Slide 62
- Categorical versus numerical variables

- A categorical variable can have a finite number of values:
- T-shirt sizes, places of embarkment for titanic, gender, …
- There are 2 types of categorical variables
- Ordinal (ordered) 		“S/M/L/XL/XXL”
- Nominal (unordered) 		“Male/Female”
- A numerical variable can have any quantitative value:
- Height, weight, number of bikes you own, …
- There are 2 types of numerical variables
- Discrete (finite number of possible values) 		: number of bikes
- Continuous (infinite number of decimal values)	: height, weight

- 62

## Slide 63
- Categorical versus numerical variables

- Let’s say “age” is in the database
- Is a continuous numerical field if: You store the age as number with digits behind the comma (1,675; 3,54; 43,33453; …)
- Is a discrete numerical field if: You store it as an age (1, 3, 43, …)
- Is an ordered categorical field if: You can only have a limited number of ages, like kids in a kindergarten class (2, 3 or 4, but nothing else)
- Is never an unordered categorical field.

- 63

## Slide 64
- Categorical variables

- Why is this important?
- If you have categorical data and you tell pandas, pandas will take it into account when creating graphs
- How then?
- Unordered:
- Ordered:

- 64

## Slide 65
- Cars notebook

- Part 2 of the notebook is about selections and aggregations.
- Make sure you understand the basics well.

- 65

## Slide 66
- Exercises

- Kaggle course Pandas: https://www.kaggle.com/learn/pandas
- Make the exercises from lessons 1 - 2 - 4 – 5
- Notebook Flights

- 66

## Slide 67
- Resources

- https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
- https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

- 67
