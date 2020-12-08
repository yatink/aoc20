from copy import deepcopy

test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

real_input = """<paste problem input here>"""

instr_ptr = 0
acc = 0
previously_run_instruction = set()

def parse_line(line):
    instr, num = line.split(" ")
    return instr, int(num)

def run(instructions, previously_run_instructions, instr_ptr, acc):
    #import pdb; pdb.set_trace()
    if instr_ptr in previously_run_instructions:
        print previously_run_instructions
        print instr_ptr
        return (acc, previously_run_instructions, False)
    else:
        previously_run_instructions.append(instr_ptr)

    try:
        current_instr, val = instructions[instr_ptr]
    except IndexError:
        return (acc, previously_run_instructions, True)
    if current_instr == "acc":
        acc += val
        instr_ptr += 1
    elif current_instr == "jmp":
        instr_ptr += val
    elif current_instr == "nop":
        instr_ptr += 1
    else:
        raise ValueError("Bad instruction")

    return run(instructions, previously_run_instructions, instr_ptr, acc)


def modify(instructions, previously_run_instructions):
    swap = {'jmp': 'nop', 'nop': 'jmp'}
    for attempt in xrange(len(previously_run_instructions)):
        candidate_instruction = instructions[previously_run_instructions[attempt]]
        if candidate_instruction[0] == "acc":
            continue
        elif candidate_instruction[0] in {'jmp', 'nop'}:
            modified_instructions = deepcopy(instructions)
            modified_candidate_instruction = swap[candidate_instruction[0]], candidate_instruction[1]
            modified_instructions[previously_run_instructions[attempt]] = modified_candidate_instruction
            acc, _, success = run(modified_instructions, [], 0, 0)
            if success:
                return acc, candidate_instruction
            else:
                continue

print run([parse_line(line) for line in real_input.split("\n")], list(), 0, 0)

def part2(code):
    # first run
    acc, path, _ = run(code, list(), 0, 0)
    return modify(code, path)

print part2([parse_line(line) for line in real_input.split("\n")])
