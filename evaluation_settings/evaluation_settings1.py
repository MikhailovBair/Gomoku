from itertools import product
import json

cnt = 0
with open("./parameter2.py", "w") as write_file:
    write_file.write('eval_score = {')
    for i1, i2, i3, i4, i5 in product(range(-1, 2), range(-1, 2),
                                      range(-1, 2), range(-1, 2), range(-1, 2)):
        basic_value: float = (i1 + i2 + i3 + i4 + i5) / 5
        combo_value: float = 0
        cnt += 1
        if i1 == i2 == i3 == i4 == i5:
            combo_value += 100 * i1
        elif i1 == i2 == i3 == i4:
            combo_value += 0.95 * i1
        elif i1 == i2 == i3:
            combo_value += 0.75 * i1
        elif i1 == i2:
            combo_value += 0.25 * i1
        else:
            combo_value += 0.05 * i5

        if i1 == i2 == i3 == i4 == i5:
            combo_value += 100 * i5
        elif i2 == i3 == i4 == i5:
            combo_value += 0.9 * i5
        elif i3 == i4 == i5:
            combo_value += 0.75 * i5
        elif i4 == i5:
            combo_value += 0.25 * i5
        else:
            combo_value += 0.1 * i5

        value = basic_value * 0.02 + combo_value * 0.9
        write_file.write(str((i1, i2, i3, i4, i5)))
        write_file.write(': ')
        write_file.write(str(value))
        write_file.write(', \n             ')
    write_file.write('}')

    print(cnt)
