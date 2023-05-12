import sys

year = int(input("Please type the year you were born: "))

if year <= 2001:
    sys.stdout.write("%s \n" % "You are old.")
elif year >= 2002:
    sys.stdout.write("%s \n" % "I bet you you're addicted to TikTok")

month = input("Please type the month you were born: ").lower()
date = int(input("Please type the date you were born: "))

listofmonths = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
starsign = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"]

if month == "january" and 20 <= date <= 31:
    sys.stdout.write("%s \n" % "You are an Aquarius")
    starsign[0]
elif month == "february" and 1 <= date <= 18:
    sys.stdout.write("%s \n" % "You are an Aquarius")
    starsign[0]
    
elif month == "february" and 19 <= date <= 29:
    sys.stdout.write("%s \n" % "You are a Pisces")
    starsign[1]
elif month == "march" and 1 <= date <= 20:
    sys.stdout.write("%s \n" % "You are a Pisces")
    starsign[1]

if month == "february" and date >= 30:
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "march" and 21 <= date <= 31:
    sys.stdout.write("%s \n" % "You are an Aries")
    starsign[2]
elif month == "april" and 1 <= date <= 19:
    sys.stdout.write("%s \n" % "You are an Aries")
    starsign[2]
    
elif month == "april" and 20 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Taurus")
    starsign[3]
elif month == "may" and 1 <= date <= 20:
    sys.stdout.write("%s \n" % "You are a Taurus")
    starsign[3]

if month == "april" and date >= 31:
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "may" and 21 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Gemini")
    starsign[4]
elif month == "june" and 1 <= date <= 20:
    sys.stdout.write("%s \n" % "You are a Gemini")
    starsign[4]
    
elif month == "june" and 21 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Cancer")
    starsign[5]
elif month == "july" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Cancer")
    starsign[5]

if month == "june" and date >= 31:
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "july" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Leo")
    starsign[6]
elif month == "august" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Leo")
    starsign[6]
    
elif month == "august" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Virgo")
    starsign[7]
elif month == "september" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Virgo")
    starsign[7]
    
elif month == "september" and 23 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Libra")
    starsign[8]
elif month == "october" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Libra")
    starsign[8]

if month == "september" and date >= 31:
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "october" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Scorpio")
    starsign[9]
elif month == "november" and 1 <= date <= 21:
    sys.stdout.write("%s \n" % "You are a Scorpio")
    starsign[9]

elif month == "november" and 21 <= date <= 30:
    sys.stdout.write("%s \n" % "You are a Sagittarius")
    starsign[10]
elif month == "december" and 1 <= date <= 22:
    sys.stdout.write("%s \n" % "You are a Sagittarius")
    starsign[10]

if month == "november" and date >= 31:
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "december" and 23 <= date <= 31:
    sys.stdout.write("%s \n" % "You are a Capricorn")
    starsign[11]
elif month == "january" and 1 <= date <= 19:
    sys.stdout.write("%s \n" % "You are a Capricorn")
    starsign[11]

if month not in listofmonths or date not in range(1,32):
    sys.stdout.write("%s \n" % "Try again. Obviously you can't follow simple instructions")
    
horoscope = input("What would you like to know about your future? LOVE? HEALTH? FAMILY? WORK? FINANCE? TRAVEL? ").lower()
future = ["love", "health", "family", "work", "finance", "travel"]

if horoscope == "love" and starsign[0]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[0]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[0]:
    #randomly pick
elif horoscope == "work" and starsign[0]:
    #randomly pick
elif horoscope == "finance" and starsign[0]:
    #randomly pick
elif horoscope == "travel" and starsign[0]:
    #randomly pick

elif horoscope == "love" and starsign[1]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[1]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[1]:
    #randomly pick
elif horoscope == "work" and starsign[1]:
    #randomly pick
elif horoscope == "finance" and starsign[1]:
    #randomly pick
elif horoscope == "travel" and starsign[1]:
    #randomly pick

elif horoscope == "love" and starsign[2]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[2]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[2]:
    #randomly pick
elif horoscope == "work" and starsign[2]:
    #randomly pick
elif horoscope == "finance" and starsign[2]:
    #randomly pick
elif horoscope == "travel" and starsign[2]:
    #randomly pick

elif horoscope == "love" and starsign[3]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[3]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[3]:
    #randomly pick
elif horoscope == "work" and starsign[3]:
    #randomly pick
elif horoscope == "finance" and starsign[3]:
    #randomly pick
elif horoscope == "travel" and starsign[3]:
    #randomly pick

elif horoscope == "love" and starsign[4]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[4]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[4]:
    #randomly pick
elif horoscope == "work" and starsign[4]:
    #randomly pick
elif horoscope == "finance" and starsign[4]:
    #randomly pick
elif horoscope == "travel" and starsign[4]:
    #randomly pick
    
elif horoscope == "love" and starsign[5]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[5]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[5]:
    #randomly pick
elif horoscope == "work" and starsign[5]:
    #randomly pick
elif horoscope == "finance" and starsign[5]:
    #randomly pick
elif horoscope == "travel" and starsign[5]:
    #randomly pick
    
elif horoscope == "love" and starsign[6]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[6]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[6]:
    #randomly pick
elif horoscope == "work" and starsign[6]:
    #randomly pick
elif horoscope == "finance" and starsign[6]:
    #randomly pick
elif horoscope == "travel" and starsign[6]:
    #randomly pick
    
elif horoscope == "love" and starsign[7]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[7]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[7]:
    #randomly pick
elif horoscope == "work" and starsign[7]:
    #randomly pick
elif horoscope == "finance" and starsign[7]:
    #randomly pick
elif horoscope == "travel" and starsign[7]:
    #randomly pick
    
elif horoscope == "love" and starsign[8]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[8]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[8]:
    #randomly pick
elif horoscope == "work" and starsign[8]:
    #randomly pick
elif horoscope == "finance" and starsign[8]:
    #randomly pick
elif horoscope == "travel" and starsign[8]:
    #randomly pick
    
elif horoscope == "love" and starsign[9]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[9]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[9]:
    #randomly pick
elif horoscope == "work" and starsign[9]:
    #randomly pick
elif horoscope == "finance" and starsign[9]:
    #randomly pick
elif horoscope == "travel" and starsign[9]:
    #randomly pick
    
elif horoscope == "love" and starsign[10]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[10]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[10]:
    #randomly pick
elif horoscope == "work" and starsign[10]:
    #randomly pick
elif horoscope == "finance" and starsign[10]:
    #randomly pick
elif horoscope == "travel" and starsign[10]:
    #randomly pick
    
elif horoscope == "love" and starsign[11]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "health" and starsign[11]:
    #randomly picks from 3 possible horoscopes
elif horoscope == "family" and starsign[11]:
    #randomly pick
elif horoscope == "work" and starsign[11]:
    #randomly pick
elif horoscope == "finance" and starsign[11]:
    #randomly pick
elif horoscope == "travel" and starsign[11]:
    #randomly pick
