from itertools import combinations

print('n blanks?')
n_blanks = int(input())

print('total sum to target?')
target = int(input())

print("""Enter the numeric choices.
Enter 'done' or '' (blank) when done.""")
terminators = ['done', '']
choices = []
cur_choice = None
while(cur_choice not in terminators):
    cur_choice = input()
    try:
        c = int(cur_choice)
        choices.append(c)
        print('ok')
    except ValueError:
        if cur_choice not in terminators:
            print('not a number; skipping')

print('INPUTS:')
print(n_blanks, target, choices)
print()

print('SOLUTIONS:')
S = set()
for combo in combinations(choices, n_blanks):
    if sum(combo) == target:
        S.add(str(combo))
print('\n'.join([str(x) for x in S]))
