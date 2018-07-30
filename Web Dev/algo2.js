function printUpTo(x){
  
	for (var i=1; i<x+1; i++){
    
		if (x<0){
      
			return false
    
		}
    
	consol.log(i)
  
	}

}

function printSum(x){
  
	var sum = 0;
  
	for(var i=0; i<x+1; i=i+1){
    
		sum = sum+i;
  
	} 
return sum
;
}

function printSumArray(x){
  
	var sum = 0;
  
	for(var i=0; i<x.length; i++) {
    
		sum = sum+x[i]; 
	}
  
return sum;

}