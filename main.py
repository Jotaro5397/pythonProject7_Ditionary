Playerstats = dict ( Flyabiltiy = 0, Stealth = 0 )
pickups = dict(Daggers = 0, BluePotions = 0, GoldenFeather = 0, Manuscripts = 0 )

while True:
    try:
        playerchoice = int(input("\nYou notice an item while walking,which item would like to select,\n\n1.Dagger,\n\n2.BluePotion"
                            "\n\n3.GoldenFeather\n\n4.Manuscripts,\n\nWhat do you choose? "))
        if playerchoice == 1:
            pickups["Daggers"] += 1
            print("\n", Playerstats)
            print("\n", pickups)
        elif playerchoice == 2 and Playerstats ['Stealth']  < 5:
            Playerstats['Stealth'] += 1
            pickups ['BluePotions'] += 1
            print("\n", Playerstats)
            print("\n", pickups)
        elif playerchoice == 3 and Playerstats [ 'Flyabiltiy'] <5:
            Playerstats['Flyabiltiy'] += 1
            pickups['GoldenFeather'] += 1
            print("\n", Playerstats)
            print("\n", pickups)
        elif playerchoice == 4:
            pickups['Manuscripts'] += 1
            print("\n", Playerstats)
            print("\n", pickups)
        elif Playerstats['Flyabiltiy'] == 5 or Playerstats['Stealth'] ==5 or playerchoice != (1,2,3,4):
            print("\n\nTry a different item\n\n")
    except ValueError:
        print("\nNumber Requested\n")