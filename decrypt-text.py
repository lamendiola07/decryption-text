# Name: Logie A. Mendiola
# Year and Section: BSCPe 1-5
# Course: Object Oriented Programming
# Task: Program #2: Decryption


# Imported font colours
from termcolor import colored, cprint
from pyfiglet import figlet_format

first_colour = 'white'
second_colour = 'blue'
third_colour = 'yellow'
fourth_colour = 'red'
fifth_colour = 'green'

# Given encrypted text to decrypt
output_encrypt = "th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g"

import pyfiglet
from simple_colors import *

# Printing given encrypted text for reference
print(pyfiglet.figlet_format("\nHere is the Encrypted Text For This Program:\n", font = 'bulbhead'))
print(red(output_encrypt, ['bold', 'underlined']))
output_decrypt = ""

# Main code for decryption
for i in range (len(output_encrypt)):
    # if *, change to a
    if output_encrypt[i] == "*":
        output_decrypt += "a"
    
    # if &, change to e
    elif output_encrypt[i] == "&":
        output_decrypt += "e"
    
    # if #, change to i
    elif output_encrypt[i] == "#":
        output_decrypt += "i"
    
    # if +, change to o
    elif output_encrypt[i] == "+":
        output_decrypt += "o"
    
    # if !, change to u
    elif output_encrypt[i] == "!":
        output_decrypt += "u"
    
    else:
        output_decrypt += output_encrypt[i]

# Printing Results for Decrypted Text
print(pyfiglet.figlet_format("\nHere is the Decrypted Version of the Text:\n", font ='bulbhead'))
print(green(output_decrypt, ['bold', 'underlined']))
print(pyfiglet.figlet_format("\nThat's it for today! Thank you so much for participating and have a nice day! :D", font = 'bulbhead'))
