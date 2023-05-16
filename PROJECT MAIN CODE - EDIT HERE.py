import sys, random

year = int(input("Please type the year you were born: "))

if year <= 2001:
    sys.stdout.write("%s \n" % "Damn. You are old.")
elif year >= 2002:
    sys.stdout.write("%s \n" % "I bet you you're addicted to TikTok")

month = input("Please type out the month you were born: ").lower()
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

lovelist0 = ["You have a face only a mother could love", "I can't imagine anyone would be particularly excited to marry you", "Good luck with that"]
healthlist0 = []
familylist0 = []
worklist0 = []
financelist0 = []
travellist0 = []
if horoscope == "love" and starsign[0]:
    sys.stdout.write(random.choice(lovelist0))
elif horoscope == "health" and starsign[0]:
    sys.stdout.write(random.choice(healthlist0))
elif horoscope == "family" and starsign[0]:
    sys.stdout.write(random.choice(familylist0))
elif horoscope == "work" and starsign[0]:
    sys.stdout.write(random.choice(worklist0))
elif horoscope == "finance" and starsign[0]:
    sys.stdout.write(random.choice(financelist0))
elif horoscope == "travel" and starsign[0]:
    sys.stdout.write(random.choice(travellist))

lovelist1 = []
healthlist1 = []
familylist1 = []
worklist1 = []
financelist1 = []
travellist1 = []       
elif horoscope == "love" and starsign[1]:
    sys.stdout.write(random.choice(lovelist1))
elif horoscope == "health" and starsign[1]:
    sys.stdout.write(random.choice(healthlist1))
elif horoscope == "family" and starsign[1]:
    sys.stdout.write(random.choice(familylist1))
elif horoscope == "work" and starsign[1]:
    sys.stdout.write(random.choice(worklist1))
elif horoscope == "finance" and starsign[1]:
    sys.stdout.write(random.choice(financelist1))
elif horoscope == "travel" and starsign[1]:
    sys.stdout.write(random.choice(travellist1))

lovelist2 = []
healthlist2 = []
familylist2 = []
worklist2 = []
financelist2 = []
travellist2 = [] 
elif horoscope == "love" and starsign[2]:
    sys.stdout.write(random.choice(lovelist2))
elif horoscope == "health" and starsign[2]:
    sys.stdout.write(random.choice(healthlist2))
elif horoscope == "family" and starsign[2]:
    sys.stdout.write(random.choice(familylist2))
elif horoscope == "work" and starsign[2]:
    sys.stdout.write(random.choice(worklist2))
elif horoscope == "finance" and starsign[2]:
    sys.stdout.write(random.choice(financelist2))
elif horoscope == "travel" and starsign[2]:
    sys.stdout.write(random.choice(travellist2))

lovelist3 = []
healthlist3 = []
familylist3 = []
worklist3 = []
financelist3 = []
travellist3 = [] 
elif horoscope == "love" and starsign[3]:
    sys.stdout.write(random.choice(lovelist3))
elif horoscope == "health" and starsign[3]:
    sys.stdout.write(random.choice(healthlist3))
elif horoscope == "family" and starsign[3]:
    sys.stdout.write(random.choice(familylist3))
elif horoscope == "work" and starsign[3]:
    sys.stdout.write(random.choice(worklist3))
elif horoscope == "finance" and starsign[3]:
    sys.stdout.write(random.choice(financelist3))
elif horoscope == "travel" and starsign[3]:
    sys.stdout.write(random.choice(travellist3))

lovelist4 = []
healthlist4 = []
familylist4 = []
worklist4 = []
financelist4 = []
travellist4 = [] 
elif horoscope == "love" and starsign[4]:
    sys.stdout.write(random.choice(lovelist4))
elif horoscope == "health" and starsign[4]:
    sys.stdout.write(random.choice(healthlist4))
elif horoscope == "family" and starsign[4]:
    sys.stdout.write(random.choice(familylist4))
elif horoscope == "work" and starsign[4]:
    sys.stdout.write(random.choice(worklist4))
elif horoscope == "finance" and starsign[4]:
    sys.stdout.write(random.choice(financelist4))
elif horoscope == "travel" and starsign[4]:
    sys.stdout.write(random.choice(travellist4))
    
lovelist5 = []
healthlist5 = []
familylist5 = []
worklist5 = []
financelist5 = []
travellist5 = [] 
elif horoscope == "love" and starsign[5]:
    sys.stdout.write(random.choice(lovelist5))
elif horoscope == "health" and starsign[5]:
    sys.stdout.write(random.choice(healthlist5))
elif horoscope == "family" and starsign[5]:
    sys.stdout.write(random.choice(familylist5))
elif horoscope == "work" and starsign[5]:
    sys.stdout.write(random.choice(worklist5))
elif horoscope == "finance" and starsign[5]:
    sys.stdout.write(random.choice(financelist5))
elif horoscope == "travel" and starsign[5]:
    sys.stdout.write(random.choice(travellist5))
  
lovelist6 = []
healthlist6 = []
familylist6 = []
worklist6 = []
financelist6 = []
travellist6 = [] 
elif horoscope == "love" and starsign[6]:
    sys.stdout.write(random.choice(lovelist6))
elif horoscope == "health" and starsign[6]:
    sys.stdout.write(random.choice(healthlist6))
elif horoscope == "family" and starsign[6]:
    sys.stdout.write(random.choice(familylist6))
elif horoscope == "work" and starsign[6]:
    sys.stdout.write(random.choice(worklist6)
elif horoscope == "finance" and starsign[6]:
    sys.stdout.write(random.choice(financelist6))
elif horoscope == "travel" and starsign[6]:
    sys.stdout.write(random.choice(travellist6))
   
lovelist7 = []
healthlist7 = []
familylist7 = []
worklist7 = []
financelist7 = []
travellist7 = [] 
elif horoscope == "love" and starsign[7]:
    sys.stdout.write(random.choice(lovelist7))
elif horoscope == "health" and starsign[7]:
    sys.stdout.write(random.choice(healthlist7))
elif horoscope == "family" and starsign[7]:
    sys.stdout.write(random.choice(familylist7))
elif horoscope == "work" and starsign[7]:
    sys.stdout.write(random.choice(worklist7))
elif horoscope == "finance" and starsign[7]:
    sys.stdout.write(random.choice(financelist7))
elif horoscope == "travel" and starsign[7]:
    sys.stdout.write(random.choice(travellist7))
    
lovelist8 = []
healthlist8 = []
familylist8 = []
worklist8 = []
financelist8 = []
travellist8 = [] 
elif horoscope == "love" and starsign[8]:
    sys.stdout.write(random.choice(lovelist8))
elif horoscope == "health" and starsign[8]:
    sys.stdout.write(random.choice(healthlist8))
elif horoscope == "family" and starsign[8]:
    sys.stdout.write(random.choice(familylist8))
elif horoscope == "work" and starsign[8]:
    sys.stdout.write(random.choice(worklist8))
elif horoscope == "finance" and starsign[8]:
    sys.stdout.write(random.choice(financelist8))
elif horoscope == "travel" and starsign[8]:
    sys.stdout.write(random.choice(travellist8))
    
lovelist9 = []
healthlist9 = []
familylist9 = []
worklist9 = []
financelist9 = []
travellist9 = [] 
elif horoscope == "love" and starsign[9]:
    sys.stdout.write(random.choice(lovelist9))
elif horoscope == "health" and starsign[9]:
    sys.stdout.write(random.choice(healthlist9))
elif horoscope == "family" and starsign[9]:
    sys.stdout.write(random.choice(familylist9))
elif horoscope == "work" and starsign[9]:
    sys.stdout.write(random.choice(worklist9))
elif horoscope == "finance" and starsign[9]:
    sys.stdout.write(random.choice(financelist9))
elif horoscope == "travel" and starsign[9]:
    sys.stdout.write(random.choice(travellist9))
    
lovelist10 = []
healthlist10 = []
familylist10 = []
worklist10 = []
financelist10 = []
travellist10 = [] 
elif horoscope == "love" and starsign[10]:
    sys.stdout.write(random.choice(lovelist10))
elif horoscope == "health" and starsign[10]:
    sys.stdout.write(random.choice(healthlist10))
elif horoscope == "family" and starsign[10]:
    sys.stdout.write(random.choice(familylist10))
elif horoscope == "work" and starsign[10]:
    sys.stdout.write(random.choice(worklist10))
elif horoscope == "finance" and starsign[10]:
    sys.stdout.write(random.choice(financelist10))
elif horoscope == "travel" and starsign[10]:
    sys.stdout.write(random.choice(travellist10))
    
lovelist11 = []
healthlist11 = []
familylist11 = []
worklist11 = []
financelist11 = []
travellist11 = [] 
elif horoscope == "love" and starsign[11]:
    sys.stdout.write(random.choice(lovelist11)
elif horoscope == "health" and starsign[11]:
    sys.stdout.write(random.choice(healthlist11))
elif horoscope == "family" and starsign[11]:
    sys.stdout.write(random.choice(familylist11))
elif horoscope == "work" and starsign[11]:
    sys.stdout.write(random.choice(worklist11))
elif horoscope == "finance" and starsign[11]:
    sys.stdout.write(random.choice(financelist11))
elif horoscope == "travel" and starsign[11]:
    sys.stdout.write(random.choice(travellist11))
