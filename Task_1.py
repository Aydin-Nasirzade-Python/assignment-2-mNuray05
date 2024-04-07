#import libraries here

def main():
l=input("Enter a letter of the alphabet: ")
vowels=["a", "o", "u", "i", "e"]
both="y"
if l in vowels:
    print("Entered alphabet is a vowel!")
elif l==both:
    print("Sometimes it is a vowel, and sometimes it is a consonant!")
else:
    print("Entered alphabet is a consonant!") 
  
  pass

if __name__ == "__main__":
  main()
