from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods =['GET','POST'])
def push():
    if request.method == 'POST':
        gender =  request.form["gender"]
        age =  request.form["age"]
        day =  request.form["day"]
        city =  request.form["city"]
        f,m,a,days = format(gender,age,day)

        print(f,m,a,days)

        return "POST"
    else:
        return "Hello World!"

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
    else:
        a = min(int(age)/100.0,1.0)

    weekdays = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
    zeros = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

    for x in range(len(weekdays)):
        if weekdays[x] == day:
            zeros[x] = 1.0

    return f,m,a,zeros

if __name__ == "__main__":
    app.run()
