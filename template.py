def task_one(lines):
    pass

def task_two(lines):
    pass

if __name__ == '__main__':
    # Read input.txt
    with open('day_%__DAY__%/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    solution_one = task_one(lines)
    solution_two = task_two(lines)
    print(f'Task one:\n{solution_one}')
    print()
    print(f'Task two:\n{solution_two}')