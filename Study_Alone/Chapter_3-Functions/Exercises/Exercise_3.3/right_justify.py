# right_justify.py
# Lawrence X. Amlord
# License: GPL v3

def right_justify(s):
    offset = 70 - len(s)
    print((' ' * offset) + s)

right_justify('allen')
