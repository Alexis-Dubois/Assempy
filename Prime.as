// top of the interval
mov x28 #10000
// bottom of the interval-2
mov x0 #1

// going through all odd number in the interval
loop1:
add x0 x0 #2
cmp x0 x28
b.gt PrimeEnd
mov x1 #1

// trying to divide the number
loop2:
add x1 x1 #2
mul x2 x1 x1
cmp x2 x0
b.gt PrimeFound
mod x3 x0 x1
cmp x3 #0
b.eq loop1
b loop2

// we found a prime and we want to show it
PrimeFound:
printf
b loop1

// we went through the entire interval
PrimeEnd:
exit