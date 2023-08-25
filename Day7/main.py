# #!/usr/bin/python3
import os 
import string
from collections import deque
from itertools import islice






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
        stack.append(f"/{directory}")


def _ls(command: list[str], stack: deque[str], sub_directories: dict[str, set], directories: dict[str, dict[str, int]]):
    if command[0] == "dir":
        if stack[-1] not in sub_directories:
            sub_directories[stack[-1]] = set()
        sub_dir = sub_directories[stack[-1]].add(command[1])
    
    elif command[0][0] in string.digits:
        
        for i in range(1,len(stack)+1):
            directory_list = islice(stack,i)
            directory = "".join(directory_list)
            if directory not in directories:
                directories[directory] = {}
            directories[directory]["/".join(command[1])] = int(command[0])
            
def _dir_size(directories: dict[str, dict[str, int]]):
    total_size = 0
    

    
    for directory in directories:
        files = directories[directory]
        dir_size = 0
        for file in files:
            dir_size += files[file]
        if dir_size <= 100000:
            total_size += dir_size
            # print(f"Directory: {directory}, Size: {dir_size}")
    
  
    
    return total_size

def main():
    path = os.path.dirname(os.path.realpath(__file__)) + "/input.csv"
    file = [line.strip() for line in open(path, "r")]
    
    size = _execute(file)
    print(size)

if __name__ == "__main__":
    main()


# #!/usr/bin/python3
# import sys
# from collections import defaultdict
# infile = sys.argv[1] if len(sys.argv)>1 else './Day7/input.csv'
# data = open(infile).read().strip()
# lines = [x for x in data.split('\n')]

# # directory path -> total size of that directory (including subdirectories)
# SZ = defaultdict(int)
# path = []
# for line in lines:
#     words = line.strip().split()
#     if words[1] == 'cd':
#         if words[2] == '..':
#             path.pop()
#         else:
#             path.append(words[2])
#     elif words[1] == 'ls':
#         continue
#     elif words[0] == 'dir':
#         continue
#     else:
#         sz = int(words[0])
#         # Add this file's size to the current directory size *and* the size of all parents
#         for i in range(1, len(path)+1):
#             SZ['/'.join(path[:i])] += sz

# max_used = 70000000 - 30000000
# total_used = SZ['/']
# need_to_free = total_used - max_used

# p1 = 0
# p2 = 1e9
# for k,v in SZ.items():
#     #print(k,v)
#     if v <= 100000:
#         p1 += v
#         print(f"Directory: {k.split('/')[-1]}, Size: {v}")
#     if v>=need_to_free:
#         p2 = min(p2, v)
# print(p1)
# print(p2)