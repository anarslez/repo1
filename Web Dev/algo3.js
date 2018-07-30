function printAverage(x){
   
	var sum = 0;
   
	for (var i=0; i<x.length; i++){
     
		sum = sum+x[i];
     
		sum = sum/x.length
	}

return sum
}

function returnOddArray(){
	var arr=[]
	for(var i=1; i<256; i = i+2){
		arr.push(i)
	}
return arr
}

function squareValue(x){
   	for(var i=0; i<x.length; i++){
		x[i] = x[i]*x[i];
	}
   return x;
}
