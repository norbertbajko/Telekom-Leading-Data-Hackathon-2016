import csv
import datetime

csv_location = './merged.csv'


def csv_load(csv_loc=csv_location):
    data = []
    with open(csv_loc) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            line[1] = int(line[1])

            line[2] = datetime.datetime(int(line[2][:4]), int(line[2][5:7]), int(line[2][8:10]),
            int(line[2][11:13]), int(line[2][14:16]), int(line[2][17:19]))
            data.append(line)
    return data


def prepare_for_train():
    None

if __name__ == '__main__':
    data = csv_load()
    for x in data:
        print(x)
    print()
