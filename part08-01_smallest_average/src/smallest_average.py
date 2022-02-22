def smallest_average(person1: dict, person2: dict, person3: dict):
#person1 = {"name": "Anna", "result1": 1, "result2": 1, "result3": 1}
#person2 = {"name": "Anna", "result1": 2, "result2": 2, "result3": 2}
#person3 = {"name": "Anna", "result1": 3, "result2": 3, "result3": 3}
    scores_1 = []
    for k in person1:
        if k == "name":
            continue
        else:
            scores_1.append(person1[k])
    avg_1 = sum(scores_1) / 3

    scores_2 = []
    for k in person2:
        if k == "name":
            continue
        else:
            scores_2.append(person2[k])
    avg_2 = sum(scores_2) / 3

    scores_3 = []
    for k in person3:
        if k == "name":
            continue
        else:
            scores_3.append(person3[k])
    avg_3 = sum(scores_3) / 3

    if (avg_1 < avg_2) and (avg_1 < avg_3):
        return person1
    elif (avg_2 < avg_1) and (avg_2 < avg_3):
        return person2
    else:
        return person3