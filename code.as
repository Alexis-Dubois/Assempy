mov x28 #10000
mov x0 #1

loop1:
add x0 x0 #2
cmp x0 x28
b.gt PrimeEnd
mov x1 #1

loop2:
add x1 x1 #2
mul x2 x1 x1
cmp x2 x0
b.gt PrimeFound
mod x3 x0 x1
cmp x3 #0
b.eq loop1
b loop2

PrimeFound:
printf
b loop1

PrimeEnd:
exit