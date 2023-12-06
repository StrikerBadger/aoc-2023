import math

def task_one(lines):
    times = [int(x) for x in filter(lambda x: x != '', lines[0].split(' ')[1:])]
    distances = [int(x) for x in filter(lambda x: x != '', lines[1].split(' ')[1:])]
    res = 1
    for i, time in enumerate(times):
        discriminant = time**2 - 4*(distances[i] + 1)
        if discriminant < 0:
            res *= 0
        else:
            x_1, x_0 = math.floor((time + math.sqrt(discriminant))/2), math.ceil((time - math.sqrt(discriminant))/2)
            res *= x_1 - x_0 + 1
    return res
            

def task_two(lines):
    lines[0] = lines[0].replace(' ', '').replace(':', ' ')
    lines[1] = lines[1].replace(' ', '').replace(':', ' ')
    return task_one(lines)

if __name__ == '__main__':
    # Read input.txt
    with open('day_6/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    solution_one = task_one(lines)
    solution_two = task_two(lines)
    print(f'Task one:\n{solution_one}')
    print()
    print(f'Task two:\n{solution_two}')