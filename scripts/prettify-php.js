/*
 * prettifies gross looking print_r outputs. 
 * Potentially to be a larger (small) web app
 */

var args = process.argv;

if(args.length > 3 && typeof args[2] == "string") {
    console.log("incorrect arguments");
    return;
}

var arrayString = args[2];


var str ="";
var substr = "";
var openBracketCount = 0;
for(var i = 0; i < arrayString.length; i++) {
    str += arrayString[i];

    if(arrayString[i] == "[") {
	openBracketCount++;	
    }
    
    // Inital Array()
    if(str == "Array(")
	str += "\n";

    if()    
   
   

}

console.log(str);


