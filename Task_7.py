#import libraries here

def main():
  x=float(input("Enter x: "))
  y=float(input("Enter y: "))
  if ((y>=(x-2)**2-3) or x>=abs(y) or y>0) and (y>=(x-2)**2-3 or y<0 or x<=abs(y)):
    print("The point is in the shaded area")
  else:
    print("The point is not in the shaded area")
  pass

if __name__ == "__main__":
  main()
