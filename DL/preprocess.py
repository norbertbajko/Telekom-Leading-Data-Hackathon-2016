import csv
import datetime

csv_location = './merged.csv'
# zip_code_location = './hungarian_zipcodes.csv'
city_coorditanion_location = './hungarian_city_coor.csv'
data = []
# zipcodes = {}
coordinates = {}
coordinates_cache = {}


# def load_hungarian_zipcodes():
#     with open(zip_code_location) as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader, None)
#         next(reader, None)
#         for line in reader:
#             zipcodes[line[0]] = line[1]


def load_hungarian_coordinates():
    with open(city_coorditanion_location) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for line in reader:
            lon = float(line[1][:2]) + (float(line[1][3:5]) / 60) + (float(line[1][6:8]) / 3600)
            lat = float(line[2][:2]) + (float(line[2][3:5]) / 60) + (float(line[2][6:8]) / 3600)
            coordinates[line[0]] = [lat, lon]


def csv_load(csv_loc=csv_location):
    line_number = 0
    error_number = 0
    with open(csv_loc) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            # if line[3] in zipcodes.keys():
            try:
                line2 = []
                line2.append(line[0])
                line2.append(int(line[1]))
                line2.append(datetime.datetime(int(line[2][:4]), int(line[2][5:7]), int(line[2][8:10]), int(
                    line[2][11:13]), int(line[2][14:16]), int(line[2][17:19])).weekday())
            except Exception as e:
                print(e)
            if int(line[2][14:16]) < 30:
                line2.append(float(line[2][11:13]))
            else:
                line2.append(float(line[2][11:13]) + 0.5)

            key = None
            if line[3] in coordinates_cache.keys() and line[4] in coordinates_cache[line[3]].keys():
                key = coordinates_cache[line[3]][line[4]]
            else:
                for x in coordinates:
                    key = x
                    break
                key_error = abs(coordinates[key][0] - float(line[3])) + abs(coordinates[key][1] - float(line[4]))
                for x in coordinates:
                    # print(key_error)
                    actual_error = abs(coordinates[x][1] - float(line[3])) + abs(coordinates[x][0] - float(line[4]))
                    if actual_error < key_error:
                        print('bent')
                        key=x
                        key_error=actual_error
                coordinates_cache.update({line[3]: {line[4]: key}})
            line2.append(coordinates[key][0])
            line2.append(coordinates[key][1])
            line2.append(int(line[5]))
            data.append(line2)
            if line_number % 1000 == 0 and line_number != 0:
                print(line_number)
            line_number += 1
        #     else:
        #         error_number += 1
        # print()
        # print(error_number)
        # print()


def prepare_for_train():
    data_x=[]
    data_y=[]


if __name__ == '__main__':

    # load_hungarian_zipcodes()
    # print(zipcodes.keys())
    load_hungarian_coordinates()
    csv_load()
    # for x in coordinates_cache:
    #     print(x, coordinates_cache[x])
    # print()
