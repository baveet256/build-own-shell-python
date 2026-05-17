import os
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
            elif input_list[1] == "type":
                sys.stdout.write(f"{input_list[1]} is a shell builtin\n")
            else:
                for dir in sys.path:
                    try:
                        with open(f"{dir}/{input_list[1]}") as f:
                            ## file exists 
                            ## checking if its executable 
                            if os.access(f"{dir}/{input_list[1]}", os.X_OK):
                                sys.stdout.write(f"{input_list[1]} is {dir}/{input_list[1]}\n")
                                break
                            else:
                                ## file exists but is not executable
                                continue
                    except FileNotFoundError:
                        ## file does not exist in this directory, check the next one
                        continue
                
                ## we are here if we have checked all directories and not found the command
                sys.stdout.write(f"{input_list[1]} not found\n")
                
            continue

        if input_list[0] == "echo":
            sys.stdout.write(" ".join(input_list[1:]) + "\n")
        else:
            sys.stdout.write(f"{input}: command not found\n")



if __name__ == "__main__":
    main()
