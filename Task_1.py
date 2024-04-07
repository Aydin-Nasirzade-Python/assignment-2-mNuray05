#import libraries here

def main():
 n=input("Enter a letter of the alphabet: ")
 if n in "aeiouAEOUI":
  print("Entered alphabet is a vowel!\n")
 elif n in "Yy":
 print("Sometimes it is a vowel, and sometimes it is a consonant!\n")
 elif n in "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM":
print("Entered alphabet is a consonant!\n")  
  
  pass

if __name__ == "__main__":
  main()
