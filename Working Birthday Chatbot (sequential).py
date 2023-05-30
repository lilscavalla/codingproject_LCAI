import sys, random, time
import urllib.request
import re

def slowtype(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
#'slowtype' means the outputs look as though they are being typed at that moment

inputmonth = []
inputdate = []
# empty lists, for user information to be appended into for later use

slowtype("Hello, I am a birthday chatbot. \nI can tell you your horoscope and which celebrities you share a birthday with. \nAll I need to know is your birthday!")
#intro message

slowtype("\nPlease type the year you were born: ")
# requesting input

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
starsign = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"] #so the programme knows what starsigns are

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
        slowtype("I'm afraid that isn't a real month buddy. Try again: ")
        # loop to give the user the opportunity to type in the month again if they made a mistake

while month in monthdatematrix:
    date = int(input())
    inputdate.append(date)
    if date in daterange:
        slowtype("%s \n" % "Great stuff.")
        time.sleep(0.85)
        break
    else:
        slowtype("Try again dumbass. Obviously you can't follow simple instructions: ")
        # loop to give the user the opportunity to type in the date again if they made a mistake

# the while loops test for membership in the dictionary, the first tests the KEY (months)
# the second tests the ITEM (date) in relation to the specific month, so correct month~dates are input
# "break" exits loop after condition met

for item in inputmonth:
    for item in inputdate:
        if month == "january" and 20 <= date <= 31:
            slowtype("%s \n" % "You are an Aquarius")
            ss = starsign[0]
        elif month == "february" and 1 <= date <= 18:
            slowtype("%s \n" % "You are an Aquarius")
            ss = starsign[0] #makes the programme know which starsign it has just output
        break
        
# for loop basically tests for membership in the list that the users info was appended to
# diff loop for each ss/[index] because embedding 12 loops was painful

for item in inputmonth:
    for item in inputdate:
        if month == "february" and 19 <= date <= 29:
            slowtype("%s \n" % "You are a Pisces")
            ss = starsign[1]
        elif month == "march" and 1 <= date <= 20:
            slowtype("%s \n" % "You are a Pisces")
            ss = starsign[1]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "march" and 21 <= date <= 31:
            slowtype("%s \n" % "You are an Aries")
            ss = starsign[2]
        elif month == "april" and 1 <= date <= 19:
            slowtype("%s \n" % "You are an Aries")
            ss = starsign[2]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "april" and 20 <= date <= 30:
            slowtype("%s \n" % "You are a Taurus")
            ss = starsign[3]
        elif month == "may" and 1 <= date <= 20:
            slowtype("%s \n" % "You are a Taurus")
            ss = starsign[3]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "may" and 21 <= date <= 31:
            slowtype("%s \n" % "You are a Gemini")
            ss = starsign[4]
        elif month == "june" and 1 <= date <= 20:
            slowtype("%s \n" % "You are a Gemini")
            ss = starsign[4]
        break
    
for item in inputmonth:
    for item in inputdate:
        if month == "june" and 21 <= date <= 30:
            slowtype("%s \n" % "You are a Cancer")
            ss = starsign[5]
        elif month == "july" and 1 <= date <= 22:
            slowtype("%s \n" % "You are a Cancer")
            ss = starsign[5]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "july" and 23 <= date <= 31:
            slowtype("%s \n" % "You are a Leo")
            ss = starsign[6]
        elif month == "august" and 1 <= date <= 22:
            slowtype("%s \n" % "You are a Leo")
            ss = starsign[6]
        break

for item in inputmonth:
    for item in inputdate:    
        if month == "august" and 23 <= date <= 31:
            slowtype("%s \n" % "You are a Virgo")
            ss = starsign[7]
        elif month == "september" and 1 <= date <= 22:
            slowtype("%s \n" % "You are a Virgo")
            ss = starsign[7]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "september" and 23 <= date <= 30:
            slowtype("%s \n" % "You are a Libra")#
            ss = starsign[8]
        elif month == "october" and 1 <= date <= 22:
            slowtype("%s \n" % "You are a Libra")
            ss = starsign[8]
        break
    
for item in inputmonth:
    for item in inputdate:
        if month == "october" and 23 <= date <= 31:
            slowtype("%s \n" % "You are a Scorpio")
            ss = starsign[9]
        elif month == "november" and 1 <= date <= 21:
            slowtype("%s \n" % "You are a Scorpio")
            ss = starsign[9]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "november" and 21 <= date <= 30:
            slowtype("%s \n" % "You are a Sagittarius")
            ss = starsign[10]
        elif month == "december" and 1 <= date <= 22:
            slowtype("%s \n" % "You are a Sagittarius")
            ss = starsign[10]
        break

for item in inputmonth:
    for item in inputdate:
        if month == "december" and 23 <= date <= 31:
            slowtype("%s \n" % "You are a Capricorn")
            ss = starsign[11]
        elif month == "january" and 1 <= date <= 19:
            slowtype("%s \n" % "You are a Capricorn")
            ss = starsign[11]
        break

time.sleep(0.85)
# tie delay for better flow

slowtype("What aspect of your future would you like to find out about?") 
time.sleep(0.2)
slowtype(" \nChoose from: LOVE, HEALTH, FAMILY, WORK, FINANCE, and TRAVEL \nInput your choice here: ") 
time.sleep(0.5)
future = ["love", "health", "family", "work", "finance", "travel"] # so the programme knows which horoscopes can be requested

lovelist0 = ["You have a face only a mother could love", "I can't imagine anyone would be particularly excited to marry you", "Good luck with that"]
healthlist0 = ["You will step on an upturned plug - I would recommend wearing shoes.", "You should stop talking so much. You'll... um... get more air in your lungs that way.", "Your hair will start falling out if you keep stressing so much."]
familylist0 = ["Sometimes your family purposely don't invite you to things.", "One of your family members is out to get you.", "You will want to hit your siblings, we definitely don't suggest this..."]
worklist0 = ["Your coworkers are definitely not gossiping about your outfit in the break room.", "Take a leap of faith, do what you love. No point making almost no money doing something you hate.", "Someone will start stealing your lunch from the fridge. I'm surprised considering your cooking... yuck."]
financelist0 = ["Don't spend all day looking for lucky pennies. I've bumped into lots of lamp posts that way.", "Your computer will be hacked and they will get access to your bank account. Luckily for you, there was nothing in there anyway.", "Money can't buy happiness. That's a lie, it definitely can - maybe someday you'll be happy."]
travellist0 = ["You are going to get sunburnt, use sun cream - or don't, I can't tell you what to do.", "Watch out for pickpockets, they target hopeless tourists like you.", "Watch out for exotic foods, food poisoning is in your future. Enjoy."]

lovelist1 = ["The situationship you are in is a relationship. Just pick up the courage to accept that, so you both can move forward.", "Asking someone out is daunting. You don't have it in you. Maybe work on that this week.", "You will see a beautiful stranger in the queue at the club. You will not be allowed in though."]
healthlist1 = ["You will sneeze 37 times next week. Count them, I dare you.", "You will finally start going to the gym this week - let's hope it continues this way.", "Stay away from foods you could choke on. Your future may depend on it this week."]
familylist1 = ["Call your family - they won't answer but it's worth a shot.", "The ghost that haunts your family home is angry with you.","You will get a gut feeling that one of your family members is ugly."]
worklist1 = ["Have you considered a job in the circus? I think it would suit you better.", "It feels great making a difference in the world. Shame you're pressing keys in a cubicle all day.", "No one will forget what you did at the work Christmas party... no one..."]
financelist1 = ["Have you tried gambling before? It's a great way to lose all your money.", "This is the perfect time to take a risk, live a little, or buy something you wouldn't have otherwise. Maybe it will help you be less boring.", "You should try hiring an accountant - you do not have the skills to organise your finances yourself."]
travellist1 = ["The airline you trust most will lose your luggage.", "I see a foreign romance in you future, it doesn't involve you but you will witness someone else's happiness.", "Stay at home, you are not suited to travel abroad."] 

lovelist2 = ["You already know what I'm going to say. Come back next week, maybe there will be some good news.", "The club isn't the best place to find a lover so you should try your housemate. That will end well.", "In a strange turn of events, you're fiery personality may actually be the reason you are in your current relationship."]
healthlist2 = ["You will finally manage to phone the GP to try to get an appointment but you will have to wait 2 months for the appointment. You should've phone 2 months ago when the problem actually started happening...", "You will find that eating ten apples a day actually does not keep the doctor away - those seeds have cyanide in them.", "You will live in a perpetual cycle of constipation and diarrhoea."]
familylist2 = ["You were a surprise to your parents.", "Family rivalry is rife - control your ever present anger, they aren't worth it.", "Your competitive side will cause serious issues at game night."]
worklist2 = ["I've heard HR wants a word. The way you.. uh.. stare... it's kinda creepy...", "However bad your job is, at least you're not one of those people who hand out leaflets and make awkward eye contact all day.", "It's the boss's birthday soon. Consider your choice of gift... carefully."]
financelist2 = ["No, I will not help you to stop spending money on houseplants.", "Buying an exercise machine you will use once every January is probably not a good decision, no.", "You will find £100 on the street! It will be in old £20 notes though and who has the time to exchange them at the bank?"]
travellist2 = ["Imagine beautiful beaches and cocktails. Hold onto that thought because its going to be a long while before you experience it again.", "You will be stuck on a day trip with the most annoying British family - its your family.", "Your seat partner on the plane will steal you armrest - stand your ground!"] 

lovelist3 = ["Ironically, the club IS the best place to find a lover. You're just never there.", "I see children in your future - they may be yours, otherwise future you is spending an unreasonable amount time at the park.", "Someone loves you. It is your pet."]
healthlist3 = ["I sense you will get Covid this month. Blame the 5G.", "You're diet will consist of salads this week - I'm sorry.", "One day this week you will give yourself food poisoning."]
familylist3 = ["Someone in your family will be possessed by an evil spirit - my bet is it's you.", "You will betray your family - they deserved it.", "Your family think you don't have a backbone - continue proving them right."]
worklist3 = "You'll find your stapler in a block of jelly tomorrow.", "Remember, this isn't senior school. Who you sit with at lunch isn't the end all or be all.", "That time off for a holiday you're trying to get? Sorry, no chance."
financelist3 = ["Wow!! I see you'll win the lottery next month!! Shame you won't live long enough to enjoy it.", "You will feel a strong desire to throw a penny into a fountain. Why do people even do that?", "Your plan to spend your student loan on a holiday this summer is a very good idea! Think of all the memories you'll make in Italy! Now keep them in mind when you are poor next year."]
travellist3 = ["Try your best to not be British on holiday - other countries will not appreciate your sarcasm.", "Loud Americans will sit next to you on the plane - take your headphones!", "Sometimes booking the cheapest flights/hotels is not the best idea - keep this in mind."]

lovelist4 = ["You will meet a good looking barista. They will serve you coffee. Then they will tell you for the third time that they have a partner and that you are being creepy.", "Is that marriage I see on the horizon? Nope, that's a smudge on my window.", "You will regret not saying 'hi' to the cutie in your seminar - you would have embarrassed yourself but at least you would have shot your shot."]
healthlist4 = ["I sense that the next time you exercise you will suffer greatly. Nothing bad will happen, you're just really unfit.", "You will discover that the GP has forgotten you exist and your history has been lost to the void.", "Your back pain stems from tension and stress. Treat yourself with a massage this week."]
familylist4 = ["You will discover that you are the secret evil twin.", "Family drama is on the horizon - they know what you did.", "Minor tensions will arise today - will you remember to use your words?"]
worklist4 = ["I sense a meeting that should've been an email in your future.", "As a kid, what did you want to be when you grew up? How cute, it's completely unrealistic for you.", "It's not healthy to just live off of coffee and meal deals you know."]
financelist4 = ["Next week you'll find something that you just *have* to buy. And the week after that, and the week after that. It never ends...", "I predict that if you stop buying food, you will save a lot of money. You should try it!", "You will watch a clip of a 'successful' white man explaining how he made millions by getting up at 4am everyday. Do not believe him. His money comes from his trust fund."]
travellist4 = ["Unfortunately, there is no travelling in your near future - travelling costs money and currently you're broke.", "The German tourists will take all the sunbeds at the hotel pool.", "There will be no cold water at the hotel - you will need to come up with an ingenious way to cool down or just be uncomfortable and complain about it."] 

lovelist5 = ["Shoot your shot with that hottie you've been crushing on. Your hopes will most likely be crushed but that shouldn't stop you from trying.", "When the time comes for marriage and kids you will have lived many lives already.", "Summer romance is good while it lasts - unfortunately for you, it won't last."]
healthlist5 = ["No, eating an entire packet of cookies is not healthy.", "Yoga is the answer to all your aches and pains.", "Bacon is not that good for you. It is protein though and it tastes really good - scratch that I think bacon is good for you."]
familylist5 = ["An estranged uncle will tell you the truth about your birth.", "Be nice to your family - it is will writing season.", "Your future mother in law will not like you."]
worklist5 = ["Someone in the office will microwave leftover fish pie this week. In other words, quit while you still can.", "Have you applied for new jobs? I'd recommend getting started if not, it ain't looking too good for you.", "Gmail will go down this week. In other words, you'll spend a day sitting there spamming refresh."]
financelist5 = ["Have you tried playing the stock market? Don't do it, you'll pick only the wrong things.", "Going food shopping hungry will cause havoc on your bank account.", "Mortgages are awful aren't they? Never buy a house."]
travellist5 = ["You will suffer from lots of mosquito bites this summer - coat yourself in bug spray if you want to avoid the itching.", "There will be a time when you can afford to travel, that time is not now.", "That friend you made on holiday when you were 7 has forgotten about you."] 

lovelist6 = ["Summer romances never last. Winter romances on the other hand... will also not last for you.", "Sometimes it's just easier not to say anything...", "Someone has got their eye on you. They may be a stalker but I can't quite tell."]
healthlist6 = ["You're a shining beacon of health! If health meant not exercising, eating only junk food, and being hunched over a desk all day.", "You will have so much coffee this week that your nervous system will panic and start shutting down.", "Someone will give you the secret to weight loss this week. It is not what you would expect."]
familylist6 = ["You are not your pets favourite human - give them more treats.", "At family weddings this year you will be a liability.", "Your inheritance will come into question this week - tread carefully."]
worklist6 = ["Something something meetings, something something work quotas. I don't know, I write horoscopes, I don't have a real job!", "Your boss will go through a sudden negative mood change. It happens whenever you talk to him.", "Whatever it is your work does will become suddenly in demand due to a short-lived tiktok trend. Have fun while it lasts."]
financelist6 = ["A Nigerian prince will come to you seeking help in the future. Give him all your money, it can't go wrong, I promise.", "You will get a gut feeling that someone has stolen your identity and spent all your money. It was definitely just you, you are in denial.", "Those TV adverts for loans are a really good deal - definitely use them in your time of need."]
travellist6 = ["You will win an all inclusive trip to Malta! Just kidding you won't.", "I have a feeling you will start to get travel sick, not just on boats but planes and cars too. Maybe even trains.", "Your tan lines will be embarrassing no matter what you do to try and fix them."]

lovelist7 = ["Your true love is just around the corner at Greggs. It's sausage rolls!", "You will meet someone this week that has only green flags. They ARE too good to be true.", "A little bit of booze will advance a budding relationship. I said a little bit."]
healthlist7 = ["Yep, those vitamin gummies will definitely fix all your health problems.", "You will get lots of vitamin D this week, unfortunately this will also come with painful sunburn.", "There is a high chance of you spraining your ankle on a night out."]
familylist7 = ["One of your family members will eat your leftovers.", "Be wary of siblings, they will betray you to save themselves.", "Harm will come to you if you don't embarrass your children."]
worklist7 = ["Whatever you do, don't open the red door.", "You know Sandra in the office? I heard she makes your coffee decaf...  no wonder you've been falling asleep at your desk.", "Gentle reminder, playing video games in your mum's basement is not 'work'."]
financelist7 = ["Have you considered *not* getting takeaway once a week? I predict it would be healthier for your body and your wallet.", "Someone is going to knock on your door and make sure you have a TV licence this week - I would sort that out if I were you.", "Stop freeloading off your neighbours wifi. You know the bandwidth isn't big enough and you can't be that broke."]
travellist7 = ["A seagull will poop on you at the beach.", "You will burn your feet on the hot white sand - the salty water will not be pleasant after this.", "Your expensive foreign ice cream will fall on the floor."] 

lovelist8 = ["There is a spring in your step this week. Either you found a new sweetheart or you found spiders living in your underwear drawer.", "Sometimes you have to lower your standards else you will end up alone. Basically, go for people at your level.", "Trust your gut. It was right about the petrol station sushi and it knows what you need to do about you relationship situation."]
healthlist8 = ["I think there's something wrong with your brain. Really? Are you sure? No, there's definitely something wrong with your brain.", "Someone will offer you a trip to Taco Bell this week. Think carefully about this.", "Don't let your friends cook for you this week. They will give you food poisoning."]
familylist8 = ["Be wary of dinner invitations from family - they are not as innocent as they seem.", "Tension is brewing - your family may not agree with your choices this week.", "Someone in your family was swapped at birth."]
worklist8 = ["Imagine how great it must feel to be promoted! Hold on to that feeling, cos it's never going to happen to you.", "I see a 2 hour long after-hours staff meeting in your future. I truly fear for you.", "Whatever your paycheck is, double it. That's what your rent will cost next month. :)", "Whatever your paycheck is, double it. That's what your rent will cost next month. :)"]
financelist8 = ["I see wealth and riches in your future. That is, if you corner the market of t-shirts for people who like metal detecting, born in July with 2 children called Barry and Samantha. There's a lot of demand, I promise.", "Is that a great opportunity for passive income I see? Nevermind, it's just endless debt.", "The new coins and notes are going to have King Charles on them instead of Queenie. Ghastly."]
travellist8 = ["Knock off purchases rarely last very long - maybe leave the Gukki handbag next time.", "All the sunbeds at the beach will be taken if you get there after 10am - you will need to work on your morning routine if you want one.", "Your family will get annoyed with you for working while you are on holiday."] 

lovelist9 = ["There is romance in your future. You may have to go on dates with yourself to experience it though.", "Stop waiting around for something to happen to you. Get out there, talk to people - they don't (always) bite.", "You could be quite smooth, emphasis on 'could'. Stop trying so hard and maybe something good will come from it."]
healthlist9 = ["You really should get that plastic surgery you're considering. Oh, you're not considering plastic surgery? Oops, my bad.", "You will wake up with a sore throat tomorrow. You will not be unwell, you just snore quite aggressively.", "Take some time to really think about your breathing today. Also, you can always see your nose. And your tongue is too big for your mouth."]
familylist9 = ["Take some time away from family this week - they are sick of you.", "A distant member of your family will turn up to insult you.", "You will have a gut feeling that your family went on holiday without you - they did."]
worklist9 = ["Stay away from middle management. It's contagious.", "The air conditioner at work is broken. Put on extra deodorant this week. Probably a good idea anyway...", "If only your boss knew what 'rising cost of living' meant. Maybe then you could afford the nice pesto."]
financelist9 = ["How much cryptocurrency do you own? Wow, that says a lot about you.", "You should save that loose change - dark days are ahead.", "I predict that your wallet will get bigger in the next week - unfortunately it is full of receipts not cash."]
travellist9 = ["A seagull will steal your doughnut and flap its wings into your face.", "Allowing other people to plan your trip doesn't always work in your favour.", "Your new passport will only arrive the day you are planning to leave for your holiday."]

lovelist10 = ["Love can be beautiful, but you'll be lucky if it has a great personality and laughs at your jokes.", "Sleep on the couch tonight. You'll thank me later.", "You thought you could do better than them. You were wrong and now you have no hope."]
healthlist10 = ["Are you 5 years old? No? Then why do you refuse to eat vegetables?", "You do not drink enough water - you will need hydration this week so you should work on that.", "Make an effort to eat healthily this week. That way you can drink a ludicrous amount at the weekend and it cancels out."]
familylist10 = ["Your family have joined a cult - they will try to indoctrinate you.", "A distant member of your family will contact you about you car's extended warranty.", "You may find yourself cleaning crayon off the walls wondering where you went wrong."]
worklist10 = ["Um, what's that smell? Oh no, there's a Karen coming.", "I see a long and boring conversation about your coworkers' children in your future.", "I sense the higher-ups have no clue what your job actually involves. I didn't need to be an oracle to know that."]
financelist10 = ["Bad news is the cost of living is rising and you're not going to be able to afford a house in your lifetime. Good news is... uh, I'll get back to you on that.", "NFTs are a great investment - the hype isn't dying down what do you mean?", "Fuel prices will go down at 3pm on Friday - only for an hour though so you'll have to be quick."]
travellist10 = ["Suncream will leak into your suitcase - this is unfortunate for many reasons. Firstly, sun cream is very expensive and secondly, your clothes will be covered in it.", "There is part of me that doesn't want to tell you this but you won't find the love of your life on a beach in spain.", "If you order lamb in the mediterranean, it will most likely be goat."] 

lovelist11 = ["Sometimes you just have to know when to give up.", "Maybe pick a different aspect... I don't think you'll like this one.", "AHAHAHAHAHA ah thank you, I needed a good laugh."]
healthlist11 = ["You will stub your toe on the coffee table. You will also cry about it. Wimp.", "10k steps a day is not a good replacement for actual exercise.", "You will suddenly become lactose intolerant."]
familylist11 = ["A distant member of your family has found your secret stash.", "You may find yourself alone at the dinner table, wondering where you went wrong.", "If you're going on a family holiday this summer, prepare for some drama."]
worklist11 = ["Those deadlines are looming close... of course you leave it to the last minute.", "Have you considered telling your boss what you really think of them? It would open many doors for you. In particular, the door for the way out.", "There will be ants in the staffroom next week. It was probably because of all the crumbs you leave on the floor."]
financelist11 = ["You're going to place a bet and win! But the winnings will be less than what you bet. What a stupid bet.", "If you think someone is screwing you this week, you are probably right. In fact, you are definitely right.", "I predict a sudden and inexplicable increase of your income. Shame it won't happen to me."]
travellist11 = ["Your plane will be delayed because you packed the wrong size bag.", "Seasickness will ruin any future sailing experiences.", "Your inability to learn the language of the country you are visiting will come back to bite you."] 
# All the potential horoscopes: three for each starsign and horoscope type

while True:
    horoscope = input().lower()
    if horoscope == "love" and ss == starsign[0]:
        slowtype(random.choice(lovelist0)) #randomly picks from the list of three horoscopes.
    elif horoscope == "health" and ss == starsign[0]:
        slowtype(random.choice(healthlist0))
    elif horoscope == "family" and ss == starsign[0]:
        slowtype(random.choice(familylist0))
    elif horoscope == "work" and ss == starsign[0]:
        slowtype(random.choice(worklist0))
    elif horoscope == "finance" and ss == starsign[0]:
        slowtype(random.choice(financelist0))
    elif horoscope == "travel" and ss == starsign[0]:
        slowtype(random.choice(travellist0))

    elif horoscope == "love" and ss == starsign[1]:
        slowtype(random.choice(lovelist1))
    elif horoscope == "health" and ss == starsign[1]:
        slowtype(random.choice(healthlist1))
    elif horoscope == "family" and ss == starsign[1]:
        slowtype(random.choice(familylist1))
    elif horoscope == "work" and ss == starsign[1]:
        slowtype(random.choice(worklist1))
    elif horoscope == "finance" and ss == starsign[1]:
        slowtype(random.choice(financelist1))
    elif horoscope == "travel" and ss == starsign[1]:
        slowtype(random.choice(travellist1))
        
    elif horoscope == "love" and ss == starsign[2]:
        slowtype(random.choice(lovelist2))
    elif horoscope == "health" and ss == starsign[2]:
        slowtype(random.choice(healthlist2))
    elif horoscope == "family" and ss == starsign[2]:
        slowtype(random.choice(familylist2))
    elif horoscope == "work" and ss == starsign[2]:
        slowtype(random.choice(worklist2))
    elif horoscope == "finance" and ss == starsign[2]:
        slowtype(random.choice(financelist2))
    elif horoscope == "travel" and ss == starsign[2]:
        slowtype(random.choice(travellist2))
     
    elif horoscope == "love" and ss == starsign[3]:
        slowtype(random.choice(lovelist3))
    elif horoscope == "health" and ss == starsign[3]:
        slowtype(random.choice(healthlist3))
    elif horoscope == "family" and ss == starsign[3]:
        slowtype(random.choice(familylist3))
    elif horoscope == "work" and ss == starsign[3]:
        slowtype(random.choice(worklist3))
    elif horoscope == "finance" and ss == starsign[3]:
        slowtype(random.choice(financelist3))
    elif horoscope == "travel" and ss == starsign[3]:
        slowtype(random.choice(travellist3))
        
    elif horoscope == "love" and ss == starsign[4]:
        slowtype(random.choice(lovelist4))
    elif horoscope == "health" and ss == starsign[4]:
        slowtype(random.choice(healthlist4))
    elif horoscope == "family" and ss == starsign[4]:
        slowtype(random.choice(familylist4))
    elif horoscope == "work" and ss == starsign[4]:
        slowtype(random.choice(worklist4))
    elif horoscope == "finance" and ss == starsign[4]:
        slowtype(random.choice(financelist4))
    elif horoscope == "travel" and ss == starsign[4]:
        slowtype(random.choice(travellist4))
        
    elif horoscope == "love" and ss == starsign[5]:
        slowtype(random.choice(lovelist5))
    elif horoscope == "health" and ss == starsign[5]:
        slowtype(random.choice(healthlist5))
    elif horoscope == "family" and ss == starsign[5]:
        slowtype(random.choice(familylist5))
    elif horoscope == "work" and ss == starsign[5]:
        slowtype(random.choice(worklist5))
    elif horoscope == "finance" and ss == starsign[5]:
        slowtype(random.choice(financelist5))
    elif horoscope == "travel" and ss == starsign[5]:
        slowtype(random.choice(travellist5))
       
    elif horoscope == "love" and ss == starsign[6]:
        slowtype(random.choice(lovelist6))
    elif horoscope == "health" and ss == starsign[6]:
        slowtype(random.choice(healthlist6))
    elif horoscope == "family" and ss == starsign[6]:
        slowtype(random.choice(familylist6))
    elif horoscope == "work" and ss == starsign[6]:
        slowtype(random.choice(worklist6))
    elif horoscope == "finance" and ss == starsign[6]:
        slowtype(random.choice(financelist6))
    elif horoscope == "travel" and ss == starsign[6]:
        slowtype(random.choice(travellist6))
       
    elif horoscope == "love" and ss == starsign[7]:
        slowtype(random.choice(lovelist7))
    elif horoscope == "health" and ss == starsign[7]:
        slowtype(random.choice(healthlist7))
    elif horoscope == "family" and ss == starsign[7]:
        slowtype(random.choice(familylist7))
    elif horoscope == "work" and ss == starsign[7]:
        slowtype(random.choice(worklist7))
    elif horoscope == "finance" and ss == starsign[7]:
        slowtype(random.choice(financelist7))
    elif horoscope == "travel" and ss == starsign[7]:
        slowtype(random.choice(travellist7))
        
    elif horoscope == "love" and ss == starsign[8]:
        slowtype(random.choice(lovelist8))
    elif horoscope == "health" and ss == starsign[8]:
        slowtype(random.choice(healthlist8))
    elif horoscope == "family" and ss == starsign[8]:
        slowtype(random.choice(familylist8))
    elif horoscope == "work" and ss == starsign[8]:
        slowtype(random.choice(worklist8))
    elif horoscope == "finance" and ss == starsign[8]:
        slowtype(random.choice(financelist8))
    elif horoscope == "travel" and ss == starsign[8]:
        slowtype(random.choice(travellist8))
         
    elif horoscope == "love" and ss == starsign[9]:
        slowtype(random.choice(lovelist9))
    elif horoscope == "health" and ss == starsign[9]:
        slowtype(random.choice(healthlist9))
    elif horoscope == "family" and ss == starsign[9]:
        slowtype(random.choice(familylist9))
    elif horoscope == "work" and ss == starsign[9]:
        slowtype(random.choice(worklist9))
    elif horoscope == "finance" and ss == starsign[9]:
        slowtype(random.choice(financelist9))
    elif horoscope == "travel" and ss == starsign[9]:
        slowtype(random.choice(travellist9))
        
    elif horoscope == "love" and ss == starsign[10]:
        slowtype(random.choice(lovelist10))
    elif horoscope == "health" and ss == starsign[10]:
        slowtype(random.choice(healthlist10))
    elif horoscope == "family" and ss == starsign[10]:
        slowtype(random.choice(familylist10))
    elif horoscope == "work" and ss == starsign[10]:
        slowtype(random.choice(worklist10))
    elif horoscope == "finance" and ss == starsign[10]:
        slowtype(random.choice(financelist10))
    elif horoscope == "travel" and ss == starsign[10]:
        slowtype(random.choice(travellist10))
        
    elif horoscope == "love" and ss == starsign[11]:
        slowtype(random.choice(lovelist11))
    elif horoscope == "health" and ss == starsign[11]:
        slowtype(random.choice(healthlist11))
    elif horoscope == "family" and ss == starsign[11]:
        slowtype(random.choice(familylist11))
    elif horoscope == "work" and ss == starsign[11]:
        slowtype(random.choice(worklist11))
    elif horoscope == "finance" and ss == starsign[11]:
        slowtype(random.choice(financelist11))
    elif horoscope == "travel" and ss == starsign[11]:
        slowtype(random.choice(travellist11))

    if horoscope not in future:
        slowtype("%s \n" % "Did I say I could do that? You will have to start again.")
        sys.exit() # exits program because of user incompetence
    
    time.sleep(0.85)
    
    slowtype("\nDo you want to learn about another aspect of your future? ")
    if input().lower() == "no":
        break
    else:
        slowtype("\nChoose from: LOVE, HEALTH, FAMILY, WORK, FINANCE, and TRAVEL \nInput your choice here: ")
# loop to allow user to get a prediction from each of the horoscope types. 
        
slowtype("\nWould you like to know the celebrities you share a birthday with? ")

if input().lower()!= "no":  #if input is not 'no' - to account for 'yeah' 'yep' 'sure'
    slowtype("\nHere we go!")
else:
    slowtype("Goodbye!")
    sys.exit() #exits programme 

def date_input_to_data(dateInput):
    dateDict = {
        "01": "january",
        "02": "february",
        "03": "march",
        "04": "april",
        "05": "may",
        "06": "june",
        "07": "july",
        "08": "august",
        "09": "september",
        "10": "october",
        "11": "november",
        "12": "december"
    }
    try:
        day = dateInput[0:2]
        month_number = dateInput[3:5]
    except:
        raise Exception("Invalid date input, should be in the format DD-MM. Example: 01-01 or 31-12")
    
    # If month_number is a key in dateDict, set month to the value of that key
    if month_number in dateDict:
        month = dateDict[month_number]
        # print(f"Inputted date: {day} {month}")
        return f"{month}{day}"
    else:
        raise Exception("Invalid month number")

def get_famous_birthdays(date_input):
    # Number of celebrities to be displayed
    number_of_celebrities = 5
    
    # Convert the date input to the format used in the URL
    date = date_input_to_data(date_input)
    
    # Request the data from the URL
    url = f"https://www.famousbirthdays.com/{date}.html"
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            
            # Find all the celebrities using regular expressions
            pattern = r'<div class="tile__item">\s*<a.*?href="(.*?)"'
            celebrities = re.findall(pattern, html)
            if celebrities:
                # Iterate through the celebrities and print their name and occupation
                for i, celeb in enumerate(celebrities[:number_of_celebrities]):
                    try:
                        with urllib.request.urlopen(celeb) as response:
                            html = response.read().decode('utf-8')
                            try:
                                image_url_pattern = r'<img\s+src="([^"]+)"\s+alt="">'
                                image_url = re.findall(image_url_pattern, html)[0]
                            except:
                                image_url = "Unknown"
                            try:
                                name_pattern = r'<span class="bio-module__first-name">(.*?)</span>'
                                name = re.findall(name_pattern, html)[0]
                            except:
                                name = "Unknown"
                            try:
                                occupation_pattern = r'<p class="type-20-24 bio-module__profession">\s*<a[^>]*>([^<]+)'
                                occupation = re.findall(occupation_pattern, html)[0].strip()
                            except:
                                occupation = "Unknown"
                            try:
                                birthyear_pattern = r'<a[^>]*>(\d{4})</a>'
                                birth_year = re.findall(birthyear_pattern, html)[0]
                            except:
                                birth_year = "Unknown"
                            try:
                                age_pattern = r'<p>\s*<span class="type-16-18">Age </span>\s*<span><a[^>]*>(\d+).*?</a></span>'
                                age = re.findall(age_pattern, html)[0]
                            except:
                                age = "Unknown"
                            try:
                                birthplace_pattern = r'<p>\s*<span class="type-16-18">Birthplace</span>\s*<span>\s*<a[^>]*>([^<]+)</a>,\s*<a[^>]*>([^<]+)</a>'
                                birthCity, birthState = re.findall(birthplace_pattern, html)[0]
                                birthState = birthState.strip()
                            except:
                                birthCity = "Unknown"
                                birthState = "Unknown"
                    except urllib.error.HTTPError as e:
                        # If the request was unsuccessful, print a message
                        print(f"HTTP Error {e.code}: {e.reason} with {celeb}")
                    except urllib.error.URLError as e:
                        # If there was a URL error, print a message
                        print(f"URL Error: {e.reason} with {celeb}")
                        
                    # This is where it prints for each celebrity, change this however you want it to be displayed
                    slowtype(f"{i+1}. {name}, {occupation}, {birth_year}, {age}, {birthCity}, {birthState}\n{image_url}\n")
            
            
            else:
                # If no celebrities were found, print a message
                print("No famous birthdays found for the given date.")
    except urllib.error.HTTPError as e:
        # If the request was unsuccessful, print a message
        print(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        # If there was a URL error, print a message that displays what error
        print(f"URL Error: {e.reason}")
        
    return

# Prompt the user to enter a date in the format "month-day", also provides prompt to restart this service
def loop():
    while True:
        slowtype("\nEnter your date of birth in this format (DD-MM): ")
        date_input = input()
        get_famous_birthdays(date_input)
        print("\n")
        slowtype("Retry? (y/n): ")
        retry = input()
        if retry.lower() == "n":
            break

loop()

slowtype("Thank you! I have been the birthday chatbot, hope you have an average day.")
# exit message
