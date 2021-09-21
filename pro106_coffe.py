import numpy as np
import csv

def get_data_source(data_path):
    cup_of_coffe = []
    sleep_hours = []
    with open (data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            cup_of_coffe.append(float(row["Coffee in ml"]))
            sleep_hours.append(float(row["sleep in hours"]))
        
    return {"x" : cup_of_coffe,"y" : sleep_hours}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between cup of coffe and hours of sleep  is ",correlation[0,1]) 

def main ():
    data_path = "cups of coffee vs hours of sleep.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

main()