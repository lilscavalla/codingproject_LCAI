import sys, random, time
import horoscopes #separate file the programme uses to import the horoscopes without them taking up a load of space in this main code

def slowtype(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
#'slowtype' means the outputs look as though they are being typed at that moment

slowtype("Please type the year you were born: ")
#year = int(input()) 

while True:
    year = int(input())
    if year <= 2000:
        slowtype("%s \n" % "Damn. You are old.")
    elif year == 2001:
        slowtype("%s \n" % "A good year!")
    elif year in range(2002, 2016):
        slowtype("%s \n" % "I bet you're addicted to TikTok.")
    elif year >= 2016:
        slowtype("%s \n" % "You are far too young for this, go away.")
        break
# this allows for different outputs based on the year, and will exit the program entirely if they're deemed "too young"


# listofmonths = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"] #so the programme knows what months are actual dates
# ^^ didn't want to delete this incase the dictionary failed
horoscopes.starsign = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"] #so the programme knows what horoscopes.starsigns are



monthdatematrix = {
    "january": range(1, 32),
    "february": range(1, 29),
    "march": range(1, 32),
    "april": range(1, 31),
    "may": range(1, 32),
    "june": range(1, 31),
    "july": range(1, 32),
    "august": range(1, 32),
    "sepember": range(1, 31),
    "october": range(1, 32),
    "november": range(1, 31),
    "december": range(1, 32)
}

slowtype("Please type out the month you were born: " )
# requesting input 

while True:
    month = input().lower()
    if month in monthdatematrix:
        slowtype("%s \n" % "Awesome!\nPlease type the date you were born:")
        daterange = monthdatematrix[month]
    else:
        slowtype("%s \n" % "I'm afraid that isn't a real month buddy. Try again.")
    while True:
        date = int(input())
        if date in daterange:
            slowtype("%s \n" % "Great stuff.")
        else:
            slowtype("%s \n" % "Try again dumbass.")

# the while loops test for membership in the dictionary, the first tests the KEY (months)
# the second tests the ITEM (date) in relation to the specific month, so correct month~dates are input



if month == "january" and 20 <= date <= 31:
    slowtype("%s \n" % "You are an Aquarius")
    ss = horoscopes.starsign[0]
elif month == "february" and 1 <= date <= 18:
    slowtype("%s \n" % "You are an Aquarius")
    ss = horoscopes.starsign[0] #makes the programme know which starsign it has just outputted
    
elif month == "february" and 19 <= date <= 29:
    slowtype("%s \n" % "You are a Pisces")
    ss = horoscopes.starsign[1]
elif month == "march" and 1 <= date <= 20:
    slowtype("%s \n" % "You are a Pisces")
    ss = horoscopes.starsign[1]

if month == "february" and date >= 30:
    slowtype("%s \n" % "Try again. Obviously you can't follow simple instructions.") #stops the user inputting an invalid date for february specifically
    
elif month == "march" and 21 <= date <= 31:
    slowtype("%s \n" % "You are an Aries")
    ss = horoscopes.starsign[2]
elif month == "april" and 1 <= date <= 19:
    slowtype("%s \n" % "You are an Aries")
    ss = horoscopes.starsign[2]
    
elif month == "april" and 20 <= date <= 30:
    slowtype("%s \n" % "You are a Taurus")
    ss = horoscopes.starsign[3]
elif month == "may" and 1 <= date <= 20:
    slowtype("%s \n" % "You are a Taurus")
    ss = horoscopes.starsign[3]

if month == "april" and date >= 31:
    slowtype("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "may" and 21 <= date <= 31:
    slowtype("%s \n" % "You are a Gemini")
    ss = horoscopes.starsign[4]
elif month == "june" and 1 <= date <= 20:
    slowtype("%s \n" % "You are a Gemini")
    ss = horoscopes.starsign[4]
    
elif month == "june" and 21 <= date <= 30:
    slowtype("%s \n" % "You are a Cancer")
    ss = horoscopes.starsign[5]
elif month == "july" and 1 <= date <= 22:
    slowtype("%s \n" % "You are a Cancer")
    ss = horoscopes.starsign[5]

if month == "june" and date >= 31:
    slowtype("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "july" and 23 <= date <= 31:
    slowtype("%s \n" % "You are a Leo")
    ss = horoscopes.starsign[6]
elif month == "august" and 1 <= date <= 22:
    slowtype("%s \n" % "You are a Leo")
    ss = horoscopes.starsign[6]
    
elif month == "august" and 23 <= date <= 31:
    slowtype("%s \n" % "You are a Virgo")
    ss = horoscopes.starsign[7]
elif month == "september" and 1 <= date <= 22:
    slowtype("%s \n" % "You are a Virgo")
    ss = horoscopes.starsign[7]
    
elif month == "september" and 23 <= date <= 30:
    slowtype("%s \n" % "You are a Libra")
    ss = horoscopes.starsign[8]
elif month == "october" and 1 <= date <= 22:
    slowtype("%s \n" % "You are a Libra")
    ss = horoscopes.starsign[8]

if month == "september" and date >= 31:
    slowtype("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "october" and 23 <= date <= 31:
    slowtype("%s \n" % "You are a Scorpio")
    ss = horoscopes.starsign[9]
elif month == "november" and 1 <= date <= 21:
    slowtype("%s \n" % "You are a Scorpio")
    ss = horoscopes.starsign[9]

elif month == "november" and 21 <= date <= 30:
    slowtype("%s \n" % "You are a Sagittarius")
    ss = horoscopes.starsign[10]
elif month == "december" and 1 <= date <= 22:
    slowtype("%s \n" % "You are a Sagittarius")
    ss = horoscopes.starsign[10]

if month == "november" and date >= 31:
    slowtype("%s \n" % "Try again. Obviously you can't follow simple instructions.")
    
elif month == "december" and 23 <= date <= 31:
    slowtype("%s \n" % "You are a Capricorn")
    ss = horoscopes.starsign[11]
elif month == "january" and 1 <= date <= 19:
    slowtype("%s \n" % "You are a Capricorn")
    ss = horoscopes.starsign[11]

if month not in listofmonths or date not in range(1,32):
    slowtype("%s \n" % "Try again. Obviously you can't follow simple instructions") #stops the user inputting invalid dates in general

slowtype("What aspect of your future would you like to find out about? \nChoose from: LOVE, HEALTH, FAMILY, WORK, FINANCE, and TRAVEL \nInput your choice here: ")
horoscope = input().lower()
future = ["love", "health", "family", "work", "finance", "travel"] #so the programme knows which horoscopes can be requested


if horoscope == "love" and ss == horoscopes.starsign[0]:
    slowtype(random.choice(horoscopes.lovelist0)) #randomly picks from the list to output the horoscope
elif horoscope == "health" and ss == horoscopes.starsign[0]:
    slowtype(random.choice(horoscopes.healthlist0))
elif horoscope == "family" and ss == horoscopes.starsign[0]:
    slowtype(random.choice(horoscopes.familylist0))
elif horoscope == "work" and ss == horoscopes.starsign[0]:
    slowtype(random.choice(horoscopes.worklist0))
elif horoscope == "finance" and ss == horoscopes.starsign[0]:
    slowtype(random.choice(horoscopes.financelist0))
elif horoscope == "travel" and ss == horoscopes.starsign[0]:
    slowtype(random.choice(horoscopes.travellist0))
      
elif horoscope == "love" and ss == horoscopes.starsign[1]:
    slowtype(random.choice(horoscopes.lovelist1))
elif horoscope == "health" and ss == horoscopes.starsign[1]:
    slowtype(random.choice(horoscopes.healthlist1))
elif horoscope == "family" and ss == horoscopes.starsign[1]:
    slowtype(random.choice(horoscopes.familylist1))
elif horoscope == "work" and ss == horoscopes.starsign[1]:
    slowtype(random.choice(horoscopes.worklist1))
elif horoscope == "finance" and ss == horoscopes.starsign[1]:
    slowtype(random.choice(horoscopes.financelist1))
elif horoscope == "travel" and ss == horoscopes.starsign[1]:
    slowtype(random.choice(horoscopes.travellist1))

elif horoscope == "love" and ss == horoscopes.starsign[2]:
    slowtype(random.choice(horoscopes.lovelist2))
elif horoscope == "health" and ss == horoscopes.starsign[2]:
    slowtype(random.choice(horoscopes.healthlist2))
elif horoscope == "family" and ss == horoscopes.starsign[2]:
    slowtype(random.choice(horoscopes.familylist2))
elif horoscope == "work" and ss == horoscopes.starsign[2]:
    slowtype(random.choice(horoscopes.worklist2))
elif horoscope == "finance" and ss == horoscopes.starsign[2]:
    slowtype(random.choice(horoscopes.financelist2))
elif horoscope == "travel" and ss == horoscopes.starsign[2]:
    slowtype(random.choice(horoscopes.travellist2))
 
elif horoscope == "love" and ss == horoscopes.starsign[3]:
    slowtype(random.choice(horoscopes.lovelist3))
elif horoscope == "health" and ss == horoscopes.starsign[3]:
    slowtype(random.choice(horoscopes.healthlist3))
elif horoscope == "family" and ss == horoscopes.starsign[3]:
    slowtype(random.choice(horoscopes.familylist3))
elif horoscope == "work" and ss == horoscopes.starsign[3]:
    slowtype(random.choice(horoscopes.worklist3))
elif horoscope == "finance" and ss == horoscopes.starsign[3]:
    slowtype(random.choice(horoscopes.financelist3))
elif horoscope == "travel" and ss == horoscopes.starsign[3]:
    slowtype(random.choice(horoscopes.travellist3))

elif horoscope == "love" and ss == horoscopes.starsign[4]:
    slowtype(random.choice(horoscopes.lovelist4))
elif horoscope == "health" and ss == horoscopes.starsign[4]:
    slowtype(random.choice(horoscopes.healthlist4))
elif horoscope == "family" and ss == horoscopes.starsign[4]:
    slowtype(random.choice(horoscopes.familylist4))
elif horoscope == "work" and ss == horoscopes.starsign[4]:
    slowtype(random.choice(horoscopes.worklist4))
elif horoscope == "finance" and ss == horoscopes.starsign[4]:
    slowtype(random.choice(horoscopes.financelist4))
elif horoscope == "travel" and ss == horoscopes.starsign[4]:
    slowtype(random.choice(horoscopes.travellist4))
    
elif horoscope == "love" and ss == horoscopes.starsign[5]:
    slowtype(random.choice(horoscopes.lovelist5))
elif horoscope == "health" and ss == horoscopes.starsign[5]:
    slowtype(random.choice(horoscopes.healthlist5))
elif horoscope == "family" and ss == horoscopes.starsign[5]:
    slowtype(random.choice(horoscopes.familylist5))
elif horoscope == "work" and ss == horoscopes.starsign[5]:
    slowtype(random.choice(horoscopes.worklist5))
elif horoscope == "finance" and ss == horoscopes.starsign[5]:
    slowtype(random.choice(horoscopes.financelist5))
elif horoscope == "travel" and ss == horoscopes.starsign[5]:
    slowtype(random.choice(horoscopes.travellist5))
   
elif horoscope == "love" and ss == horoscopes.starsign[6]:
    slowtype(random.choice(horoscopes.lovelist6))
elif horoscope == "health" and ss == horoscopes.starsign[6]:
    slowtype(random.choice(horoscopes.healthlist6))
elif horoscope == "family" and ss == horoscopes.starsign[6]:
    slowtype(random.choice(horoscopes.familylist6))
elif horoscope == "work" and ss == horoscopes.starsign[6]:
    slowtype(random.choice(horoscopes.worklist6))
elif horoscope == "finance" and ss == horoscopes.starsign[6]:
    slowtype(random.choice(horoscopes.financelist6))
elif horoscope == "travel" and ss == horoscopes.starsign[6]:
    slowtype(random.choice(horoscopes.travellist6))
   
elif horoscope == "love" and ss == horoscopes.starsign[7]:
    slowtype(random.choice(horoscopes.lovelist7))
elif horoscope == "health" and ss == horoscopes.starsign[7]:
    slowtype(random.choice(horoscopes.healthlist7))
elif horoscope == "family" and ss == horoscopes.starsign[7]:
    slowtype(random.choice(horoscopes.familylist7))
elif horoscope == "work" and ss == horoscopes.starsign[7]:
    slowtype(random.choice(horoscopes.worklist7))
elif horoscope == "finance" and ss == horoscopes.starsign[7]:
    slowtype(random.choice(horoscopes.financelist7))
elif horoscope == "travel" and ss == horoscopes.starsign[7]:
    slowtype(random.choice(horoscopes.travellist7))
    
elif horoscope == "love" and ss == horoscopes.starsign[8]:
    slowtype(random.choice(horoscopes.lovelist8))
elif horoscope == "health" and ss == horoscopes.starsign[8]:
    slowtype(random.choice(horoscopes.healthlist8))
elif horoscope == "family" and ss == horoscopes.starsign[8]:
    slowtype(random.choice(horoscopes.familylist8))
elif horoscope == "work" and ss == horoscopes.starsign[8]:
    slowtype(random.choice(horoscopes.worklist8))
elif horoscope == "finance" and ss == horoscopes.starsign[8]:
    slowtype(random.choice(horoscopes.financelist8))
elif horoscope == "travel" and ss == horoscopes.starsign[8]:
    slowtype(random.choice(horoscopes.travellist8))
     
elif horoscope == "love" and ss == horoscopes.starsign[9]:
    slowtype(random.choice(horoscopes.lovelist9))
elif horoscope == "health" and ss == horoscopes.starsign[9]:
    slowtype(random.choice(horoscopes.healthlist9))
elif horoscope == "family" and ss == horoscopes.starsign[9]:
    slowtype(random.choice(horoscopes.familylist9))
elif horoscope == "work" and ss == horoscopes.starsign[9]:
    slowtype(random.choice(horoscopes.worklist9))
elif horoscope == "finance" and ss == horoscopes.starsign[9]:
    slowtype(random.choice(horoscopes.financelist9))
elif horoscope == "travel" and ss == horoscopes.starsign[9]:
    slowtype(random.choice(horoscopes.travellist9))
    
elif horoscope == "love" and ss == horoscopes.starsign[10]:
    slowtype(random.choice(horoscopes.lovelist10))
elif horoscope == "health" and ss == horoscopes.starsign[10]:
    slowtype(random.choice(horoscopes.healthlist10))
elif horoscope == "family" and ss == horoscopes.starsign[10]:
    slowtype(random.choice(horoscopes.familylist10))
elif horoscope == "work" and ss == horoscopes.starsign[10]:
    slowtype(random.choice(horoscopes.worklist10))
elif horoscope == "finance" and ss == horoscopes.starsign[10]:
    slowtype(random.choice(horoscopes.financelist10))
elif horoscope == "travel" and ss == horoscopes.starsign[10]:
    slowtype(random.choice(horoscopes.travellist10))
    
elif horoscope == "love" and ss == horoscopes.starsign[11]:
    slowtype(random.choice(horoscopes.lovelist11))
elif horoscope == "health" and ss == horoscopes.starsign[11]:
    slowtype(random.choice(horoscopes.healthlist11))
elif horoscope == "family" and ss == horoscopes.starsign[11]:
    slowtype(random.choice(horoscopes.familylist11))
elif horoscope == "work" and ss == horoscopes.starsign[11]:
    slowtype(random.choice(horoscopes.worklist11))
elif horoscope == "finance" and ss == horoscopes.starsign[11]:
    slowtype(random.choice(horoscopes.financelist11))
elif horoscope == "travel" and ss == horoscopes.starsign[11]:
    slowtype(random.choice(horoscopes.travellist11))

if horoscope not in future:
    slowtype("%s \n" % "Did I say I could do that? Try again") #stops user requesting a horoscope we havent programmed
