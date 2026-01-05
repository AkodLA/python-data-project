"""This file shows analysed and filtered information extracted from the csv file.
This is the main file that runs the whole program."""

from data_grab import read_path
from data_treat import *

def main():
    dictionnary = read_path("../data/sample_data.csv")
    print(f"The register:\n{dictionnary}\n")
    print(f"The average score:\n{average_score(dictionnary)}\n")
    print(f"The best one:\n{find_best(dictionnary)}\n")
    print(f"The last one:\n{find_worst(dictionnary)}\n")
    
    #Beneath is was showcasing fuctions done in day 3
    number_pers = f"There are {len(dictionnary)} persons" 
    average = f"The average score is {average_score(dictionnary)}"
    best = find_best(dictionnary)
    print(number_pers)
    print(average)
    print(best)


if __name__ == "__main__": #To run the program from the project directory, you'll need to run: python src/main.py
    main()

            


