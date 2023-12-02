import requests
import os

# Hardcoded year
YEAR = 2023

# Get the input for the day
def get_day(day):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    r = requests.get(url, cookies={'session': os.environ['AOC_SESSION_COOKIE']})
    return r.text

# Create the directory for the day
def make_day_dir():
    folders = list(filter(lambda x: 'day' in x, os.listdir()))
    if folders == []:
        os.mkdir(f'day_1')
        return 1
    else:
        folders = sorted(folders)
        last_folder = folders[-1]
        last_day = int(last_folder.split('_')[-1])
        os.mkdir(f'day_{last_day+1}')
        return last_day+1
    

if __name__ == '__main__':
    day = make_day_dir()
    with open(f'day_{day}/input.txt', 'w') as f:
        f.write(get_day(day))
    with open(f'template.py', 'r') as f:
        file_text = f.read().replace('%__DAY__%', str(day))
    with open(f'day_{day}/solution.py', 'w') as f:
        f.write(file_text)
    print('New day has been created!')