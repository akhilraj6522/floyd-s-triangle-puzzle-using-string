# floyd-s-triangle-puzzle-using-string

Rohan and Jeet are learning coding. They give each other different tasks. Today's tasks are as follows: -  
 
They are given a string and they need to create a triangle with the pattern as follows and also consider Row as one based indexed.  
 
If (RowIndex % 3 != 0) then they need to write a string from right to left order. While in other cases I need to write strings from left to right.  
 
If the string ends it will be started again and the end of the triangle need not be the end of the string. 
 
For eg: string is "INDORE" and height of triangle is “5” 

I  
D  N  
O R E  
O D N I  
D N I E R  
 
You will ask Jeet Q questions and he needs to tell the frequency of a character C in a row of triangle R.  First line will contain N, the height of the triangle. Next line contain a string consists only of Uppercase English Alphabets, length not exceed 106 

 Third line contains a single integer Q, the number of queries to be asked. Each query contains two space separated integers, R and C, where R is the row number and C is the character. 
 
Output:  For each query, output in a single line the frequency of the alphabet in the given row.  
 
Constraints:  
1 ≤ N ≤ 10^18
1 ≤ Q ≤ 50000  
1≤R≤N A≤C≤Z  
 
Sample Input: 
5  
INDORE  
2  
1 I  
2 D  
 
Sample Output:  
1  
1 
