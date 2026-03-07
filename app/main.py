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

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
