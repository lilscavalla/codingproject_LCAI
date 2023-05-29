import sys, random, time
import horoscopes #separate file the programme uses to import the horoscopes without them taking up a load of space in this main code
# currently "import horoscopes" doesn't work

def slowtype(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
#'slowtype' means the outputs look as though they are being typed at that moment

inputmonth = []
inputdate = []
# empty lists, for user information to be appended into for later use

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
        sys.exit()
    break
# this allows for different outputs based on the year, and will exit the program entirely if they're deemed "too young"
time.sleep(0.85)

# listofmonths = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"] #so the programme knows what months are actual dates
# ^^ didn't want to delete this incase the dictionary failed
horoscopesstarsign = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"] #so the programme knows what horoscopes.starsigns are



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

slowtype("Please type the month you were born: " )
# requesting input 

while True:
    month = input().lower()
    inputmonth.append(month)
    if month in monthdatematrix:
        slowtype("%s \n" % "Awesome!")
        time.sleep(0.85)
        slowtype("Please type the date you were born: ")
        daterange = monthdatematrix[month]
        break
    else:
        slowtype("I'm afraid that isn't a real month buddy. Try again. ")

while month in monthdatematrix:
    date = int(input())
    inputdate.append(date)
    if date in daterange:
        slowtype("%s \n" % "Great stuff.")
        time.sleep(0.85)
        break
    else:
        slowtype("Try again dumbass. Obviously you can't follow simple instructions. ")

# the while loops test for membership in the dictionary, the first tests the KEY (months)
# the second tests the ITEM (date) in relation to the specific month, so correct month~dates are input
# "break" exits loop after condition met

for item in inputmonth:
    for item in inputdate:
        if month == "january" and 20 <= date <= 31:
            slowtype("%s \n" % "You are an Aquarius")
        elif month == "february" and 1 <= date <= 18:
            slowtype("%s \n" % "You are an Aquarius")
        ss = horoscopesstarsign[0] #makes the programme know which starsign it has just output
        break
        
# for loop basically tests for membership in the list that the users info was appended to
# diff loop for each ss/[index] thing because embedding 12 loops was painful

for item in inputmonth:
    for item in inputdate:
        if month == "february" and 19 <= date <= 29:
            slowtype("%s \n" % "You are a Pisces")
        elif month == "march" and 1 <= date <= 20:
            slowtype("%s \n" % "You are a Pisces")
        ss = horoscopesstarsign[1]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "march" and 21 <= date <= 31:
            slowtype("%s \n" % "You are an Aries")
        elif month == "april" and 1 <= date <= 19:
            slowtype("%s \n" % "You are an Aries")
        ss = horoscopesstarsign[2]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "april" and 20 <= date <= 30:
            slowtype("%s \n" % "You are a Taurus")
        elif month == "may" and 1 <= date <= 20:
            slowtype("%s \n" % "You are a Taurus")
        ss = horoscopesstarsign[3]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "may" and 21 <= date <= 31:
            slowtype("%s \n" % "You are a Gemini")
        elif month == "june" and 1 <= date <= 20:
            slowtype("%s \n" % "You are a Gemini")
        ss = horoscopesstarsign[4]
        break
    
for item in inputmonth:
    for item in inputdate:
        if month == "june" and 21 <= date <= 30:
            slowtype("%s \n" % "You are a Cancer")
        elif month == "july" and 1 <= date <= 22:
            slowtype("%s \n" % "You are a Cancer")
        ss = horoscopesstarsign[5]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "july" and 23 <= date <= 31:
            slowtype("%s \n" % "You are a Leo")
        elif month == "august" and 1 <= date <= 22:
            slowtype("%s \n" % "You are a Leo")
        ss = horoscopesstarsign[6]
        break

for item in inputmonth:
    for item in inputdate:    
        if month == "august" and 23 <= date <= 31:
            slowtype("%s \n" % "You are a Virgo")
        elif month == "september" and 1 <= date <= 22:
            slowtype("%s \n" % "You are a Virgo")
        ss = horoscopesstarsign[7]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "september" and 23 <= date <= 30:
            slowtype("%s \n" % "You are a Libra")
        elif month == "october" and 1 <= date <= 22:
            slowtype("%s \n" % "You are a Libra")
        ss = horoscopesstarsign[8]
        break
    
for item in inputmonth:
    for item in inputdate:
        if month == "october" and 23 <= date <= 31:
            slowtype("%s \n" % "You are a Scorpio")
        elif month == "november" and 1 <= date <= 21:
            slowtype("%s \n" % "You are a Scorpio")
        ss = horoscopesstarsign[9]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "november" and 21 <= date <= 30:
            slowtype("%s \n" % "You are a Sagittarius")
        elif month == "december" and 1 <= date <= 22:
            slowtype("%s \n" % "You are a Sagittarius")
        ss = horoscopesstarsign[10]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "december" and 23 <= date <= 31:
            slowtype("%s \n" % "You are a Capricorn")
        elif month == "january" and 1 <= date <= 19:
            slowtype("%s \n" % "You are a Capricorn")
        ss = horoscopesstarsign[11]
        break

time.sleep(0.85)

slowtype("What aspect of your future would you like to find out about?") 
time.sleep(0.2)
slowtype(" \nChoose from: LOVE, HEALTH, FAMILY, WORK, FINANCE, and TRAVEL \nInput your choice here: ") 
time.sleep(0.5)
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
