## Module 4.3: Transforming Data with Pandas

### Overview

In this lesson, students will learn to manipulate data using the Pandas library in Python. They will perform mathematical operations on DataFrame columns, format and replace text within a DataFrame, and create new columns. They will also become familiar with the "Apply" function, which allows them to transform a DataFrame's column.

### Class Objectives

By the end of today's class, the students will be able to:

* Create new columns in a DataFrame.

* Use “Apply” to transform a column in Pandas.

* Fill or drop missing values.

* Replace text in a DataFrame.

* Format text in a DataFrame.

* Use Pandas to answer abstract questions.

---

### Instructor Notes

In this lesson, students will explore various functionalities of the Pandas library, a staple in the Python ecosystem for data manipulation and analysis. They will learn to perform mathematical operations, manipulate text, handle missing values, and create new DataFrame columns. In addition, they will also familiarize themselves with the 'Apply' function, an important tool for transforming data in Pandas.

---

### Class Slides

The slides for this lesson can be viewed on Google Drive here: [Module 4.3 Slides](https://docs.google.com/presentation/d/1oyJp5IdW1AHfE_FsDLy0DGUuK8w2jZ85d3M4IzsQbXE/edit#slide=id.g21f2d3f9243_0_462).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit).

**Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

---

### Time Tracker

| Start Time | Number | Activity                                           | Duration |
| ---------- | ------ | -------------------------------------------------- | -------- |
| 6:30 PM    | 1      | Instructor Do: Introduction to the Class           | 0:05     |
| 6:35 PM    | 2      | Instructor Do: Creating New Columns                | 0:10     |
| 6:45 PM    | 3      | Student Do: Column Creation                        | 0:10     |
| 6:55 PM    | 4      | Review: Column Creation                            | 0:10     |
| 7:05 PM    | 5      | Instructor Do: Apply Function                      | 0:15     |
| 7:20 PM    | 6      | Students Do: Apply Taxes                           | 0:15     |
| 7:35 PM    | 7      | Review: Apply Taxes                                | 0:15     |
| 7:50 PM    | 8      | Everyone Do: Cleaning Data                         | 0:30     |
| 8:20 PM    | 9      | Break                                              | 0:15     |
| 8:35 PM    | 10     | Instructor Do: Answering Abstract Questions        | 0:15     |
| 8:50 PM    | 11     | Everyone Do: Answering Abstract Questions          | 0:35     |
| 9:25 PM    | 12     | End Class                                          | 0:05     |
| 9:30 PM    |        | END                                                |          |

---

### 1. Instructor Do: Introduction to the Class (5 min)

Welcome the students, and explain that in today’s lesson they will learn how to transform data contained in DataFrames. Transforming data entails the creation of new columns, splitting existing columns into two columns, and rectifying and ensuring certain columns are of the same format. The transformation of data is necessary in order to organize data prior to analyzing data. Let’s begin!

—--

### 2. Instructor Do: Creating New Columns (10 min)

**Corresponding Activity:** [01-Ins_Data_Functions](Activities/01-Ins_Data_Functions)

Continue using the slideshow to accompany this demonstration.

Continue using the slideshow to cover the following talking points:

* There are various reasons why someone working with Pandas may want to create a new column. This could include:

* Mathematical operations between two columns, such as adding values together and inputting the sum of them in a new column;

* String manipulation to concatenate two string columns, perhaps combining a Name and Surname column into a Full Name column;

* Calculation of the difference between dates between two columns in order to determine time elapsed between the two; and

* Data cleaning, whereby any trailing blank spaces are removed from a string column.

* Table visualization is not the only benefit of using Pandas DataFrames. Many of the functions and methods that come packaged with Pandas allow for quick and easy analysis of large datasets.

Open the solution file within the Jupyter notebook, share the file with the students, share your screen, and make sure to point out how an external CSV file is being imported. Students will learn how to do this later in today's lesson.

* The first method to describe is `head()`, which takes a DataFrame and presents only the first five rows of data inside of it. This number can be increased or decreased by placing an integer within the parentheses.

* The `head()` method is helpful because it allows the programmer to check a minified version of a larger table. Then, they can make informed changes without searching through the entire dataset.

* Another useful method is `describe()`, which will print out a DataFrame containing some analysis of the table and its columns. It also indicates some of the other data functions that can be performed on a DataFrame or Series, such as `count()`, `mean()`, `std()`, `min()`, and `max()`. This is captured in the following image:

  ![Panda describe function](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_3/img/05-DataFunction_describe.png)

* Most data functions can also be performed on a Series by referencing a single column within the whole DataFrame. Similar to referencing a key within a dictionary, we’d take the DataFrame and follow it up with parentheses containing the desired column's header.

* Multiple columns can be referenced, as well, by placing all of the column headers desired within a pair of double parentheses. If two sets of parentheses are not used, then Pandas will return an error.

* The following image captures three examples of how specific columns can be referenced and used.

  ![Column Reference.](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_3/img/05-DataFunction_ColumnReference.png)

* In some situations, it is helpful to list out all of the unique values stored within a column. This is precisely what the `unique()` function does as the following code shows:

  ```python
  # The unique method shows every element only once
  unique = data_file_df["Car"].unique()
  unique
  ```

  * The result is an array containing all the different values:

    ![Unique Values.](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_3/img/M4-L3-dataframe-unique.png)

* Another method with similar functionality is `value_counts()`, which not only returns a list of all unique values within a series but also counts how many times a value appears, as the following code shows:

  ```python
  # The value_counts method counts unique values in a column
  count = data_file_df["Gender"].value_counts()
  count
  ```

  * The following image shows the value counts of each unique value in the "Gender" column:

    ![Value Counts](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_3/img/M4-L3-dataframe-value-counts.png)

* Calculations can also be performed on columns and then added into the DataFrame as a new column by referencing the DataFrame, placing the desired column header within parentheses, and then setting it equal to a Series, as the following code shows:

  ```python
  # Calculations can also be performed on Series and added into DataFrames as new columns
  thousands_of_dollars = data_file_df["Amount"]/1000
  data_file_df["Thousands of Dollars"] = thousands_of_dollars

  data_file_df.head()
  ```

  * The following image shows the DataFrame:

    ![Column Calculations.](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_3/img/M4-L3-calculated-column.png)

Data Source: Data generated by Mockaroo, LLC. (2021) Realistic Data Generator. [https://www.mockaroo.com/](https://mockaroo.com/). Data for this dataset was generated by edX Boot Camps LLC, and is intended for educational purposes only.

---

### 3. Student Do: Column Creation (10 min)

**Corresponding Activity:** [02-Stu_TrainingGrounds_DataFunctions](Activities/02-Stu_TrainingGrounds_DataFunctions)

Continue through the slideshow, using the next slides as an accompaniment to this activity.

This activity will give students an idea of how to view numeric statistics on a DataFrame, find data about specific columns involving arithmetic operations, and creatie a new column using transformed data from an existing column.

---

### 4. Review: Column Creation (10 min)

**Corresponding Activity:** [02-Stu_TrainingGrounds_DataFunctions](Activities/02-Stu_TrainingGrounds_DataFunctions)

Continue using the slideshow to facilitate a review of the activity.

Open and share solution file, and go through the code with the class, answering any questions that students may have.

* Cover the following key points when discussing this activity:

  * By collecting the unique values for the "Trainer" column, it’s much easier to identify the employees who are currently with the "Training Grounds" gym.

  * To convert "Membership (Days)" into "Membership (Weeks)", the code simply takes the values stored within the initial column, divides them by seven, and then adds this edited Series into a newly created column:

    ```python
    # Convert the membership days into weeks and then adding a column to the DataFrame
    weeks = training_df["Membership (Days)"]/7
    training_df["Membership (Weeks)"] = weeks

    training_df.head()
    ```

    * The output is a DataFrame containing the newly created "Membership (Weeks)":

      ![Training Grounds Column Code](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_3/img/06-TrainingGrounds_new_column.png)

---

### 5. Instructor Do: Apply Function (15 min)

**Corresponding Activity:** [03-Ins_Apply](Activities/03-Ins_Apply/)

Continue using the slideshow to accompany this demonstration.

The `DataFrame(apply()` function is used to apply a function along an axis of the DataFrame or Series. Instead of using traditional iterative loops to iterate over a DataFrame, the `.apply()` function can be used. It takes a function as an input, and applies the function to the whole DataFrame. For tabular data, the function requires specification of which axis the function should act on, where 0 represents the columns, and 1 represents the rows.

Often, before data can be used for AI or machine learning, it needs to be manipulated in certain ways to facilitate more efficient data processing. The apply() function is an essential function for data manipulation, which enables efficient versatile operations on DataFrames and Series.

Walk students through the following steps:

```python
# Import the data

import pandas as pd
file = '../Resources/donors2021.csv'
donors_df = pd.read_csv(file)
donors_df.head()
```

The next step requires creating a new column to reflect 10% of the value of an existing column:

```python
# If 10% of every donation was fully matched by an 
# anonymous philanthropist, making a new column would be easy.

donors_df['Match Amount'] = donors_df['Amount'] * 0.1
donors_df.head()
```

The match requirements may change, and fluctuate based on the amount donated, as shown in the following code:

```python
# What if the match percentage changed based on the amount donated?
# 10% on donations below $500, and 20% on donations of $500 or more.
# We need a new solution! A perfect opportunity for 'apply'.

# Define a function
def match_amount(amount):
    if amount < 500:
        return amount * 0.1
    return amount * 0.2

# "Apply" the function to the amount column
donors_df['Match Amount'] = donors_df['Amount'].apply(match_amount)
donors_df.head()
```

Next, we consider a situation that has even more constraints on the matching amounts.

```python
# Apply can also use values from multiple columns by
# setting the axis argument to 1. Suppose the donor 
# was only matching donations from Delaware.

def match_amount(row):
    if (row['State'] != 'DE'):
        return 0
    if (row['Amount'] < 500):
        return row['Amount'] * 0.1
    return row['Amount'] * 0.2

# "Apply" the function to the DataFrame
donors_df['Match Amount'] = donors_df.apply(match_amount, axis = 1)
donors_df.head()
```

The `apply()` function can also be used in conjunction with the lambda function.

```python
# Finally, apply can also be used with lambda functions.

donors_df['Match Amount'] = donors_df['Amount'].apply(lambda x: x * 0.1 if x < 500 else x * 0.2)
donors_df.head()
```

---

### 6. Students Do: Apply Taxes (15 min)

**Corresponding Activity:** [04-Stu_Apply_Taxes](Activities/04-Stu_Apply_Taxes/)

Continue through the slideshow, using the next slides to accompany this activity.

This activity will give students a chance to practice their use of the `apply` function and lambda functions with a simple example.

---

### 7. Review: Apply Taxes (15 min)

**Corresponding Activity:** [04-Stu_Apply_Taxes](Activities/04-Stu_Apply_Taxes/)

Open the solution, share and go over the file with the class, answering whatever questions students may have.

Cover the following key points during the discussion:

Import pandas and the data as follows:

```python
# Import the data
import pandas as pd
file = '../Resources/SFO_Airport_Utility_Consumption.csv'
utilities_df = pd.read_csv(file)
utilities_df.head()
```

In the next step, students were required to add a column that displays the tax rate of 5%, except 2019 onwards, which has a tax rate of 5.5%. Use the following code:

```python
# Add a column that tracks the tax rate
# Assume every year and type of utility had 
# a tax rate of 5%, except for 2019 when the 
# tax was raised to 5.5%

# Define a function
def tax_rate(year):
    return 0.055 if year >= 2019 else 0.05

# Apply the function to the Year column
utilities_df['Tax Rate'] = utilities_df['Year'].apply(tax_rate)
utilities_df.tail()
```

Students were then required to recalculate the tax rate with commission-owned units taxed an additional 1% on their electricity bill:

```python
# Recalculate the tax rate assuming that
# commission owned units were taxed an
# additional 1% on Electricity.

# Define a function
def tax_rate(row):
    rate = 0.05
    if row['Year'] == 2019:
        rate += 0.005
    if (row['Owner'] == 'Commission') & (row['Utility'] == 'Electricity'):
        rate += 0.01
    return rate

# Apply the function to the DataFrame
utilities_df['Tax Rate'] = utilities_df.apply(tax_rate, axis = 1)
utilities_df.tail()
```

Lastly, the lambda function is used to set the existing Tax Rate to 0 if the utility was “Passengers”:

```python
# Use apply with a lambda function to set
# the existing Tax Rate column to 0 if
# the utility was "Passengers"

# Apply a lambda function
utilities_df['Tax Rate'] = utilities_df\
            .apply(lambda x: 0 if x['Utility'] == 'Passengers' else x['Tax Rate'],
                axis = 1)

utilities_df.head()
```

---

### 8. Everyone Do: Cleaning Data (30 min)

**Corresponding Activity:** [05-Stu_Data_Cleaning](Activities/05-Stu_Data_Cleaning)

In this part of the lesson, walk through data cleaning activity with students.

Review data cleaning from a conceptual standpoint and have the students help you live code the activity, encouraging them to find solutions to each task using the official [Pandas Documentation](https://pandas.pydata.org/docs/). Mention the following points:

* Data cleaning is important because it removes all of the issues and errors that would block or inhibit computation.

* Without data cleaning, financial data can be calculated and aggregated incorrectly and inaccurately. Data quality issues can skew financial numbers. Since numbers drive business decisions in the financial world, use of incorrect data can have catastrophic implications.

Open the unsolved file and live code the activity solution with the students.

* The `shape` function provides a quick and easy way to understand the structure of a DataFrame, including the number of columns and rows in the DataFrame.

  ```python
  csv_data.shape
  ```

  ```output
  (504, 13)
  ```

* Performing a `count` is a great way to assess how many records were loaded into a DataFrame for each Series. The output of `count` reflects the total number of non-null values.

  ```python
  csv_data.count()
  ```

  ```output
  name                  502
  sector                501
  price                 500
  price_per_earnings    497
  dividend_yield        499
  earnings_per_share    498
  52_week_low           500
  52_week_high          500
  market_cap            500
  ebitda                492
  price_per_sales       500
  price_per_book        492
  sec_filings           500
  dtype: int64
  ```

Ask students what steps should be taken if all values in a Series are null (Answer: The Series should be dropped.)

* Nulls can throw a wrench in an analytic pipeline. The `isnull` function will identify which Series has nulls. If there are nulls, they can be removed or filled. The `dropna` and `fillna` functions provide this functionality, respectively. Note that it's important to understand which fields can have nulls and which cannot.

  ```python
  csv_data.isnull()
  ```

* Using `mean` and `sum` with `isnull` will calculate the percentage and number of nulls for a DataFrame. This is important when considering the distribution of missing values in a DataFrame. The percentage and number of nulls can impact how the missing values are cleaned.

  ```python
  csv_data.isnull().mean() * 100
  csv_data.isnull().sum()
  ```

* Instead of dropping nulls in a Series, nulls can be filled with a default value. Common default values are "Unknown", 0, and mean().

* The `dtypes` function can be used on a DataFrame to identify Series data types. A Series data type can also be identified by using `dtype`.

* Identifying data types is valuable because it allows for incorrectly inferred data types to be corrected and converted to the appropriate data types.

* If needed, a Series can be converted to the appropriate data type using the `astype` function (e.g., converting a date field from `string` to `Date`). Some conversions might require values to be cleaned before they can be converted (e.g., removing `$` from an amount field).

If time allows, engage the students with the following review questions:

* True or false: It's okay to have currency symbols and commas in amount fields.

  **Answer:** False. Amount fields should be floats. Floats cannot have symbols or commas, as these are strings.

* What two functions are used to identify and remove currency symbols?

  **Answer:** `contains()` can be used to identify currency symbols, and `replace()` can be used to remove them.

To guide students, you may want to follow up with questions such as the following:

* I used `fillna(0)` to fill NaN or null values in my DataFrame, but now my first_name and last_name fields have 0s in them. What happened? What should I have done instead?

  **Answer:** `fillna(0)` fills all null/NaN values in the DataFrame, regardless of the data type of the Series where the null is. `fillna()` should have been applied against the specific Series that needed the nulls converted to 0.

* True or false: Data quality rules do not conflict with one another.

  **Answer:** False. Technical rules might be disregarded in order to satisfy business rules.

* What changed since the data was cleaned?

* What new analyses can be performed now that the data has been cleaned?

* What measurements have changed since the data has been cleaned?

For more comprehensive data cleaning strategies, slack out the following [link](https://www.kaggle.com/chrisbow/kernels?sortBy=relevance&group=everyone&search=Cleaning+data+with+Python&page=1&pageSize=20&userId=1541110) for curious students who want to learn more about data-cleaning processes using Python. Ask if there are any questions before moving on.

---

### 9. Break (15 min)

—--

### 10. Instructor Do: Answering Abstract Questions (15 min)

**Corresponding Activity:** [06-Evr_Answering_Abstract_Questions](Activities/06-Evr_Answering_Abstract_Questions)

Continue using the slideshow to accompany this demonstration.

Explain to students their role in solving a business’s problems. As a data analyst working with AI and machine learning within a business, you will often be posed abstract questions by management, such as “Who do we need to market to more?”, “What is the company’s best product?” or “Who are our best customers?”.

The key to answering these abstract questions is to first dissect and make sense of them, perhaps even refine them to be less vague. Big data and data analytics are paramount in gathering, analyzing, and presenting the information that will be able to provide insight into these questions. This will result in an organization that is making more informed business decisions, boosting their revenues, cutting back on key costs, and improving the overall customer experience.

#### The Data Analysis Process

Cover the data analysis process. In order to approach the key questions, data analytics follows a rigorous process involving the following broad steps:

* Defining the question

* Determination of the analysis method

* Data collection

* Data cleaning

* Data analysis

* Sharing the results

These steps will guide you towards your goal of finding answers, but remember that these steps are not set in stone, and are iterative in nature. Understanding the entirety of the process and realizing that there may be overlaps between sections is important.

#### Defining the question

Questions posed by management may be vague or open to interpretation. For example, the question “What is the company’s best product?” can be interpreted in a few ways. Could it be referring to the most profitable product overall? Or perhaps, which product has sold the most units? Perhaps the best product may be the product that is branded well, has gone “viral,” and brings in the most customers. Refine the question and ensure that the business is in alignment with the refined question. Once there is agreement on the question, the next step is to determine the analysis method.

#### Determination of the analysis method

The type of question would determine the type of data that needs to be collected, and the resulting method of analysis. The data analyst must ask themselves what type of data needs to be collected, how much data, and the sources of data.

The type of data collected would determine the method of analysis chosen. There is no use choosing a method of analysis that requires a certain type of data, and you are unable to source the required data. Some of the analysis methods include:

* Predictive models
* Time series analysis
* Machine learning techniques

#### Data collection

Explain the data collection phase to students. Now that you have defined the overarching question, it’s time to start collecting the data. Many organizations collect an abundance of data, so it’s critical that you refine your data collection to only the most relevant data.

Data sources within the organization are preferred, and this is referred to as first-party data. Generally, first-party data is structured and well organized. Alternative sources of data include second- and third-party data. Second-party data is the first-party data of another organization. This data should also be relatively well structured, but may be a little less relevant than first-party data. Third-party data is data collected through multiple sources, and is generally much more unstructured.

#### Data cleaning

The data that is going to be fed into your machine learning models needs to be of a high quality. If low quality data is used as inputs into the model, the outputs may be ineffective or misleading. The data cleaning process ensures that major errors, outliers, and unnecessary data points are removed, while also ensuring that all the data collected is in the appropriate structure. The creation of new columns, and the transformation of column data that you learned about earlier is relevant in this phase of the data analytics process.

#### Data analysis

Once all the data is collected, cleaned, and ready, the data analysis process can begin. Business intelligence tools such as Tableau or the statistical analysis within Pandas that you learned about are useful in this phase. The method of data analysis depends on the question you are trying to answer. Some of the techniques include univariate or bivariate analysis, time-series analysis, and regression analysis. These methods can be considered under the following broad categories:

* Descriptive analysis:  The identification of what has already occurred.
* Diagnostic analysis: Focuses on why certain events have occurred.
* Predictive analysis: The identification of future trends based on historical data.
* Prescriptive analysis: Focuses on recommendations for the future.

#### Sharing the results

At this stage, the data analysis should ideally provide clarity in answering the question you sought out to solve. Before sharing the results with the rest of the team, it’s essential to find the most appropriate way to present the data in a clear and concise manner. Keep in mind that the business will likely make a costly decision based on the results of your findings, so it is imperative that there is no ambiguity in your results. It’s worth flagging any “blind spots” or shortcomings in the data so that the team has a good overview of the situation.

Some software applications may have built-in dashboards and graphs that are ready to go, but sometimes it may be necessary to create some visualizations with Microsoft PowerPoint or Google Slides.

---

### 11. Everyone Do: Answering Abstract Questions (35 min)

**Corresponding Activity:** [06-Evr_Answering_Abstract_Questions](Activities/06-Evr_Answering_Abstract_Questions/)

In this activity, students are asked to answer a single question based on the utility consumption data from SFO airport: “Which utility’s usage changed the most from 2013 to 2018?” The goal of this activity is to push students to start with a blank page and find a solution. In that spirit, it is recommended that you start with the blank file in the unsolved folder to begin this activity, and prompt students to help you through the analysis process one step at a time. Feel free to have the solution file open on a second monitor as a guide if needed, but if the students guide you to a different solution (or if you prefer a different solution) you are encouraged to deviate from the given solution. In the end, it is important that students understand that there is not a single “correct” way to answer this question, and that comparing different solutions is one of the best ways to learn.

Open the blank file from the unsolved folder and live code a solution by following the data analysis process. Remind students that the process is not rigid, and steps can be performed multiple times, out of order, or all together depending on the question and the data.

1. Start by prompting students to define the question. Use the following questions to guide students if they struggle to give responses:

    * What number might we use to represent the “change” from 2013 to 2018? Should it be a raw number? A percentage? A boolean?

    * To which columns does the question pertain? Is the column relevant? Is the month number relevant?

    * What should the results look like in the end? Should there be a DataFrame or will there be a single value? What units will we work in?

2. Once your students have a relatively firm grasp of the question at hand, transition from defining the question to determining the analysis method. Use whatever methods your class will respond to, but the following suggestions may help:

    * Write very broad comments in cells in the Jupyter notebook to sketch out the steps of the process.

    * If students are stuck, jump to the end and use the discussion from the previous step to work backwards from the desired end result.

    * Encourage students not to get stuck on how they will perform a particular step. You can tell them to imagine that the step is already finished; what will they do next?

    * Remind the class periodically that this is only a rough plan, and that you will very likely still encounter problems in the analysis phase that they didn’t foresee. Assure them that it is expected and all part of the process.

    * When you see or hear students with different approaches than the one you are using, make sure to tell them that there are many solutions to this question and that different doesn't mean wrong.

3. Once a rough map of the steps are in place, move into actually coding the problem, starting with data collection. Tell students that this step often involves selecting the rows and/or columns of the data relevant to the question. The recommended code is below:

    ```python
    import pandas as pd

    # Import the data
    file = '../Resources/SFO_Airport_Utility_Consumption.csv'
    utilities_df = pd.read_csv(file)

    utilities_df.head()

    # Data Collection and Cleaning
    # Select only the needed columns
    utils_df_cleaning = utilities_df[['Year', 'Utility', 'Units', 'Usage']].copy()
    utils_df_cleaning.head()
    ```

    ![The first 5 rows of utils_df_cleaning](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_3/img/utils_df_cleaning.png)

4. With the necessary data in hand, move onto cleaning. Have students rely on the steps made in Step 2, but don’t be afraid to point out where they might have missed something and add or remove code as needed. Try to run code as often as possible and show what the DataFrame looks like at different stages. The recommended code is below:

    ```python
    # Scale the Usage column to be more readable
    # Rows with "Water" as the utility can be left as is
    def scale_to_millions(row):
        if row['Utility'] == 'Water':
            return row['Usage']
        return row['Usage'] / 1000000

    utils_df_cleaning['Usage'] = utils_df_cleaning.apply(scale_to_millions, axis = 1)
    utils_df_cleaning.head()

    # Alter the Units column to reflect the changes
    def millions_of_units(row):
        if row['Utility'] == 'Water':
            return row['Units']
        return 'Million ' + row['Units']
        
    utils_df_cleaning['Units'] = utils_df_cleaning.apply(millions_of_units, axis = 1)
    utils_df_cleaning.head()

    # Combine the Utility and Units columns
    # by putting Units in parentheses
    def combine_utility_and_units(row):
        return f"{row['Utility']} ({row['Units']})"

    utils_df_cleaning['Utility'] = utils_df_cleaning.apply(combine_utility_and_units, axis = 1)
    utils_df_cleaning.head()

    # Create two new DataFrames with data from 2013
    # and 2018 that each contain only the Utility and 
    # Usage column. Reset the index  for each 
    # DataFrame to Utility
    utils_2013_df_cleaned = utils_df_cleaning\
                    .loc[utils_df_cleaning['Year'] == 2013, ['Utility', 'Usage']]\
                    .copy()\
                    .set_index('Utility')
    utils_2018_df_cleaned = utils_df_cleaning\
                    .loc[utils_df_cleaning['Year'] == 2018, ['Utility', 'Usage']]\
                    .copy()\
                    .set_index('Utility')

    utils_2018_df_cleaned.head()
    ```

    The output is shown below:


    ![The first 5 rows of the utils_2018_df_cleaned dataframe](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_3/img/utility_df_cleaned.png)

5. Analyze the clean data by having your students guide you through the code to write. If they ask you to write code you know to be wrong, you can write it anyway and troubleshoot with them, or you can point them back to the question at hand and let them know why their suggestion might not be the right solution. The suggested code is below:

    ```python
    # Analyze

    # Calculate the totals for each utility
    utilities = utils_2013_df_cleaned.index.unique()
    totals_2013 = {'Period': 2013}
    totals_2018 = {'Period': 2018}
    for utility in utilities:
        totals_2013[utility] = utils_2013_df_cleaned.loc[utility, 'Usage'].sum()
        totals_2018[utility] = utils_2018_df_cleaned.loc[utility, 'Usage'].sum()

    print(totals_2013)
    print(totals_2018)

    # Calculate the change per utility as a percentage
    # of each utility's 2013 total.

    def get_percentage(original, final):
        return round((final - original) / original, 3) * 100

    data = []
    for utility in totals_2013.keys():
        if utility == 'Period':
            continue
        original = totals_2013[utility]
        final = totals_2018[utility]
        row = {
            'Utility': utility,
            '2013': round(original, 1),
            '2018': round(final, 1),
            'Difference': round(final - original, 1),
            'Change %': get_percentage(original, final)
        }
        data.append(row)



    # Create a dataframe with the results
    summary_df = pd.DataFrame(data)
    summary_df

    # Set the index to the utility column
    summary_df = summary_df.set_index('Utility')

    # Sort the rows based on Change %
    summary_df = summary_df.sort_values('Change %', ascending=False)
    summary_df
    ```

    The output is shown below:

    ![The summary DataFrame is shown](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_3/img/summary_df.png)

6. Now that the analysis is complete, summarize the results with your students! Some recommended questions follow:

    * Which utility changed the most?

    * Are “Passengers” considered a utility?

    * Are these numbers good or bad? Why?

    * Are there any reasons that our analysis may be wrong or biased?

    * Could we improve our analysis? Would we need more time? More data?

If you followed the solution file, the results should show that the number of passengers using the airport grew 28% in just 5 short years! Water consumption rose slightly at 4.9%, but despite the increase in airport traffic, Electricity and Gas usage were both down in 2018 compared to 2013, with Gas leading the charge with a 6.8% decline. This is a major victory in terms of emissions, and it also helps the bottom line due to cost reduction. We didn’t research how the data was collected, and it is possible that the data is incomplete or biased in some unknown way. We could improve our analysis by digging deeper into the source of the data to better understand where it comes from.

---

### 12. End Class (5 min)

Congratulate students on completing this module. Remind students that at this point, they should have a fair understanding of Pandas, and how to explore and transform data within Pandas.

Remind students what they learned in this lesson: how to create new columns in a DataFrame, perform mathematical operations on columns, and the use of the apply() function to transform data.

**Reflection and Feedback:** Ask the students if they would like to discuss anything in particular, or how the work they learnt in this module factors into the broader course learnings thus far.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
