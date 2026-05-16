import sys


def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        sys.stdout.write("$ ")
        input = sys.stdin.readline().strip()
        if input == "exit":
            break
        sys.stdout.write(f"{input}: command not found\n")



if __name__ == "__main__":
    main()
