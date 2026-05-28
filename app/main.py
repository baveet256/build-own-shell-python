import os
from pathlib import Path
import sys
import subprocess

def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        sys.stdout.write("$ ")
        input = sys.stdin.readline().strip()
        if input == "exit":
            break
        input_list = input.split()

        if input_list[0] == "type":
            if input_list[1] == "pwd":
                sys.stdout.write(f"{input_list[1]} is a shell builtin\n")
                continue
            if input_list[1] == "exit":
                sys.stdout.write(f"{input_list[1]} is a shell builtin\n")
                continue
            if input_list[1] == "type":
                sys.stdout.write(f"{input_list[1]} is a shell builtin\n")
                continue
            if input_list[1] == "echo":
                sys.stdout.write(f"{input_list[1]} is a shell builtin\n")
            
            else:
                for dir in os.environ.get('PATH', '').split(os.pathsep):
                    file_path = Path(f"{dir}/{input_list[1]}")
                    if file_path.is_file():
                        ## file exists, check if its executable 
                        if os.access(file_path, os.X_OK):
                                sys.stdout.write(f"{input_list[1]} is {file_path.absolute()}\n")
                                break
                ## we are here if we have checked all directories and not found the command
                else:
                    sys.stdout.write(f"{input_list[1]} not found\n")
                
            continue
        
        if input_list[0] == "pwd":
            sys.stdout.write(os.getcwd() + "\n")
            continue
        
        if input_list[0] == "cd":   
            if input_list[1] == "~":
                os.chdir(os.getenv('HOME'))
                continue
            if input_list[1] == "..":
                os.chdir(os.path.dirname(os.getcwd()))
                continue

            dir_path = Path(input_list[1])
            if dir_path.is_dir():
                os.chdir(dir_path)
            else:
                sys.stdout.write(f"cd: {input_list[1]}: No such file or directory\n")    
            continue

        if input_list[0] == "exit":
            sys.stdout.write("exit\n")
            break

        if input_list[0] == "echo":

            full_part = " ".join(input_list[1:])

            if full_part[0] == "'":

                part = full_part
                first_quote = part.find("'")
                second_quote = part.find("'", first_quote + 1)
                part = part[first_quote + 1:second_quote]
                sys.stdout.write(part + "\n")
                continue
            if full_part[0] == '"':
                part = full_part
                first_quote = part.find('"')
                second_quote = part.find('"', first_quote + 1)
                part = part[first_quote + 1:second_quote]
                sys.stdout.write(part + "\n")
                continue
           
            sys.stdout.write(full_part + "\n")
            continue

        ## check if path exists and is executable
        for dir in os.environ.get('PATH', '').split(os.pathsep):
                file_path = Path(f"{dir}/{input_list[0]}")
                if file_path.is_file() and os.access(file_path, os.X_OK):
                    subprocess.run(input_list, executable=str(file_path))
                    break
            ## we are here if we have checked all directories and not found the command
        else:
            sys.stdout.write(f"{input_list[0]}: command not found\n")


if __name__ == "__main__":
    main()
