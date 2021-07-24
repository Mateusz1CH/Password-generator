#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""

#user console
print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

nr_letters_ch = []
nr_symbols_ch = []
nr_numbers_ch = []

#creation of list of random letters, numbers, symbols
for i in range(0,nr_letters):
    x = random.randint(0,len(letters)-1)
    choosen_letter = letters[x]
    nr_letters_ch.append(choosen_letter)
print("selected letters: {}".format(nr_letters_ch))

for j in range(0,nr_numbers):
    xx = random.randint(0,len(numbers)-1)
    choosen_number = numbers[xx]
    nr_numbers_ch.append(choosen_number)
print("selected numbers: {}".format(nr_numbers_ch))

for k in range(0,nr_symbols):
    xxx = random.randint(0,len(symbols)-1)
    choosen_symbol = symbols[xxx]
    nr_symbols_ch.append(choosen_symbol)
print("selected symbols: {}".format(nr_symbols_ch))

#creation of list with all elements
whole_list = nr_letters_ch + nr_symbols_ch + nr_numbers_ch

whole_list_len = len(whole_list)
whole_list_copy = whole_list.copy()

#password generator
for l in range(0,len(whole_list)):
    xxxx = random.randint(0,whole_list_len-1)
    whole_list_len = whole_list_len - 1
    z = whole_list_copy.pop(xxxx)
    password = password + str(z)

print("\nGenerated password:\n{}".format(password))