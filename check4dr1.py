import requests
import bs4
import re
import pyttsx
import time

# FUNCTION speak_number IS TO SEPERATE THE NUMBER INTO SEPERATE DIGITS,
# BECAUSE WHEN PASS TO VOICE FUNCTION NORMALLY WILL ANNOUNCE IN THE FORMAT
# LIKE THOSE IN WRITING CHEQUE. I WANT IT TO SAY DIGIT BY DIGIT.
# TO DO IT, CONTINUOUS MODULUS THE NUMBER % WITH 10, THEN DIVIDE /10, UNTIL THE END.
# APPEND EACH RESULT INTO AN ARRAY, THEN REVERSE THE ARRAY WHEN EVERYTHING FINISH
# THERE IS ONE PROBLEM THOUGH. FOR 0xxx, 00xx, 000x, 0000, IT WILL ONLY INSERT THE X 
# INTO THE ARRAY, NOT THE 0. I NEED TO INSERT THE 0 INTO THE ARRAY, SO THE VOICE 
# FUNCTION WILL SAY ZERO-ZERO-X-X INSTEAD OF JUST X-X.
  
def split_number(number):
  digits=[]
	
  while number>0:
    digits.append(number%10)
    number/=10
  
  digits.reverse()
  print digits
  
  if len(digits) == 3:
    print "ok3"
    digits.insert(0, 0)
  
  elif len(digits) == 2:
    print "ok2"
    digits.insert(0, 0)
    digits.insert(1, 0)
  
  elif len(digits) == 1:
    print "ok1"
    digits.insert(0, 0)
    digits.insert(1, 0)  
    digits.insert(2, 0)
  
  elif len(digits) == 0:
    digits.insert(0, 0)
    digits.insert(1, 0)  
    digits.insert(2, 0)
    digits.insert(3, 0)
    print "ok0"
	
  else: pass
  print digits
  return digits;

	


def speak_number(digit):
  engine = pyttsx.init()
  engine.setProperty('rate', 100)
  engine.say(digit)
  engine.runAndWait()
  return;
  
def speak_words(word):
  engine = pyttsx.init()
  engine.setProperty('rate', 100)
  engine.say(word)
  engine.runAndWait()
  return;

  
# ------------------------------------------------------------------------------
# FOR GETTING THE WEBPAGE HTML - ALL
# ------------------------------------------------------------------------------
 
  
#fetch = requests.get('http://www.check4d.com')
fetch = requests.get('http://www.check4d.com/past-results?drawpastdate=2016-05-03')


# ------------------------------------------------------------------------------
# FOR MAGNUM FIRST SECOND THIRD PRIZES
# ------------------------------------------------------------------------------

mo = re.findall('<td class="resultm4dlable">Magnum 4D 萬能</td></tr></table></td></tr><tr><td colspan="5"><table class="resultTable2" cellpadding="0" cellspacing="5"><tr><td class="resultdrawdate">(.+?)</table></div>' , fetch.text)

matched = mo[0]
print matched

fetch.raise_for_status()
# fetched = bs4.BeautifulSoup(fetch.text, "lxml")
fetched = bs4.BeautifulSoup(matched, "lxml")
resultsBig = fetched.select('.resulttop')


speak_words('choi saan dough, choi saan dough, choi saan dough');

for i in range (0,3,1):

  print 'Magnum '+ str(i+1) + ' : ' + resultsBig[i].getText()
  numberBig = int(resultsBig[i].getText())
  #split_number(numberBig);
  digits=split_number(numberBig);
  if i == 0:
    speak_words('Magnum tau john');
  elif i == 1:
    speak_words('Magnum yi john');
  else: 
    speak_words('Magnum saam john');
  speak_number(digits);
  speak_number(digits);
  time.sleep(2)
  
print '====='


# ------------------------------------------------------------------------------
# FOR MAGNUM SPECIAL PRIZES + CONSOLATION PRIZES
# ------------------------------------------------------------------------------

resultsSmall = fetched.select('.resultbottom')

i=0
array = []

for table_row in fetched.select('.resultbottom'):
	print table_row
	j = table_row.getText()
	if j.isdigit() == True:
		array.append(j)
	i=i+1
	print i
	print j

print array
print len(array)

if len(array) < 20:
	speak_words('results incomplete, come back later')
else:
speak_words('Magnum Special');

for k in range (0, 10, 1):
  print 'Magnum Special: ' + array[k]
  numberSmallSpecial = int(array[k])
  digits=split_number(numberSmallSpecial);
  speak_number(digits);


  
speak_words('Magnum Consolation');

for k in range (10, 20, 1):
  print 'Magnum Consolation: ' + array[k]
  numberSmallSpecial = int(array[k])
  digits=split_number(numberSmallSpecial);
  speak_number(digits);

  
  





  
  


