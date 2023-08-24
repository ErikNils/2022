import os 


def _overlaps(path: str) -> tuple[int,int]:
    file = [line.strip() for line in open(path, "r")]
    
    sum1 = 0
    sum2 = 0

    for i,line in enumerate(file):
        assignments = line.split(",")
        assignment1 = [int(x) for x in assignments[0].split("-")]
        assignment2 = [int(x) for x in assignments[1].split("-")]
        
        
        if (assignment1[0] <= assignment2[0] and assignment1[1] >= assignment2[1]) or \
        (assignment2[0] <= assignment1[0] and assignment2[1] >= assignment1[1]):
            sum1 += 1
            
        if (assignment1[0] <= assignment2[0] and assignment1[1] >= assignment2[0]) or \
        (assignment2[0] <= assignment1[0] and assignment2[1] >= assignment1[0]):
            sum2 += 1
            
    return sum1, sum2


def main():
    path = os.path.dirname(os.path.realpath(__file__)) + "/input.csv"
    
    sum1, sum2 = _overlaps(path)
    print(f"Sum1: {sum1}")
    print(f"Sum2: {sum2}")



if __name__ == "__main__":
    main()