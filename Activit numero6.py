with open("/Users/arnav.gautam.29/Desktop/codingal/Python/Session16/activity2.txt","w") as f:
  f.write("Hello World!")
  f.write(f"Hello World!\n")
  f.write(f"Hello World!\n")
  f.write(f"Hello World!\n")

f.close()

#Split File into words (._.)

with open("/Users/arnav.gautam.29/Desktop/codingal/Python/Session16/activity2.txt","r") as f:
  data = f.readlines()
  print("Words in the file are: ")
  for line in data:
    words = line.split()
    print(words)
    

f.close()

#newfile = open("atharva.txt", "x")

#newfile.close()

import os

#print("Checking if my file exists or not...")

#if os.path.exists("activity2.txt"):
  #os.remove("activity2.txt")
#else:
  #print("The file does not exist so you cannot remove it.")
if os.path.exists("barba.txt"):
  print("Nothing")

else:
  newfile1 = open("barba.txt","x")
  newfile1.close()

