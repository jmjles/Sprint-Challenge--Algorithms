#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n)
    While the the loop could go on for a while, It's a 0(n) operation since it is simply assigning a variable with another value.

b)  O(n log n)
    The for loop is a O(n) operation and the while loop is essentially being halved, making it an O(log n)

c) 0(n)
    This recursive function is 0(n) since the function is only doing one operation and decreasing n to the base conditional.

## Exercise II

While the doesn't break # O(log n)
    multiply floor by 2
while egg breaks at current floor # O(n)
    subtract floor
    if egg doesn't break at new floor # 0(1)
        return new floor
overall time complexity: 0(n log n)
