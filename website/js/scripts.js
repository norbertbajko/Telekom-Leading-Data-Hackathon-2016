$(document).ready( () => {

    var data = [
        {
          z: [[1,20,30,50,1],
              [20,1,60,80,30],
              [34,20,77,-10,40],
              [60,40,6,-10,40],
              [30,60,1,-17,50],
              [30,60,1,-80,20],
              [30,60,1,-20,20],
              [35,61,15,-140,20],
              [37,60,41,-60,20],
              [36,60,51,-70,20],
              [30,60,51,-15,20],
              [30,60,41,-110,20],
              [30,60,13,-60,20],
              [30,60,11,-40,20],
              [30,60,14,-70,20],
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
          x: ["Monday","Tuesday","Wednesday","Thursday","Friday"],
          y: ["16:00","15:30","15:00","14:30","14:00","13:30","13:00","12:30","12:00","11:30","11:00","10:30","10:00","9:30","9:00"],
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
        // TODO $.ajax();
    });

});
