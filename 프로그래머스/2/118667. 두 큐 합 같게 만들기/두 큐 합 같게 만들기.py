def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    
    if total % 2 != 0:
        return -1

    target = total // 2
    q = queue1 + queue2
    n = len(queue1)

    left = 0
    right = n
    curr = sum(queue1)
    count = 0

    while left < len(q) and right < len(q):
        if curr == target:
            return count
        elif curr < target:
            curr += q[right]
            right += 1
        else:
            curr -= q[left]
            left += 1
        count += 1

    return -1