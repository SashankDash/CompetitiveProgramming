'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
# Write your code here
dict=["WS", "MS","AS", "AS","MS","WS","WS","MS","AS","AS","MS","WS"]
no1=int(input())
for i in range(108):
 seat_no = int(input())
 #to find test case no
 if (seat_no <=108 and seat_no>=1):
   comp = seat_no//12
   #to find seat position
   x = seat_no % 12
   #find the difference
   y = 13-x
   if x!=0 :
      opposite_seat = str(y + (comp*12))
      print(opposite_seat + " " + dict[y-1])
   elif x==0:
      opposite_seat = str((comp*12)-11)
      print(opposite_seat + " " + dict[11])


