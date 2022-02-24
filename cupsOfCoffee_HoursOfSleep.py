import csv
import numpy as np

def getDataSource(data_path):
    cups_of_coffee = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))

    return {"x" : cups_of_coffee, "y": hours_of_sleep}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between cups of coffee and hours_of_sleep:- \n", correlation[0,1])
    
def setUp():
    data_path = "cups of coffee vs hours of sleep.csv"

    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setUp()