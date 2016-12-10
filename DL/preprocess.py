import copy
import csv
import datetime
import math

csv_location = './merged.csv'
# zip_code_location = './hungarian_zipcodes.csv'
# city_coorditanion_location = './hungarian_city_coor.csv'

# zipcodes = {}
coordinates = {}
coordinates_cache = {}
# expected_output = {}


# def load_hungarian_zipcodes():
#     with open(zip_code_location) as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader, None)
#         next(reader, None)
#         for line in reader:
#             zipcodes[line[0]] = line[1]


def load_hungarian_coordinates(city_coorditanion_location = './hungarian_city_coor.csv'):
    with open(city_coorditanion_location) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for line in reader:
            lon = float(line[1][:2]) + (float(line[1][3:5]) / 60) + (float(line[1][6:8]) / 3600)
            lat = float(line[2][:2]) + (float(line[2][3:5]) / 60) + (float(line[2][6:8]) / 3600)
            coordinates[line[0]] = [lat, lon]


def csv_load(csv_loc=csv_location):
    load_hungarian_coordinates()
    data = []
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
            line2.append(float(line[2][11:13]))

            key = None
            if line[3] in coordinates_cache.keys() and line[4] in coordinates_cache[line[3]].keys():
                key = coordinates_cache[line[3]][line[4]]
                # print('cached')
            else:
                for k in coordinates:
                    key = k
                    break
                key_error = math.sqrt(
                    (coordinates[key][0] - float(line[3]))**2 + (coordinates[key][1] - float(line[4]))**2)
                for x in coordinates:
                    # print(key_error)
                    actual_error = math.sqrt(
                        (coordinates[x][0] - float(line[3]))**2 + (coordinates[x][1] - float(line[4]))**2)
                    if actual_error < key_error:
                        # print('bent')
                        key = copy.deepcopy(x)
                        key_error = copy.deepcopy(actual_error)
                coordinates_cache.update({line[3]: {line[4]: key}})
            line2.append(coordinates[key][0])
            line2.append(coordinates[key][1])
            line2.append(int(line[5]))
            data.append(line2)
            if line_number % 2500 == 0 and line_number != 0:
                print(line_number)
            line_number += 1
        #     else:
        #         error_number += 1
        # print()
        # print(error_number)
        print()
        return data


def prepare_for_train(data):
    expected_output = {}
    data_x = []
    data_y = []
    max_lat = 48.58512448
    min_lat = 45.73711415
    max_lon = 22.89696693
    min_lon = 16.11411095
    hour_index = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0]
    for x in data:
        if x[3] in hour_index:

            f, m, a = 0.0, 0.0, 0.0
            gender, age = x[0], x[1]
            day = [0.0 for x in range(7)]
            h = [0.0 for x in range(18)]
            lat, lon, call, sms = x[4], x[5], x[6], x[7]

            if gender == "M":
                m = 1.0
            elif gender == "F":
                f = 1.0

            if age == "" or age == 0:
                a = 0.5
            else:
                a = min(int(age) / 100.0, 1.0)

            day[x[2]] = 1.0

            h[hour_index.index(x[3])] = 1.0

            norm_lat = (lat - min_lat) / (max_lat - min_lat)
            norm_lon = (lon - min_lon) / (max_lon - min_lon)

            key = '|'.join(str(e) for e in [f, m, a, norm_lat, norm_lon])
            if key in expected_output:

                expected_output[key][x[2]][h.index(1.0)][0] += call
                expected_output[key][x[2]][h.index(1.0)][1] += sms
            else:

                expected_output[key] = [[[0.0, 0.0] for a in range(9)] for a in range(7)]
                expected_output[key][x[2]][h.index(1.0)] = [float(call), float(sms)]

    for x in expected_output:
        for y in range(len(expected_output[x])):
            expected_output[x][y] = [item for sublist in expected_output[x][y] for item in sublist]
            tmp = []
            it = iter(expected_output[x][y])
            for ite in it:
                point = 0.5
                one, two = ite,next(it)
                if one == 0:
                    point -= one * 0.2
                    if two == 0:
                        point -= one * 0.1
                    else:
                        point += one * 0.05
                else:
                    point += one * 0.1
                    if two == 0:
                        point += one * 0.05
                    else:
                        point += one * 0.2
                tmp.append(point)
            expected_output[x][y] = copy.deepcopy(tmp)
            # print(expected_output[x][y])
        # print()
    for x in data:
        if x[3] in hour_index:

            f, m, a = 0.0, 0.0, 0.0
            gender, age = x[0], x[1]
            day = [0.0 for x in range(7)]
            h = [0.0 for x in range(18)]
            lat, lon, call, sms = x[4], x[5], x[6], x[7]

            if gender == "M":
                m = 1.0
            elif gender == "F":
                f = 1.0

            if age == "" or age == 0:
                a = 0.5
            else:
                a = min(int(age) / 100.0, 1.0)

            day[x[2]] = 1.0

            h[hour_index.index(x[3])] = 1.0

            norm_lat = (lat - min_lat) / (max_lat - min_lat)
            norm_lon = (lon - min_lon) / (max_lon - min_lon)

        tmp = [f, m, a]
        for element in day:
            tmp.append(element)
        tmp.append(norm_lat)
        tmp.append(norm_lon)
        data_x.append(tmp)

        key = '|'.join(str(e) for e in [f, m, a, norm_lat, norm_lon])

        data_y.append(expected_output[key][day.index(1.0)])

    return data_x, data_y


def aggregate(data):
    call_data = {}
    sms_data = {}
    for x in data:
        key = '|'.join(str(e) for e in x[:-1])
        if x[-1] == 1 or x[-1] == 2:
            if key in call_data.keys():
                call_data[key] += 1
            else:
                call_data[key] = 1
        else:
            if key in sms_data.keys():
                sms_data[key] += 1
            else:
                sms_data[key] = 1

    merged_data = []
    for x in call_data:
        y = x.split('|')
        y[1] = int(y[1])
        y[2] = int(y[2])
        y[3] = float(y[3])
        y[4] = float(y[4])
        y[5] = float(y[5])
        y.append(call_data[x])
        if x in sms_data:
            sms = sms_data[x]
        else:
            sms = 0
        y.append(sms)
        merged_data.append(y)
    return merged_data

if __name__ == '__main__':
    # load_hungarian_zipcodes()
    # print(zipcodes.keys())
    load_hungarian_coordinates('./hungarian_city_coor.csv')
    data_x, data_y = prepare_for_train(aggregate(csv_load()))
    # for x in range(len(data_x)):
    #     print(data_x[x])
    #     print(data_y[x])
    #     print()
    # print()
