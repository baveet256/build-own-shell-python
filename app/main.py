import sys


def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        sys.stdout.write("$ ")
        input = sys.stdin.readline().strip()
        if input == "exit":
            break
        if sys.argv[1] == "echo":
            for arg in sys.argv[2:]:
                sys.stdout.write(arg + " ")
            sys.stdout.write("\n")
        else:
            sys.stdout.write(f"{input}: command not found\n")



if __name__ == "__main__":
    main()
