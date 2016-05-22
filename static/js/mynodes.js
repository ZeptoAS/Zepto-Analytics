

$(document).ready ( function(){
   table();
});


function print_filter(filter){
	var f=eval(filter);
	if (typeof(f.length) != "undefined") {}else{}
	if (typeof(f.top) != "undefined") {f=f.top(Infinity);}else{}
	if (typeof(f.dimension) != "undefined") {f=f.dimension(function(d) { return "";}).top(Infinity);}else{}
	console.log(filter+"("+f.length+") = "+JSON.stringify(f).replace("[","[\n\t").replace(/}\,/g,"},\n\t").replace("]","\n]"));
};

var dataTable = dc.dataTable("#dataTable");

var ndx;
var user = "Eirik";

function table(){
	d3.json("http://127.0.0.1:8000/api/data/10", function(error, jsondata) {

	//	jsondata.forEach(function(d) {
	//	});

		ndx = crossfilter(jsondata);

		tableDimension = ndx.dimension(function(d) {return d.x;});

		print_filter(tableDimension);

		dataTable.width(800).height(800)
			.dimension(tableDimension)
			.group(function(d) { return "" })
			.size(100)
			.columns([
				function(d) { return d.x; },
				function(d) { return d.y; },

				function(d) { return '<div class="btn-group"><button class="btn btn-sm btn-info" data-toggle="modal" data-target="#DownloadModal"><span class="glyphicon-sm glyphicon-cloud-download"></span></button><button class="btn btn-sm btn-info" data-toggle="modal" data-target="#EditModal">Edit</button></div>'}
				//function(d) { return '<button class="btn btn-sm btn-primary" data-toggle="modal" data-target="#EditModal">Edit</button>'}
			])
			.sortBy(function(d){ return d.x; })
			// (optional) sort order, :default ascending
			.order(d3.ascending);

		dc.renderAll();

	});
};