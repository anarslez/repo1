//1
function one(){
	var arr = []
	for(var i=0; i<256; i++){
		arr = arr.push(i);
	}
return arr
}

//2
function two(){
	var sum=0;
	for(var i=0; i<1001; i = i+2){
		sum=sum+i;
	}
return sum
}

//3
function three(){
	var sum = 0;
	for(var i=1; i<5000; i = i+2){
		sum = sum+i;
	}
return sum
}

//4
function four()
var sum = 0;
	for(var i=1; i<arr.length; i = i+1){
		sum = sum+arr[i];
	}
return sum
}

//5
function five(arr){
	var max = arr[0];
	for(var i=1; i<arr.length; i++){
		if(arr[i]>max){
			max = arr[i]
		}
	}
return max
}

//6
function six(arr){
	var av = 0;
	for(var i=1; i<arr.length; i = i+1){
		av = av+arr[i];
	}
return av/arr.length
}

//7
function seven(){
	var arr = []
	for(var i=1; i<50; i=i+2){
		arr = arr.push(i);
	}
return arr
}

//8
function eight(arr,y){
	var count = 0
	for(var i=1; i<arr.length; i = i+1){
		if(arr[i]>y){
			count = count+1;
		}
	}
return count
}

//9
function nine(arr){
	for(var i=1; i<arr.length; i = i+1){
		arr[i] = arr[i]*arr[i];
	}
return arr
}

//10
function ten(arr){
	for(var i=1; i<arr.length; i = i+1){
		if(arr[i]<0){
			arr[i] =0;
		}
	}
return arr
}

//11
function eleven(arr){
	var max = arr[0];
	var max = arr[0];
	var av = 0;
	var newarr = [];
	for(var i=1; i<arr.length; i++){
		if(arr[i]>max){
			max = arr[i];
		}
		if(arr[i]<min){
			min = arr[i];
		}
		av = av+arr[i];
	}
newarr = newarr.push(max);
newarr = newarr.push(min);
newarr = newarr.push(av/arr.length);
return newarr
}

//12
function twelve(arr){
	var first = arr[0];
	var last = arr[arr.length-1];
	arr[0] = last;
	arr[arr.length-1] = first;
}

//13 
function thirteen(arr){
	for(var i=1; i<arr.length; i = i+1){
		if(arr[i]<0){
			arr[i] ='dojo';
		}
	}
return arr
}











