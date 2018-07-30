//1
function one(arr){
	for(var i=1; i<arr.length; i = i+1){
		if(arr[i]>0){
			arr[i] ='big';
		}
	}
return arr
}

//2
function two(arr){
	var max = arr[0];
	var min = arr[0];
	for(var i=1; i<arr.length; i++){
		if(arr[i]>max){
			max = arr[i];
		}
		if(arr[i]<min){
			min = arr[i];
		}
	}
console.log(min);
return max
}

//3
function three(arr){
	console.log(arr.length-2)
	for(var i=0; i<arr.length; i++){
		if (arr[i]%2 != 0){
			return arr[i]
		}
	}
}

//4
function four(arr){
	var newarr = [];
	for(var i=0; i<arr.length; i++){
		newarr[i] = arr[i]*2;
	}
return newarr
}

//5
function five(arr){
	var count = 0;
	for(var i=0; i<arr.length; i++){
		if (arr[i] > 0){
			count = count+1;
		}
	}
arr[arr.length-1] = count;
return arr
}

//6
function six(arr){
	var countodd = 0;
	var counteven = 0;
	for(var i=0; i<arr.length; i++){
		if(arr[i] % 2 == 0){
			counteven = counteven+1;
			countodd = 0;
		}
		if(arr[i] % 2 != 0){
			countodd = countodd+1;
			counteven = 0;
		}
		if(counteven>=3){
			console.log('even more so');
		}
		if(countodd>=3){
			console.log('that's odd');
		}
	}
}

//7
function seven(arr){
	for(var i=1; i<arr.length; i=i+2){
		arr[i] = arr[i]+1;
		console.log(arr[i]);
	}
reutn arr
}

//8
function eight(arr){
	for(var i = 1; i<arr.length; i++){
		arr[i] = arr[i-1].length
	}
return arr
}

//9
function nine(arr){
	var newarr = [];
	for(var i=1; i<arr.length; i++){
		newarr[i-1]=arr[i]+7;
	}
return newarr
}

//10
function thirteen(arr){
	var tmp=0;
	for(var i=0;i<arr.length/2;i = i++){
		tmp = arr[i];
		arr[i]=arr[arr.length-1-i];
		arr[arr.length-1-i]=tmp;
	}
}

//11
function eleven(arr){
	for(var i=0; i<arr.length; i++){
		if(arr[i]>0){
			arr[i] = arr[i]*-1;
		}
	}
return arr
}

//12
function twelve(arr){
	var count = 0;
	for(var i=0; i<arr.length; i++){
		if(arr[i] == 'food'){
			count = count+1;
			console.log('yummy');
		}
	}
	if(count == 0){
		console.log('i'm hungry');
	}
}

//13
function thirteen(arr){
	var tmp=0;
	for(var i=0;i<arr.length/2;i = i+2){
		tmp = arr[i];
		arr[i]=arr[arr.length-1-i];
		arr[arr.length-1-i]=tmp;
	}
}

//14
function fourteen(arr,x){
	for(var i=0; i<arr.length; i++){
		arr[i] = arr[i]*x;
	}
return arr
}






