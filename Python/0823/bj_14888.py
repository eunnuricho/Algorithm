def cal(idx, result):
    global _min, _max

    if idx == N:
        if result > _max:
            _max = result
        if result < _min:
            _min = result
        return

    if _opr[0] > 0:
        _opr[0] -= 1
        cal(idx + 1, result + nums[idx])
        _opr[0] += 1

    if _opr[1] > 0:
        _opr[1] -= 1
        cal(idx + 1, result - nums[idx])
        _opr[1] += 1

    if _opr[2] > 0:
        _opr[2] -= 1
        cal(idx + 1, result * nums[idx])
        _opr[2] += 1

    if _opr[3] > 0:
        _opr[3] -= 1
        if result < 0:
            cal(idx + 1, -((-result) // nums[idx]))
        else:
            cal(idx + 1, result // nums[idx])
        _opr[3] += 1

N = int(input())
nums = list(map(int, input().split()))
_opr = list(map(int, input().split()))      # +, -, *, %

_max = -9876543210
_min = 9876543210

cal(1, nums[0])

print(_max)
print(_min)