import random

TOTAL_ROWS = 10  # can be configured to generate different number of rows
TOTAL_COUNT = 6
lucky_row = []

for n in range(TOTAL_ROWS):
    for i in range(TOTAL_COUNT):
        lucky_number = random.randint(1, 49)

        while lucky_number in lucky_row:
            lucky_number = random.randint(1, 49)
        lucky_row.append(lucky_number)

    lucky_row.sort()
    print(' '.join(str(e) for e in lucky_row))
    lucky_row = []
