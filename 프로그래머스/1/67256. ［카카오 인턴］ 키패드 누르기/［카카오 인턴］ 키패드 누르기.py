def solution(numbers, hand):
    answer = []
    L_set = (1, 4, 7, '*')   
    R_set = (3, 6, 9, '')
    now_L, now_R =  '*', '#'
    
    pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    def dist(a, b):
        (x1,y1), (x2,y2) = pos[a], pos[b]
        return abs(x1-x2) + abs(y1-y2)

    
    for i in numbers:
        if i in L_set:
            answer.append('L')
            now_L = i
        elif i in R_set:
            answer.append('R')
            now_R = i
        else:
            dl, dr = dist(now_L, i), dist(now_R, i)
            if dl < dr or (dl == dr and hand == "left"):
                answer.append('L')
                now_L = i
            else:
                answer.append('R')
                now_R = i
            
    return  ''.join(answer)