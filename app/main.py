import sys

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
            else:
                print(f"{command_param}: not found")
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
