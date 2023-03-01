# EncodeCMD
This program encodes a given input file using a randomly generated key and writes the result to an output file. The encoding algorithm replaces each letter in the input file with a unique string of 6 lowercase letters, followed by the original letter enclosed in percentage signs. Non-letter characters are left as is.

## Disclaimer

This script is for educational and demonstration purposes only. The author does not endorse or condone the use of this script for any criminal or malicious activities and it should only be used where explicitly allowed with proper permission.

## Description:
This code encodes a command script using a substitution cipher. It generates a random lowercase alphabet table key for each
letter in the English alphabet. Each key consists of a string of 6 lowercase letters, followed by the original letter
enclosed in percentage signs, forming a unique string. The code then reads an input file, converts it to lowercase,
and substitutes each letter with its corresponding key value. Non-letter characters are left unchanged. The encoded
message is then written to an output file along with the randomly generated key for each letter. The output file
also includes a full encoded cmd file that can be used by the user. If the input file is not found, an error message is
displayed, and the program exits.

## Input:
The input file should be a text file with any arbitrary length and content, and must be located in the same directory
as this script. The name of the input file is specified at the top of the script.

## Output:
The output file will be a text file containing the encoded message in the format of a Windows command script. The name
of the output file is specified at the top of the script.

## Example usage:
Suppose the input file is named "unencoded.txt" and contains the text "echo Hello, world!". Running this script will
generate an output file named "encoded.cmd" containing the encoded message. To decode the message, the output file
should be run as a Windows command script.

![alt text](https://github.com/ATTACKnDEFEND/EncodeCMD/blob/main/images/running_script.png)


