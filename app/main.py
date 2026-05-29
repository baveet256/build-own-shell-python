import os
from pathlib import Path
import sys
import subprocess
import shlex

def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        input = sys.stdin.readline().strip()
        if input == "":
            continue
        if input == "exit":
            break
        input_list = shlex.split(input)

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
            if ">" in input_list:
                redirect_idx = input_list.index(">")
                if redirect_idx + 1 >= len(input_list):
                    sys.stdout.write("echo: missing output file\n")
                    continue
                output_file = input_list[redirect_idx + 1]
                echo_args = input_list[1:redirect_idx]
                with open(output_file, "w") as file:
                    file.write(" ".join(echo_args) + "\n")
                continue
            else:
                sys.stdout.write(" ".join(input_list[1:]) + "\n")
                continue

        if input_list[0] == "cat":
            for file in input_list[1:]:
                file_path = Path(file)
                if file_path.is_file():
                    with open(file_path, 'r') as file:
                        sys.stdout.write(file.read())
                else:
                    sys.stdout.write(f"cat: {file}: No such file or directory\n")
            sys.stdout.flush()
            continue
        ## check if path exists and is executable

        if input_list[0] == "ls":
            if ">" in input_list:
                redirect_idx = input_list.index(">")
                if redirect_idx + 1 >= len(input_list):
                    sys.stdout.write("ls: missing output file\n")
                    continue
                output_file = input_list[redirect_idx + 1]
                ls_args = input_list[1:redirect_idx]
                with open(output_file, "w") as file:
                    subprocess.run(["ls", *ls_args], stdout=file, text=True)
                continue

            else:
                subprocess.run(["ls", *input_list[1:]], text=True)
                continue
        
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
