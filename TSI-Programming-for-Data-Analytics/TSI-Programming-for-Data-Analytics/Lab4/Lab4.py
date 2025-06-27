#!/usr/bin/env python
# coding: utf-8

# # Python for Data Analytics
# ## Week 4 lab: Numerical Python with NumPy

# ### EXERCISE 1
# 
# Create:
# 1. A three-dimensional NumPy array of zeros
# 2. A two-dimensional NumPy array of random integer numbers (from a given range)
# 3. A three-dimensional NumPy array with first 27 prime numbers (you can use a primePy package or just enter them manually)
# 
# 

# In[1]:


import numpy as np

array_of_zeros = np.zeros((3,3,4))

np.random.randint(0, 2, size=(3, 4))
array_random_int = np.random.randint(0, 2, size=(3, 4))

np.random.randint(1, 28, size=(3,3,3))
prime_num = np.random.randint(1, 28, size=(3,3,3))
# prime_num = np.array(range(27)).reshape((3,3,3))

print("Three-dimensional NumPy array of zeros")
print(array_of_zeros)
print("\nTwo-dimensional NumPy array of random integer numbers")
print(array_random_int)
print("\nThree-dimensional NumPy array with first 27 prime numbers")
print(prime_num)


# ### EXERCISE 2
# 
# Write a programme to replace zeros with np.nan values in a given NumPy array
# 

# In[2]:


import numpy as np

def replace_zeros_with_nan(input_array):
    input_array = input_array.astype(float)
    zero_num = input_array == 0
    input_array[zero_num] = np.nan
    return input_array

input_array = np.random.randint(0, 3, size=(3,3,3))
array_with_nan = replace_zeros_with_nan(input_array)

print(f"Original array:\n", input_array)
print(f"\nReplaced zeros to (nan):\n",array_with_nan)


# ### EXERCISE 3
# 
# Create a NumPy array of booleans and illustrate the following methods
# 1. .any()
# 2. .all()
# 
# Apply these methods for the complete array and by every dimension (e.g., by rows)
# 
# 

# In[3]:


import numpy as np

boolean_array = np.random.choice([True, False], size=(2, 3))

print("Boolean Array:")
print(boolean_array)

print("\n.any() for the entire array:", boolean_array.any())
print(".all() for the entire array:", boolean_array.all())

print("\n.any() along axis 0 (columns):", boolean_array.any(axis=0))
print(".all() along axis 0 (columns):", boolean_array.all(axis=0))

print("\n.any() along axis 1 (rows):", boolean_array.any(axis=1))
print(".all() along axis 1 (rows):", boolean_array.all(axis=1))


# ### EXERCISE 4
# 
# Create two 4x4 NumPy arrays of random numbers from the range [0,100].
# Create a boolean mask from the second array, which is 1 for all value more than 50 and 0 otherwise and use it to filtering the first array (replace elements, where mask is 0, with zetos).
# 
# 

# In[4]:


import numpy as np

array1 = np.random.randint(0, 101, size=(4, 4))

array2 = np.random.randint(0, 101, size=(4, 4))

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

mask = (array2 > 50).astype(int) # .astype(bool)

print("\nBoolean mask for Array 2:\n", mask)

array1_filtered = np.where(mask, array1, mask)

print("\nFiltered Array 1:")
print(array1_filtered)


# ### EXERCISE 5
# 
# Write a  program to compute the mean, median, standard deviation, and variance of a given NumPy array along the second axis and provide several test cases for the programme. Recall the meaning of mentioned statistical characteristics.
# 
# 

# In[5]:


import numpy as np

def comp_prog(array):
    
    mean = np.mean(array, axis=1)
    median = np.median(array, axis=1)
    std_dev = np.std(array, axis=1)
    variance = np.var(array, axis=1)

    return mean, median, std_dev, variance


test_array1 = np.array(np.arange(1,10)).reshape(3,3)
test_array2 = np.random.randint(1, 100, size=(3, 3))

result1 = comp_prog(test_array1)
result2 = comp_prog(test_array2)

print("Test_1:")
print(test_array1)
print("Mean:", result1[0])
print("Median:", result1[1])
print("Standard Deviation:", result1[2])
print("Variance:", result1[3])
print()

print("Test_2:")
print(test_array2)
print("Mean:", result2[0])
print("Median:", result2[1])
print("Standard Deviation:", result2[2])
print("Variance:", result2[3])


# ### EXERCISE 6
# 
# Write a  program to calculate the difference between the maximum and the minimum values of a given NumPy array along the all available dimensions.
# 
# E.g., for a matrix:
# 
# [[1, 2, 3]
# 
#  [10, 2, 30]
# 
#  [5, 20, 10]]
# 
# 
# the programme should return:
# 
# Axis 0: [2, 28, 15]
# 
# Axis 1: [9, 18, 27]
# 

# In[6]:


import numpy as np

def calc_diff(array):
    diff_axis_0 = np.max(array, axis=0) - np.min(array, axis=0)
    diff_axis_1 = np.max(array, axis=1) - np.min(array, axis=1)

    print(f"Axis 0: {diff_axis_0}")
    print(f"Axis 1: {diff_axis_1}")

example_array = np.array([[1, 2, 3],
                          [10, 2, 30],
                          [5, 20, 10]])

calc_diff(example_array)


# ### EXERCISE 7
# 
# Create a 7x7 NumPy array of random integers and subset all possible 5x5 sub-arrays (including overlapping ones).

# In[7]:


import numpy as np

np.random.seed(42)

array_7x7 = np.random.randint(0, 10, size=(7, 7))

print("Original 7x7 array:")
print(array_7x7)
print()

subarray_size = 5

sub_arrays = []

for i in range(array_7x7.shape[0] - subarray_size + 1):
    for j in range(array_7x7.shape[1] - subarray_size + 1):
        sub_array = array_7x7[i:i+subarray_size, j:j+subarray_size]
        sub_arrays.append(sub_array)

for idx, sub_array in enumerate(sub_arrays):
    print(f"{subarray_size}x{subarray_size} Subarray {idx + 1}:\n{sub_array}\n")


# ### EXERCISE 8
# 
# Write a program that delete duplicates from a NumPy array and a provided dimension (e.g., duplicate rows). Records are duplicates if all value for all other dimensions are the same. Test the programme for 2D and 3D arrays.

# In[8]:


import numpy as np

def del_dupl(arr, axis=0):

    unique_arr = np.unique(arr, axis=0)
    return unique_arr

arr2D =  np.array([[1, 2, 3],
                   [4, 5, 6],
                   [1, 2, 3],
                   [7, 8, 9]])

print("Original 2D array:")
print(arr2D)
print("\n2D array with duplicates removed:")
print(del_dupl(arr2D))

arr3D = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[1, 2, 3], [7, 8, 9]],
                  [[1, 2, 3], [4, 5, 6]]])

print("\nOriginal 3D array:")
print(arr3D)
print("\n3D array with duplicates removed:")
print(del_dupl(arr3D))


# ### EXERCISE 9
# 
# Illustarate solution of 2-3 systems of linear equations from the "Mathematics for Data Analytics" course using np.linalg

# In[9]:


import numpy as np

A = np.array([[1, 1, 1], [1, -1, 2], [2, 1, 3]])
b = np.array([3, 2, 1])
x = np.linalg.solve(A, b)
print(f"Solution: {x}")

A = np.array([[-1, -1, -1], [-1, 1, -2], [-2, -1, -3]])
b = np.array([-3, -2, -1])
x = np.linalg.solve(A, b)
print(f"\nSolution: {x}\n")

A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
b = np.array([7, 7, 7])
x = np.linalg.solve(A, b)
print(f"Solution: {x}")


# ### EXERCISE 10
# 
# Load numeric data from the CSV file, utilised in Lab 3 Exercise 9 into a NumPy array and calculate its statistics (by columns)

# In[10]:


import numpy as np

def load_data(file_name):
    
    with open(file_name, 'r', encoding='utf-8') as file:
        column_names = file.readline().strip().split(',')
    
    data = np.genfromtxt(file_name, delimiter=',', dtype=float, skip_header=1)
    return data, column_names

def calculate_statistics(data, column_names):

    for i, name in enumerate(column_names):
        column = data[:, i]
        if np.isfinite(column).any(): #if np.all(float):    
            print(f"\nStatistics for column '{name}':")
            print("  Mean:", np.nanmean(column))
            print("  Median:", np.nanmedian(column))
            print("  Standard Deviation:", np.nanstd(column))
            print("  Minimum:", np.nanmin(column))
            print("  Maximum:", np.nanmax(column))
        else:
            print(f"\nColumn '{name}' is not numeric.")

def main():
    file_name = "EXERCISE_9_kpi1.csv"
    data, column_names = load_data(file_name)
    
    num_rows, num_columns = data.shape
    print(f"Number of columns: {num_columns}")
    print(f"Number of rows: {num_rows}")
       
    calculate_statistics(data, column_names)

if __name__ == "__main__":
    main()


# ### EXERCISE 11
# 
# Using the presentations for this week and any image of your choice, illustrate
# 1. Loading of an image into a Numpy array
# 2. Flipping the image (by sorting the array)
# 3. Rotating the image (by transposing)
# 4. Filtering R,G,and B colors
# 5. Clipping a reactangular area the image by slicing
# 6. Grayscaling of the image by different colour weighting schemes - https://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
# 
# 

# In[11]:


import numpy as np
from PIL import Image
from IPython.display import display

image_path = 'download.jpeg' #Guido van Rossum
image = Image.open(image_path)
image_arr = np.array(image)

flipped_image = Image.fromarray(image_arr[:, ::-1])
rotated_image = image.transpose(Image.ROTATE_180)

im_R = image_arr.copy()
im_R[150:250, 110:170, 1:] = 0
im_G = image_arr.copy()
im_G[150:250, 110:170, [0, 2]] = 0
im_B = image_arr.copy()
im_B[150:250, 110:170, :-1] = 0

clipped_image = Image.fromarray(image_arr[10:140, 20:130, :])

gray_lightness = ((np.max(image_arr, axis=2) + np.min(image_arr, axis=2)) / 2).astype('uint8')
gray_average = np.mean(image_arr, axis=2).astype('uint8')
gray_luminosity = (0.21 * image_arr[:, :, 0] + 0.72 * image_arr[:, :, 1] + 0.07 * image_arr[:, :, 2]).astype('uint8')

print("11.1.0 Loading of an Image:")
display(image)
print("11.2.0 Flipped Image by sorting the array:")
display(flipped_image)
print("11.3.0 Rotated Image by transposing:")
display(rotated_image)
print("11.4.1 Filtering by Red Channel:")
display(Image.fromarray(im_R))
print("11.4.2 Filtering by Green Channel:")
display(Image.fromarray(im_G))
print("11.4.3 Filtering by Blue Channel:")
display(Image.fromarray(im_B))
print("11.5.0 Clipping a reactangular area the Image by slicing:")
display(clipped_image)
print("11.6.1 Grayscaling of the image by (Lightness):")
display(Image.fromarray(gray_lightness))
print("11.6.2 Grayscaling of the image by (Average):")
display(Image.fromarray(gray_average))
print("11.6.3 Grayscaling of the image by (Luminosity):")
display(Image.fromarray(gray_luminosity))


# ### EXERCISE 12
# 
# Implement the following procedure for the text of "Alice in Wonderland" (see the Week 3 presentations):
# 1. Split the text into three pieces with similar number of words: Part1, Part2, Part3
# 2. For every part calculate the relative frequency of each word (number of word occurances divided by number of words in a Part)
# 3. Combine frequencies for all parts into NumPy array (the first dimension should correspond to the number of parts, 3)
# 4. Compare frequencies of word "alice" between the parts
# 5. Print 10 words with most significant (maximum) change of frequencies between parts
# 6. Print 10 words with most stable frequency (minimum) between parts
# 
# If you are interested in text analysis, read about TF-IDF - e.g., https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089
# 

# In[12]:


import numpy as np
import string
from collections import Counter

def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read().translate(str.maketrans('', '', string.punctuation))

def split_into_parts(text, n_parts=3):
    words = np.array(text.split())
    total_words = len(words)
    words_per_part = total_words // n_parts
    extra_words = total_words % n_parts

    parts = []
    for i in range(n_parts):
        start_index = i * words_per_part
        end_index = start_index + words_per_part
        if i == n_parts - 1:
            end_index += extra_words
        parts.append(words[start_index:end_index])
    
    return total_words, parts

def calculate_relative_frequencies(words):
    word_count = len(words)
    return {word: count / word_count for word, count in Counter(words).items()}

def frequency_difference(word, frequencies):
    freqs = [frequencies[i].get(word, 0) for i in range(len(frequencies))]
    return max(freqs) - min(freqs)

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

text = read_text('alice_in_wonderland.txt')
total_words, parts = split_into_parts(text)

print(f"Total words in the text: {total_words}")

relative_frequencies = [calculate_relative_frequencies(part) for part in parts]
all_words = set().union(*parts)

for i, part in enumerate(parts):
    write_to_file(f'part{i+1}.txt', ' '.join(part))
    print(f"Words in part {i+1}: {len(part)}")

for i, freq in enumerate(relative_frequencies):
    print(f"\nRelative frequencies for Part {i+1}:")
    top_10_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:10]
    for word, frequency in top_10_words:
        print(f"{word}: {frequency:.30f}")

alice_counts = [part.tolist().count('Alice') / len(part) for part in parts]
print("\nFrequency of 'Alice' in each part:", alice_counts)

word_differences = {word: frequency_difference(word, relative_frequencies) for word in all_words}
top_10_words = sorted(word_differences, key=word_differences.get, reverse=True)[:10]
top_10_words_dict = {word: word_differences[word] for word in top_10_words}

print("\nTop 10 words with the highest frequency differences:", top_10_words_dict)

most_stable_words = sorted(word_differences, key=word_differences.get)[:10]
most_stable_words_dict = {word: word_differences[word] for word in most_stable_words}

print("\nMost stable words:", most_stable_words_dict)


# In[ ]:




