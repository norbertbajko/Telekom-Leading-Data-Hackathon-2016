$(document).ready( () => {

    var data = [
        {
          z: [ [0.10829078, 0.10343076,  0.09587876,  0.10375294,  0.11709766,  0.11976036,
              0.13561906 , 0.12008411  ,0.0960855]
          // [1,20,30,50,1,11,2],
          //     [20,1,60,80,22,34,11],
          //     [60,40,6,-10,40,14,55],
          //     [30,60,1,-20,20,55,11],
          //     [35,61,15,-140,6,5,1],
          //     [36,60,51,-70,44,66,77],
          //     [1,6,51,-15,33,5,55],
          //     [40,60,13,-60,1,66,11],
          //     [55,6,11,-40,33,66,33]
            ],
            colorscale: [
            ['0.0', 'rgb(64,8,4)'],
            ['0.111111111111', 'rgb(127,16,8)'],
            ['0.222222222222', 'rgb(255,40,67)'],
            ['0.333333333333', 'rgb(191,25,12)'],
            ['0.444444444444', 'rgb(239,3,14)'],
            ['0.555555555556', 'rgb(170,170,170)'],
            ['0.666666666667', 'rgb(65,229,49)'],
            ['0.777777777778', 'rgb(54,191,41)'],
            ['0.888888888889', 'rgb(36,127,27)'],
            ['1.0', 'rgb(18,64,14)']
          ],
          y: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
          x: ["17:00","16:00","15:00","14:00","13:00","12:00","11:00","10:00","9:00"],
          type: "heatmap",
          hoverinfo: "z",
        }
    ];

    Plotly.newPlot('chart',data);

    var weekdays = ["SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"];
    $('#weekday-text').val(weekdays[new Date().getDay()]);

    $('#gender-dropdown li').on('click',(e) => {
      var elem = e.target;
      var label = elem.text;
      $('#gender-text').val(label);
    });

    $('#weekday-dropdown li').on('click',(e) => {
      var elem = e.target;
      var label = elem.text;
      $('#weekday-text').val(label);
    });

    $('#submit').on('click', (e) => {
         $.ajax({
           method: 'POST',
           url: 'http://localhost:5000',
           data: { gender: $('#gender-text').val(), age: $('#age-text').val(), day: $('#weekday-text').val(), city: $('#city-text').val() }
         }).done( (result) => {
            console.log(result);
         });
    });

});
