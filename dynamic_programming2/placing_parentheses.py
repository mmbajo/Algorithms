# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def Min_Max(i, j, mins, maxs, ops):
    minimum = 1000000000000000
    maximum = -10000000000000000
    for k in range(i, j):
        a = evalt(maxs[i][k], maxs[k + 1][j], ops[k])
        b = evalt(maxs[i][k], mins[k + 1][j], ops[k])
        c = evalt(mins[i][k], maxs[k + 1][j], ops[k])
        d = evalt(mins[i][k], mins[k + 1][j], ops[k])
        minimum = min([minimum, a, b, c, d])
        maximum = max([maximum, a, b, c, d])
    return (minimum, maximum)


def get_maximum_value(dataset):
    nums = dataset[::2]
    nums = [int(n) for n in nums]
    ops = list(dataset[1::2])
    mins = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums)):
        mins[i][i] = nums[i]
        
    maxs = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums)):
        maxs[i][i] = nums[i]

    for s in range(1, len(nums)):
        for i in range(len(nums) - s):
            j = i + s
            mins[i][j], maxs[i][j] = Min_Max(i, j, mins, maxs, ops)
    return maxs[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
