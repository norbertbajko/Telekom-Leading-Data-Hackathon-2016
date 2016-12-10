$(document).ready(() => {

    var weekdays = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"];
    $('#weekday-text').val(weekdays[new Date().getDay()]);

    $('#gender-dropdown li').on('click', (e) => {
        var elem = e.target;
        var label = elem.text;
        $('#gender-text').val(label);
    });

    $('#weekday-dropdown li').on('click', (e) => {
        var elem = e.target;
        var label = elem.text;
        $('#weekday-text').val(label);
    });


    $('#submit').on('click', (e) => {

      var gender = $('#gender-text').val();
      var age = $('#age-text').val();
      var city = $('#city-text').val();
      if(gender != '' && age != null && city != null){
        $.ajax({
            method: 'POST',
            url: 'http://localhost:5000',
            data: {
                gender: gender,
                age: age,
                day: $('#weekday-text').val(),
                city: city
            }
        }).done((result) => {
            result = JSON.parse(result);
            console.log(result)
            var array = [];
            var second = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
            for (var j = 0; j < 9; j++)
                array.push(second);

            console.log(array)

            for (var i = 0; i < 9; i++) {
                var row = []
                for (var j = 0; j < 7; j++) {
                    row.push(parseFloat(result[i][j]))
                }
                array[i] = row.slice()
            }
            console.log(array);

            var data = [{
                z: array,
                colorscale: [
                    // ['0.0', 'rgb(64,8,4)'],
                    // ['0.111111111111', 'rgb(127,16,8)'],
                    // ['0.222222222222', 'rgb(255,40,67)'],
                    // ['0.333333333333', 'rgb(191,25,12)'],
                    // ['0.444444444444', 'rgb(239,3,14)'],
                    // ['0.555555555556', 'rgb(170,170,170)'],
                    // ['0.666666666667', 'rgb(65,229,49)'],
                    // ['0.777777777778', 'rgb(54,191,41)'],
                    // ['0.888888888889', 'rgb(36,127,27)'],
                    // ['1.0', 'rgb(18,64,14)']

                    ['0.0', 'rgb(120,12,13)'],
                    ['0.111111111111', 'rgb(170,30,40)'],
                    ['0.222222222222', 'rgb(200,25,25)'],
                    ['0.333333333333', 'rgb(210,25,20)'],
                    ['0.444444444444', 'rgb(220,20,25)'],
                    ['0.555555555556', 'rgb(170,170,170)'],
                    ['0.666666666667', 'rgb(120,200,120)'],
                    ['0.777777777778', 'rgb(90,235,80)'],
                    ['0.888888888889', 'rgb(65,229,49)'],
                    ['1.0', 'rgb(54,191,41)']
                ],
                x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                y: ["17:00", "16:00", "15:00", "14:00", "13:00", "12:00", "11:00", "10:00", "9:00"],
                type: "heatmap",
                hoverinfo: "z",
            }];

            Plotly.newPlot('chart', data);


        });
      }else{
        $.notify("You need to fill every field!", "error");
      }

    });

});
