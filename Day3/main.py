import string
import os 


def _calc_priority(path: str, prioritization: dict) -> int:
    sum = 0
    
    file = [line.strip() for line in open(path, "r")]
    for line in file:
        size = len(line)//2
        compartment1 = line[:size]
        compartment2 = line[size:]
        for item in compartment1:
            if item in compartment2:
                sum += prioritization[item]
                break
    
    return sum

def _calc_badges(path: str, prioritization: dict) -> int:
    sum = 0
    
    file = [line.strip() for line in open(path, "r")]
    lines_badges = [file[i:i+3] for i in range(0, len(file), 3)]
    for lines in lines_badges:
        for item in lines[0]:
            if item in lines[1] and item in lines[2]:
                sum += prioritization[item]
                break
        
    return sum
    

def main():
    path = os.path.dirname(os.path.realpath(__file__)) + "/input.csv"
    prioritization = dict(zip(string.ascii_letters, range(1,53)))
    
    sum = _calc_priority(path, prioritization)
    print(sum)
    
    sum = _calc_badges(path, prioritization)
    print(sum)



if __name__ == "__main__":
    main()