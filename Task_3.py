#import libraries here

def main():
  
l=int(input("Enter the wavelength in nm:"))
if l>=380 or l<450:
    print("The relevant color is Violet")
elif l>=450 or l<495:
    print("The relevant color is Blue")
elif l>=495 or l<570:
    print (" The relevant color is Green")
elif l>=570 or l<590:
    print(" The relevant color is Yellow")
elif l>=590 or l<620:
    print("The relevant color is Orange")
elif l>=620 or l<750:
    print("The relevant color is Red")
else:
    print ("Invalid input!")
  pass

if __name__ == "__main__":
  main()
