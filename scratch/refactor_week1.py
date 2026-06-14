import sys

file_path = r'c:\Users\hp\OneDrive\Desktop\TinkeresLab\technical-innovation.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Delete Day 4 from sidebar
start_idx = -1
for i, line in enumerate(lines):
    if '<a class="day-btn" href="#day4Page">' in line:
        start_idx = i
        break

if start_idx != -1:
    lines.pop(start_idx)
    lines.pop(start_idx)
    lines.pop(start_idx)

# 2. Find Day 3 and Day 4 content
day3_idx = -1
day4_idx = -1
for i, line in enumerate(lines):
    if '<!-- DAY 3 FULL SCREEN -->' in line:
        day3_idx = i
    if '<!-- DAY 4 FULL SCREEN -->' in line:
        day4_idx = i

if day3_idx != -1 and day4_idx != -1:
    # Delete from day3_idx to day4_idx - 1
    del lines[day3_idx:day4_idx]

# 3. Rename Day 4 to Day 3 in the new Day 3 (old Day 4)
for i, line in enumerate(lines):
    if '<!-- DAY 4 FULL SCREEN -->' in line:
        lines[i] = line.replace('DAY 4', 'DAY 3')
    if '<div id="day4Page"' in line:
        lines[i] = line.replace('day4Page', 'day3Page')
    if '<h1 class="doc-title-main">Day 4:' in line:
        lines[i] = line.replace('Day 4:', 'Day 3:')

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('File updated successfully.')
