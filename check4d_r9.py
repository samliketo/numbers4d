# -*- coding: utf-8 -*-

import requests
import bs4
import re
import pyttsx
import time
import sys
import pygame
import subprocess
import os


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
  """
  engine = pyttsx.init()
  engine.setProperty('rate', 180)
  engine.say(digit)
  engine.runAndWait()
  """
  for ticker in digit:
	  #subprocess.call('sudo espeak -s 160 -vzh+f1 ' + str(ticker), shell=True)
          FNULL = open(os.devnull, 'w')
          retcode = subprocess.call(["espeak", "-s 160", "-ven", str(ticker), "aplay"], stdout=FNULL, stderr=subprocess.STDOUT)
          #subprocess.call('sudo espeak ' + str(ticker) '2>/dev/null', shell=True)
  time.sleep(0.5)
  
  return;
  
def speak_words(word):
  engine = pyttsx.init()
  engine.setProperty('rate', 180)
  engine.say(word)
  engine.runAndWait()
  return;

  
# ------------------------------------------------------------------------------
# FOR GETTING THE WEBPAGE HTML - ALL
# ------------------------------------------------------------------------------
 
  
fetch = requests.get('http://www.check4d.com')
#fetch = requests.get('http://www.check4d.com/past-results?drawpastdate=2016-04-12')

# ------------------------------------------------------------------------------
# FOR MAGNUM FIRST SECOND THIRD PRIZES
# ------------------------------------------------------------------------------

KTM = ['Magnum', 'DaMaCai', 'Toto']
KTM_Pronounce = ['Magnum', 'thye mar choi', 'Toto']

#speak_words('choi saan dough, choi saan dough, choi saan dough');


"""

song = "choy_san_dou.ogg"
pygame.init()
pygame.display.set_mode((200,100))
pygame.mixer.init()


#pygame.mixer.music.load(song)
#pygame.mixer.music.set_volume(1)
#pygame.mixer.music.play(0)
#play(loops=0, maxtime=0, fade_ms=0)

themesong = pygame.mixer.Sound(song)
themesong.play(loops=0, maxtime=0, fade_ms=10000)

while pygame.mixer.get_busy(): 
	pygame.time.Clock().tick(10)


"""


match_date = re.search(r'<td class="resultdrawdate">(.+?)</td>' , fetch.text)
print match_date.group(0)
print match_date.group(1)
speak_words(match_date.group(1));	


match_M = re.search(r'<td class="resultm4dlable">Magnum 4D 萬能(.+?)</table></div>' , fetch.text)
if match_M != None: match_M = 1 
else: match_M = 0

match_K = re.search(r'<td class="resultdamacailable">Da Ma Cai 1\+3D 大馬彩(.+?)</table></div>' , fetch.text)
if match_K != None: match_K = 1 
else: match_K = 0
	
match_T = re.search(r'<td class="resulttotolable">SportsToto 4D 多多(.+?)</table></div>' , fetch.text)
if match_T != None: match_T = 1 
else: match_T = 0	
	

b = [[0,3,1], [0,2,1,], [0,3,2], [0,2,1], [1,3,1], [1,3,2], [2,3,1], [3,3,1]]

dic = {'111':b[0], '110':b[1], '101':b[2], '100':b[3], '011':b[4], '010':b[5], '001':b[6], '000':b[7]}

x, y, z = dic['111']

print x, y, z
print match_M, match_K, match_T
print str(match_M) + str(match_K) + str(match_T)
X_num = str(match_M) + str(match_K) + str(match_T)
print dic[X_num]



for counter in range (x, y ,z):
	
	if counter == 0:
		try:
			mo = re.search(r'<td class="resultm4dlable">Magnum 4D 萬能(.+?)</table></div>' , fetch.text)
			matched = mo.group()
			print matched
		except:
			print("Cannot get Magnum!!!", sys.exc_info()[0])
			break
	elif counter == 1:
		try:
			mo = re.search(r'<td class="resultdamacailable">Da Ma Cai 1\+3D 大馬彩(.+?)</table></div>' , fetch.text)
			matched = mo.group()
			print matched
		except:
			print("Cannot get Da Ma Cai!!!", sys.exc_info()[0])
			break
	
	else:
		try:
			mo = re.search(r'<td class="resulttotolable">SportsToto 4D 多多(.+?)</table></div>' , fetch.text)
			matched = mo.group()
			print matched
		except:
			print ("Cannot get Toto!!!", sys.exc_info()[0])
			break
			
	speak_words(KTM_Pronounce[counter] + ' choi saan dough');
	

	
	#matched = mo[0]
	#print matched

	fetch.raise_for_status()
	# fetched = bs4.BeautifulSoup(fetch.text, "lxml")
	fetched = bs4.BeautifulSoup(matched, "lxml")
	resultsBig = fetched.select('.resulttop')






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

	
	speak_words(KTM_Pronounce[counter]+' Consolation');

	for k in range (10, 20, 1):
		print KTM[counter]+' Consolation: ' + array[k]
		numberSmallSpecial = int(array[k])
		digits=split_number(numberSmallSpecial);
		speak_number(digits);
		
	
	
	speak_words(KTM_Pronounce[counter]+' Special');
	
	for k in range (0, 10, 1):
		print KTM[counter]+' Special: ' + array[k]
		numberSmallSpecial = int(array[k])
		digits=split_number(numberSmallSpecial);
		speak_number(digits);

	
	
	# ------------------------------------------------------------------------------
	# FOR MAGNUM 1,2,3 PRIZES
	# ------------------------------------------------------------------------------ 
  
  
  
	for i in range (0,3,1):

		print KTM[counter] + ' ' + str(i+1) + ' : ' + resultsBig[i].getText()
		numberBig = int(resultsBig[i].getText())
		#split_number(numberBig);
		digits=split_number(numberBig);
		if i == 0:
			speak_words(KTM_Pronounce[counter]+' tau john');
		elif i == 1:
			speak_words(KTM_Pronounce[counter]+' yi john');
		else: 
			speak_words(KTM_Pronounce[counter]+' saam john');
		speak_number(digits);
		speak_number(digits);
		time.sleep(2)
	  
	print '====='

	counter = counter + 1

	
	
	
themesong.play(loops=0, maxtime=0, fade_ms=0)

while pygame.mixer.get_busy(): 
	pygame.time.Clock().tick(10)
