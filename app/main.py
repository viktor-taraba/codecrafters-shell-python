import sys
import os
import itertools 

builtin_commands = ["exit", "echo", "type"]

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input().strip()

        if command.lower() == "exit":
            break

        elif command.startswith("echo "):
            print(command[5:])

        elif command.startswith("type "):
            command_param = command[5:].strip()
            if command_param in builtin_commands:
                print(f"{command_param} is a shell builtin")
            
            # locate executable files
            else:
            # go through every directory in PATH 
                PATH = os.environ.get('PATH').split(os.pathsep)
                extensions = [''] # Always check the exact name first
                path_extensions = os.environ.get('PATHEXT', '.COM;.EXE;.BAT;.CMD').split(os.pathsep)
                extensions.extend([ext.lower() for ext in path_extensions])

                for directory, ext in itertools.product(PATH, extensions):
                    file_path = os.path.join(directory, command_param + ext)

                    if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                        print(f"{command_param} is {file_path}")
                        break
                    else:
                        pass
                else: # no file located in the fir loop
                    print(f"{command_param}: not found")

        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
