def lights_on_individual_brightness(filename):
    on = 0
    w, h = 1000, 1000
    Matrix = [[0 for x in range(w)] for y in range(h)]
    ops = {
        "turn on": lambda x: x + 1,
        "turn off": lambda x: x - 1 if x else 0,
        "toggle": lambda x: x + 2}
    with open(filename) as f:
        for line in f:
            entries = line.split()
            if entries[0] == "turn":
                op = " ".join(entries[:2])
                left = entries[2].split(",")
                right = entries[4].split(",")
            else:
                op = entries[0]
                left = entries[1].split(",")
                right = entries[3].split(",")
            leftx = int(left[0])
            lefty = int(left[1])
            rightx = int(right[0])
            righty = int(right[1])
            for x in range(leftx, rightx + 1):
                for y in range(lefty, righty + 1):
                    Matrix[x][y] = ops[op](Matrix[x][y])

    for x in range(1000):
        for y in range(1000):
            on += Matrix[x][y]
    # print(f'Total on individual brightness: {on}')
    return on


if __name__ == '__main__':
    print(lights_on_individual_brightness("coding_challenge_input.txt"))
    print(lights_on_individual_brightness("coding_challenge_input2.txt"))
