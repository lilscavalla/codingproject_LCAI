import sys

year = int(input("Please type the year you were born: "))

if year <= 2001:
    sys.stdout.write("%s \n" % "You are old.")
elif year >= 2002:
    sys.stdout.write("%s \n" % "I bet you you're addicted to TikTok")

month = input("Please type the month you were born: ")
date = int(input("Please type the date you were born: "))

listofmonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if month == "January" and 20 <= date <= 31:
    sys.stdout.write("%s \n" % "You are an Aquarius")
elif month == "Febraury" and 1 <= date <= 18:
    sys.stdout.write("%s \n" % "You are an Aquarius")
    
elif month == "February" and 19 <= date <= 29:
    sys.stdout.write("%s \n" % "You are a Pisces")
elif month == "March" and 1 <= date <= 20:
    sys.stdout.write("%s \n" % "You are a Pisces")
    
elif month == "March" and 21 <= date <= 31:
    sys.stdout.write("%s \n" % "You are an Aries")
elif month == "April" and 1 <= date <= 19:
    sys.stdout.write("%s \n" % "You are an Aries")
    
elif month == "April" and 20 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Taurus")
elif month == "May" and 1 <= date <= 20:
    sys.stdout.write("%s \n" % "You are a Taurus")
    
elif month == "May" and 21 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Gemini")
elif month == "June" and 1 <= date <= 20:
    sys.stdout.write("%s \n" % "You are a Gemini")
    
elif month == "June" and 21 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Cancer")
elif month == "July" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Cancer")
    
elif month == "July" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Leo")
elif month == "August" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Leo")
    
elif month == "August" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Virgo")
elif month == "September" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Virgo")
    
elif month == "September" and 23 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Libra")
elif month == "October" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Libra")
    
elif month == "October" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Scorpio")
elif month == "November" and 1 <= date <= 21:
    sys.stdout.write("%s \n" % "You are a Scorpio")
    
elif month == "November" and 21 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Sagittarius")
elif month == "December" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Sagittarius")
    
elif month == "December" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Capricorn")
elif month == "January" and 1 <= date <= 19:
    sys.stdout.write("%s \n" % "You are a Capricorn")

if month not in listofmonths or date not in range(1,31):
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions")

