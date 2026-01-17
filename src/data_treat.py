"""This file conatains all the functions that will operate on data to analyse and filtrate data.
This file is for data treatment and analyse."""

def average_score(dictionnary):
    if not dictionnary: #To count the average score only if dictionnay is not empty -> len(dictionnary) = 0
        return None
    total = 0
    num_pers = 0
    for tupple in dictionnary:
        total += dictionnary[tupple]
        num_pers += 1
    average = total / num_pers
    return f"{average:.2f}"


#find_best and find_worst are repetitive, so i'll use find function as a help function to avoid repetition code
def find(dictionnary, value):
    if not dictionnary: #To find the person, i need data in the datastructure and it can't be a none data
        return None
    for key in dictionnary:
        if dictionnary[key] == value:
            result = f"Name: {key[0]}, Age: {key[1]}, Score: {value}" #formate the returned value and return it
    return result


def find_best(dictionnary):
    if not dictionnary:
        return None
    maximum = max(dictionnary.values()) #find the highest score by going through all of the items
    best = find(dictionnary, maximum)
    return best
    

def find_worst(dictionnary):
    if not dictionnary:
        return None
    last = min(dictionnary.values())
    worst = find(dictionnary, last)         
    return worst

#score filter and age filter is repetitive, it can be a third one where you put a last argument "age" or "score" and it does it for you
def filter(dictionnary, value, topic):
    filtered = {}
    if topic.lower() == "score":
        for person in dictionnary:
            if dictionnary[person] >= value:
                filtered[person] = dictionnary[person] #make another dictionnary containing filtered persons based on a minimum score
    elif topic.lower() == "age":
        for person in dictionnary:
            if person[1] <= value:
                filtered[person] = dictionnary[person] #make another dictionnary containing filtered persons based on a maximum age
    return filtered


def score_filter(dictionnary, minscore):
    return filter(dictionnary, minscore, "Score")


def age_filter(dictionnary, maxage):
    return filter(dictionnary, maxage, "Age")


def combined_filter(dictionnary, minscore, maxage):
    my_list = []
    score_filtered = score_filter(dictionnary, minscore)
    age_filtered = age_filter(dictionnary, maxage)
    for person in dictionnary:
        if person in score_filtered and person in age_filtered:
            pers = f"Name: {person[0]}, Age: {person[1]}, Score: {dictionnary[person]}"
            my_list.append(pers)
    return my_list