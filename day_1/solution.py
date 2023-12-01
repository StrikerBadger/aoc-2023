def task_one(lines):
    digits = '0123456789'
    sum = 0
    for line in lines:
        line_digits = []
        for char in line:
            if char in digits:
                line_digits.append(char)
        sum += int(line_digits[0] + line_digits[-1])
    return sum

def task_two(lines):
    digit_mapping = dict(zip(['zero','one','two','three','four','five','six','seven','eight','nine'], range(10)))
    digits = '0123456789'
    line_res = []
    for line in lines:
        line_digits = []
        dead = [-1]
        for key, value in digit_mapping.items():
            pos = line.find(key)
            while pos not in dead:
                line_digits.append((pos, value))
                dead.append(pos)
                pos = line.find(key, pos+len(key))
        for key in digits:
            value = int(key)
            pos = line.find(key)
            while pos not in dead:
                line_digits.append((pos, value))
                dead.append(pos)
                pos = line.find(key, pos+len(key))
        line_digits = sorted(line_digits, key=lambda x: x[0])
        line_res.append(10*line_digits[0][1] + line_digits[-1][1])
    return sum(line_res)
    

if __name__ == '__main__':
    # Read input.txt
    with open('day_1/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    solution_one = task_one(lines)
    solution_two = task_two(lines)
    print(f'Task one:\n{solution_one}')
    print()
    print(f'Task two:\n{solution_two}')