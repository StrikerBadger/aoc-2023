def task_one(lines):
    currval = [int(x) for x in lines[0][7:].split(' ')]
    edited = [False for _ in currval]
    for line in lines[3:]:
        if 'map' in line or line == '':
            edited = [False for _ in currval]
            continue
        line_vals = [int(x) for x in line.split(' ')]
        to_add = line_vals[0] - line_vals[1]
        for i, val in enumerate(currval):
            if edited[i] or val < line_vals[1] or val >= line_vals[1]+line_vals[2]:
                continue
            currval[i] += to_add
            edited[i] = True
    return min(currval)
            
            
def task_two(lines):
    seeds = [int(x) for x in lines[0].split(' ')[1:]]
    seed_intervals = []
    
    def intersection(interval1, interval2): 
        if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
            return (-1, -1)
        return (max(interval1[0], interval2[0]), min(interval1[1], interval2[1]))
    
    def difference(interval1, interval2):
        intersect = intersection(interval1, interval2)
        if interval1 == interval2:
            return []
        elif intersect == (-1, -1):
            return [interval1, interval2]
        else:
            return [(min(interval1[0], interval2[0]), intersect[0]-1),
                    (intersect[1]+1, max(interval1[1], interval2[1]))]
        
        
    for i, start in enumerate(seeds):
        if i % 2 == 1:
            continue
        seed_intervals.append((False, (start, start+seeds[i+1]-1)))
    for line in lines[3:]:
        if 'map' in line or line == '':
            seed_intervals = [(False, interval) for _, interval in seed_intervals]
            continue
        line_vals = [int(x) for x in line.split(' ')]
        line_interval = (line_vals[1], line_vals[1]+line_vals[2]-1)
        to_add = line_vals[0] - line_vals[1]
        for i, seed_interval_meta in enumerate(seed_intervals):
            seed_interval = seed_interval_meta[1]
            edited = seed_interval_meta[0]
            if edited:
                continue
            intersecting_interval = intersection(seed_interval, line_interval)
            if intersecting_interval == (-1, -1):
                continue
            difference_of_intervals = difference(seed_interval, intersecting_interval)
            seed_intervals[i] = ((True, (intersecting_interval[0]+to_add, intersecting_interval[1]+to_add)))
            seed_intervals += [(False, diff) for diff in difference_of_intervals]
    return min([x[1][0] for x in seed_intervals])
            
    

if __name__ == '__main__':
    # Read input.txt
    with open('day_5/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    solution_one = task_one(lines)
    solution_two = task_two(lines)
    print(f'Task one:\n{solution_one}')
    print()
    print(f'Task two:\n{solution_two}')