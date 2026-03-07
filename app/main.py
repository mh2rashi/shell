import sys


def main():

    command = input("$ ")
    sys.stdout.write(f"{command}: command not found ")


if __name__ == "__main__":
    main()
