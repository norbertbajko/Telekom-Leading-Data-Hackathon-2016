from flask import Flask, request
app = Flask(__name__)
import sys
sys.path.insert(0,"../DL")
import network
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
import json

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


model = None

@app.route("/", methods =['GET','POST'])
@crossdomain(origin='*')
def push():
    if request.method == 'POST':
        gender =  request.form["gender"]
        age =  request.form["age"]
        day =  request.form["day"]
        city =  request.form["city"]
        f,m,a,days = format(gender,age,day)

        data = network.model_predict("../DL/hungarian_city_coor.csv",model,m,f,a,days,city)
        data = data.transpose()
        data = data.tolist()
        for x in range(len(data)):
            for y in range(len(data[x])):
                data[x][y] = str(data[x][y])
        print(data)
        return json.dumps(data)
    else:
        return "Use the service with HTTP POST method - params: {gender,age,day,city}"

def format(gender,age,day):
    f = 0.0
    m = 0.0
    a = 0.0

    if gender == "MALE":
        m = 1.0
    elif gender == "FEMALE":
        f = 1.0

    if age == "":
        a = 0.5
    elif age == 0:
        a = 0.5
    else:
        a = min(int(age)/100.0,1.0)

    weekdays = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
    zeros = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

    for x in range(len(weekdays)):
        if weekdays[x] == day:
            zeros[x] = 1.0

    return f,m,a,zeros

if __name__ == "__main__":
    model = network.model_build("../DL/weights/weights-batch_size_64-dense_256_512-1081-0.37.hdf5")
    app.run()
