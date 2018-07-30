//algo 4
//1
function greaty(arr,y){
	var count = 0;
	for(var i=0;i<arr.length;i++){
		if (arr[i]<y){
			console.log(arr[i]);
			count = count+1;
		}
	}
}

//2
function minmaxav(arr){
	var min=arr[0], max=arr[0], av=0;
	for(var i = 0; i<arr.length; i=i+1){
		if(max<arr[i]){
		max = arr[i]
		}
		if(min>arr[i]){
		min = arr[i]
		}
		av = av+arr[i];
		av = av/arr.length;
	}
console.log(min)
console.log(max)
console.log(av)
}

//3
function negdojo(arr){
	for(var i = 0; i<arr.length; i=i+1){
		if(arr[i]<0){
			arr[i] = 'dojo';
		}
	}
return arr
}

//4
function removeval(arr,i1,i2){
	newarr = [];
	for(var i = 0; i<i1; i=i+1){
		newarr = newarr.push(arr[i]);
	}
	for(var i = i2+1; i<arr.length; i=i+1){
		newarr = newarr.push(arr[i]);
	}
}




