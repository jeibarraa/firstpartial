https://replit.com/join/xizglpwlqc-jose-emilioem22
print("This program will evaluate how good student you are depending if you had class participation and a good average grade and a good project score")

x=int(input("Introduce the average grade"))
y=input("Did the student had classroom participation? (Please answer yes or no)")
z=int(input("Introduce the project score 1-100"))

if x>=75 and y=="yes":
  print("You are in a good academic standing")
else:
  print("You are not in a good academic standing, you should improve your grade by studying more, payon attention in classes or maybe if required it is recommended asking for an extra session with the teacher")

if z>90:
  print("Excellent! You will receive a distinction for your high grade!")

if x<60  or y=="no":
  print("You need to improve your perfomance")
