def task_one(lines):
    scores = []
    for line in lines:
        card = line.split('|')
        non_eps = lambda x: x != ''
        winning = list(filter(non_eps, card[0].split(':')[1].split(' ')))
        numbers = list(filter(non_eps, card[1].split(' ')))
        hits = len(list(filter(lambda x: x in winning, numbers)))   
        if hits == 0:
            continue
        scores.append(2**(hits-1))
    return sum(scores)

def task_two(lines):
    amnts = {i: 1 for i in range(1, len(lines)+1)}
    for i, line in enumerate(lines):
        i += 1
        card = line.split('|')
        non_eps = lambda x: x != ''
        winning = list(filter(non_eps, card[0].split(':')[1].split(' ')))
        numbers = list(filter(non_eps, card[1].split(' ')))
        hits = len(list(filter(lambda x: x in winning, numbers)))
        for offset in range(1, hits+1):
            if i+offset > len(lines):
                break
            amnts[i+offset] += amnts[i]
    return sum(amnts.values())
        

if __name__ == '__main__':
    # Read input.txt
    with open('day_4/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    solution_one = task_one(lines)
    solution_two = task_two(lines)
    print(f'Task one:\n{solution_one}')
    print()
    print(f'Task two:\n{solution_two}')