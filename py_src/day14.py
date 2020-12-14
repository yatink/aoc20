import itertools
import re
from copy import deepcopy

test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

real_input = """<enter input here>"""

test_input2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


def parse_mask_line1(line):
    _, mask = line.split(' = ')
    ones = ''.join(['1' if c == '1' else '0' for c in mask])
    zeros = ''.join(['0' if c == '0' else '1' for c in mask])
    return int(ones, base=2), int(zeros, base=2)


def parse_mask_line2(line):
    _, mask = line.split(' = ')
    return mask

        
def parse_mem_line(line):
    pattern = r'mem\[(?P<mem_location>[0-9]+)\] = (?P<value>[0-9]+)'
    groups = re.search(pattern, line).groupdict()
    return int(groups['mem_location']), int(groups['value'])


def process_input(inpts):

    lines = inpts.split("\n")
    ones, zeros = parse_mask_line1(lines[0])
    mem = {}
    for line in lines[1:]:
        if line.startswith('mask'):
            ones, zeros = parse_mask_line1(line)
        if line.startswith('mem'):
            location, value = parse_mem_line(line)
            mem[location] = (value & zeros) | ones 
    return mem


def mask_x_mem(mask, mem):
    def m_x_m(i):
        mask_i, mem_i = i
        if mask_i == '1':
            return '1'
        if mask_i == 'X':
            return 'X'
        return mem_i
    return ''.join(map(m_x_m, zip(mask, mem)))

def process_input2(inpts):
    lines = inpts.split("\n")
    a = [0,1]
    mask = parse_mask_line2(lines[0])
    mem = {}
    for line in lines[1:]:
        if line.startswith('mask'):
            mask = parse_mask_line2(line)
        if line.startswith('mem'):
            location, value = parse_mem_line(line)
            mem_mask = mask_x_mem(mask, '{0:036b}'.format(location))
            idxs = len([idx for (idx, c) in enumerate(mask) if c == 'X'])
            combos = map(list, itertools.product(*([a] * idxs)))
            for combo in combos:
                str_mask = mem_mask.replace('X', '{}').format(*combo)
                mem_pos = int(str_mask, base=2)
                mem[mem_pos] = value
    return mem


def part1(inpt):
    mem = process_input(inpt)
    return sum(mem.itervalues())


def part2(inpt):
    mem = process_input2(inpt)
    print mem
    return sum(mem.itervalues())


print part1(real_input)
print part2(real_input)
