import sys


def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        sys.stdout.write("$ ")
        input = sys.stdin.readline().strip()
        if input == "exit":
            break
        input_list = input.split()

        if input_list[0] == "type":
            if input_list[1] == "echo":
                sys.stdout.write(f"{input_list[1]} is a shell builtin\n")
            elif input_list[1] == "exit":
                sys.stdout.write(f"{input_list[1]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{input_list[1]} not found\n")
                
        if input_list[0] == "echo":
            sys.stdout.write(" ".join(input_list[1:]) + "\n")
        else:
            sys.stdout.write(f"{input}: command not found\n")



if __name__ == "__main__":
    main()
