to_round = [1/1, 1/2, 1/3]

for item in to_round:
    if item%1 == 0:
        print("{:.0f}".format(item))
    else:
        print("{:.1f}".format(item))