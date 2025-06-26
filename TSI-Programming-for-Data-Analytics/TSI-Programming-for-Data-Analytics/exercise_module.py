import sys
import json
import csv
import random
import re

def get_info(test):
    def hashable(item):
        return isinstance(item, (bool, str, int, float, tuple, bytes))

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
    else:
        return {"Type": type(test).__name__, "Size in Memory": sys.getsizeof(test)}


def exercise_1():
    print("EXERCISE 1\n")

    get_tests = [True, "String", 314, 3.14, [3, 1, 4], (3, 1, 4), {"a": 3, "b": 1, "c": 4}, {3, 1, 4}]

    get_tests.sort(key=lambda x: sys.getsizeof(x), reverse=False)
    print("Information ordering by Size in Memory:\n")
    
    for test in get_tests:
        result = get_info(test)
        print(f"Information for {test}:")
        
        if isinstance(result, list):
            for item_info in result:
                print()
                for key, value in item_info.items():
                    print(f"    {key}: {value}")
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"    {key}: {value}")
        
        print()


def exercise_2():
    print("EXERCISE 2\n")

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

def get_power(n):
    powers_of = [power**i for i in range(1, n)]
    return powers_of


def exercise_3():
    print("EXERCISE 3\n")

    def get_power(start, end):
        powers_of = [power**i for i in range(1, end)]
        return powers_of

    power = 2
    get_list_of = 6

    result = get_power(power, get_list_of)
    print(result)


def get_power(start, end):
    powers_of = [power**i for i in range(int(start.bit_length()), end.bit_length())
                 if power**i >= start and power**i <= end]
    return powers_of


def exercise_4():
    print()
    print("EXERCISE 4\n")

    def get_power_range(start, end):    
        powers_of = [power**i for i in range(int(start.bit_length()), end.bit_length()) 
                      if power**i >= start and power**i <= end]
        return powers_of

    power = 2    
    start_value = 5
    end_value = 50

    result = get_power_range(start_value, end_value)
    print(result)


def print_file_tail(filename, count=(500)):
    text = ""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            text = text + " " + str(line)
    tail = text[-count:]
    print("...")
    print(tail)

def exercise_5():
    print()
    print("EXERCISE 5\n")

    file_name = 'alice_in_wonderland.txt'
    print_file_tail(file_name, 40)

def exercise_6():
    print()
    print("EXERCISE 6\n")

    with open("alice_in_wonderland.txt", "r", encoding="utf-8") as file:
        text = file.read()

    text = re.sub(r'[^A-Za-z ]+', '', text).lower().split()

    words = set(text)
    print(f"Total number of words: {len(words)}")

    word_stat = {}
    for word in words:
        word_stat[word] = text.count(word)
    word_stat = sorted(word_stat.items(), key=lambda x: x[1], reverse=True)
    print("Most popular words:")
    word_stat[:10]

def todict(lst):
    result_dict = {}
    for letter in lst:
        result_dict[letter] = result_dict.get(letter, 0) + 1
    return result_dict

def exercise_7():
    print()
    print("EXERCISE 7\n")

    input_list = ["a", "b", "c", "b", "b", "c"]
    result = todict(input_list)
    print(result)

def exercise_8():
    print()
    print("EXERCISE 8\n")

    with open("countries.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    country_dict = data

    unique_languages = sorted(set(language for country_data in country_dict.values() for language in country_data["languages"]))

    for language in unique_languages:
        print(language)

def exercise_9():
    print()
    print("EXERCISE 9\n")

    with open("EXERCISE_9_kpi1.csv", "r", encoding="utf-8") as csv_file:
        lines = [tuple(line) for line in csv.reader(csv_file)]

    n = random.randint(1, len(lines))

    print(f"Randomly selected number of observations: {n}\n")
    print("Randomly selected observation:")

    chosen_rows = random.sample(lines, k=n)

    chosen_values = [random.choice(row) for row in chosen_rows]
    print(chosen_values)

def exercise_10():
    print()
    print("EXERCISE 10\n")

    with open("EXERCISE_10_political_parties_metadata.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    observations = data.get("tableSchema", {}).get("columns", [])

    num_observations = len(observations)
    print(f"Total number of observations: {num_observations}\n")

    random_observation = random.choice(observations)
    print("Randomly selected observation:\n")
    print(json.dumps(random_observation, indent=2, ensure_ascii=False))

    
def exercise_11():
    print()
    print("EXERCISE 11\n")
    print("Data saved to students.json")
    print("Data saved to city_population.json")
    print("Data saved to city_connect_riga.json")
    print("Data saved to city_connect_daugavpils.json")
    print("Data saved to used_vw.json")
        
def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
#     print(f'Data saved to {filename}')

def restore_from_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    print(f'Data restored from {filename}')
    return data

# Exercise_10_Lab2
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
            "Longitude": "56.95079648641561", 
            "Latitude": "24.10080816776086"
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

# Exercise_11_Lab2
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

# Exercise_12_Lab2
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