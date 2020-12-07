import itertools

print('n blanks')
n_blanks = input()

print('total sum to target')
target = input()

print("""Enter the numeric choices.
Enter 'done' when done.""")
choices = []
cur_choice = None
while(cur_choice != 'done'):
    cur_choice = input()
    try:
        c = int(cur_choice)
        choices.append(c)
    except ValueError:
        pass

print(n_blanks, target, choices)
