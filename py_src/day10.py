import itertools

test_input = """16
10
15
5
1
11
7
19
6
12
4"""

test_input2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

real_input = """<enter input here>"""

def parse_line(line):
    return int(line)



def part1(lines):
    input = [parse_line(line) for line in lines.split("\n")]
    input.append(0)
    input.append(max(input) + 3)
    input.sort()
    diffs = [input[y] - input[x] for x,y in zip(xrange(len(input) - 1), xrange(1, len(input)))]
    ones = [i for i in diffs if i == 1]
    threes = [i for i in diffs if i == 3]
    
    return diffs, len(ones), len(threes), len(ones) * len(threes)

def part2(lines):
    ip = [parse_line(line) for line in lines.split("\n")]
    ip.append(0)
    ip.append(max(ip) + 3)
    ip.sort(reverse=True)

    mp = {ip[0]: 1}
    remaining = ip[1:]
    acc = 1
    
    while True:
        # [0, 1, 2, 3, 6]
        if not remaining:
            break
        next = remaining[0]
        candidates = dict(filter(lambda x: x[0] <= next + 3, mp.iteritems()))
        candidates[next] = sum(candidates.itervalues())
        mp = candidates
        remaining = remaining[1:]
    return mp[0]

#print part1(real_input)
with open('/tmp/hello.in') as f:
    large_input = f.read()
    print part2(large_input)


