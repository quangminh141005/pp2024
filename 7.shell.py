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
        output = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE)
        if output.stderr:
            print(output.stderr.decode())

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
        if result.stderr:
            print(result.stderr.decode())

def execute(command):
    parts = command.split()
    result = subprocess.run(parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())
    if result.stderr:
        print(result.stderr.decode())

def process_pipe(command):
    # Indentidy each process
    processes = command.split('|')
    prev_result = None
    for i, process in enumerate(processes):
        parts = process.strip().split()
        if i == 0:
            prev_result = subprocess.Popen(parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            result = subprocess.Popen(parts, stdin=prev_result.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = prev_result.communicate()       
    print(output.decode())
    if output.stderr:
        print(output.stderr.decode())

def process(command):
    try:   
        if '>' in command:
            process_output(command)
        elif '<' in command:
            process_input(command)
        elif '|' in command:
            process_pipe(command)
        else:
            execute(command)
    except Exception as e:
        print(f"Error: {e}")

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




    