"""
Using your knowledge of escape sequences, create a single print() statement with single string inside of it that displays this when the program is run:

*******
 *****
  ***
   *
"""

print("*******" + "\n ***** " + "\n  ***  " + "\n   *   ")

#upgrade
hm = int(input("How many asterisk '*' do you want in the base of your pyramd? \n")) #need a error validation
upordown = input("Do you want your pyramd UP or DOWN? \n")
while upordown != "up" and upordown != "down":
  upordown = input("Plese inform if you pyramd will be UP or DOWN: \n")
else:
  print("")
  if upordown == "up":
    sp = int(hm / 2)
    for i in range(1, hm + 1, 2):
      print(sp * " ",i * "*")
      sp -= 1
  elif upordown == "down":
    sp = 0
    for i in range(hm, 0, -2):
      print(sp * " ",i * "*")
      sp += 1
