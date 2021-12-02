def solveProblem1(instructions):
    horizontal = 0
    depth = 0
    for instruction in instructions:
        action = instruction.split(" ")[0]
        value = int(instruction.split(" ")[1])
        if (action == "up"):
            depth -= value
        elif (action == "down"):
            depth += value
        elif (action == "forward"):
            horizontal += value

    print(f"problem 1 is {depth * horizontal}")

def solveProblem2(instructions):
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        action = instruction.split(" ")[0]
        value = int(instruction.split(" ")[1])
        if (action == "up"):
            aim -= value
        elif (action == "down"):
            aim += value
        elif (action == "forward"):
            horizontal += value
            depth += aim * value
    
    print(f"problem 2 is {depth * horizontal}")

if __name__ == '__main__':
    try:
        with open("input.txt", "r") as file:
            data = [str(line.strip()) for line in file]
    except IOError:
        print("Error: Can't open file")
        import sys
        sys.exit(0)
    
    solveProblem1(data)
    solveProblem2(data)

    file.close()

