
def _calculate_calories(path: str) -> list:
    calories_arr = []
    calories = 0
    with open(path, "r") as file:
        for line_raw in file:
            line = line_raw.strip()
            if line == "":
                calories_arr.append(calories)
                calories = 0
            else:
                calories += int(line) 
    
    return calories_arr

def main():
    calories_arr = _calculate_calories("./input.csv")
    print(max(calories_arr))
    print(sum(sorted(calories_arr)[-3:]))
    
if __name__ == '__main__':
    main()