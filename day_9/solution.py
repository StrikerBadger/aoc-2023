def task_one(lines):
    lines = [[int(x) for x in line.split(' ')] for line in lines]
    res = 0
    for line in lines:
        curr_sequence = line
        sequences = [curr_sequence]
        while not all(map(lambda x: x == 0, curr_sequence)):
            new_sequence = []
            for i, num in enumerate(curr_sequence):
                if i == 0:
                    continue
                new_sequence.append(num - curr_sequence[i-1])
            curr_sequence = new_sequence 
            sequences.append(curr_sequence)
        prediction = 0
        for sequence in sequences:
            prediction += sequence[-1]
        res += prediction
    return res
        
        

def task_two(lines):
    return task_one([' '.join(reversed(line.split(' '))) for line in lines])

if __name__ == '__main__':
    # Read input.txt
    with open('day_9/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    solution_one = task_one(lines)
    solution_two = task_two(lines)
    print(f'Task one:\n{solution_one}')
    print()
    print(f'Task two:\n{solution_two}')