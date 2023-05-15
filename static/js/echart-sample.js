var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

var listaMunicipios = JSON.parse(document.getElementById('lista_municipios').innerText);
var listaDatas = JSON.parse(document.getElementById('lista_datas').innerText);
var listaSeries = JSON.parse(document.getElementById('lista_series').innerText);

var seriesState = {
  enabled: false,  // Indica se a série está habilitada ou desabilitada
  opacity: 0      // Opacidade da série quando habilitada
};

option = {
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: listaMunicipios
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  toolbox: {
    feature: {
      saveAsImage: {}
    }
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: listaDatas
  },
  yAxis: {
    type: 'value'
  },
  series: listaSeries,

};

option && myChart.setOption(option);
myChart.dispatchAction({
  type: 'legendToggleSelect',
  name: 'SAO PAULO'
});
myChart.dispatchAction({
    type: 'legendInverseSelect'
})