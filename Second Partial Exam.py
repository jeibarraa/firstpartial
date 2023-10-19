https://replit.com/join/qxxgqrrqlf-jose-emilioem22

print("This program will help us know in what state is our plant Ruby, and what do we need to do depending on the conditions")

x=int(input("Enter the temperature in Celcius "))
y=input("Enter what day of the week are we in  ")
z=int(input("Enter the humidity "))

if x<20:
  print("Bring it inside the house")
  
if x<25 and x>20:
    print("Good conditions")

if x>25:
  print("Bring it inside the house and turn on the fan")

if y.lower()=="tuesday" or y.lower()=="thursdays" or y.lower()=="saturdays":
  print("Water Ruby ")
else:
  print("Ruby has enough water right now")

if z<20:
  print("You should water Ruby")

if z>=20 and z<=22:
  print("Suitable Humidity")

if z>22 and y.lower()=="monday" or y.lower()=="wednesday" or y.lower()=="friday" or y.lower()=="sunday":
  print("It's not necessary to water Ruby")
