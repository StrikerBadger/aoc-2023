def task_one(lines):
    waypoints = {waypoint.split(' = ')[0] : tuple(waypoint.split(' = ')[1][1:-1].split(', ')) for waypoint in lines[2:]}
    instructions = lines[0]
    curr_waypoint = 'AAA'
    step = 0
    while curr_waypoint != 'ZZZ':
        curr_waypoint = waypoints[curr_waypoint][0] if instructions[step % len(instructions)] == 'L'\
                        else waypoints[curr_waypoint][1]
        step += 1
    return step
        
def task_two(lines):
    waypoints = {waypoint.split(' = ')[0] : tuple(waypoint.split(' = ')[1][1:-1].split(', ')) for waypoint in lines[2:]}
    instructions = lines[0]
    curr_waypoints = list(filter(lambda x: x[-1] == 'A', waypoints.keys()))
    step = 0
    while curr_waypoint != 'ZZZ':
        curr_waypoint = waypoints[curr_waypoint][0] if instructions[step % len(instructions)] == 'L'\
                        else waypoints[curr_waypoint][1]
        step += 1
    return step




if __name__ == '__main__':
    # Read input.txt
    with open('day_8/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    # solution_one = task_one(lines)
    solution_two = task_two(lines)
    # print(f'Task one:\n{solution_one}')
    print()
    print(f'Task two:\n{solution_two}')