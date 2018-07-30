//1
function one(num){
	var sum = 0;
	for(i = 1; i<num+1; i++){
		sum = sum+i;
	}
return sum
}

//2
function two(num){
	var fact = 1;
	for(i = 1; i<num+1; i++){
		fact = fact*i;
	}
return fact
}

//3
function three(num){
	var fib = []
	for( var i=2; i<num+1;i++){
		fib[0] = 0;
		fib[1] = 1;
		fib[i] = fib[i-1]+fib[i-2];
	}
}

//4
function four(arr){
	if (arr.length >= 2){
		return arr[arr.length-2]
	}
	else {
		return null
	}
}

//5
functionfive(arr,x){
	if (arr.length >= x){
		return arr[arr.length-x]
	}
	else {
		return null
	}
}

//6
function six(arr){
	var max = arr[0];
	var maxtwo = arr[0];
	for(var i=1; i<arr.length; i++){
		if(arr[i]>max){
			max = arr[i];
		}
	}
	for(var i=1; i<arr.length; i++){
		if(arr[i]>maxtwo && arr[i]<max){
			maxtwo = arr[i];
		}
	}
return maxtwo
}

//7
function seven(arr){
	newarr= [];
	for(var i=0; i<arr.length; i++){
		newarr = newarr.push(arr[i]);
		newarr = newarr.push(arr[i]);
	}
arr = newarr;
return arr
} 

//fib
function Fib(n) {   
    
	if(n==1) {
      
		return 0;    
    
	}   
    
	else if(n==2) {      
      
		return 1;
    
	}
    
	else {     
      
		var num1 = Fib(n-2);
      
		var num2 = Fib(n-1);
      
		return num1 + num2;
    
	}

}









