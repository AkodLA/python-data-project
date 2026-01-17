"""This file has a function that reads the filepath of a csv file that it taken as argument and organise it in a datastructure.
This file is for grabing data from the datafile."""
import csv

#Add a error class to handle the empty csv file
class EmptyCSVError(Exception):
    """Raised when csv file contain headers but no data rows"""
    pass

class NegativeScoreError(Exception):
    """Raised when a score value is negative"""
    pass

class InvalidRowError(Exception):
    """Raised when the row has an invalid data"""
    pass


def read_path(filepath):
    dictionnary = {} #start with the datastructure
    ignored_lines = 0
    with open(filepath, newline='') as file: #newline tells Python to let the newline format as it is in the csv file
        reader = csv.DictReader(file) #read the files
        
        for line_num, row in enumerate(reader,start=2):
            try:
                name, age, score = verify_row(row, line_num)
                dictionnary[(name,age)] = score
            except InvalidRowError as e:
                print(f"Error: {e}")
                ignored_lines += 1
    
    if not dictionnary: #if no data are in the dictionnary, this means data rows are empty
        raise EmptyCSVError("The csv file has headers but no data rows")
        
    return dictionnary, ignored_lines


def verify_row(row, line_num):
    if not row.get("age"): #age is empty
        raise InvalidRowError(f"[LOG] Line {line_num} missing age")
        
    if not row.get("score"): #score is empty
        raise InvalidRowError(f"[LOG] Line {line_num} missing score")
        
    try: #score or age aren't 'int' type.
        age = int(row["age"])
        score = int(row["score"])
    except ValueError:
        raise InvalidRowError (f"[LOG] Line {line_num} age/score wrong datatype")
    
    if age <= 0:
        raise NegativeScoreError(f"Error: unvalid age in line {line_num}")
        
    if score < 0: #score is negative
        raise NegativeScoreError(f"Error: unvalid score in line {line_num}")
    
    return row["name"], age, score



