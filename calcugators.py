from itertools import combinations

print('n blanks?')
n_blanks = int(input())

print('total sum to target?')
target = int(input())

print("""Enter the numeric choices.
Enter 'done' when done.""")
choices = []
cur_choice = None
while(cur_choice != 'done'):
    cur_choice = input()
    try:
        c = int(cur_choice)
        choices.append(c)
        print('ok')
    except ValueError:
        if cur_choice != 'done':
            print('not a number; skipping')

print(n_blanks, target, choices)

for combo in combinations(choices, n_blanks):
    if sum(combo) == target:
        print()
        print(combo)
        print(sum(combo))
