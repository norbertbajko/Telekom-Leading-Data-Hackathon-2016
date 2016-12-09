import csv
import datetime

csv_location = './merged.csv'
data = []

def csv_load(csv_loc=csv_location):
    with open(csv_loc) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            line2=[]
            line2.append(line[0])
            line2.append(int(line[1]))
            line2.append(datetime.datetime(int(line[2][:4]), int(line[2][5:7]), int(line[2][8:10]),
            int(line[2][11:13]), int(line[2][14:16]), int(line[2][17:19])).weekday())
            if int(line[2][14:16]) < 30:
                line2.append(float(line[2][11:13]))
            else:
                line2.append(float(line[2][11:13])+0.5)
            line2.append(float(line[3]))
            line2.append(float(line[4]))
            line2.append(int(line[5]))
            data.append(line2)


def prepare_for_train():
    data_x = []
    data_y = []


if __name__ == '__main__':
    csv_load()
    for x in data:
        print(x)
    print()
