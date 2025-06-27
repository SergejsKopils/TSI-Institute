#!/usr/bin/env python
# coding: utf-8

# # Python for Data Analytics
# ## Week 5 lab: Pandas

# ### EXERCISE 1
# 
# Create a small pandas dataframe from a dictionary of country names, their capital cities and populations of 5-6 countries
# 1. Extend the database with a couple of countries and one column with the latest GDP values
# 2. Calculate a new column with GDP per capita values
# 3. Filter top 2 countries with highest GDP per capita
# 4. Visualise GDP per capita in countries using an appropriate plot (from pandas library)
# 5. Add a new column with Independance dates (or other national holiday) of countries in 2022 and ensure that it has an appropriate data type
# 6. Set the row index to country names
# 7. Using the resulting data frame, illustrate the difference between _.loc_ and _.iloc_ selectors

# In[1]:


# EXERCISE 1.0
import pandas as pd
import matplotlib.pyplot as plt

data_create_1 = {
    'Country': ['Estonia', 'Lithuania', 'Latvia', 'Sweden', 'Norway', 'Finland'],
    'Capital': ['Tallinn', 'Vilnius', 'Riga', 'Stockholm', 'Oslo', 'Helsinki'],
    'Population': [1329254, 27955321, 1883162, 10415811, 5408320, 5541696]
}

df = pd.DataFrame(data_create_1)
df


# In[2]:


# EXERCISE 1.1
data_create_2 = {
    'Country': ['Luxembourg', 'Netherlands', 'Belgium'],
    'Capital': ['Luxembourg', 'Amsterdam', 'Brussels'],
    'Population': [639070, 17533405, 11587882],
}

df2 = pd.DataFrame(data_create_2)

df_combined = pd.concat([df, df2], ignore_index=True)
df_combined


# In[3]:


# EXERCISE 1.2
gdp_data = [38.1, 71, 40.93, 591.2, 579.4, 282.9, 81.6, 1009.4, 583.4]
df_combined['GDP'] = gdp_data
df_combined


# In[4]:


# EXERCISE 1.3
df_combined['GDP per capita'] = df_combined['GDP'] * 1000 / df_combined['Population']
df_combined


# In[5]:


# EXERCISE 1.4
top_2_countries = df_combined.nlargest(2, 'GDP per capita')
top_2_countries


# In[6]:


# EXERCISE 1.5
plt.figure(figsize=(10, 6))
plt.barh(df_combined['Country'], df_combined['GDP per capita'], color='skyblue')
plt.xlabel('GDP per Capita')
plt.title('GDP per Capita in Countries')
plt.gca().invert_yaxis()
plt.show()


# In[7]:


# EXERCISE 1.6
holiday_data = ['2023-02-24', '2023-02-16', '2023-11-18', '2023-06-06', '2023-05-17', '2023-12-06', '2023-06-23', 
                '2023-04-27', '2023-07-21']
df_combined['Holiday'] = holiday_data
df_combined['Holiday'] = pd.to_datetime(df_combined['Holiday'])
df_combined


# In[8]:


# EXERCISE 1.7
index_data = ['EST', 'LTU', 'LVA', 'SWE', 'NOR', 'FIN', 'LUX', 'NLD', 'BEL']
df_combined.index = index_data
df_combined


# In[9]:


# EXERCISE 1.8
df_slice = df_combined.loc['EST':'SWE', 'Country':'Holiday']
df_slice


# In[10]:


# EXERCISE 1.9
df_slice_iloc = df_combined.iloc[0:4, 0:6]
df_slice_iloc


# In[11]:


# EXERCISE 1 types
df_combined.dtypes


# ### EXERCISE 2
# 
# Using the the Bike Sharing Demand data set from the presentation
# 1. Select summer season's rentals using row index and loc
# 
# 2. Create two new columns with temperature and humidity values, rounded to tens (10,20,30,40, etc.). Sort the data set by these two columns: rounded temperature first, rounded humidity second
# 
# 3. Transform the _datetime_ into datetime data type, set it as index and sort the data frame
# 
# 4. Using groupby functions, calculate:
# 
#     a) average number of bike rentals by rounded temperature and humidity values
#     
#     b) average number of bike rentals by hours of a day
#     
#     c) min, max and standard deviation of temperatures by seasons
#     
# 5. Transform the given data frame into the _long_ (longest) data format, where every row contains exactly one value

# In[12]:


# EXERCISE 2.0
import pandas as pd

file_path = 'bikes.csv'
bike_data = pd.read_csv(file_path)
bike_data.head()


# In[13]:


# EXERCISE 2.1
summer_rentals = bike_data[bike_data['season'] == 'summer']
summer_rentals.head()


# In[14]:


# EXERCISE 2.2
bike_data_copy = bike_data.copy()

bike_data_copy.loc[:, 'temp_rounded'] = (bike_data_copy['temp'] / 10).round() * 10
bike_data_copy.loc[:, 'humidity_rounded'] = (bike_data_copy['humidity'] / 10).round() * 10

bike_data = bike_data_copy.sort_values(by=['temp_rounded', 'humidity_rounded'])
bike_data.head()


# In[15]:


# EXERCISE 2.3
bike_data = pd.read_csv(file_path)

bike_data = bike_data[bike_data['season'] == 'summer'].copy()

bike_data.loc[:, 'temp_rounded'] = (bike_data['temp'] / 10).round() * 10
bike_data.loc[:, 'humidity_rounded'] = (bike_data['humidity'] / 10).round() * 10

bike_data['datetime'] = pd.to_datetime(bike_data['datetime'], format='%d/%m/%Y %H:%M')
bike_data.set_index('datetime', inplace=True)

sorted_bike_data = bike_data.sort_index()

sorted_bike_data['hour'] = sorted_bike_data.index.hour
avg_rentals_by_hour = sorted_bike_data.groupby('hour')['count'].mean()


# In[16]:


# EXERCISE 2.3.1
avg_rentals_by_temp_humidity = sorted_bike_data.groupby(['temp_rounded', 'humidity_rounded'])['count'].mean()
avg_rentals_by_temp_humidity.head(10)


# In[17]:


# EXERCISE 2.3.2
bike_data.index[:10]


# In[18]:


# EXERCISE 2.4 Lab5
sorted_bike_data['hour'] = sorted_bike_data.index.hour
avg_rentals_by_hour = sorted_bike_data.groupby('hour')['count'].mean()
avg_rentals_by_hour.head(24)


# In[19]:


# EXERCISE 2.5
temp_stats_by_season = sorted_bike_data.groupby('season')['temp'].agg(['min', 'max', 'std'])
temp_stats_by_season.head(1)


# In[20]:


# EXERCISE 2.6
long_format_df = sorted_bike_data.reset_index()
long_format_df = long_format_df.melt(id_vars=['datetime'], var_name='variable', value_name='value')
long_format_df


# ### EXERCISE 3
# 
# Develop  a function that split rows of the given data frame into two sub frames in a given proportion. E.g., _df_split(df, propostion=0.8)_ returns a tuple of two data frames, where the first contains about 80% of df rows, and the seconds - other rows.
# 
# Use the developed function to split a data frame from any other exercise and concatenate them back using "_train_" as an index of the first one and "_test_" as an index for the second one.

# In[21]:


# EXERCISE 3.0
import pandas as pd

def df_split(bike_data, proportion=0.8):

    if not 0 <= proportion <= 1:
        raise ValueError("Proportion must be between 0 and 1.")

    first_sub_frame = bike_data.sample(frac=proportion)

    second_sub_frame = bike_data.drop(first_sub_frame.index)

    return first_sub_frame, second_sub_frame

df1, df2 = df_split(bike_data, proportion=0.8)
print(df1.shape)
print(df2.shape)

# EXERCISE 3.1
train_df, test_df = df_split(sorted_bike_data, proportion=0.8)

train_df['index'] = 'train'
test_df['index'] = 'test'

concatenated_df = pd.concat([train_df, test_df]).set_index('index')

concatenated_df


# In[22]:


# EXERCISE 3.2
import pandas as pd

def df_split(bike_data, proportion=0.8):

    if not 0 <= proportion <= 1:
        raise ValueError("Proportion must be between 0 and 1.")

    first_sub_frame = bike_data.sample(frac=proportion)

    second_sub_frame = bike_data.drop(first_sub_frame.index)

    return first_sub_frame, second_sub_frame

df1, df2 = df_split(bike_data, proportion=0.8)
print(df1.shape)
print(df2.shape)

# EXERCISE 3.3
train_df, test_df = df_split(sorted_bike_data, proportion=0.8)

train_df['index'] = 'train'
test_df['index'] = 'test'

concatenated_df = pd.concat([train_df, test_df]).set_index('index')

concatenated_df


# In[23]:


# EXERCISE 3.4
import pandas as pd

def df_split(df_combined, proportion=0.8):
    
    if not 0 <= proportion <= 1:
        raise ValueError("Proportion must be between 0 and 1.")

    first_sub_frame = df_combined.sample(frac=proportion)

    second_sub_frame = df_combined.drop(first_sub_frame.index)

    return first_sub_frame, second_sub_frame

df1, df2 = df_split(df_combined, proportion=0.8)
print(df1.shape)
print(df2.shape)

# EXERCISE 3.5
train_df, test_df = df_split(df_combined, proportion=0.8)

train_df['index'] = 'train'
test_df['index'] = 'test'

concatenated_df = pd.concat([train_df, test_df]).set_index('index')

concatenated_df


# ### EXERCISE 4
# 
# Using the _.read_html_ function, collect infomation from any category of a public advertisement website (e.g., ss.lv):
# 1. Collect advertisements from 2-3 pages into data frames and concatenate them into one data frame
# 2. Develop a function for cleaning up the collected price - extracting numeric values. Apply the function for transforming the column _price_ of the data frame into numeric.
# 3. Calculate descriptive statistics of the prices - mean, median, standard deviation, min, max, etc.
# 4. Plot the box plot of prices

# In[24]:


# EXERCISE 4.0
import pandas as pd
import re
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from io import StringIO

ss_bmw = pd.read_html('https://www.ss.com/en/transport/other/the-sailing-charter/motorboats/', header=0)
main_table = sorted(ss_bmw,key=lambda x:len(x), reverse=True)[0]
main_table.dropna(axis='columns').head()


# In[25]:


# EXERCISE 4.1
def get_table_from_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    tables = pd.read_html(StringIO(str(soup)), header=0)
    main_table = sorted(tables, key=lambda x: len(x), reverse=True)[0]
    return main_table.dropna(axis='columns')

def scrape_pages(base_url, total_pages=4):
    all_data = []
    for page in range(1, total_pages + 1):
        url = f"{base_url}/page{page}.html"
        table = get_table_from_url(url)
        if table is None or len(table) == 0:
            print(f"No data found on page {page}")
            break
        all_data.append(table)
        print(f"Scraped page {page}")

    return pd.concat(all_data, ignore_index=True)

base_url = 'https://www.ss.com/en/transport/other/the-sailing-charter/motorboats'

result = scrape_pages(base_url)
result


# In[26]:


# EXERCISE 4.1.1
result.dtypes


# In[27]:


# EXERCISE 4.2
def clean_price(price):
 
    cleaned_price = re.sub(r'[^\d.]', '', price)

    try:
        numeric_price = float(cleaned_price)
    except ValueError:
        numeric_price = None
    
    return numeric_price

result['Price'] = result['Price'].apply(clean_price)

result


# In[28]:


# EXERCISE 4.2.1
result.dtypes


# In[29]:


# EXERCISE 4.3
price_stats = result['Price'].describe()

print("Descriptive statistics of prices:")
print(price_stats)

median_price = result['Price'].median()
print("\nMedian of prices:")
print(median_price)


# In[30]:


# EXERCISE 4.4
plt.figure(figsize=(10, 6))
plt.boxplot(result['Price'].dropna(), vert=False)
plt.title('Box Plot of Prices')
plt.xlabel('Price')
plt.show()


# ### EXERCISE 5
# 
# Using the _students_df_, _groups_df_, _courses_df_, and _results_df_ data frames from the presentations, construct the following data frames:
# 1. Course names with number of students, attended the course (0 if no students)
# 2. Group names with total number of students and average attendance values
# 3. Student names with average attendance and grades
# 4. Course names with number of students who attended (attendance>0), but don't have the final grade (NaN)
# 5. A main data frame that includes all information from the original data frames and illustrate extraction of the original data frames from the main one

# In[31]:


# EXERCISE 5.0.1
import pandas as pd

students_df = pd.read_csv('st_students.csv')
students_df.head()


# In[32]:


# EXERCISE 5.0.2
groups_df = pd.read_csv('st_groups.csv')
groups_df.head()


# In[33]:


# EXERCISE 5.0.3
courses_df = pd.read_csv('st_courses.csv')
courses_df.head()


# In[34]:


# EXERCISE 5.0.4
results_df = pd.read_csv('st_results.csv')
results_df.head()


# In[35]:


# EXERCISE 5.1
course_student_df = pd.merge(courses_df, results_df, on='course_id', how='left')

course_student_count = course_student_df.groupby('course_name')['student_id'].nunique().reset_index()

course_student_count.rename(columns={'student_id': 'number_of_students'}, inplace=True)

all_courses = courses_df['course_name'].to_frame()
course_student_count = pd.merge(all_courses, course_student_count, on='course_name', how='left')

course_student_count['number_of_students'].fillna(0, inplace=True)
course_student_count['number_of_students'] = course_student_count['number_of_students'].astype(int)

course_student_count.head()


# In[36]:


# EXERCISE 5.2
group_student_df = pd.merge(students_df, groups_df, on='group_id', how='left')

group_attendance_df = pd.merge(group_student_df, results_df, on='student_id', how='left')

group_info = group_attendance_df.groupby('group_name').agg(
    total_students=('student_id', 'nunique'),
    average_attendance=('attendance', 'mean')
).reset_index()

group_info['average_attendance'].fillna(0, inplace=True)

group_info.head()


# In[37]:


# EXERCISE 5.3
student_performance_df = pd.merge(students_df, results_df, on='student_id', how='left')

student_info = student_performance_df.groupby(['firstname', 'lastname']).agg(
    average_attendance=('attendance', 'mean'),
    average_grade=('grade', 'mean')
).reset_index()

student_info['average_attendance'].fillna(0, inplace=True)
student_info['average_grade'].fillna(0, inplace=True)

student_info.head()


# In[38]:


# EXERCISE 5.4
attended_no_grade_df = results_df[(results_df['attendance'] > 0) & results_df['grade'].isna()]

attended_no_grade_course_df = pd.merge(courses_df, attended_no_grade_df, on='course_id', how='left')

course_no_grade_count = attended_no_grade_course_df.groupby('course_name')['student_id'].nunique().reset_index()

course_no_grade_count.rename(columns={'student_id': 'number_of_students_no_grade'}, inplace=True)

course_no_grade_count.head()


# In[39]:


# EXERCISE 5.5.0
main_df = pd.merge(students_df, groups_df, on='group_id', how='left')

main_df = pd.merge(main_df, results_df, on='student_id', how='left')

main_df = pd.merge(main_df, courses_df, on='course_id', how='left')

main_df.head()


# In[40]:


# EXERCISE 5.5.1
extracted_students_df = main_df[['student_id', 'lastname', 'firstname', 'group_id']].drop_duplicates()
extracted_students_df.head()


# In[41]:


# EXERCISE 5.5.2
extracted_groups_df = main_df[['group_id', 'group_name', 'group_year_started']].drop_duplicates()
extracted_groups_df.head()


# In[42]:


# EXERCISE 5.5.3
extracted_courses_df = main_df[['course_id', 'course_name']].drop_duplicates()
extracted_courses_df.head()

