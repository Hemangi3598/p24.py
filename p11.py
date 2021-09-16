# wapp to read marks (0 to 100) and print grad
# m>=80 --> Grade A, m>= 60---> Grade B
# m>= 40 ---> Grade C else Grade D

marks = int(input("enter your marks"))
if marks < 0 or marks > 100:
	print("invalid marks")
elif marks >= 80:
	print("Grade A")
elif marks >= 60:
	print("Grade B")
elif marks >= 40:
	print("Grade C ")
else :
	print("Grade D")
