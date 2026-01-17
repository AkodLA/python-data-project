"""This file shows analysed and filtered information extracted from the csv file.
This is the main file that runs the whole program."""

from data_grab import *
from data_treat import *
import sys

def main():
    try: #The main file is the boundary of the program and where errors are handled
        dictionnary, ignored_lines = read_path("./data/sample_data.csv")
        print(f"There are {ignored_lines} ignored lines in the file.")
        print(f"The register:\n{dictionnary}\n")
        print(f"The average score:\n{average_score(dictionnary)}\n")
        print(f"The best one:\n{find_best(dictionnary)}\n")
        print(f"The last one:\n{find_worst(dictionnary)}\n")

        #Beneath, i show fuctions done in day 3
        number_pers = f"There are {len(dictionnary)} persons" 
        average = f"The average score is {average_score(dictionnary)}"
        best = find_best(dictionnary)
        print(number_pers)
        print(average)
        print(best)
    except FileNotFoundError:
        print("Error: The csv file is not found or the filename is incorrect.")
        sys.exit(1)
    except EmptyCSVError as err:
        print(f"Error: {err}")
        sys.exit(1)
    except NegativeScoreError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__": #To run the program from the project directory, you'll need to run: python src/main.py
    main()

            


