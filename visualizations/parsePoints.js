var csv = require("fast-csv");
var jsonfile = require("jsonfile")

var file = "real.json"

var circleData = {
	"0":
	[
		
	],
	"1":
	[
		
	],
	"2":
	[
		
	],
	"3":
	[
		
	]
}
var flag = -1;

i = 0;
csv
 .fromPath("cluster.csv")
 .on("data", function(data){
 	if(data[0] == "Cluster") {
 		console.log(flag)
 		flag += 1;
 		if (flag != 0){
 			i++;
 		}
 	} else {
 		console.log(i)
 		circleData[i].push({"circle":{"coordinates":[data[0],data[1]]}})
 	}
 	
 })
 .on("end", function(){
     jsonfile.writeFile(file, circleData, function (err) {
		//console.error(err)
	})
 });