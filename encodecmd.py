# Description:
# This code encodes a command script using a substitution cipher. It generates a random lowercase alphabet table key for each
# letter in the English alphabet. Each key consists of a string of 6 lowercase letters forming a unique string. 
# The code then reads an input file, converts it to lowercase, and substitutes each letter with its corresponding key value. 
# Non-letter characters are left unchanged. The encoded message is then written to an output file along with the randomly generated key for each letter.
# The output file also includes a full encoded cmd file that can be used by the user. 
# If the input file is not found, an error message is displayed, and the program exits.

# Disclaimer
# This script is for educational and demonstration purposes only. 
# The author does not endorse or condone the use of this script for any criminal or malicious activities and it should only be used where explicitly
# allowed with proper permission.

# Author: Ag3nt047

# Input:
# The input file should be a text file in the format of a Windows command script. 
# The name of the input file is specified at the top of the script.

# Output:
# The output file will be a text file containing the encoded message in the format of a Windows command script. The name
# of the output file is specified at the top of the script.

# Example usage:
# Suppose the input file is named "unencoded.txt" and contains the text "echo Hello, world!". Running this script will
# generate an output file named "encoded.cmd" containing the encoded message. To decode the message, the output file
# should be run as a Windows command script.

import random
import os

# Input and output file names
input_file = "unencoded.cmd"
output_file = "encoded.cmd"

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Create a dictionary for the key
key = {}
for letter in alphabet:
    # Generate a random string of 6 lowercase letters to represent each letter of the alphabet
    value = ''.join(random.choice(alphabet) for i in range(6))
    key[letter] = f'{value}'

# Print the key for reference and write it to output file
with open(output_file, 'w') as f:
    # Add "@echo off" to the first line of the output file
    f.write("@echo off\n")
    
    key_items = list(key.items())
    random.shuffle(key_items)
    for letter, value in key_items:
        # print a line of 11 random letters before the next key line
        f.write(f":{''.join(random.choice(alphabet) for i in range(11))}\n")
        f.write(f"set {value}={letter}\n")

# Function to encode a string using the key
def encode(string):
    # Convert the string to lowercase
    string = string.lower()
    # Initialize an empty result string
    result = ""
    # Iterate over each character in the string
    for char in string:
        # If the character is a letter, replace it with its corresponding key value
        if char.isalpha():
            result += f"%{key[char]}%"
        # If the character is not a letter, leave it as is
        else:
            result += char
    # Return the encoded string
    return result

# Encode the input file and write the result to the output file
if os.path.exists(input_file):
    with open(input_file, 'r') as input_f, open(output_file, 'a') as output_f:
        message = input_f.read()
        encoded_message = encode(message)
        output_f.write(f":{''.join(random.choice(alphabet) for i in range(11))}\n")
        output_f.write(f"{encoded_message}\n")

    print(f"Original message:\n{message}")
    print(f"Encoded message:\n{encoded_message}")
    print(f"See {output_file} for full encoded cmd file to use")
    print("Finished.")
else:
    print(f"Error: {input_file} does not exist.")
