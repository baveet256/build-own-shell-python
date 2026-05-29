import os
from pathlib import Path
import sys
import subprocess
import shlex

def parse_stdout_redirect(args):
    for idx, token in enumerate(args):
        if token in (">", "1>"):
            if idx + 1 < len(args):
                return idx, args[idx + 1]
            return idx, None
        if token.startswith("1>") and len(token) > 2:
            return idx, token[2:]
        if token.startswith(">") and len(token) > 1:
            return idx, token[1:]
    return None, None

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
            redirect_idx, output_file = parse_stdout_redirect(input_list[1:])
            if redirect_idx is not None:
                if not output_file:
                    sys.stdout.write("echo: missing output file\n")
                    continue
                echo_args = input_list[1:1 + redirect_idx]
                with open(output_file, "w") as file:
                    subprocess.run(["echo", *echo_args], stdout=file, text=True)    
                continue
            else:
                subprocess.run(["echo", *input_list[1:]], text=True)
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
            redirect_idx, output_file = parse_stdout_redirect(input_list[1:])
            if redirect_idx is not None:
                if not output_file:
                    sys.stdout.write("ls: missing output file\n")
                    continue
                ls_args = input_list[1:1 + redirect_idx]
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
