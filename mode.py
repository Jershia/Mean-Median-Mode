from collections import Counter
import csv
import statistics

with open("HeightWeight.csv" , newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

data = Counter(new_data)
mode = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
    }

for height,occurence in data.items():
    if 75 < float(height)< 85:
        mode["75-85"] =+ occurence

    elif 85 < float(height)< 95:
        mode["85-95"] =+ occurence

    elif 95 < float(height)< 105:
        mode["95-105"] =+ occurence

    elif 105 < float(height)< 115:
        mode["105-115"] =+ occurence

    elif 115 < float(height)< 125:
        mode["115-125"] =+ occurence

    elif 125 < float(height)< 135:
        mode["125-135"] =+ occurence

    elif 135 < float(height)< 145:
        mode["135-145"] =+ occurence

    elif 145 < float(height)< 155:
        mode["145-155"] =+ occurence

    elif 155 < float(height)< 165:
        mode["155-165"] =+ occurence

    elif 165 < float(height)< 175:
        mode["165-175"] =+ occurence

mode_range, mode_occurence= 0,0
for range,occurence in mode.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float((mode_range[0]+mode_range[1])/2)
print(f"Mode Is : {mode:2f}")