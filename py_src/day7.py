from collections import defaultdict
import re


test_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

real_input = """<paste problem input here>"""

def parse_part1(input):
    outer, inner = input.split(" bags contain ")
    if inner == "no other bags.":
        return
    inner_pattern = r'(?P<num>\d+) (?P<colour>[A-Za-z ]+) bags?[,\.]?'
    ret = []
    return [(outer, re.search(inner_pattern, x).groupdict()) for x in inner.split(",")]

def reduce_1(acc, x):
    acc[x[1]['colour']].add(x[0])
    return acc

def runner1(ip):
    parsed = [ix for x in filter(bool, [parse_part1(line) for line in ip.split("\n")]) for ix in x]
    return reduce(reduce_1, parsed, defaultdict(set))

def parse_part2(input):
    outer, inner = input.split(" bags contain ")
    if inner == "no other bags.":
        return {outer: []}
    inner_pattern = r'(?P<num>\d+) (?P<colour>[A-Za-z ]+) bags?[,\.]?'
    return {outer: [re.search(inner_pattern, x).groupdict() for x in inner.split(",")]}

def reduce2(acc, x):
    acc.update(x)
    return acc

def runner2(ip):
    parsed = [parse_part2(line) for line in ip.split("\n")]
    return reduce(reduce2, parsed)

def part1(bag_map, colour):
    print colour
    if colour not in bag_map:
        print set()
        return set()
    print bag_map[colour]
    return bag_map[colour] | reduce(lambda acc, x: acc | part1(bag_map, x), bag_map[colour], set())

def part2(bag_map, colour):
    print colour
    print bag_map[colour]
    current_level = sum(int(c['num']) for c in bag_map[colour])
    print current_level
    return current_level + sum((int(c['num']) * part2(bag_map, c['colour'])) for c in bag_map[colour])


parsed_entries = runner2(real_input)
print(parsed_entries)
num_bags = part2(parsed_entries, "shiny gold")
print num_bags
