def solution(participant, completion):
    answer = '' 
    # for i in completion:
    #     participant.remove(i)     
    # print(participant[0])
    # return participant[0]
    
    # 단 한명
    # part, comple sort해서 비교
    
    # 
    dict1 = {}
    for i in participant:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
            
    for i in completion:
        dict1[i] -= 1
        
    for key, value in dict1.items():
        if value:
            return key
        
    return participant[0]