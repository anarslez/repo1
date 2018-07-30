//pg. 16 coding probs
//setting and swapping
var myNumber = 42;
var myName = "addi";
var num = myNumber;
var myNumber = myName;
var myName = myNumber;

//print -52 to 1066
for (var num = -52; num < 1067; num = num+1)
{
	console.log(num)
}

//don't worry, be happy
function beCheerful()
{
	for(var i=1; i<99; i=i+1)
	{
		console.log('good morning!')
	}
}

//multiples of three but not all
for (var num = -300; num < 3; num = num+3)
{
	if (num == -3 || num == -6)
	{
		continue;
	}
	console.log(num)
}

//printing integers with while 
var i = 2000;
while (i<5281)
{
	console.log(i)
	i = i+1
}

//you say it's your birthday
function bday(a,b)
{
	if ((a == 4 || a == 3) && (b == 4 || b == 3))
	{
		console.log('How did you know?')
	}
	else
	{
		console.log('Just another day...')
	}
}

//leap year
function leap(year)
{
	if (Number.isInteger(year/400) == true)
	{
		console.log('Leap Year!')
	}
	else if (Number.isInteger(year/400) == true && Number.isInteger(year/100) == false)
	{
		console.log('Leap Year!')
	}
	else
	{
		console.log('Not a Leap Year')
	}
}

//print and count
var x = 0;

for(var i=512; i<4092; i=i+1)

	{
  
		if (Number.isInteger(i/5)==true)
  
		{
   
			 x = x+1
  
		}

	}

console.log(x)

//multiples of six
var i = 0;
while (i < 60001)
{
	console.log(i)
	i = i+6;
}

//counting the dojo way
for(var i = 1; i<101; i = i+1)
{
	if (Number.isInteger(i/5) == true && Number.isInteger(i/10) == false)
	{
		console.log('Coding')
	}
	else if (Number.isInteger(i/10) == true)
	{
		console.log('Dojo')
	}
	else
	{
		console.log(i)
	}
}

//what do you know?
function input(incoming)
{
	console.log(incoming)
}

//whoa, that sucker's huge...
var x = 0;
for (var i = -299999; i<300000; i = i+2)
{
	x = 0+i;
}
//and yes the short cut is that the answer will be zero if you start at -x and end at x
console.log(x)

//countdown by fours
var i = 2016;
while (i > 0)
{
	i = i-4;
	console.log(i)
}

//flexible countdown
function flexcd(lowNum, highNum, mult)
{
	for (var i = lowNum; i<highNum+1; i = i+1)
	{
		if (Number.isInteger(i/mult) == true)
		{
			console.log(i)
		}
	}
}

//final countdown
function finalcd(param1,param2,param3,param4)
{
	var i = param2;
	while (i < param3+1)
	{
		if (Number.isInteger(i/mult) == true && i != param4)
		{
			console.log(i)
		}
	}
}

//countdown
function countdown(num)
{
var arr = []
var length = num
for(var i = length; i>-1; i = i-1)
	{
		arr.push(i)
	}	
console.log(arr)
}

//print and return
function pr(arr)
{
console.log(arr[0])
return(arr[1])
}
console.log(arr[1])

//first plus length
function fpl(arr)
{
var first = arr[0]
var length = arr.length
console.log(first+length)
}

//values greater than second
var arr =  [1,3,5,7,9,13];
var arr2 = [];
for(var i = 0; i<7; i = i+1)
{
	if (arr[i] > arr[1])
	{
		console.log(arr[i])
		arr2.push(arr[i])
	}
}
console.log(arr2.length)

//values greater than second generalized
function vgts(arr)
{
if (arr.length > 1)
{
var arr2 = [];
for(var i = 0; i<arr.length+1; i = i+1)
{
	if (arr[i] > arr[1])
	{
		console.log(arr[i])
		arr2.push(arr[i])
	}
}
console.log(arr2.length)
}
else
{
console.log('not long enough')
}
}

//this length, that value
function lenval(num1,num2)
{
	if (num1 != num2)
	{
		var arr = []
		for(var i = 0; i<num1; i = i+1)
		{
			arr.push(num2)
		}
	console.log(arr)
	}
	else
	{
	console.log('Jinx')
	}
}	

//fit the first value
function fitfval(arr)
{
	if (arr[0] > arr.length)
	{
		console.log('Too Big!')
	}
	else if (arr[0] < arr.length)
	{
		console.log('Too Small!')
	}
	else if (arr[0] = arr.length)
	{
		console.log('Just Right!')
	}
}

//fahrenheit to celsius
function fahrenheitToCelsius(fdegrees)
{
var cdegrees = (fdegrees - 32)*5/9
console.log(cdegrees)
}

//celsius to fahrenheit 
function celsiustofahrenheit(cdegrees)
{
var fdegrees = (9/5)*cdegrees + 32
console.log(fdegrees)
}

//biggie size
function makeitbig(arr){
	for(var i = 0; i<arr.length;i=i+1){
	if (arr[i]<0){
		arr[i] = 'big'
		}
	}
console.log(arr)
}

//print low, return high
function plrh(arr){
	var min=arr[0], max=arr[0];
	for(var i = 0; i<arr.length; i=i+1){
		if(max<arr[i]){
		max = arr[i]
		}
		if(min>arr[i]){
		min = arr[i]
		}
	}
console.log(min)
return(max)
}
console.log(max)

//print one, return another
function pora(arr){
console.log(arr[arr.length-2])
	for(var i = 0; i<arr.length; i = i+1){
		if ((arr[i]%2) !== 0){
			return arr[i]
		}
	}
}

//double vision
function double(arr){
	newarr = [];
	for(var i=0; i<arr.length; i = i+1){
		newarr[i] = arr[i]*2
	}
console.log(newarr)
return newarr
}

//count positives
function countp(arr){
var x = 0;
	for(var i=0; i<arr.length; i=i+1){
		if (arr[i] > 0){
			x = x+1;
		}
	}
arr[arr.length-1] = x;
console.log(arr)
return arr
}

//evens and odds
function evod(arr){
	for(var i=0; i<arr.length; i=i+1){
		if ((arr[i]%2) !== 0 && (arr[i+1]%2) !== 0 && (arr[i+2]%2) !== 0){
			console.log("That's odd!")
		}
		if ((arr[i]%2) == 0 && (arr[i+1]%2) == 0 && (arr[i+2]%2) == 0){
			console.log("Even more so!")
		}
	}
}

//increment the seconds
function incsec(arr){
	for(var i=0; i<arr.length; i=i+1){
		if ((arr[i]%2) !== 0){
			arr[i] = arr[i]+1
		}
		console.log(arr[i])
	}
	return arr
}

//previous lengths
function prevlen(arr){
	for( var i = 0; i<arr.length; i=i+1){
		arr[i] = arr[i].length
	}
arr.unshift(0);
console.log(arr)
}

//add seven to most
function addsev(arr){
	var newarr =[]
	for( var i = 0; i<arr.length; i=i+1){
		if (i == 0){
			newarr[i] = arr[i]
		}
		if (i !== 0){
			newarr[i] = arr[i]+7
		}
	}
return newarr
}

//reverse array
function revarr(arr){
	var samearr = []
	for( var x = 0; x<arr.length; x=x+1){
			samearr[x] = arr[x]
	}
	for( var i = 0; i<arr.length; i=i+1){
			arr[i] = samearr[arr.length-1-i]
	}
console.log(arr)
}

//outlook: negative
function neg(arr){
	var newarr = []
	for(var i=0; i<arr.length; i = i+1){
		if(arr[i]<0){
			newarr[i] = arr[i]
		}
		if(arr[i]>0){
			newarr[i] = -1*arr[i]
		}
	}
return newarr
}

//always hungry (NOT COMPLETED)
function hungry(arr){
	for(var i=0; i<arr.length; i=i+1){
		if (arr[i] !== 'food'){
			console.log("I'm hungry")
			break
		}
		else if (arr[i] == 'food'){ 
		console.log("yummy")
		}
	}
}

//swap towards the center
function swapcent(arr){
	var samearr = []
	for( var x = 0; x<arr.length; x=x+1){
			samearr[x] = arr[x]
	}
	arr[0] = samearr[arr.length-1];
	arr[arr.length-1] = samearr[0];
	arr[2] = samearr[arr.length-3];
	arr[arr.length-3] = samearr[2];
	console.log(arr)
}
		
//scale the array
function scale(arr,num){
	for(var i=0; i<arr.length; i=i+1){
		arr[i] = arr[i]*num;
	}
return arr
}



