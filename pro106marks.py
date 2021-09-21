import numpy as np
import csv

def get_data_source(data_path):
    days_present = []
    marks = []
    with open (data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            days_present.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))
        
    return {"x" : days_present,"y" : marks}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between days_present and marks obtained is ",correlation[0,1]) 

def main ():
    data_path = "Student Marks vs Days Present.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

main()