from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    answer = [0, 0]  # [가입자 수, 판매액]

    for rates in product(discounts, repeat=len(emoticons)):
        plus = 0
        total = 0

        for user_discount, user_limit in users:
            user_total = 0

            for emoticon_price, rate in zip(emoticons, rates):
                if rate >= user_discount:
                    discounted_price = emoticon_price * (100 - rate) // 100
                    user_total += discounted_price

            if user_total >= user_limit:
                plus += 1
            else:
                total += user_total

        if plus > answer[0]:
            answer = [plus, total]
        elif plus == answer[0]:
            answer[1] = max(answer[1], total)

    return answer
