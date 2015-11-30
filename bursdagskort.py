#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, time, subprocess, platform

def any():
	raw_input("\nTrykk ENTER for aa fortsette...")
	

def clear():
	subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)
	time.sleep(0.02)
	
def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.025)

def intro():
	clear()
	delay_print("kittens.Voice presenterer...\n")
	time.sleep(2.75)
	clear()
	print"    _/_/_/    _/    _/  _/_/_/      _/_/_/  _/_/_/      _/_/      _/_/_/    "
	print"   _/    _/  _/    _/  _/    _/  _/        _/    _/  _/    _/  _/          "
	print"  _/_/_/    _/    _/  _/_/_/      _/_/    _/    _/  _/_/_/_/  _/  _/_/     "
	print" _/    _/  _/    _/  _/    _/        _/  _/    _/  _/    _/  _/    _/      "
	print"_/_/_/      _/_/    _/    _/  _/_/_/    _/_/_/    _/    _/    _/_/_/       \n"
	time.sleep(1.5)
	print"            _/_/      _/        _/    "                                     
	print"         _/    _/  _/_/      _/  _/  "                                      
	print"            _/      _/      _/  _/  "                                       
	print"         _/        _/      _/  _/  "                                        
	print"      _/_/_/_/    _/  _/    _/    "
	time.sleep(1.5)
	delay_print("\n\nBURSDAGSKORTSPILLET!\n")
	time.sleep(2)
	any()
	clear()
	
def level_1():
	print "  _    _____   _____ _      _  "
	print " | |  | __\ \ / / __| |    / | "
	print " | |__| _| \ V /| _|| |__  | | "
	print " |____|___| \_/ |___|____| |_| "
	print "                               "
	time.sleep(1)
	delay_print("First things first...")
	time.sleep(2)
	delay_print("\nHar du bursdag i dag? (ja/nei): ")
	
	answer = raw_input()
	answer = answer.lower()
	
	while(answer != "ja"):
		clear()
		print "  _    _____   _____ _      _  "
		print " | |  | __\ \ / / __| |    / | "
		print " | |__| _| \ V /| _|| |__  | | "
		print " |____|___| \_/ |___|____| |_| "
		print "                               "
		delay_print("Luringen... ;) Proev igjen!")
		time.sleep(0.5)
		delay_print("\nHar du bursdag i dag? (ja/nei): ")
		answer = raw_input()
		answer = answer.lower()

	clear()
	print "  _    _____   _____ _      _  "
	print " | |  | __\ \ / / __| |    / | "
	print " | |__| _| \ V /| _|| |__  | | "
	print " |____|___| \_/ |___|____| |_| "
	print "                               "
	delay_print("GRATULERER! Her, ta et digitalt kakestykke:")
	time.sleep(0.8)
	print ""
	print "              .-.				"
	print "           .' _  \				"
	print "         ,'  (_)  \_				"
	print "      _.-|`-._      \--._		"
	print "    .' .-(=._ `-._   \-. `.	    "
	print "   /  /  |   `=.  `-._\ \  \	    "
	print "  |  |    `-._  `=._  | .|  |	"
	print "   \  \  ;' .,`--._ `=| '/  /	"
	print "    `._``--..._____`--'-''_.'	"
	print "       `--.._________..--'		"
	time.sleep(2)
	delay_print("\nFerdig med stykket snart? ")
	time.sleep(0.8)
	delay_print("BRA!")
	time.sleep(1.5)
	any()
	clear()

def level_2():
	print "  _    _____   _____ _      ___  "
	print " | |  | __\ \ / / __| |    |_  ) "
	print " | |__| _| \ V /| _|| |__   / /  "
	print " |____|___| \_/ |___|____| /___| \n\n"
	time.sleep(1)
	delay_print("Tre spoersmaal...")
	time.sleep(2)
	
	clear()
	print "  _    _____   _____ _      ___  "
	print " | |  | __\ \ / / __| |    |_  ) "
	print " | |__| _| \ V /| _|| |__   / /  "
	print " |____|___| \_/ |___|____| /___| \n\n"
	
	delay_print("Spoersmaal 1: Hva er meningen med livet, universet og alt?\n")
	answer = raw_input()
	
	hint = 0
	while(answer != "42"):
		hint += 1
		clear()
		print "  _    _____   _____ _      ___  "
		print " | |  | __\ \ / / __| |    |_  ) "
		print " | |__| _| \ V /| _|| |__   / /  "
		print " |____|___| \_/ |___|____| /___| \n\n"
		delay_print("Er du helt sikker? Tror du skal proeve igjen... ;-)\n")
		delay_print("Hva er meningen med livet, universet og alt?\n")
		if hint >= 2:
			delay_print("\nHINT: Det er et tall!\n")
		answer = raw_input()
		
		
	
	clear()
	print "  _    _____   _____ _      ___  "
	print " | |  | __\ \ / / __| |    |_  ) "
	print " | |__| _| \ V /| _|| |__   / /  "
	print " |____|___| \_/ |___|____| /___| \n\n"
	
	delay_print("AWESOME! Naa, spoersmaal nummer 2: Hvilket dyr er det tristeste i skogen?\n")
	answer = raw_input()
	answer = answer.lower()
	
	hint = 0
	while(answer != "ugla"):
		hint += 1
		clear()
		print "  _    _____   _____ _      ___  "
		print " | |  | __\ \ / / __| |    |_  ) "
		print " | |__| _| \ V /| _|| |__   / /  "
		print " |____|___| \_/ |___|____| /___| \n\n"
		delay_print("Tror nok du maa gjette en gang til...\n")
		delay_print("Hvilket dyr er det tristeste i skogen?\n")
		if hint >= 2:
			delay_print("\nHINT: \"uhuuu\"\n")
		answer = raw_input()
		answer = answer.lower()
		hint = hint + 1
	
	clear()
	print "  _    _____   _____ _      ___  "
	print " | |  | __\ \ / / __| |    |_  ) "
	print " | |__| _| \ V /| _|| |__   / /  "
	print " |____|___| \_/ |___|____| /___| \n\n"
	
	delay_print("SUPERT! Siste spoersmaal foer LEVEL 3: Hva blir 1+2+3+4+5+6?\n")
	
	answer = raw_input()
	
	hint = 0
	while(answer != "21"):
		hint += 1
		clear()
		print "  _    _____   _____ _      ___  "
		print " | |  | __\ \ / / __| |    |_  ) "
		print " | |__| _| \ V /| _|| |__   / /  "
		print " |____|___| \_/ |___|____| /___| \n\n"
		delay_print("Det er enklere enn du tror...\n")
		delay_print("Hva blir 1+2+3+4+5+6?\n")
		if hint >= 2:
			delay_print("\nHINT: Alder\n")
		answer = raw_input()
		answer = answer.lower()
		hint = hint + 1
	
	clear()
	print "  _    _____   _____ _      ___  "
	print " | |  | __\ \ / / __| |    |_  ) "
	print " | |__| _| \ V /| _|| |__   / /  "
	print " |____|___| \_/ |___|____| /___| \n\n"
	delay_print("WOHOO, du klarte det :D")
	time.sleep(2)
	delay_print("\nHer, se paa dette vakre \"miksebordet\" foer du gaar videre :-)\n\n")
	
	print"     /    o   oooo ooo oooo   o o o  /\    "
	print"    /    oo  ooo  oo  oooo   o o o  / /    "
	print"   /    _________________________  / /     "
	print"  / // / // /// // /// // /// / / / /      "
	print" /___ //////////////////////////_/ /       "
	print" \____\________________________\_\/ 		 "
	
	time.sleep(2)
	any()
	clear()

def hangman_graphic(guesses):
	if guesses == 6:
		print "________      "
		print "|      |      "
		print "|             "
		print "|             "
		print "|             "
		print "|             "
	elif guesses == 5:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|             "
		print "|             "
		print "|             "
	elif guesses == 4:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /       "
		print "|             "
		print "|             "
	elif guesses == 3:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|      "
		print "|             "
		print "|             "
	elif guesses == 2:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|\     "
		print "|             "
		print "|             "
	elif guesses == 1:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|\     "
		print "|     /       "
		print "|             "
	else:
		print "________      "
		print "|      |      "
		print "|      0      "
		print "|     /|\     "
		print "|     / \     "
		print "|             "
	 
def level_3():
	print"  _    _____   _____ _      ____ "
	print" | |  | __\ \ / / __| |    |__ / "
	print" | |__| _| \ V /| _|| |__   |_ \ "
	print" |____|___| \_/ |___|____| |___/ \n\n"
	
	time.sleep(1)
	delay_print("Let's play HANGMAN!")
	time.sleep(2)
	clear()
	
	next_level=False

	while(next_level == False):
		word = "eventtekniker"
		guesses = ''
		turns = 6
		while turns > 0:     
			print"  _    _____   _____ _      ____ "
			print" | |  | __\ \ / / __| |    |__ / "
			print" | |__| _| \ V /| _|| |__   |_ \ "
			print" |____|___| \_/ |___|____| |___/ \n\n"
			failed = 0   
			
			hangman_graphic(turns)
			
			for char in word:      
				if char in guesses:    
					print char,    
				else:
					print "_", 
					failed += 1   
					
			if len(guesses) > 0:
				print "\nBrukte bokstaver: " + guesses
			else:
				print "\n"

			# print You Won
			if failed == 0:        
				print "\nGRATULERER! Du VANT!"  
				time.sleep(4)
				next_level=True
				break              
			print
			
			guess = raw_input("Gjett en bokstav:") 
			guesses += guess + ","   
			
			if guess not in word:  
				turns -= 1        
				print "Feil...\n"    

				if turns == 0: 
					clear()
					print"  _    _____   _____ _      ____ "
					print" | |  | __\ \ / / __| |    |__ / "
					print" | |__| _| \ V /| _|| |__   |_ \ "
					print" |____|___| \_/ |___|____| |___/ \n\n"
					hangman_graphic(turns)
					print "\nHuffda... Proev igjen! :-)\n"  
					time.sleep(3)
					
			clear()
	clear()
	
def the_end():
	delay_print("HURRA, DU HAR BURSDAG!!! :D\n")
	time.sleep(1)
	delay_print("For aa motta bursdagsgaven, er du nodt til aa taste inn ditt kontonummer,\n11 siffer: ")
	account = raw_input()
	clear()
	
	delay_print("\nDu tastet: ")
	delay_print(account)
	time.sleep(1)
	delay_print("\nEr dette korrekt? (ja/nei): ")
	answer = raw_input()
	answer = answer.lower()
	
	while(answer != "ja"):
		clear()
		delay_print("Tast inn kontonummer, 11 siffer: ")
		account = raw_input()
		delay_print("\nDu tastet: ")
		delay_print(account)
		time.sleep(0.5)
		delay_print("\nEr dette korrekt? (ja/nei): ")
		answer = raw_input()
		answer = answer.lower()
		answer = answer.lower()
	
	clear()
	delay_print("Skriver kontonummer til fil")
	clear()
	print"Skriver kontonummer til fil."
	time.sleep(0.8)
	clear()
	print"Skriver kontonummer til fil.."
	time.sleep(0.8)
	clear()
	print "Skriver kontonummer til fil..."
	time.sleep(0.8)
	
	text_file = open("kontonummer.txt", "w")
	text_file.write(str(account))
	text_file.close()
	delay_print("\nDONE!")
	time.sleep(2)
	clear()
	delay_print("FLOTT, DU HAR VUNNET: *trommevirvel*")
	time.sleep(2)
	clear()
	print "FLOTT, DU HAR VUNNET:      \n"
	print "#######	 					"   
	print "#        					"
	print "#       						"
	print "######  						"
	print "      # 						"
	print "#     #  					"
	print " ##### 						"
	time.sleep(0.8)
	clear()
	print "FLOTT, DU HAR VUNNET:      \n"
	print "#######   ###          		"   
	print "#        #   #     			"
	print "#       #     #  			"
	print "######  #     #  			"
	print "      # #     #  			"
	print "#     #  #   #     			"
	print " #####    ###     			"
	time.sleep(0.8)
	clear()
	print "FLOTT, DU HAR VUNNET:      \n"
	print "#######   ###     ###      	"   
	print "#        #   #   #   #  		"
	print "#       #     # #     # 		"
	print "######  #     # #     # 		"
	print "      # #     # #     # 		"
	print "#     #  #   #   #   #  		"
	print " #####    ###     ### 		"
	time.sleep(0.8)
	delay_print("\nNORSKE KRONER!\n\n")
	time.sleep(2)
	delay_print("Pengene overfoeres saa snart Tommy faar tak i kontonummeret ditt :-)")
	
	time.sleep(5)
	clear()
	
	delta = 0.11
	while(delta < 1):
		clear()
		print("GRATULERER MED DAGEN, PK! :D\n\n")
		print "      )          "			
		print "     (			"
		print "    .-`-.		"
		print "    :   :		"
		print "    :TNT:		"
		print "    :___:		"
		time.sleep(0.5)
		
		clear()
		print("GRATULERER MED DAGEN, PK! :D\n\n")
		print "    \|/			"
		print "   - o -			"
		print "    /-`-.		"
		print "    :   :		"
		print "    :TNT:		"
		print "    :___:		"
		time.sleep(delta)
		
		clear()
		print("GRATULERER MED DAGEN, PK! :D\n\n")
		print "    .---.		"
		print "    : | :		"
		print "    :-o-:		"
		print "    :_|_:		"
		time.sleep(delta)

		clear()
		print("GRATULERER MED DAGEN, PK! :D\n\n")
		print "    .---.		"
		print "    (\|/)		"
		print "    --0--		"
		print "    (/|\)		"
		time.sleep(delta)

		clear()
		print("GRATULERER MED DAGEN, PK! :D\n\n")
		print "   '.\|/.'		"
		print "   (\   /)		"
		print "   - -O- -		"
		print "   (/   \)		"
		print "   ,'/|\'.		"
		time.sleep(delta)

		clear()
		print("GRATULERER MED DAGEN, PK! :D\n\n")
		print "'.  \ | /  ,'	"
		print "  `. `.' ,'		"
		print " ( .`.|,' .)		"
		print " - ~ -0- ~ -		"
		print " (				"
		time.sleep(delta)

		clear()
		print("GRATULERER MED DAGEN, PK! :D\n\n")
		print "','|'.` )		"
		print "  .' .'. '.		"
		print ",'  / | \  '.	"
		print "    \ '  \"  	"
		print " ` . `.' ,'		"
		print " . `` ,'. \"		"
		print "   ~ (   ~ -		"
		print "'				"
		time.sleep(delta)

		clear()
		print("GRATULERER MED DAGEN, PK! :D\n\n")
		print ". ','|` ` .		"
		print "  .'  \"  '		"
		print ",   ' , '  `		"
		time.sleep(delta)

		clear()
		print("GRATULERER MED DAGEN, PK! :D\n\n")
		print "   (  ) (		"
		print "    ) ( )		"
		print "    (  )			"
		print "     ) /  	 	"
		print "    ,---.        " 
		time.sleep(1)
	
	
def main():
	intro()
	level_1()
	level_2()
	level_3()
	the_end()	
	
if __name__ == "__main__":
    main()
