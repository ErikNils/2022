#!/usr/bin/python3
import os 
import string
from collections import deque






def _execute(file: list[str]):
    sub_directories: dict[str, set] = {}
    directories: dict[str, dict[str, int]] = {}
    stack = deque("/")
    
    ls_flag = False
    
    for line in file:
        command = line.split(" ")

        if command[0] == "$":
            if command[1] == "cd":
                _cd(command[2], stack, sub_directories)
                ls_flag = False
            if command[1] == "ls":
                ls_flag = True
        elif ls_flag:
            _ls(command, stack, sub_directories, directories)


    return _dir_size(directories)


def _cd(directory: str, stack: deque, sub_directories: dict[str, set]):
    if directory == "/":
        stack = deque("/")
    elif directory == "..":
        stack.pop()
    elif directory in sub_directories[stack[-1]]:
        stack.append(directory)


def _ls(command: list[str], stack: deque[str], sub_directories: dict[str, set], directories: dict[str, dict[str, int]]):
    if command[0] == "dir":
        if stack[-1] not in sub_directories:
            sub_directories[stack[-1]] = set()
        sub_dir = sub_directories[stack[-1]].add(command[1])
    
    elif command[0][0] in string.digits:
        for directory in stack:
            if directory not in directories:
                directories[directory] = {}
            directories[directory][command[0]] = int(command[0])
            
def _dir_size(directories: dict[str, dict[str, int]]):
    total_size = 0
    
    del_dir = directories.get("/")
    
    for directory in directories:
        files = directories[directory]
        dir_size = 0
        for file in files:
            dir_size += files[file]
        if dir_size <= 100000:
            total_size += dir_size
            print(f"Directory: {directory}, Size: {dir_size}")
        
    
    return total_size

def main():
    path = os.path.dirname(os.path.realpath(__file__)) + "/input.csv"
    file = [line.strip() for line in open(path, "r")]
    
    size = _execute(file)

    print(size)

if __name__ == "__main__":
    main()


