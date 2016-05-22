
$(document).ready ( function(){
   chart();
});


function print_filter(filter){
	var f=eval(filter);
	if (typeof(f.length) != "undefined") {}else{}
	if (typeof(f.top) != "undefined") {f=f.top(Infinity);}else{}
	if (typeof(f.dimension) != "undefined") {f=f.dimension(function(d) { return "";}).top(Infinity);}else{}
	console.log(filter+"("+f.length+") = "+JSON.stringify(f).replace("[","[\n\t").replace(/}\,/g,"},\n\t").replace("]","\n]"));
};

var barChart = dc.barChart("#barChart");
var lineChart = dc.lineChart("#lineChart");



function chart(){
	d3.json("http://127.0.0.1:8000/api/data2", function(error, jsondata) {

	// Function to change data from query
//		jsondata.forEach(function(d) {
//			d.x = +d.dataId;
//			d.y = +d.data;
//		});

		ndx = crossfilter(jsondata);

		dataDimension = ndx.dimension(function(d) {return d.x;});

		dataGroup = dataDimension.group().reduceSum(function(d) {return d.y;});

		print_filter(dataDimension);
		print_filter(dataGroup);

		barChart
				.height(400)
				.width(800)
				.dimension(dataDimension)
				.group(dataGroup)
				.transitionDuration(0)
				.centerBar(true)
				.gap(17)
				.x(d3.scale.ordinal())//.domain(["", "a", "b", "c"]))
				.xUnits(dc.units.ordinal)
				.elasticY(true)
				.xAxis().tickFormat(function(v) {return v;});


		  lineChart
		    .width(800)
		    .height(400)
		    .dimension(dataDimension)
		    .group(dataGroup)

		    .x(d3.scale.linear().domain([0,20]))
		    .brushOn(false)
		    .yAxisLabel("Y-axis")
		    .xAxisLabel("X-axis")
		    //.clipPadding(10)
		    .elasticY(true)
		    .mouseZoomable(true)
		    //.seriesAccessor(function(d) {return "Expt: " + d.key[0];})
		    //.keyAccessor(function(d) {return +d.key[1];})
		    //.valueAccessor(function(d) {return +d.value - 500;})
		    //.legend(dc.legend().x(350).y(350).itemHeight(13).gap(5).horizontal(1).legendWidth(140).itemWidth(70));
		  //lineChart.yAxis().tickFormat(function(d) {return d3.format(',d')(d+299500);});
  		  //lineChart.margins().left += 40;

		dc.renderAll();
	});
};


function load_button(file) {
	return function load_it() {
	    d3.csv(file, function(error, experiments) {
	        ndx.remove();
            ndx.add(experiments);
            dc.redrawAll();
        });
    };
};

var button1 = load_button("morley.csv"),
    button2 = load_button("morley2.csv"),
    button3 = load_button("morley3.csv");



