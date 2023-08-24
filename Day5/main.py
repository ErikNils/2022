import os 
import string



def _init_crates(file: list[str], crates: list[list]):
    
    for line in file:
        if line[1] == "1": break
        for i in range(1, len(line), 4):
            crate = line[i]
            if crate in string.ascii_uppercase:
                crates[i//4].append(crate)
                
    for crate in crates:
        crate.reverse()
        

def _move_crates(file: list[str], crates: list[list]):
    for i in range (10, len(file)):
        commands = [int(split) for split in file[i].strip().split(" ") if split[0] in string.digits]
        move = -commands[0]
        start = crates[commands[1]-1]
        end = crates[commands[2]-1]
        
        moving = start[move:]
        
        #####Part 1 ########
        #moving.reverse()
        ####################
        
        end += moving
        del start[move:]
        

def main():
    path = os.path.dirname(os.path.realpath(__file__)) + "/input.csv"
    file = [line for line in open(path, "r")]
    crates = [[] for _ in range(9)]
    
    _init_crates(file, crates)
    _move_crates(file, crates)
    print([crate[-1] for crate in crates])
  



if __name__ == "__main__":
    main()