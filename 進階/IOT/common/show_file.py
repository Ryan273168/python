import os

print(os.listdir())

file = input('Read File name:')
lines = open(file)

for each_lines in lines:
    each_lines = each_lines.strip()
    print(each_lines + '\n')