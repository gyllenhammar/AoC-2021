
def solveProblem1(numbers):
    num_increase = 0
    prev_number = 0

    for number in numbers:
        if int(number) > prev_number:
            num_increase = num_increase + 1
        prev_number = int(number)

    print(f"problem 1 is {num_increase - 1}")

def solveProblem2(numbers):
    num_increase = 0
    
    for i in range(2, len(numbers) -1):
        if (numbers[i - 2] + numbers[i - 1] + numbers[i]) < (numbers[i-1] + numbers[i] + numbers[i + 1]):
            num_increase += 1
    
    print(f"problem 2 is {num_increase}")


if __name__ == '__main__':
    try:
        with open("input.txt", "r") as file:
            data = [int(line.strip()) for line in file]
    except IOError:
        print("Error: Can't open file")
        import sys
        sys.exit(0)
    
    solveProblem1(data)
    solveProblem2(data)

    file.close()