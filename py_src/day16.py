import re
import itertools

def parse_rules(lines):
    pattern = r'(?P<field>[a-z ]+): (?P<min1>[0-9]+)\-(?P<max1>[0-9]+) or (?P<min2>[0-9]+)\-(?P<max2>[0-9]+)'
    min_maxes = []
    for line in lines:
        groups = re.search(pattern, line).groupdict()
        min_maxes.append((int(groups['min1']), int(groups['max1'])))
        min_maxes.append((int(groups['min2']), int(groups['max2'])))
    return min_maxes

def parse_rules2(lines):
    pattern = r'(?P<field>[a-z ]+): (?P<min1>[0-9]+)\-(?P<max1>[0-9]+) or (?P<min2>[0-9]+)\-(?P<max2>[0-9]+)'
    min_maxes = {}
    for line in lines:
        groups = re.search(pattern, line).groupdict()
        min_maxes[groups['field']] = [
            (int(groups['min1']), int(groups['max1'])),
            (int(groups['min2']), int(groups['max2']))]
    return min_maxes


def parse_nearby_tickets(tickets, rules):
    vals = [
        val
        for ticket in tickets
        for val in map(int, ticket.split(','))]
    invalid = []
    for val in vals:
        if not any(m1 <= val <= m2 for m1, m2 in rules):
            invalid.append(val)
    return invalid

def parse_nearby_tickets2(tickets, rules):
    valid_tickets = []
    for ticket in tickets:
        parsed_ticket = map(int, ticket.split(','))
        if all(any(m1 <= val <= m2 for checks in rules.itervalues() for m1,m2 in checks) for val in parsed_ticket):
            valid_tickets.append(parsed_ticket)
    return valid_tickets

def part1(inpts):
    inpts = inpts.split("\n")
    rules = list(itertools.takewhile(lambda x: x!="", inpts))
    rest = list(itertools.dropwhile(lambda x: x!="", inpts))
    my_ticket = list(itertools.takewhile(lambda x: x!="", rest[1:]))
    nearby_tickets = list(itertools.dropwhile(lambda x: x!="", rest[1:]))
    nearby_tickets = nearby_tickets[2:]
    my_ticket = my_ticket[1:]
    min_maxes = parse_rules(rules)
    invalid_values = parse_nearby_tickets(nearby_tickets, min_maxes)
    return sum(invalid_values)

def matching_fields(val, min_maxes):
    return {name
            for name, checks in min_maxes.iteritems()
            for m1, m2 in checks
            if m1 <= val <= m2}
        
def part2(inpts):
    inpts = inpts.split("\n")
    rules = list(itertools.takewhile(lambda x: x!="", inpts))
    rest = list(itertools.dropwhile(lambda x: x!="", inpts))
    my_ticket = list(itertools.takewhile(lambda x: x!="", rest[1:]))
    nearby_tickets = list(itertools.dropwhile(lambda x: x!="", rest[1:]))
    nearby_tickets = nearby_tickets[2:]
    my_ticket = map(int, my_ticket[1].split(','))
    min_maxes = parse_rules2(rules)
    valid_tickets = parse_nearby_tickets2(nearby_tickets, min_maxes)
    import pdb; pdb.set_trace()
    possible_fields = [set(min_maxes.iterkeys()) for _ in min_maxes]
    for ticket in valid_tickets:
        for idx, val in enumerate(ticket):
            possible_fields[idx] &= matching_fields(val, min_maxes)
    while max(map(len, possible_fields)) > 1:
        for i in xrange(len(possible_fields)):
            if len(possible_fields[i]) == 1:
                for j in xrange(len(possible_fields)):
                    if len(possible_fields[j]) > 1:
                        possible_fields[j] -= possible_fields[i]

    import pdb; pdb.set_trace()
    fields = [f for fs in possible_fields for f in fs]
    pairing = {f:v for f,v in zip(fields, my_ticket)}
    return fields, pairing, reduce(lambda x,y: x*y, (v for k,v in pairing.iteritems() if k.startswith('departure')))

test_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

test_input2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

real_input = """<enter input here>"""

print part2(real_input)
