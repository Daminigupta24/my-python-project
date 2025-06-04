# score_list=[12,32,34,54,23,45,56,34,67,78,12,21,9]
# max_score=score_list[0]
# for i in score_list:
#     if i>max_score:
#         max_score=i
# print(max_score)
#password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=""
for i in range(0,nr_letters):
    password=password+ (random.choice(letters))
for i in range(0,nr_symbols):
    password=password+(random.choice(symbols))
for i in range(0,nr_numbers):
    password+=random.choice(numbers)
print(password)
password_list=[]
for i in range(0,len(password)):
    password_list.append(password[i])
random.shuffle(password_list)#shuffle works with a list
print("".join(password_list))