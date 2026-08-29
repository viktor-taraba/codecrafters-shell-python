import sys
import os
import itertools 
import subprocess

builtin_commands = ["exit", "echo", "type", "pwd"]


def is_executable(file_name):
    "helper function to check whether file_name is executable program"

    PATH = os.environ.get('PATH').split(os.pathsep)
    extensions = [''] # Always check the exact name first
    path_extensions = os.environ.get('PATHEXT', '.COM;.EXE;.BAT;.CMD').split(os.pathsep)
    extensions.extend([ext.lower() for ext in path_extensions])

    for directory, ext in itertools.product(PATH, extensions):
        file_path = os.path.join(directory, file_name + ext)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path
        else:
            pass
    else:
        return None


def main():
    while True:
        sys.stdout.write("$ ")
        command = input().strip()

        if command.lower() == "exit":
            break
        elif command.startswith("echo "):
            print(command[5:])
        elif command.startswith("pwd"):
            print(os.getcwd())

        elif command.startswith("type "):
            command_param = command[5:].strip()
            if command_param in builtin_commands:
                print(f"{command_param} is a shell builtin")
            else:
                # locate executable files - go through every directory in PATH 
                file_path = is_executable(command_param)
                if file_path:
                    print(f"{command_param} is {file_path}")
                else: # no file located in the fir loop
                    print(f"{command_param}: not found")

        elif command.startswith("cd "):
            folder_path = command[3:].strip()
            if os.path.exists(folder_path):
                os.chdir(folder_path)
            else:
                print(f"cd: {folder_path}: No such file or directory")

        else: # run a program
            program_parts = command.split()
            program_name = program_parts[0]

            if is_executable(program_name):
                subprocess.run(program_parts)
            else:
                sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()