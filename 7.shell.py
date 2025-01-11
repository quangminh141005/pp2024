'''
1. Split the command
2. Test case '>' inlclude
    Indetify parts
    Run
3. Test case '<' include
    Indentify part
    Read file
    Print
4. Test other case
    Run
'''

import os
import subprocess

def redirect_output(command):
    # Indentify string parts
    parts = command.split( )
    index = parts.index('>')
    input = parts[:index]
    output_file = part[index + 1]

    # Run
    with open(output_file, 'w') as f:
        output = subprocess.run(input, stdout = f, stderr=subprocess.PIPE)

def redirected_input(command):
    #indentify string parts
    parts = command.split( )
    index = parts.index('<')
    input_file = part[]