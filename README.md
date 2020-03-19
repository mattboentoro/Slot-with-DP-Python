# Slot-with-DP-Python
Given a matrix size of M x N consisting of numbers and points. The ball will go down from top to bottom, if you find a number, then the ball moves to the next slot (right or left). There are certainly no adjacent numbers other than the last line. Print a slot, the number of numbers found from the maximum and minimum value in 1 ball trip!

## Input Format

First row: 2 <= M, N <= 1000

2nd ~ last line: a combination of numbers and periods of number N with (-10000 <= v <= 10000) separated by spaces


## Output Format

The first line consists of three numbers separated by spaces (Ball slot, maximum value of Ball travel, number of numbers found)

The second line consists of three numbers separated by spaces (Ball slot, minimum value of Ball travel, number of numbers found)

The maximum / minimum total travel value of the Ball is guaranteed to be unique.

## Example Input

6 5
. . . . .  
. 10 . . .  
. . 30 . .  
. . 20 . 30  
. . . . .  
20 30 10 5 50  

## Examples of Outputs

2 70 3  
4 5 1

## Explaination

Explanation of the maximum value of
Slot 2: 10 (select right) + 30 (select left) + 30 = 70

While the ball is sliding, encounters 3 numbers (10, 30, 30)

So that: 2 70 3


Explanation of the minimum value of
Slot 4: 5 = 5

While the ball is sliding, encounters 1 number (5)

So that: 4 5 1

## Solutions

I used dynamic programming to from the bottom row to find the maximum or minimum value obtained when I see the item.
