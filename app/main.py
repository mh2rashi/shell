import sys


def main():

    while True: 
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()

        if command == "exit":
            break

        elif command[:4] == "echo":
            sys.stdout.write(f"{command[5:]}\n")

        elif command.startswith("type"):
             
            if command[5:] in ['echo', 'exit', 'type']:
                print(f"{command[5:]} is a shell builtin")
            else:
                print(f"{command[5:]}: not found")

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
