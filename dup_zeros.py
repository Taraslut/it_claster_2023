def duplicate_zeros(donuts):
    rezult = []
    for i in range(len(donuts)):
        if donuts[i] == 0:
            rezult.append(0)
            rezult.append(0)
        else:
            rezult.append(i)
    return rezult


for item in duplicate_zeros([1, 2, 3, 4, 0, 1, 0, 2, 4]):
    print(item)
