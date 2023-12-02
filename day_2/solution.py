def task_one(lines):
    constraints = {'red': 12, 'green': 13, 'blue': 14}
    valid_ids = []
    for line in lines:
        game, subsets = line.split(':')
        game_id = int(game.split(' ')[1])
        subsets = subsets.split(';')
        valid = True
        for subset in subsets:
            colors = subset.split(',')
            for color in colors:
                amnt, id = color.split(' ')[1:]
                amnt = int(amnt)
                valid = constraints[id] >= amnt and valid
        if valid:
            valid_ids.append(game_id)
    return sum(valid_ids)
        

def task_two(lines):
    powers = []
    for line in lines:
        _, subsets = line.split(':')
        subsets = subsets.split(';')
        maxs = {'red': -1, 'green': -1, 'blue': -1}
        for subset in subsets:
            colors = subset.split(',')
            for color in colors:
                amnt, id = color.split(' ')[1:]
                amnt = int(amnt)
                maxs[id] = maxs[id] if maxs[id] >= amnt else amnt
        res = 1
        for max in maxs.values():
            res *= max
        powers.append(res)
    return sum(powers)

if __name__ == '__main__':
    # Read input.txt
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    solution_one = task_one(lines)
    solution_two = task_two(lines)
    print(f'Task one:\n{solution_one}')
    print()
    print(f'Task two:\n{solution_two}')