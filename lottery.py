import random

def get_number():
    return random.randrange(1,46)

lotto = []
num = 0

while num < 6:
    number = get_number()
    if number not in lotto:
        lotto.append(number)
        num += 1

for i in sorted(lotto):
    print(i, end=" ")
