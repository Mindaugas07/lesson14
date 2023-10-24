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


# def calculate_sum_of_numbers(list_of_ten_random_numbers) -> int:
#     return sum(list_of_ten_random_numbers)

# print(calculate_sum_of_numbers(ten_random_numbers_list))

# def ten_random_integers_from_input() -> list:
#     input_string = input("Please enter 10 random integers from 1 to 100 in one string as '1, 6, 18, 45, 99 ...etc' ")
#     ten_random_number_list = [int(number) for number in input_string.split(",")]
#     return (ten_random_number_list)

# def multiplication_highest_lowest_number_from_list(ten_random_integers_from_input: List[int]) -> int:
#     ten_interger_list: List[int] = ten_random_integers_from_input() 
#     return max(ten_interger_list) * min(ten_interger_list)

# print(multiplication_highest_lowest_number_from_list(ten_random_integers_from_input))

# # def numbers_of_string_in_opposite_order(ten_random_integers_from_input: List[int]) -> list:
# #     ten_integer_list = ten_random_integers_from_input()
# #     ten_integer_list.sort(reverse=True)
# #     return ten_integer_list

# # print(numbers_of_string_in_opposite_order(ten_random_integers_from_input))

# User enters two names separated by comma : for example :('Mindaugas PiktasDestytojas, Mindaugas Juokauja') 
# Create a function that would swipe surnames and will prduxe new name surname and 
# another function funtion that will swap names.

# from typing import List

# def names_from_input_to_tuple() -> tuple:
#     input_string: str = input("Enter two names separated by comma: for example ('Mindaugas PiktasDestytojas, Mindaugas Juokauja') " )
#     separate_names_string: str = input_string.replace(",", "")
#     separate_names_list: List[str] = separate_names_string.split(" ")
#     return separate_names_list[0] + " " + separate_names_list[3], separate_names_list[2] + " " + separate_names_list[1]
        

# print(names_from_input_to_tuple())

