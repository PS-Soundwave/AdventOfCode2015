import hashlib


def day1_part1():
    line = open("day1.txt").readlines()[0][:-1]

    count = 0
    for c in line:
        if c == '(':
            count += 1
        if c == ')':
            count -= 1

    print(count)


def day1_part2():
    line = open("day1.txt").readlines()[0][:-1]

    count = 0
    for i, c in enumerate(line):
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
        if count < 0:
            print(i + 1)
            return


def day2_part1():
    lines = [line[:-1] for line in open("day2.txt").readlines()]

    amount = 0
    for line in lines:
        dims = [int(dim) for dim in line.split('x')]
        dims = sorted(dims)
        amount += 3 * dims[0] * dims[1] + 2 * dims[0] * dims[2] + 2 * dims[1] * dims[2]

    print(amount)


def day2_part2():
    lines = [line[:-1] for line in open("day2.txt").readlines()]

    amount = 0
    for line in lines:
        dims = [int(dim) for dim in line.split('x')]
        dims.sort()
        amount += 2 * dims[0] + 2 * dims[1] + dims[0] * dims[1] * dims[2]

    print(amount)


def day3_part1():
    line = open("day3.txt").readlines()[0][:-1]

    s = set()
    x = 0
    y = 0
    s.add((x, y))
    for c in line:
        if c == '^':
            y -= 1
        elif c == 'v':
            y += 1
        elif c == '>':
            x += 1
        elif c == '<':
            x -= 1
        s.add((x, y))

    print(len(s))


def day3_part2():
    line = open("day3.txt").readlines()[0][:-1]

    s = set()
    x = 0
    y = 0
    rx = 0
    ry = 0
    turn = True
    s.add((x, y))
    for c in line:
        if turn:
            if c == '^':
                y -= 1
            elif c == 'v':
                y += 1
            elif c == '>':
                x += 1
            elif c == '<':
                x -= 1
            s.add((x, y))
        else:
            if c == '^':
                ry -= 1
            elif c == 'v':
                ry += 1
            elif c == '>':
                rx += 1
            elif c == '<':
                rx -= 1
            s.add((rx, ry))
        turn = not turn

    print(len(s))


def day4_part1():
    line = open("day4.txt").readlines()[0][:-1]
    nonce = 1
    while True:
        result = hashlib.md5((line + str(nonce)).encode("ascii"))
        if result.hexdigest().startswith("00000"):
            print(nonce)
            return
        nonce += 1


def day4_part2():
    line = open("day4.txt").readlines()[0][:-1]
    nonce = 1
    while True:
        result = hashlib.md5((line + str(nonce)).encode("ascii"))
        if result.hexdigest().startswith("000000"):
            print(nonce)
            return
        nonce += 1


def day5_part1():
    lines = [line[:-1] for line in open("day5.txt").readlines()]

    result = 0
    for line in lines:
        vowel_count = 0
        double = False
        bad = False
        if line[-1] in ('a', 'e', 'i', 'o', 'u'):
            vowel_count += 1
        for i in range(0, len(line) - 1):
            if line[i] in ('a', 'e', 'i', 'o', 'u'):
                vowel_count += 1
            if line[i] == line[i + 1]:
                double = True
            if line[i] + line[i + 1] in ("ab", "cd", "pq", "xy"):
                bad = True
        if vowel_count >= 3 and double and not bad:
            result += 1

    print(result)


def day5_part2():
    lines = [line[:-1] for line in open("day5.txt").readlines()]

    result = 0
    for line in lines:
        double = False
        good = False
        for i in range(0, len(line) - 2):
            for j in range(i + 2, len(line) - 1):
                if line[i] + line[i + 1] == line[j] + line[j + 1]:
                    good = True
            if line[i] == line[i + 2]:
                double = True
        if double and good:
            result += 1

    print(result)


def day6_part1():
    lines = [line[:-1] for line in open("day6.txt").readlines()]

    grid = [[False for _ in range(0, 1000)] for _ in range(0, 1000)]
    for line in lines:
        line = line.split(" ")
        action = line[0]
        sx = 0
        ex = 0
        sy = 0
        ey = 0
        if action != "toggle":
            action = line[1]
            sx, sy = [int(c) for c in line[2].split(",")]
            ex, ey = [int(c) for c in line[4].split(",")]
        else:
            sx, sy = [int(c) for c in line[1].split(",")]
            ex, ey = [int(c) for c in line[3].split(",")]
        for i in range(sx, ex + 1):
            for j in range(sy, ey + 1):
                if action == "on":
                    grid[i][j] = True
                elif action == "off":
                    grid[i][j] = False
                elif action == "toggle":
                    grid[i][j] = not grid[i][j]

    result = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if grid[i][j]:
                result += 1

    print(result)


def day6_part2():
    lines = [line[:-1] for line in open("day6.txt").readlines()]

    grid = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]
    for line in lines:
        line = line.split(" ")
        action = line[0]
        sx = 0
        ex = 0
        sy = 0
        ey = 0
        if action != "toggle":
            action = line[1]
            sx, sy = [int(c) for c in line[2].split(",")]
            ex, ey = [int(c) for c in line[4].split(",")]
        else:
            sx, sy = [int(c) for c in line[1].split(",")]
            ex, ey = [int(c) for c in line[3].split(",")]
        for i in range(sx, ex + 1):
            for j in range(sy, ey + 1):
                if action == "on":
                    grid[i][j] += 1
                elif action == "off":
                    grid[i][j] -= 1
                    if grid[i][j] < 0:
                        grid[i][j] = 0
                elif action == "toggle":
                    grid[i][j] += 2

    result = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            result += grid[i][j]

    print(result)


def evaluate(netlist, net, memo):
    if net in memo:
        return memo[net]

    if not net[0].isalpha():
        return int(net)

    exp = netlist[net]

    if len(exp) == 1:
        result = evaluate(netlist, exp[0], memo)
        memo[net] = result
        return result

    b = "0"
    if exp[0] == "NOT":
        a = exp[1]
    else:
        a = exp[0]
        b = exp[2]

    if not a[0].isalpha():
        a = int(a)
    else:
        a = evaluate(netlist, a, memo)

    if not b[0].isalpha():
        b = int(b)
    else:
        b = evaluate(netlist, b, memo)

    result = 0
    if exp[0] == "NOT":
        result = (~a) & 0xFFFF
    elif exp[1] == "OR":
        result = (a | b) & 0xFFFF
    elif exp[1] == "AND":
        result = (a & b) & 0xFFFF
    elif exp[1] == "LSHIFT":
        result = (a << b) & 0xFFFF
    elif exp[1] == "RSHIFT":
        result = (a >> b) & 0xFFFF

    memo[net] = result
    return result


def day7_part1():
    lines = [line[:-1] for line in open("day7.txt").readlines()]

    netlist = {}
    for line in lines:
        line = line.split(" ")
        netlist[line[-1]] = line[:-2]

    print(evaluate(netlist, "a", {}))


def day7_part2():
    lines = [line[:-1] for line in open("day7.txt").readlines()]

    netlist = {}
    for line in lines:
        line = line.split(" ")
        netlist[line[-1]] = line[:-2]

    a = evaluate(netlist, "a", {})
    netlist["b"] = [str(a)]

    print(evaluate(netlist, "a", {}))


def day8_part1():
    lines = [line[:-1] for line in open("day8.txt").readlines()]

    result = 0
    for line in lines:
        i = 0
        while i < len(line):
            if line[i] == "\"":
                result += 1
                i += 1
            elif line[i] == "\\":
                result += 1
                i += 1
                if line[i] == "x":
                    result += 2
                    i += 3
                else:
                    i += 1
            else:
                i += 1

    print(result)


def day8_part2():
    lines = [line[:-1] for line in open("day8.txt").readlines()]

    result = 0
    for line in lines:
        result += 2
        i = 0
        while i < len(line):
            if line[i] == "\"":
                result += 1
            elif line[i] == "\\":
                result += 1
            i += 1

    print(result)


if __name__ == '__main__':
    day8_part2()
