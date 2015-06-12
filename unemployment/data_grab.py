import csv
import numpy as np

def Import_data(file_name="31states.csv"):

    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        data = list(reader)

    # Passing data to lists, then to arrays (should change this to make it all in one) 
    state = []
    days1 = []
    NT = []
    NP = []
    ben = []
    real_days = []

    for row in data[1:]:
        if row[0]== '' or row[1] == '' :
            pass
        else:
            if row[0]=="U":
                days1.append(int(row[4]))
                if int(row[4])>=365:
                    ben.append(1)
                else:
                    ben.append(0)
                NT.append(int(row[5]))
                NP.append(int(row[6]))
                real_days.append(int(row[8]))

    return np.array(real_days), np.array(days1), np.array(NT), np.array(NP), np.array(ben)