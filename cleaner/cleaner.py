#! /usr/bin/python3.3

import sys
import os


##### check scraping.php

scrapingphp = "../functions/scraping.php"
count = 0
sla = 0
bol = False
with open(scrapingphp) as f:
  for line in f:
    check = False
    count += 1

    if line.find("function ProductPageURL2ProductInfoAray($_url_raw, $_type=''") != -1 or line.find("echo json_encode(array(\"statusCode\" => 500,") != -1 or line.find("function extract_identifier($_url) {") != -1 or line.find("isProductRedFlagged($_productInfo) {") != -1:
      bol = not bol
      #print(bol)
    if bol:
      found = line.find("echo")
      found1 = line.find("print_r(")
      if found != -1 or found1 != -1:
        found2 = line.find("//")
        if (found < found2 and found != -1) or (found1 < found2 and found1 != -1) or found2 == -1:
          check = True
          print ("WARNING : call to "+ ("echo" if found != -1 else "print_r" )+ " detected at line " + str(count))

##### check files

while 1:
  print("\n\nIf there's mistakes please correct it otherwise you can type name of file you want to check and press enter:\n you can press enter to exit or space bar to skip model check")
  inp = input()
  print ("\n\n")
  if inp == "":
    print ("goog bye!")
    sys.exit()
  elif inp == ' ':
    break
  count = 0
  with open(inp) as retail:
    for line in retail:
      count += 1
      found = line.find("echo")
      found1 = line.find("print_r(")
      if found != -1 or found1 != -1:
        found2 = line.find("//")
        if (found < found2 and found != -1) or (found1 < found2 and found1 != -1) or found2 == -1:
          check = True
          print ("WARNING : call to "+ ("echo" if found != -1 else "print_r" )+ " detected at line " + str(count))

if check == True:
  sys.exit("please make sure all echo disapeard")

##### add files if everything is ok

i = 1
args = ""
t = len(sys.argv)
while  i < t:
  args = args + " " + sys.argv[i]
  i+= 1
os.system("git add " + args + " ../functions/scraping.php")
