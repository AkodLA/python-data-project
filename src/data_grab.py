"""This file has a function that reads the filepath of a csv file that it taken as argument and organise it in a datastructure.
This file is for grabing data from the datafile."""

import csv 

def read_path(filepath):
    dictionnary = {} #start with the datastructure
    with open(filepath, newline='') as file: #newline tells Python to let the newline format as it is in the csv file
        reader = csv.DictReader(file) #read the files
    
        for row in reader:
            row["age"] = int(row["age"])
            row["score"] = int(row["score"])
            dictionnary[(row["name"], row["age"])] = row["score"] 
    
    return dictionnary
