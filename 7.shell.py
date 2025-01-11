'''
1. Split the command
2. Test case '>' inlclude
    Indetify parts
    Run
3. Test case '<' include
    Indentify part
    Read file
    Print
4. Test case '|' include

4. Test other case
    Run
'''

import os
import subprocess

def process_output(command):
    # Indentify string parts
    parts = command.split( )
    index = parts.index('>')
    cmd = parts[:index]
    output_file = part[index + 1]

    # Run
    with open(output_file, 'w') as f:
        output = subprocess.run(cmd, stdout = f, stderr=subprocess.PIPE)

def process_input(command):
    #indentify string parts
    parts = command.split( )
    index = parts.index('<')
    cmd = parts[:index]
    input_file = part[index + 1]

    # Run
    with open(input_file, 'r') as f:
        result = subprocess.run(cmd, stdin=f, stdout=subprocess.PIPE, stderr=subprocess)
        print(result.stdout.decode())

def execute(command):
    parts = command.split()
    result = subprocess.run(parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())

def process_pipe(command):
    # Indentidy each process
    processes = command.split('|')
    prev_result = None
    for process in processes:
        parts = process.spilt()
        if prev_result == None:
            prev_result = subprocess.run(parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            result = subprocess.run(parts, stdin=prev_result, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())

def process(command):
    if '>' in command:
        process_output(command)
    elif '<' in command:
        process_input(command)
    elif '|' in command:
        process_pipe(command)
    else:
        execute(command)

def main():
    while True:
        try:
            command = input("Shell>> ")
            if command.lower() in ['exit', 'quit']:
                break
            process(command)
        except KeyboardInterrupt:
            print()
            break

if __name__ == "__main__":
    main()




    