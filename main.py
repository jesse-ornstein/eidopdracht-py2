#hier worden er dingen geimporteerd
import time
import random

#dat betekent dat het programma door moet gaan
stoppen = False

#dit is het welkom bericht als je het programma start
print("")
print("welkom bij")
print("   ___    __    __    ___   ____  ____ ")
print("  / __)  /__\  (  )  / __) (_  _)( ___)")
print(" ( (_-. /(__)\  )(__( (_-..-_)(   )__) ")
print("  \___/(__)(__)(____)\___/\____) (____)")

#de woorden waruit de computer kan kiezen
woorden = ["banaan","appel","voetbal","boom","aapje","peren","kaas","vogel","boeken","mississippi"]
goedeletter = "abcdefghijklmnopqrstuvwxyz"
time.sleep(2)
print("")
#hier word een random woord gekozen
GeheimWoord = random.choice(woorden)

#de pogingen die je hebt om het woord te raden
poging = 6
#gl staat voor geraden letters en in het begin staat die op niks
gl = ""
#hier staat de begin waarde van het aantal pogingen dat je nodig had om het woord te raden of juist niet
geraden = 0
#deze while loop zorgt ervoor dat het programma door blijt todat stoppen True is
while stoppen == False:
  #hier loopt het programma door het woord heen
  for spelen in GeheimWoord:
    if spelen in gl:
      print(spelen , end = "")
    else:
      print("_" , end = "")
  #hier worden de letters die je hebt geraden geprint
  print(" gl = " + gl)
  print("")
  #hier geef je aan welke letter je wilt kiezen of als je een woord wil raden
  spelen =input("Kies een letter of kies ? om het geheime woord te raden: ")
  #elke keer dat je iets raad gaat het aantal pogingen dat je nodig had omhoog
  geraden += 1
  #als spelen niet in het geheime woord zit gaat je poging -1
  if spelen not in GeheimWoord:
    poging -= 1
  #als je qq zegt bij letter raden stopt het programma
  if spelen == "qq":
    stoppen = True
  #als je meer dan 1 letter raad zegt het programma dat het niet mag
  elif len(spelen) >= 2:
    print("kies 1 letter alsjeblieft!")
  elif spelen == "?":
  # als je ? raad kan je zeggen wat het woord is
    print("je wilt een poging doen?")
    time.sleep(1)
    WoordRaden = input("raad het geheime woord: ")
  #dit bericht krijg je las je het woord goed raad. en dan stopt het programma
    if WoordRaden == GeheimWoord:
        print("gefeliciteerd, dat antwoord is goed!")
        print("je hebt het woord in", geraden, "keer goed geraden")
        stoppen = True
    #als je het woord fout raad is het meteen voorbij
    else:
      poging = 0
  elif spelen not in goedeletter:
    print("kies een letter alsjeblieft")  

#als je letter al hebt geraden zegt programma dat of hij voegt hij het toe aan de geraden letters
  else:
    if spelen in gl:
      print("je hebt deze letter al geraden")
    else:
      gl += spelen
#hier worden per letter die je fout hebt iets meer van de galg getekent
  if stoppen == False:
    if poging == 5:
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |___")
    elif poging == 4:
      print(" ___")
      print(" |/")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |___")
    elif poging == 3:
      print(" _________")
      print(" |/")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |___")
    elif poging == 2:
      print(" _________")
      print(" |/       |")
      print(" |       ( )")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |___")
    elif poging == 1:
      print("let op je hebt nog maar 1 kans!")
      ("")
      print(" _________")
      print(" |/       |")
      print(" |       ( )")
      print(" |       /|\ ")
      print(" |")
      print(" |")
      print(" |")
      print(" |___")
    elif poging <= 0:
      print(" _________")
      print(" |/       |")
      print(" |       ( )")
      print(" |       /|\ ")
      print(" |       / \ ")
      print(" |")
      print(" |")
      print(" |___")
      ("")
      print("helaas, GAME OVER, " + GeheimWoord + " was het juiste antwoord")
      print("je hebt het woord in", geraden, "pogingen nog steeds niet geraden geraden")
      stoppen = True


  
stoppen = True  