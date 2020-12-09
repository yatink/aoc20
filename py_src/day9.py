from itertools import product

test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

real_input = """<enter input here>"""

    
def parse_line(line):
    return int(line)

def check(preamble, test):
    pairs = filter(lambda pair: pair[0]!=pair[1], product(preamble, preamble))
    for (x,y) in pairs:
        if x+y == test:
            return True
    return False

def part1(ip, preamble_size):
    ip = [parse_line(line) for line in ip.split("\n")]
    start = preamble_size
    for i in xrange(start, len(ip)):
        if not check(ip[i-preamble_size:i], ip[i]):
            return ip[i]

def part2(magic_number, ip):
    ip = [parse_line(line) for line in ip.split("\n")]
    start = 0
    end = 1
    while True:
        curr_sum = sum(ip[start:end])
        if curr_sum == magic_number:
            soln = ip[start:end]
            return min(soln) + max(soln)
        elif curr_sum > magic_number:
            start+= 1
            end = start + 1
        elif curr_sum < magic_number:
            end += 1
        
print part1(real_input, 25)
print part2(part1(real_input, 25), real_input)
