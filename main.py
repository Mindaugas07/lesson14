# 2. Create a function that adds a string ending to each member in a list.
# from typing import List, Union 
# def add_string(some_letters: str, list_of_varablies: [float,int, str]) -> list [float, int, str]:
#     return [str(member) + some_letters for member in list_of_varablies]

# print(add_string("sdf", [1, 2.4, "weqr"]))

# 4. Create a function that returns only strings with unique characters.

# def string_with_unique_char(string: str) -> list [str]:
#     special_characters = "$%^&*()-+?_=,<>/@"
#     splited_string = string.split(" ")
#     words_with_spec_chars = [word for word in splited_string if set(special_characters).intersection(word)]
       
#     return words_with_spec_chars
        
# print(string_with_unique_char("asdf 466%54 sadf: @dsaf %"))

# Task nr.1: 
# Create a mini program that takes 10 random numbers in one input ("1,2,5 76,89 ...etc")
# Write functions to: calculate their sum, multiplication of highest and lowest numbers
# and the function which makes a new string where numbers are positioned from highest to lowest.

# from random import randint

# def ten_random_integers_from_1_to_100_generator():
#     ten_random_numbers_list = [(randint(1, 100)) for i in range(10)]
#     return ten_random_numbers_list


# def calculate_sum_of_numbers(list_of_ten_random_numbers: list) -> int:
#     return sum(list_of_ten_random_numbers)

# print(calculate_sum_of_numbers(ten_random_numbers_list))

def ten_random_integers_from_input() -> list:
    input_string = input("Please enter 10 random integers from 1 to 100 in one string as '1, 6, 18, 45, 99 ...etc' ")
    ten_random_number_list = [int(number) for number in input_string.split(",")]
    return(ten_random_number_list)

# def multiplication_highest_lowest_number_from_list(ten_random_integers_from_input: list) -> int:
#     ten_interger_list = ten_random_integers_from_input() 
#     return max(ten_interger_list) * min(ten_interger_list)

# print(multiplication_highest_lowest_number_from_list(ten_random_integers_from_input))

def numbers_of_string_in_opposite_order(ten_random_integers_from_input: list) -> list:
    ten_integer_list = ten_random_integers_from_input()
    ten_integer_list.sort(reverse=True)
    return ten_integer_list

print(numbers_of_string_in_opposite_order(ten_random_integers_from_input))

# Task nr.2:
# Create a program , which takes 3 differnt sentences(ne maziau). The input should have all 
# error checking in mind. The program then should create a dictionary of whith key values 
# corresponding to words `long` (more than 9 letters in a words) `medium`(7 letters)
# `short` (5 words)(Short < 35% , medium: 25% , long 10%). Then the pgrogram should create a new sentences (if 3 provided, 3 new sentences should be returned) 
# with following rules attached:
# All sentences should have same (or less) words amount as entered one;
# The most frequent letter from the sentence (from input) should be dominated in a new sentence as well.

# The program should return new sentences with statitstics of ratio how many words was used from all sections 
# (as for exmpale: long 25%,medium 45%, short 30%)