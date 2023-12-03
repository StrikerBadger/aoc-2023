def index_tuple(l, t):
    return l[t[0]][t[1]]

def search_point(pos, lines, visited):
    digits = '0123456789'
    found_nums = []
    for i_offset in [-1, 0, 1]:
        for j_offset in [-1, 0, 1]:
            search_pos = (pos[0]+i_offset, pos[1]+j_offset)
            if  (index_tuple(lines, search_pos) not in digits) or\
                (search_pos in visited):
                continue
            num = index_tuple(lines, search_pos)
            visited.add(search_pos)
            # Search to the left
            search_left_pos = (search_pos[0], search_pos[1]-1)
            while search_left_pos[1] >= 0 and \
                  search_left_pos not in visited and \
                  index_tuple(lines, search_left_pos) in digits:
                num = index_tuple(lines, search_left_pos) + num
                visited.add(search_left_pos)
                search_left_pos = (search_left_pos[0], search_left_pos[1]-1)
            # Search to the right
            search_right_pos = (search_pos[0], search_pos[1]+1)
            while search_right_pos[1] < len(lines[search_right_pos[0]]) and \
                  search_right_pos not in visited and \
                  index_tuple(lines, search_right_pos) in digits:
                num = num + index_tuple(lines, search_right_pos)
                visited.add(search_right_pos)
                search_right_pos = (search_right_pos[0], search_right_pos[1]+1)
            found_nums.append(int(num))
    return found_nums, visited

                
   
def task_one(lines):
    ignored = '0123456789.'
    taken_pos = set()
    resulting_numbers = []
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char in ignored:
                continue          
            taken_pos.add((i, j))      
            found_nums, taken_pos = search_point((i, j), lines, taken_pos)
            resulting_numbers += found_nums
    return sum(resulting_numbers)

def task_two(lines):
    taken_pos = set()
    resulting_numbers = []
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char != '*':
                continue          
            taken_pos.add((i, j))      
            found_nums, taken_pos = search_point((i, j), lines, taken_pos)
            if len(found_nums) == 2:
                resulting_numbers.append(found_nums[0]*found_nums[1])
    return sum(resulting_numbers)

if __name__ == '__main__':
    # Read input.txt
    with open('day_3/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    solution_one = task_one(lines)
    solution_two = task_two(lines)
    print(f'Task one:\n{solution_one}')
    print()
    print(f'Task two:\n{solution_two}')