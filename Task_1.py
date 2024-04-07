#import libraries here

def main():
    l=input("Enter a letter of the alphabet: ")
    if l in "aouieAOUIE":
        print("Entered alphabet is a vowel!")
    elif l in "yY":
        print("Sometimes it is a vowel, and sometimes it is a consonant!")
    elif l in "qQwWrRtTpPsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM":
        print("Entered alphabet is a consonant!")
    pass    

if __name__ == "__main__":
  main()
