

rules_part1 = {
    "A X" : 1+3,
    "A Y" : 2+6,
    "A Z" : 3+0,
    "B X" : 1+0,
    "B Y" : 2+3,
    "B Z" : 3+6,
    "C X" : 1+6,
    "C Y" : 2+0,
    "C Z" : 3+3
}

rules_part2 = {
    "A X" : 3+0,
    "A Y" : 1+3,
    "A Z" : 2+6,
    "B X" : 1+0,
    "B Y" : 2+3,
    "B Z" : 3+6,
    "C X" : 2+0,
    "C Y" : 3+3,
    "C Z" : 1+6
}

def _calculate_score(path: str, rules: dict) -> int:
    score = 0
    with open(path, "r") as file:
        for line in file:
            outcome = line.strip()
            score += rules[outcome]
    
    return score

def main():
    score1 = _calculate_score("./input.csv", rules_part1)
    print(f"Score part1: {score1}")
    score2 = _calculate_score("./input.csv", rules_part2)
    print(f"Score part2: {score2}")


if __name__ == "__main__":
    main()