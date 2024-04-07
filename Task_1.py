#import libraries here

def main():
    l=input("Enter a letter of the alphabet: ")
    vowels=["a", "o", "u", "i", "e","A", "O", "U", "I", "E"]
    if l in vowels:
        print("Entered alphabet is a vowel!")
    elif l=="y" or l=="Y":
        print("Sometimes it is a vowel, and sometimes it is a consonant!")
    elif l in "qQwWrRtTpPsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM"
        print("Entered alphabet is a consonant!")

if __name__ == "__main__":
  main()
