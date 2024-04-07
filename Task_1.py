#import libraries here

def main():
    l=input("Enter a letter of the alphabet: ")
    if l in "aouieAOUIE":
        print("Entered alphabet is a vowel!\n")
    elif l in "yY":
        print("Sometimes it is a vowel, and sometimes it is a consonant!\n")
    elif l in "qQwWrRtTpPsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM":
        print("Entered alphabet is a consonant!\n")
    pass    

if __name__ == "__main__":
  main()
