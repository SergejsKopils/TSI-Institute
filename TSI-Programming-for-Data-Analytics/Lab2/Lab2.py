#!/usr/bin/env python
# coding: utf-8

# # Python for Data Analytics
# ## Week 2 lab: Data Structures and Control Flow

# # Exercises
# 
# Please organise your solutions as a separate notebook and upload to the LMS (Moodle):
# * Notebook (.ipynb)
# * Generate pdf (File -> Download as -> PDF).

# ### EXERCISE 1
# 
# Review operations on lists (_adding/removing_ elements, _slicing_, _sorting_, etc.). Illustrate their usage on a list of your choice.

# In[1]:


cars_servis = {"Honda", "Toyota", "BMW", "Nissan", "Jeep", "VW", "Tesla"}

cars_servis.add("vw")
cars_servis.add("Hammer")
cars_servis.add("jeep")
cars_servis.remove("Jeep")

print("Welcom to cars servise EXERCISE 1.")
my_cars = input ("Enter your car model to check if it is in the database: ")

if my_cars in cars_servis:
    print(f"Congratulation, your {my_cars} is in the list, welcom!")
else:
    print(f"Sorry your {my_cars} is not in the list. ")


# ### EXERCISE 2
# 
# Review operations on sets (like _intersection_ or _pop_) using the table https://wesmckinney.com/book/python-builtin.html#tbl-table_set_operations and illustrate usage of at least 3 of them for a set of your choice.

# In[2]:


cars_servis1 = {"Honda", "Toyota", "BMW", "Nissan", "Jeep", "VW", "Tesla"}
cars_servis2 = {"Honda", "Toyota", "BMW", "Nissan", "Jeep", "VW", "Tesla","BMW", "VW", "Tesla", "KTM"}

difference = cars_servis2.difference(cars_servis1)
intersection = cars_servis2.intersection(cars_servis1)
union = cars_servis1.union(cars_servis2)

print("Welcom to EXERCISE 2")
my_cars = input ("What are you looking: difference, intersection or union ")


if my_cars == "difference":
    print(f"Congratulation, your difference {difference} is in the list, welcom!")  

elif my_cars == "intersection":
    print(f"Congratulation, your intersection {intersection} is in the list, welcom!")    

elif my_cars == "union":
    print(f"Congratulation, your union {union} is in the list, welcom!")

else:
    print(f"Sorry your input {my_cars} is not in the list. ")


# ### EXERCISE 3
# 
# Write a Python program to concatenate a tuple to a string.

# In[3]:


numbers = (1, 2, 3)
print(type(numbers))
print(numbers)

numbers = str(numbers)
print(type(numbers))
print(numbers)


# ### EXERCISE 4
# 
# Write a Python program to a string of comma-separated values into a tuple

# In[4]:


numbers = "1,2,3"
print(type(numbers))
print(numbers)

numbers_split = numbers.split(",")
print(type(numbers_split))
print(numbers_split)

numbers_split = tuple(numbers_split)
print(type(numbers_split))
print(numbers_split)


# ### EXERCISE 5
# 
# Write a Python program to check if all values in a list are different

# In[5]:


list1 = [1,1,2,2,3,4,5,6,7,8,9]
print(list1)

different = len(set(list1)) == len(list1)

if(different):
    print("List contains all unique elements")
    print(different)
else:
    print("List contains does not contains all unique elements")
    print(different)


# ### EXERCISE 6
# 
# Write a Python program calculate the product, multiplying all the numbers of a given tuple.
# 
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product: -864
# 
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product: 27648
# 
# 
# Original Tuple:
# (1, "Two", 3, "Four", 5)
# Product: 15

# In[6]:


list864 = (4, 3, 2, 2, -1, 18)
result = 1
for only_number in list864:
    result *= only_number
print(result)

list27648 = (2, 4, 8, 8, 3, 2, 9)
result = 1
for only_number in list27648:
    result *= only_number
print(result)


list15 = (1, "Two", 3, "Four", 5)
result = 1
for only_number in list15:
    if isinstance(only_number, int):
        result *= only_number

print(result)


# ### EXERCISE 7
# Write a script to:
# 
# * Print out the numbers from 1 to 20 but replacing numbers with 'Fizz' if divisible by 3, 'Buzz' if divisible by '5', and 'FizzBuzz' if divisible by 3 and 5.
# 
# Hint: the 'mod' operator, denoted %, is used to check divisibility. Example: 10 % 2 == 0.

# In[7]:


for num in range(1,21):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
         print("Buzz")

    else:
        print(num)


# ### EXERCISE 8
# 
# Write a program to:
# 1. Generate a random number (kept secret from the user) using random.randint(0, 32)
# 2. Prompt the user "Guess a number" and record their input.
# 3. Tell them if they were correct, too high, or too low.
# 
# BONUS POINTS: limit the number of guesses to 5.

# In[8]:


from random import randint

random_num = randint(0, 32)
print("Welcome to EXERCISE 8, Guess a number between 0 and 32")
print()
print("If you guessed the correct number in <= 5 attempts, you will receive BONUS POINTS.")
print()

attempts = 0

while True:    
    user_num = input()
    guess_num = int(user_num)
    attempts += 1
    
    if guess_num == random_num:
        print("You win!")
        if attempts <= 5:   
            print(f"Congratulations, You have +1 BONUS POINTS. Total: {attempts+1}")
        break
        
    elif guess_num < random_num:
        print("Try Higher")        
    elif guess_num > random_num:
        print("Try Lower")


# ### EXERCISE 9
# 
# Write a program that stores information about several European countries and their capital cities and conducts a quiz for the user: ask for a capital of a randomly selected country and validate the provided answer.
# 
# BONUS POINTS: Repeat 5 times and calculate the score

# In[9]:


print("EXERCISE 9")
import random

eu_country = {
    "Latvia": "Riga",
    "Estonia": "Tallinn",
    "Lithuania": "Vilnius",
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome",
    "United Kingdom": "London",
    "Netherlands": "Amsterdam",
    "Sweden": "Stockholm"
}

score = 0

for _ in range(5):
    country, capital = random.choice(list(eu_country.items()))
    print(f"What is the capital of {country}?")
    
    user_answer = input("Enter the capital city: ")
    
    if user_answer == capital:
        print("Correct!\n")
        score += 1
    else:
        print(f"The answer is not {user_answer!r}, the correct answer is {capital}.\n")
        
if score == 5:
    score += 1
    print(f"Congratulations, you have +1 BONUS POINTS {score}/5 !")
else:
    print(f"You scored {score}/5 BONUS POINTS!")


# ### EXERCISE 10
# 
# Develop a data structure for the following _Student_ object:
# 
# _Student_
# * ID
# * First name
# * Last name
# * Address
#     * Number
#     * Street
#     * City
#     * Country
#     * Postcode
#     * Coordinates
#         * Longitude
#         * Latitude
# * Courses
#     * Mathematics
#         * Attendance
#         * Final grade
#     * Programming
#         * Attendance
#         * Final grade
#     * Databases
#         * Attendance
#         * Final grade
#     * IT
#         * Attendance
#         * Final grade
# 
# Using the developed data structure, compose a list fo 3-4 students. Use the composed list for:
# 1. Printing all student names as "Last name, First name"
# 2. Getting a list of all grades for a specified course
# 3. Checking that all ID are unique
# 4. Finding students with identical addresses
# 5. Finding a student with the smallest attendance (sum of course attendances)
# 6. Finding a student with the highest performance (sum of grades)
# 7. Removing one of the students (and re-printing the list)
# 8. Finding a pair of students with closest addesses (based on coordinates)
# 

# In[10]:


student_1 = {
    "ID": "ID_ST1",
    "Fname": "FirstName1",
    "Lname": "LastName1",
    "Address": 
        {
        "Number": 3, 
        "Street": "PILS", 
        "City": "RIGA", 
        "Country": "LATVIA", 
        "Postcode": "LV1050",
        "Coordinates": 
            {
            "Longitude": 56.95079648641561, 
            "Latitude": 24.10080816776086
            }
        },
    "Courses": 
        {
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
    "Address": 
        {
        "Number": 1, 
        "Street": "LANVAS", 
        "City": "RIGA", 
        "Country": "LATVIA", 
        "Postcode": "LV1019",
        "Coordinates": 
            {
            "Longitude": 56.93937378695448, 
            "Latitude": 24.15610413561355
            }
        },
    "Courses": 
        {
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
    "Address": 
        {
        "Number": 6, 
        "Street": "VIKINGU", 
        "City": "JURMALA", 
        "Country": "LATVIA", 
        "Postcode": "LV2010",
        "Coordinates": 
            {
            "Longitude": 56.98138796275343, 
            "Latitude": 23.875114517214488
            }
        },
    "Courses": 
        {
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
    "Address": 
    {
        "Number": 27, 
        "Street": "BAZNICAS", 
        "City": "RIGA", 
        "Country": "LATVIA", 
        "Postcode": "LV1010",
        "Coordinates": 
            {
            "Longitude": 56.9573522440277, 
            "Latitude": 24.12044455167374
            }
    },
    "Courses": 
        {
        "Mathematics": {"Attendance": 70, "Final_grade": 7},
        "Programming": {"Attendance": 70, "Final_grade": 7},
        "Databases": {"Attendance": 70, "Final_grade": 7},
        "IT": {"Attendance" : 70, "Final_grade": 7}
        }        
}

students = [student_1, student_2, student_3, student_4]

# 1 Printing all student names as "Last name, First name"
print("\nEXERCISE 10.1 Printing all student names as 'Last name, First name' ".upper())

print()
for student in students: #ready
    print(f"Last name:", student["Lname"], "First name:", student["Fname"])
    
# 2 Getting a list of all grades for a specified course
print("\nEXERCISE 10.2 Getting a list of all grades for a specified course".upper())
print()    
for grades in students: 
    grade = grades.get("Courses",{}).get("Mathematics").get("Final_grade")
    print(f"Grade for mathematics: ", grade)

# 3 Checking that all ID are unique 
print("\nEXERCISE 10.3 Checking that all ID are unique".upper())
print()

for unique_ID in students:
    unique = unique_ID.get("ID")
    print(unique)
    
unique_ID = set(student["ID"] for student in students)

if len(unique_ID) == len(students):
    print("\nID are unique.")
else:
    print("\nID are not unique.")

# 4 Finding students with identical addresses - ready
print("\nEXERCISE 10.4 Finding students with identical addresses".upper())
address_st = {}

for student in students:
    city = student["Address"]["City"]
    if city not in address_st:
        address_st[city] = [student]
    else:
        address_st[city].append(student)

for city, st_address in address_st.items():
    if len(st_address) > 1:
        print(f"\nThe city of {city} has the same students:")
        for student in st_address:
            print(f"{student['Lname']}, {student['Fname']}")

# 5 Finding a student with the smallest attendance (sum of course attendances)
print("\nEXERCISE 10.5 Finding a student with the smallest attendance (sum of course attendances)".upper())
def min_attend(student):
    return sum(course["Attendance"] for course in student.get("Courses", {}).values())

min_attend_st = min(students, key=min_attend)
min_student = min_attend_st
math_attend = min_student["Courses"]["Mathematics"]["Attendance"]

print(f"\nAttendance for Mathematics for {min_student['Fname']} {min_student['Lname']}: {math_attend}")

####

min_attend_st = min(students, key=min_attend)

print("Student with the smallest attendance:", 
      min_attend_st["Fname"].strip(), min_attend_st["Lname"].strip(),",", 
      "Nr:", min_attend_st["ID"].strip(),".",
      "Total Attendance:", sum(course['Attendance'] for course in min_attend_st.get('Courses', {}).values()))

# 6 Finding a student with the highest performance (sum of grades)
print("\nEXERCISE 10.6 Finding a student with the highest performance (sum of grades)".upper())

def max_sum_grades(student):
    return sum(course["Final_grade"] for course in student.get("Courses", {}).values())
max_sum_grades = max(students, key=min_attend)

print("\nStudent with the highest performance", 
      max_sum_grades["Fname"].strip(), max_sum_grades["Lname"].strip(),",", 
      "Nr:", max_sum_grades["ID"].strip(),".",
      "Total sum:", sum(course['Final_grade'] for course in max_sum_grades.get('Courses', {}).values()))

# 7 Removing one of the students (and re-printing the list
print("\nEXERCISE 10.7 Removing one of the students (and re-printing the list)".upper())

students = [student_1, student_2, student_3, student_4]

print("\nList of students:")
for student in students:
    print("ID:", student["ID"], ", Name:", student["Fname"], student["Lname"])

students.remove(student_2)

print("\nUpdated list of students:")
for student in students:
    print("ID:", student["ID"], ", Name:", student["Fname"], student["Lname"])

# 8 Finding a pair of students with closest addesses (based on coordinates)
print("\nEXERCISE 10.8 Finding a pair of students with closest addesses (based on coordinates)".upper())

from math import radians, sin, cos, sqrt, atan2

def haversine_distance(coord1, coord2):
    
    R = 6371.0
    
    lat1, lon1 = radians(float(coord1["Latitude"])), radians(float(coord1["Longitude"]))
    lat2, lon2 = radians(float(coord2["Latitude"])), radians(float(coord2["Longitude"]))
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = R * c
    
    return distance

def find_closest_pair(students):
    
    closest_pair = None
    min_distance = float('inf')
    
    for i, student1 in enumerate(students):
        for j, student2 in enumerate(students):
            if i < j:
                distance = haversine_distance(student1["Address"]["Coordinates"], student2["Address"]["Coordinates"])
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (student1["ID"], student2["ID"])
    
    return closest_pair, min_distance

closest_pair, min_distance = find_closest_pair(students)

print("\nClosest pair of students:", closest_pair)
print("Minimum distance:", round(min_distance, 3), "km")


# ### EXERCISE 11
# 
# Develop a data structure for storing the graph data below:
# <img src="https://raw.githubusercontent.com/DmitryPavlyuk/python-da/main/week2/img/city_graph.png">
# 
# Extend the data with population of Latvian cities: https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Latvia
# 
# Use the composed data structure for:
# 1. Listing all cities, ordering them by population
# 2. Listing all cities directly connected to Riga, ordering them by distance
# 3. Finding a closiest city directly cinnected to Daugavpils

# In[11]:


print("\nEXERCISE 11. Develop a data structure for storing the graph data below:".upper())

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

ordering_cities = sorted(city_population.items(), key=lambda x: x[1], reverse=True)
print("\nCities, ordering by population:")
print()
for city, population in ordering_cities:    
    print(f"{city}: {population}")
    
    
connect_riga = sorted(city_connect_riga.items(), key=lambda x: x[1], reverse=False)
print("\nCities directly connected to Riga:")
print()
for connect, riga in connect_riga:    
    print(f"{connect}: {riga}")

    
connect_daugavpils = sorted(city_connect_daugavpils.items(), key=lambda x: x[0], reverse=True)
print("\nCities directly connected to Daugavpils:")
for connect, daugavpils in connect_daugavpils:    
    print(f"{connect}: {daugavpils}")    
closest_cities_daugavpils = [city for city, distance in city_connect_daugavpils.items() 
                  if distance == min(city_connect_daugavpils.values())]
print(f"The closest cities directly connected to Daugavpils are: {' and '.join(closest_cities_daugavpils)}")


# ### EXERCISE 12
# 
# Develop a data structure for storing the hierachical information of used cars:
# 
# Brand -> Model -> Car (year, price)
# 
# (1 brands, 2-3 models under each brand, 2-3 cars under each model).
# 
# Fill the structure with real data from a public source - e.g., http://www.ss.lv

# In[12]:


print("EXERCISE 12")
print("Develop a data structure for storing the hierachical information of used cars: Brand -> Model -> Car (year, price)")

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

ordering_cars = sorted(used_vw, key=lambda x: x.get("year", 0), reverse=True)

print("\nCars, ordering by year:")
print()

for car in ordering_cars:
    print(f"Model: {car.get('volkswagen')}, Year: {car.get('year',)}, Price: {car.get('price',)}")

