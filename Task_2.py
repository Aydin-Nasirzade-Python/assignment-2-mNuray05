#import libraries here

def main():
  if month=="March" or month=="April" or month=="May" or month=="June":
      if (month=="March" and d<20) or (month=="June" and d>=21):
          pass
      else:
          print(f"{month} {day} is in Spring\n")
  else:
      pass
  if month=="June" or month=="July" or month=="August" or month=="September":
      if (month=="June" and d<21)or(month=="September" and d>=22):
          pass
      else:
          print(f"{month} {day} is in Summer\n")
  else:
      pass
  if month=="October" or month=="November" or month=="December" or month=="September":
      if (month=="September" and d<22) or(month=="December" and d>=21):
          pass
      else:
         print(f"{month} {day} is in Fall\n")
  else:
      pass
  if month=="January" or month=="February" or month=="December" or month=="March":
      if (month=="December" and d<21) or(month=="March" and d>=20):
          pass
      else:
         print(f"{month} {day} is in Winter\n")
  pass

if __name__ == "__main__":
  main()
