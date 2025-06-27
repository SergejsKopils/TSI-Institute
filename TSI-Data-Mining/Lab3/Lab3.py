#!/usr/bin/env python
# coding: utf-8

# # Python for Data Analytics
# ## Week 3 lab: Functions, Libraries, Files

# ### EXERCISE 1
# 
# Write a function _info_ that returns information about the argument:
# 
# * type
# * size in the memory
# * length (for sequence objects)
# * hash (if hashable)
# 
# Test the function for the following types of objects: bool, str, int, float, list, tuple, dict, set

# In[1]:


import sys

def get_info(test):
    return {
        "Type": type(test).__name__,
        "Size in Memory": sys.getsizeof(test),
        "Length": len(test) if hasattr(test, "__len__") else None,
        "Hashable": hashable(test),
    }

def hashable(test):
    return isinstance(test, (bool, str, int, float, tuple, bytes))

get_tests = [True, "String", 314, 3.14, [3, 1, 4], (3, 1, 4), {"a": 3, "b": 1, "c": 4}, {3, 1, 4}]

get_tests.sort(key=lambda x: sys.getsizeof(x), reverse=False)
print("Information ordering by Size in Memory:\n")
for test in get_tests:
    result = get_info(test)
    print(f"Information for {test}:")
    for key, value in result.items():
        print(f"    {key}: {value}")
    print()


# ### EXERCISE 2
# 
# Extende the previous function to support lists, sets and tupples - it should provide info on all object in a collection argument.

# In[2]:


import sys

def get_info(test):
    def hashable(item):
        return isinstance(item,())

    def get_item_info(item):
        return {
            "Type": type(item).__name__,
            "Size in Memory": sys.getsizeof(item),
            "Length": len(item) if hasattr(item, "__len__") else None,
            "Hashable": hashable(item),
        }

    if isinstance(test, (list, set, tuple)):
        result = []
        for item in test:
            result.append(get_item_info(item))
        return result

get_tests = [[3, 1, 4], (3, 1, 4), {3, 1, 4}]

for test in get_tests:
    result = get_info(test)
    if isinstance(result, list):
        print(f"Information for {type(test).__name__}, {test}:")
        for item_info in result:
            print()
            for key, value in item_info.items():
                print(f"    {key}: {value}")
    print()


# ### EXERCISE 3
# 
# Write a programme that returns a list of first _n_ powers of 2:
# 
# get_list_2(5)
# 
# returns
# 
# 2, 4, 8, 16, 32
# 

# In[3]:


def get_power(n):
    powers_of = [power**i for i in range(1, get_list_of)]
    return powers_of

power = 2
get_list_of = 6

result = get_power(get_list_of)
print(result)


# ### EXERCISE 4
# 
# Write a programme that returns a list of powers of 2 between two specified arguments:
# 
# get_list_b(5, 50)
# 
# returns
# 
# 8, 16, 32

# In[4]:


def get_power(start, end):    
    powers_of = [power**i for i in range(int(start.bit_length()), end.bit_length()) 
    if power**i >= start and power**i <= end]
    return powers_of

power = 2    
start_value = 5
end_value = 50

result = get_power(start_value, end_value)
print(result)


# ### EXERCISE 5
# 
# The presentation notebook "3.2. Files" defines a function _print_file_head_ that prints the specified number of first symbols in the file. Write a function _print_file_tail_ that prints the specified number of last symbols in the file.

# In[5]:


def print_file_tail(filename, count=(500)):
    text = ""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            text = text + " " + str(line)
    tail = text[-count:]
    print("...")
    print(tail)

file_name = 'alice_in_wonderland.txt'
print_file_tail(file_name, 40)


# ### EXERCISE 6
# 
# Write a function that returns the most frequently used word in the text argument

# In[6]:


import re

with open("alice_in_wonderland.txt", "r", encoding="utf-8") as file:
    text = file.read()
    
text=re.sub(r'[^A-Za-z ]+', '', text).lower().split()

words = set(text)
print(f"Total number of words: {len(words)}")

word_stat = {}
for word in words:
    word_stat[word] = text.count(word)
word_stat = sorted(word_stat.items(), key=lambda x: x[1], reverse=True)
print("Most popular words:")
word_stat[:10]


# ### EXERCISE 7
# 
# Write a function that use a list argument and returns a dictionary, where every list element is linked with its number of occurances in the list:
# 
# todict(["a", "b", "c", "b", "b", "c"])
# 
# returns
# 
# {
#     "a": 1,
#     "b": 3,
#     "c": 2
# }
# 

# In[7]:


def todict(lst):
    result_dict = {}
    for letter in lst:
        result_dict[letter] = result_dict.get(letter, 0) + 1
    return result_dict

input_list = ["a", "b", "c", "b", "b", "c"]
result = todict(input_list)
print(result)


# ### EXERCISE 8
# 
# Using the _country_dict_ data structure, loaded from JSON in the presentation notebook, print all different offcial country languages in the world

# In[8]:


import json

with open("countries.json", "r", encoding="utf-8") as file:
    data = json.load(file)

country_dict = data

unique_languages = sorted(set(language for country_data in country_dict.values() for language in country_data["languages"]))

for language in unique_languages:
    print(language)


# ### EXERCISE 9
# 
# Download any CSV data set from https://data.gov.lv/dati/lv/dataset and load it to Python programme. Print number of observations (lines) and a randomly selected observation.

# In[9]:


import csv
import random

with open("EXERCISE_9_kpi1.csv", "r", encoding="utf-8") as csv_file:
    lines = [tuple(line) for line in csv.reader(csv_file)]

n = random.randint(1, len(lines))

print(f"Randomly selected number of observations: {n}\n")
print("Randomly selected observation:")

chosen_rows = random.sample(lines, k=n)

chosen_values = [random.choice(row) for row in chosen_rows]
print(chosen_values)


# ### EXERCISE 10
# 
# Download any JSON data set from https://data.gov.lv/dati/lv/dataset and load it to Python programme. Print number of observations (high-level objects) and a randomly selected observation.

# In[10]:


import json
import random

with open("EXERCISE_10_political_parties_metadata.json", "r", encoding="utf-8") as file:
    data = json.load(file)

observations = data.get("tableSchema", {}).get("columns", [])

num_observations = len(observations)
print(f"Total number of observations: {num_observations}\n")

random_observation = random.choice(observations)
print("Randomly selected observation:\n")
print(json.dumps(random_observation, indent=2, ensure_ascii=False))


# ### EXERCISE 11
# 
# Develop a function that saves Python objects into JSON file of the given name and another function to restore them.
# 
# Illustrate usage of these functions for saving/restoring data structures from Lab 2 Exercise 10, Exercise 11, and Exercise 12.

# In[11]:


import json

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f'Data saved to {filename}')

def restore_from_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    print(f'Data restored from {filename}')
    return data

#Exercise_10_Lab2
student_1 = {
    "ID": "ID_ST1",
    "Fname": "FirstName1",
    "Lname": "LastName1",
    "Address": {
        "Number": 3, 
        "Street": "PILS", 
        "City": "RIGA", 
        "Country": "LATVIA", 
        "Postcode": "LV1050",
        "Coordinates": {
            "Longitude": 56.95079648641561, 
            "Latitude": 24.10080816776086
        }
    },
    "Courses": {
        "Mathematics": {"Attendance": 100, "Final_grade": 10},
        "Programming": {"Attendance": 100, "Final_grade": 10},
        "Databases": {"Attendance": 100, "Final_grade": 10},
        "IT": {"Attendance": 100, "Final_grade": 10}
    }
}

student_2 = {
    "ID": "ID_ST2",
    "Fname": "FirstName2",
    "Lname": "LastName2",
    "Address": {
        "Number": 1, 
        "Street": "LANVAS", 
        "City": "RIGA", 
        "Country": "LATVIA", 
        "Postcode": "LV1019",
        "Coordinates": {
            "Longitude": 56.93937378695448, 
            "Latitude": 24.15610413561355
        }
    },
    "Courses": {
        "Mathematics": {"Attendance": 90, "Final_grade": 9},
        "Programming": {"Attendance": 90, "Final_grade": 9},
        "Databases": {"Attendance": 90, "Final_grade": 9},
        "IT": {"Attendance": 90, "Final_grade": 9}
    }
}

student_3 = {
    "ID": "ID_ST3",
    "Fname": "FirstName3",
    "Lname": "LastName3",
    "Address": {
        "Number": 6, 
        "Street": "VIKINGU", 
        "City": "JURMALA", 
        "Country": "LATVIA", 
        "Postcode": "LV2010",
        "Coordinates": {
            "Longitude": 56.98138796275343, 
            "Latitude": 23.875114517214488
        }
    },
    "Courses": {
        "Mathematics": {"Attendance": 80, "Final_grade": 8},
        "Programming": {"Attendance": 80, "Final_grade": 8},
        "Databases": {"Attendance": 80,"Final_grade": 8},
        "IT": {"Attendance": 80, "Final_grade": 8}
    }
}

student_4 = {
    "ID": "ID_ST4",
    "Fname": "FirstName4",
    "Lname": "LastName4",
    "Address": {
        "Number": 27, 
        "Street": "BAZNICAS", 
        "City": "RIGA", 
        "Country": "LATVIA", 
        "Postcode": "LV1010",
        "Coordinates": {
            "Longitude": 56.9573522440277, 
            "Latitude": 24.12044455167374
        }
    },
    "Courses": {
        "Mathematics": {"Attendance": 70, "Final_grade": 7},
        "Programming": {"Attendance": 70, "Final_grade": 7},
        "Databases": {"Attendance": 70, "Final_grade": 7},
        "IT": {"Attendance" : 70, "Final_grade": 7}
    }
}


#Exercise_11_Lab2

city_population = {
    "Riga": 614987,
    "Jurmala": 50842,
    "Jelgava": 55384,
    "Ventspils": 33053,
    "Liepaja": 67335,
    "Valmera": 22408,
    "Jekabpils": 21179,
    "Rezekne": 26805,
    "Daugavpils": 79299,
}
city_connect_riga = {    
    "Jurmala": 38,
    "Jelgava": 45,
    "Valmera": 107,
    "Jekabpils": 140,
}
city_connect_daugavpils = {    
    "Rezekne": 89,
    "Jelgava": 230,
    "Jekabpils": 89,
}



#Exercise_12_Lab2
used_vw = [
    {"volkswagen": "amarok", "year": 2012, "price": 15500},
    {"volkswagen": "amarok", "year": 2017, "price": 27000},
    {"volkswagen": "amarok","year": 2013, "price": 13990},
    
    {"volkswagen": "arteon", "year": 2018, "price": 26900},
    {"volkswagen": "arteon", "year": 2018, "price": 21900},
    {"volkswagen": "arteon","year": 2021, "price": 35650},
    
    {"volkswagen": "beetle", "year": 2007, "price": 2600},
    {"volkswagen": "beetle", "year": 2002, "price": 2150},
    {"volkswagen": "beetle","year": 2013, "price": 8995}
]

save_to_json([student_1, student_2, student_3, student_4], 'students.json')
save_to_json(city_population, 'city_population.json')
save_to_json(city_connect_riga, 'city_connect_riga.json')
save_to_json(city_connect_daugavpils, 'city_connect_daugavpils.json')
save_to_json(used_vw, 'used_vw.json')


# ### EXERCISE 12
# 
# Organise all functions in a module (.py) and illustrate its import and usage.

# In[12]:


import exercise_module

exercise_module.exercise_1()
exercise_module.exercise_2()
exercise_module.exercise_3()
exercise_module.exercise_4()
exercise_module.exercise_5()
exercise_module.exercise_6()
exercise_module.exercise_7()
exercise_module.exercise_8()
exercise_module.exercise_9()
exercise_module.exercise_10()
exercise_module.exercise_11()

