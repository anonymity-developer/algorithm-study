def solution(s):
    answer = []
    a = s[2:-2].split('},{') 
    b = []

    for check in a:
        temp = check.split(',')
        nums = []
        for i in temp:
            nums.append(int(i))
        b.append(nums)

    b.sort(key=len)

    seen = set()
    for group in b:
        for num in group:
            if num not in seen:
                seen.add(num)
                answer.append(num)

    return answer