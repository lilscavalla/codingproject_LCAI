import sys, random, time

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

listofmonths = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"] #so the programme knows what months are actual dates
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
    "september": range(1, 31),
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
        ss = horoscopesstarsign[0] #makes the programme know which horoscopestarsign it has just output
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

slowtype("What aspect of your future would you like to find out about? \nChoose from: LOVE, HEALTH, FAMILY, WORK, FINANCE, and TRAVEL \nInput your choice here: ")
future = ["love", "health", "family", "work", "finance", "travel"] #so the programme knows which horoscopes can be requested
#following lists contain the possible horoscopes the user will receive based on what they have input so far

lovelist0 = ["You have a face only a mother could love", "I can't imagine anyone would be particularly excited to marry you", "Good luck with that"]
healthlist0 = []
familylist0 = ["Sometimes your family purposely don't invite you to things.", "One of your family members is out to get you.", "You will want to hit your siblings, we definitley don't suggest this..."]
worklist0 = []
financelist0 = []
travellist0 = ["You are going to get sunburnt, use sun cream - or don't, I can't tell you what to do.", "Watch out for pickpockets, they target hopeless tourists like you.", "Watch out for exotic foods, food poisoning is in your future. Enjoy."]
lovelist1 = []
healthlist1 = []
familylist1 = ["Call your family - they won't answer but it's worth a shot.", "The ghost that haunts your family home is angry with you.","You will get a gut feeling that one of your family members is ugly."]
worklist1 = []
financelist1 = []
travellist1 = ["The airline you trust most will lose your luggage.", "I see a foreign romance in you future, it doesn't involve you but you will witness someone else's happiness.", "Stay at home, you are not suited to travel abroad."] 
lovelist2 = []
healthlist2 = []
familylist2 = ["You were a surprsie to your parents.", "Family rivalry is rife - control your ever present anger, they aren't worth it.", "Your competitive side will cause serious issues at game night."]
worklist2 = []
financelist2 = []
travellist2 = ["Imagine beautiful beaches and cocktails. Hold onto that thought because its going to be a long while before you experience it again.", "You will be stuck on a day trip with the most annoying British family - its your family.", "Your seat partner on the plane will steal you armrest - stand your ground!"] 
lovelist3 = []
healthlist3 = []
familylist3 = ["Someone in your family will be possessed by an evil spirit - my bet is it's you.", "You will betray your family - they deserved it.", "Your family think you don't have a backbone - continue proving them right."]
worklist3 = []
financelist3 = []
travellist3 = ["Try your best to not be British on holiday - other countries will not appreciate your sarcasm.", "Loud Americans will sit next to you on the plane - take your headphones!", "Sometimes booking the cheapest flights/hotels is not the best idea - keep this in mind."]
lovelist4 = []
healthlist4 = []
familylist4 = ["You will discover that you are the secret evil twin.", "Family drama is on the horizon - they know what you did.", "Minor tensions will arise today - will you remember to use your words?"]
worklist4 = []
financelist4 = []
travellist4 = ["Unforutnately, there is no travelling in your near future - travelling costs money and currently you're broke.", "The German tourists will take all the sunbeads at the hotel pool.", "There will be no cold water at the hotel - you will need to come up with an ingenious way to cool down or just be uncomfortable and complain about it."] 
lovelist5 = []
healthlist5 = []
familylist5 = ["An estranged uncle will tell you the truth about your birth.", "Be nice to your family - it is will writing season.", "Your future mother in law will not like you."]
worklist5 = []
financelist5 = []
travellist5 = ["You will suffer from lots of mosquito bites this summer - coat yourself in bug spray if you want to avoid the itching.", "There will be a time when you can afford to travel, that time is not now.", "That friend you made on holiday when you were 7 has forgotten about you."] 
lovelist6 = []
healthlist6 = []
familylist6 = ["You are not your pets favourite human - give them more treats.", "At family weddings this year you will be a liability.", "Your inheritance will come into question this week - tread carefully."]
worklist6 = []
financelist6 = []
travellist6 = ["You will win an all inclusive trip to Malta! Just kidding you won't.", "I have a feeling you will start to get travel sick, not just on boats but planes and cars too. Maybe even trains.", "Your tan lines will be embarrassing no matter what you do to try and fix them."]
lovelist7 = []
healthlist7 = []
familylist7 = ["One of your family members will eat your leftovers.", "Be wary of siblings, they will betray you to save themselves.", "Harm will come to you if you don't embarrass your children."]
worklist7 = []
financelist7 = []
travellist7 = ["A seagull will poop on you at the beach.", "You will burn your feet on the hot white sand - the salty water will not be pleasant after this.", "Your expensive foreign ice cream will fall on the floor."] 
lovelist8 = []
healthlist8 = []
familylist8 = ["Be wary of dinner invitations from family - they are not as innocent as they seem.", "Tension is brewing - your family may not agree with your choices this week.", "Someone in your family was swapped at birth."]
worklist8 = []
financelist8 = []
travellist8 = ["Knock off purchases rarely last very long - maybe leave the gukki handbag next time.", "All the sunbeds at the beach will be taken if you get there after 10am - you will need to work on your morning routine if you want one.", "Your family will get annoyed with you for working while you are on holiday."] 
lovelist9 = []
healthlist9 = []
familylist9 = ["Take some time away from family this week - they are sick of you.", "A distant member of your family will turn up to insult you.", "You will have a gut feeling that your family went on holiday without you - they did."]
worklist9 = []
financelist9 = []
travellist9 = ["A seagull will steal your doughnut and flap its wings into your face.", "Allowing other people to plan your trip doesn''t always work in your favour.", "Your new passport will only arrive the day you are planning to leave for your holiday."]
lovelist10 = []
healthlist10 = []
familylist10 = ["Your family have joined a cult - they will try to indoctrinate you.", "A distant member of your family will contact you about you car's extended warranty.", "You may find yourself cleaning crayon off the walls wondering where you went wrong."]
worklist10 = []
financelist10 = []
travellist10 = ["Suncream will leak into you suitcase - this is unfortanate for many reasons. Firstlly, sun cream is very expensive and secondly, your clothes will be covered in it.", "There is part of me that doesn't want to tell you this but you won't find the love of your life on a beach in spain.", "If you order lamb in the mediterranean, it will most likely be goat."] 
lovelist11 = []
healthlist11 = []
familylist11 = ["A distant member of your family has found your secret stash.", "You may find yourself alone at the dinner table, wondering where you went wrong.", "If you're going on a family holiday this summer, prepare for some drama."]
worklist11 = []
financelist11 = []
travellist11 = ["Your plane will be delayed because you packed the wrong size bag.", "Seasickness will ruin any future sailing experiences.", "Your inability to learn the language of the country you are visiting will come back to bite you."] 


while True:
    horoscope = input().lower()
    if horoscope == "love" and ss == horoscopesstarsign[0]:
        slowtype(random.choice(lovelist0)) #randomly picks from the list to output the horoscope
    elif horoscope == "health" and ss == horoscopesstarsign[0]:
        slowtype(random.choice(healthlist0))
    elif horoscope == "family" and ss == horoscopesstarsign[0]:
        slowtype(random.choice(familylist0))
    elif horoscope == "work" and ss == horoscopesstarsign[0]:
        slowtype(random.choice(worklist0))
    elif horoscope == "finance" and ss == horoscopesstarsign[0]:
        slowtype(random.choice(financelist0))
    elif horoscope == "travel" and ss == horoscopesstarsign[0]:
        slowtype(random.choice(travellist))
        slowtype(random.choice(travellist0))

    elif horoscope == "love" and ss == horoscopesstarsign[1]:
        slowtype(random.choice(lovelist1))
    elif horoscope == "health" and ss == horoscopesstarsign[1]:
        slowtype(random.choice(healthlist1))
    elif horoscope == "family" and ss == horoscopesstarsign[1]:
        slowtype(random.choice(familylist1))
    elif horoscope == "work" and ss == horoscopesstarsign[1]:
        slowtype(random.choice(worklist1))
    elif horoscope == "finance" and ss == horoscopesstarsign[1]:
        slowtype(random.choice(financelist1))
    elif horoscope == "travel" and ss == horoscopesstarsign[1]:
        slowtype(random.choice(travellist1))
        
    elif horoscope == "love" and ss == horoscopesstarsign[2]:
        slowtype(random.choice(lovelist2))
    elif horoscope == "health" and ss == horoscopesstarsign[2]:
        slowtype(random.choice(healthlist2))
    elif horoscope == "family" and ss == horoscopesstarsign[2]:
        slowtype(random.choice(familylist2))
    elif horoscope == "work" and ss == horoscopesstarsign[2]:
        slowtype(random.choice(worklist2))
    elif horoscope == "finance" and ss == horoscopesstarsign[2]:
        slowtype(random.choice(financelist2))
    elif horoscope == "travel" and ss == horoscopesstarsign[2]:
        slowtype(random.choice(travellist2))
     
    elif horoscope == "love" and ss == horoscopesstarsign[3]:
        slowtype(random.choice(lovelist3))
    elif horoscope == "health" and ss == horoscopesstarsign[3]:
        slowtype(random.choice(healthlist3))
    elif horoscope == "family" and ss == horoscopesstarsign[3]:
        slowtype(random.choice(familylist3))
    elif horoscope == "work" and ss == horoscopesstarsign[3]:
        slowtype(random.choice(worklist3))
    elif horoscope == "finance" and ss == horoscopesstarsign[3]:
        slowtype(random.choice(financelist3))
    elif horoscope == "travel" and ss == horoscopesstarsign[3]:
        slowtype(random.choice(travellist3))
        
    elif horoscope == "love" and ss == horoscopesstarsign[4]:
        slowtype(random.choice(lovelist4))
    elif horoscope == "health" and ss == horoscopesstarsign[4]:
        slowtype(random.choice(healthlist4))
    elif horoscope == "family" and ss == horoscopesstarsign[4]:
        slowtype(random.choice(familylist4))
    elif horoscope == "work" and ss == horoscopesstarsign[4]:
        slowtype(random.choice(worklist4))
    elif horoscope == "finance" and ss == horoscopesstarsign[4]:
        slowtype(random.choice(financelist4))
    elif horoscope == "travel" and ss == horoscopesstarsign[4]:
        slowtype(random.choice(travellist4))
        
    elif horoscope == "love" and ss == horoscopesstarsign[5]:
        slowtype(random.choice(lovelist5))
    elif horoscope == "health" and ss == horoscopesstarsign[5]:
        slowtype(random.choice(healthlist5))
    elif horoscope == "family" and ss == horoscopesstarsign[5]:
        slowtype(random.choice(familylist5))
    elif horoscope == "work" and ss == horoscopesstarsign[5]:
        slowtype(random.choice(worklist5))
    elif horoscope == "finance" and ss == horoscopesstarsign[5]:
        slowtype(random.choice(financelist5))
    elif horoscope == "travel" and ss == horoscopesstarsign[5]:
        slowtype(random.choice(travellist5))
       
    elif horoscope == "love" and ss == horoscopesstarsign[6]:
        slowtype(random.choice(lovelist6))
    elif horoscope == "health" and ss == horoscopesstarsign[6]:
        slowtype(random.choice(healthlist6))
    elif horoscope == "family" and ss == horoscopesstarsign[6]:
        slowtype(random.choice(familylist6))
    elif horoscope == "work" and ss == horoscopesstarsign[6]:
        slowtype(random.choice(worklist6))
    elif horoscope == "finance" and ss == horoscopesstarsign[6]:
        slowtype(random.choice(financelist6))
    elif horoscope == "travel" and ss == horoscopesstarsign[6]:
        slowtype(random.choice(travellist6))
       
    elif horoscope == "love" and ss == horoscopesstarsign[7]:
        slowtype(random.choice(lovelist7))
    elif horoscope == "health" and ss == horoscopesstarsign[7]:
        slowtype(random.choice(healthlist7))
    elif horoscope == "family" and ss == horoscopesstarsign[7]:
        slowtype(random.choice(familylist7))
    elif horoscope == "work" and ss == horoscopesstarsign[7]:
        slowtype(random.choice(worklist7))
    elif horoscope == "finance" and ss == horoscopesstarsign[7]:
        slowtype(random.choice(financelist7))
    elif horoscope == "travel" and ss == horoscopesstarsign[7]:
        slowtype(random.choice(travellist7))
        
    elif horoscope == "love" and ss == horoscopesstarsign[8]:
        slowtype(random.choice(lovelist8))
    elif horoscope == "health" and ss == horoscopesstarsign[8]:
        slowtype(random.choice(healthlist8))
    elif horoscope == "family" and ss == horoscopesstarsign[8]:
        slowtype(random.choice(familylist8))
    elif horoscope == "work" and ss == horoscopesstarsign[8]:
        slowtype(random.choice(worklist8))
    elif horoscope == "finance" and ss == horoscopesstarsign[8]:
        slowtype(random.choice(financelist8))
    elif horoscope == "travel" and ss == horoscopesstarsign[8]:
        slowtype(random.choice(travellist8))
         
    elif horoscope == "love" and ss == horoscopesstarsign[9]:
        slowtype(random.choice(lovelist9))
    elif horoscope == "health" and ss == horoscopesstarsign[9]:
        slowtype(random.choice(healthlist9))
    elif horoscope == "family" and ss == horoscopesstarsign[9]:
        slowtype(random.choice(familylist9))
    elif horoscope == "work" and ss == horoscopesstarsign[9]:
        slowtype(random.choice(worklist9))
    elif horoscope == "finance" and ss == horoscopesstarsign[9]:
        slowtype(random.choice(financelist9))
    elif horoscope == "travel" and ss == horoscopesstarsign[9]:
        slowtype(random.choice(travellist9))
        
    elif horoscope == "love" and ss == horoscopesstarsign[10]:
        slowtype(random.choice(lovelist10))
    elif horoscope == "health" and ss == horoscopesstarsign[10]:
        slowtype(random.choice(healthlist10))
    elif horoscope == "family" and ss == horoscopesstarsign[10]:
        slowtype(random.choice(familylist10))
    elif horoscope == "work" and ss == horoscopesstarsign[10]:
        slowtype(random.choice(worklist10))
    elif horoscope == "finance" and ss == horoscopesstarsign[10]:
        slowtype(random.choice(financelist10))
    elif horoscope == "travel" and ss == horoscopesstarsign[10]:
        slowtype(random.choice(travellist10))
        
    elif horoscope == "love" and ss == horoscopesstarsign[11]:
        slowtype(random.choice(lovelist11))
    elif horoscope == "health" and ss == horoscopesstarsign[11]:
        slowtype(random.choice(healthlist11))
    elif horoscope == "family" and ss == horoscopesstarsign[11]:
        slowtype(random.choice(familylist11))
    elif horoscope == "work" and ss == horoscopesstarsign[11]:
        slowtype(random.choice(worklist11))
    elif horoscope == "finance" and ss == horoscopesstarsign[11]:
        slowtype(random.choice(financelist11))
    elif horoscope == "travel" and ss == horoscopesstarsign[11]:
        slowtype(random.choice(travellist11))
        
    if horoscope not in future:
        slowtype("%s \n" % "Did I say I could do that? Try again: ") #stops user requesting a horoscope we havent programmed
        

    slowtype("\nDo you want to learn about another aspect of your future? ")
    if input().lower() == "no":
        break
    else:
        slowtype("\nChoose from: LOVE, HEALTH, FAMILY, WORK, FINANCE, and TRAVEL \nInput your choice here: ")



        
