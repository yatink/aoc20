from collections import defaultdict

def part1(inpt):
    inpt = map(int, (i for i in inpt.split(',')))
    nums = defaultdict(list)
    for idx, i in enumerate(inpt, start=1):
        num = i
        nums[i].append(idx)

    current_ctr = idx
    while True:
        # import pdb; pdb.set_trace()
        # print "num : {}".format(num)
        # print nums
        if current_ctr == 30000000:
            return num
        current_ctr += 1
        if len(nums[num]) < 2:
            num = 0
        else:
            nums[num] = nums[num][-2:]
            n = nums[num][-1] - nums[num][-2]
            num = n
        nums[num].append(current_ctr)

test_input = "0,3,6"
real_input = "13,16,0,12,15,1"
print part1(real_input)
    
