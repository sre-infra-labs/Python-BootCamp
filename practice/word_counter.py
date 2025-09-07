# Declare variables
string_pattern = 'word'
lines = []

print('Enter lines: \n')
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

def get_matching_line():
    """
    Generator to find next match line based on [string_pattern]
    """
    line_number = 0
    while True:
        if string_pattern in lines[line_number]:
            yield lines[line_number]
        line_number += 1

        # if no more lines to process
        if(line_number > len(lines)):
            return

if __name__ == '__main__':
    finder = get_matching_line()

    # get first match
    print(next(finder))
    # get second match
    print(next(finder))
    # get third match
    print(next(finder))


    """
Writing dummy words is funny
Usually it looks easier, but
I ran out of words now
Can you please help me with next word
    """