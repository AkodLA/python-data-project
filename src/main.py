from pathlib import Path

def read_file(file): #i need to make it take a path but for now it will just take a file name (it's corrected now)
    path = Path(__file__) #makes the filepath object
    path = path / file #adds the argument to the path object
    lines = path.open("r")
    dictionnary = {}
    titles = lines.readline() #reads the firstline that contains titles, not relevant data to have in datastructures
    for line in lines:
        data = line.strip().split(",")
        if len(data) > 1: #avoid irrelvant lines
            name = data[0]
            age = int(data[1])
            score = int(data[2])
            tupple = (name, age)
            dictionnary[tupple] = score
    return dictionnary


def average_score(dictionnary):
    total = 0
    num_pers = 0
    for tupple in dictionnary:
        total += dictionnary[tupple]
        num_pers += 1
    average = total / num_pers
    return f"{average:.2f}"


def find_best(dictionnary):
    #go through the items in the dict
    #find the highest score by going through all of the items, 
    #formate the returned value and return it.
    maximum = 0
    for score in dictionnary.values():
        if maximum < score:
            maximum = score
    for id in dictionnary:
        if dictionnary[id] == maximum:
            best = f"Name: {id[0]}, Age: {id[1]}, Score: {maximum}"
    return best
    

def main():
    dictionnary = read_file("c:/Users/akram/OneDrive/Dokumenter/Karriere/python-data-project/data/sample_data.csv")
    print(f"The register:\n{dictionnary}\n")
    print(f"The average score:\n{average_score(dictionnary)}\n")
    print(f"The best one:\n{find_best(dictionnary)}\n")
    

if __name__ == "__main__":
    main()

            


