#import libraries here

def main():
 month=input("Enter a month [ex. March]")
 day=int(input("Enter a day [ex. 12]"))
 if month=="December" or month== "January":
    if (month=="December" or day==22) and (month=="January" or day==19):
        print("Your zodiac sign is Capricorn")
 
 elif month=="January" or month=="February":
    if (month=="January" or day==20) and (month=="February" or day==18):
        print("Your zodiac sign is Aquarius")
 elif month=="February" or month=="March":
    if (month=="February" or day==19) and (month== "March" or day==20):
        print("Your zodiac sign is Pisces")
 elif month=="March" or month=="April":
    if (month=="March" or day==21) and (month== "April" or day==19):
        print("Your zodiac sign is Aries")
 elif month=="April" or month=="May":
    if (month=="April" or day==20) and (month== "May" or day==20):
        print("Your zodiac sign is Taurus")
 elif month=="May" or month== "June":
    if (month=="May" or day==21) and (month=="June" or day==20):
        print("Your zodiac sign is Gemini")
 elif month =="June" or month == "July":
    if (month =="June" or day==21) and (month=="July" or day==22):
        print("Your zodiac sign is Cancer")
 elif month=="July" or month=="August":
    if (month=="July" or day==23) and (month== "August" or day==22):
        print("Your zodiac sign is Leo")
 elif month== "August" or month=="September":
    if (month=="August" or day==23) and (month=="September" or day==22):
        print("Your zodiac sign is Virgo")
 elif month=="September" or month=="October":
    if(month=="September" or day==23) and (month=="October" or day==22):
        print("Your zodiac sign is Libra")
 elif month=="October" or month=="November":
    if(month=="October" or day==23) and (month=="November" or day==21):
        print("Your zodiac sign is Scorpion")
 else:
    print("Your zodiac is Sagittarius")
  pass

if __name__ == "__main__":
  main()
