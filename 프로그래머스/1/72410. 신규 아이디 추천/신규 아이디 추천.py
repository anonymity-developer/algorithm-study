import copy

def solution(new_id):
    reject_set = set(list('~!@#$%^&*()=+[{]}:?,<>/'))
    small_alpha = set(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    new_id = list(new_id)
    save_1 = []
    for a in new_id:
        if a in small_alpha:
            temp = a.lower()
            save_1.append(temp)
        else:
            save_1.append(a)
    save_2 = []
    for b in save_1:
        if b in reject_set:
            continue
        else:
            save_2.append(b)
    save_3 = []
    for i in range(len(save_2)):
        if i == 0:
            save_3.append(save_2[i])
        else:
            if save_3[-1]== '.' and save_2[i] == '.':
                continue
            save_3.append(save_2[i])
    save_4 = copy.deepcopy(save_3)
    if save_4[0] == ".":
        del save_4[0]
    if len(save_4) >= 1 and save_4[-1] == ".":
        del save_4[-1]
    save_5 = copy.deepcopy(save_4)
    if len(save_5) == 0:
        save_5.append('a')
    temp = copy.deepcopy(save_5)
    save_6 = []
    if len(save_5) >= 16:
        save_6 = temp[:15]
        if len(save_6) > 0 and save_6[-1] == ".":
            del save_6[-1]
    else:
      save_6 = temp  
    save_7 = copy.deepcopy(save_6)
    for i in range(2):
        if 1 <= len(save_7) < 3:
            save_7.append(save_7[-1])
    
    

            
        

#     answer = ''
    return ''.join(map(str, save_7))