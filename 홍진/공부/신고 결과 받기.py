def solution(id_list, report, k):
    dict_reported = {}
    dict_reporter = {}
    for i in list(set(report)):
        reporter, reported = i.split()
        if reported in dict_reported.keys():
            dict_reported[reported] += 1
        else:
            dict_reported[reported] = 1
        if reporter in dict_reporter.keys():
            dict_reporter[reporter].append(reported) 
        else:
            dict_reporter[reporter] = [reported]
    # print(dict_reported)
    # print(dict_reporter)
    reported_people = []
    for i in dict_reported.keys():
        if dict_reported[i] >= k:
            reported_people.append(i)
    # print(reported_people)
    answer = []
    for i in id_list:
        cnt = 0
        # if i in reported_people:
        #     if dict_reported[i] >= k: cnt += 1
        if i in dict_reporter.keys():
            for j in reported_people:
                if j in dict_reporter[i]: cnt += 1
        answer.append(cnt)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))