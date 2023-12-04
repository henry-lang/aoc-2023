def part_a(input: str):
    lines = input.split("\n")
    sum = 0
    for l in lines:
        nums = list(filter(lambda c: c.isnumeric(), l))
        sum += int(nums[0]) * 10
        sum += int(nums[-1])
    return sum


strs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def part_b(input: str):
    lines = input.split("\n")
    sum = 0
    for l in lines:
        for num_str in strs:
            l = l.replace(num_str, num_str * 2)
        for i, num_str in enumerate(strs):
            l = l.replace(num_str, str(i + 1))

        nums = list(filter(lambda c: c.isnumeric(), l))

        sum += int(nums[0]) * 10
        sum += int(nums[-1])
    return sum
