def solveProblem1(instructions):
    coordinates = [0, 0]
    for instruction in instructions:
        instruction = instruction.split(" ")
        if (instruction[0] == "up"):
            coordinates[1] -= int(instruction[1])
        elif (instruction[0] == "down"):
            coordinates[1] += int(instruction[1])
        elif (instruction[0] == "forward"):
            coordinates[0] += int(instruction[1])

    print(f"problem 2 is {coordinates[0] * coordinates[1]}")

def solveProblem2(instructions):
    coordinates = [0, 0]
    aim = 0
    for instruction in instructions:
        instruction = instruction.split(" ")
        if (instruction[0] == "up"):
            #coordinates[1] -= int(instruction[1])
            aim -= int(instruction[1])
        elif (instruction[0] == "down"):
            #coordinates[1] += int(instruction[1])
            aim += int(instruction[1])
        elif (instruction[0] == "forward"):
            coordinates[0] += int(instruction[1])
            coordinates[1] += aim * int(instruction[1])
    
    print(f"problem 2 is {coordinates[0] * coordinates[1]}")

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

