import urllib.request
import re

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
                    print(f"{i+1}. {name}, {occupation}, {birth_year}, {age}, {birthCity}, {birthState}\n{image_url}")
            
            
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
        date_input = input("Enter your date of birth in this format (DD-MM): ")
        get_famous_birthdays(date_input)
        print("\n")
        retry = input("Retry? (y/n): ")
        if retry.lower() == "n":
            break
    print("Exiting...")

loop()





