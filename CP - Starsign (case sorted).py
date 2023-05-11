import sys

year = int(input("Please type the year you were born: "))

if year <= 2001:
    sys.stdout.write("%s \n" % "You are old.")
elif year >= 2002:
    sys.stdout.write("%s \n" % "I bet you you're addicted to TikTok")

month = input("Please type the month you were born: ").lower()
date = int(input("Please type the date you were born: "))

listofmonths = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

if month == "january" and 20 <= date <= 31:
    sys.stdout.write("%s \n" % "You are an Aquarius")
elif month == "febraury" and 1 <= date <= 18:
    sys.stdout.write("%s \n" % "You are an Aquarius")
    
elif month == "february" and 19 <= date <= 29:
    sys.stdout.write("%s \n" % "You are a Pisces")
elif month == "march" and 1 <= date <= 20:
    sys.stdout.write("%s \n" % "You are a Pisces")

if month == "february" and date >= 30:
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "march" and 21 <= date <= 31:
    sys.stdout.write("%s \n" % "You are an Aries")
elif month == "april" and 1 <= date <= 19:
    sys.stdout.write("%s \n" % "You are an Aries")
    
elif month == "april" and 20 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Taurus")
elif month == "may" and 1 <= date <= 20:
    sys.stdout.write("%s \n" % "You are a Taurus")

if month == "april" and date >= 31:
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "may" and 21 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Gemini")
elif month == "june" and 1 <= date <= 20:
    sys.stdout.write("%s \n" % "You are a Gemini")
    
elif month == "june" and 21 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Cancer")
elif month == "july" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Cancer")

if month == "june" and date >= 31:
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "july" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Leo")
elif month == "august" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Leo")
    
elif month == "august" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Virgo")
elif month == "september" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Virgo")
    
elif month == "september" and 23 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Libra")
elif month == "october" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Libra")

if month == "september" and date >= 31:
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "october" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Scorpio")
elif month == "november" and 1 <= date <= 21:
    sys.stdout.write("%s \n" % "You are a Scorpio")

elif month == "november" and 21 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Sagittarius")
elif month == "december" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Sagittarius")

if month == "november" and date >= 31:
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "december" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Capricorn")
elif month == "january" and 1 <= date <= 19:
    sys.stdout.write("%s \n" % "You are a Capricorn")

if month not in listofmonths or date not in range(1,32):
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions")
