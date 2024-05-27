
function openNav() {
    document.getElementById("menu").setAttribute('onclick', "closeNav()");
    document.getElementById("mySidenav").style.width = "300px";
  }
  
  function closeNav() {
    document.getElementById("menu").setAttribute('onclick', "openNav()");
    document.getElementById("mySidenav").style.width = "0";
  }
  
  
  years = [2015,2020,2030,2040,2050,2060,2070,2080,2090,2100]
  colors = ['rgb(20,143,124)', 'rgb(24,47,84)', 'rgb(234,221,61)', 'rgb(222, 54, 42)', 'rgb(88,182,223)', 'rgb(231,128,28)', 'rgb(129,129,129)']
  i = 0;
  d = []
  
  const customTitle = {
    id: 'customTitle',
    beforeLayout: (chart, args, opts) => {
      const {
        display,
        font
      } = opts;
      if (!display) {
        return;
      }
  
      const {
        ctx
      } = chart;
      ctx.font = font || '12px "Helvetica Neue", Helvetica, Arial, sans-serif'
  
      const {
        width
      } = ctx.measureText(opts.text);
      chart.options.layout.padding.left = width * 1.1;
    },
    afterDraw: (chart, args, opts) => {
      const {
        font,
        text,
        color
      } = opts;
      const {
        ctx,
        chartArea: {
          top,
          bottom,
          left,
          right
        }
      } = chart;
  
      if (opts.display) {
        ctx.fillStyle = color || Chart.defaults.color
        ctx.font = font || '12px "Helvetica Neue", Helvetica, Arial, sans-serif'
        ctx.fillText(text, 3, (top + bottom) / 2)
      }
    }
  };
  
  
  var chart = new Chart('chart', {
      type: 'line',
      data: {
        labels: years,
      },
      options: {
        plugins: {
          customTitle: {
            display: true,
            text: 'Gt CO2',
          },
          title: {
                  display: true,
                  text: 'Global CO2 Emissions'
          }
        }
      },
      plugins: [customTitle],
  });
  
  function first(data) {
    d3.csv("/static/out.csv", function(data) {
      y = []
      for (x in years) {
        y.push(parseFloat(data[years[x]]))
      };
      const newDataset = {
          label: data['SCENARIO'], 
          data: y,
          fill: false,
          borderColor: colors[i],
          backgroundColor :colors[i],
          tension: 0.5
      };
      chart.data.datasets.push(newDataset);
      chart.update();
      i++;
  })
  };
  
  first();

  let img = new Image();
  img.onload = function(){
    document.getElementById('bgimg-0').style.backgroundImage = "url('" + img.src + "')";
  };
  
  img.src = "/static/background1.jpg";

  let img1 = new Image();
  img1.onload = function(){
    document.getElementById('bgimg-1').style.backgroundImage = "url('" + img1.src + "')";
  };
  
  img1.src = "/static/background2.jpg";