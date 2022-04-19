def get_bet():

    bet_typ = input(
        "Enter the assigned number for your chosen bet type.\n"
        "0 = Done, 1 = Color, 2 = Odd/Even, 3 = Inside Number: "
    )

    if not bet_typ.isnumeric():
        print("Invalid Input")
        return "invalid"
    else:
        bet_typ = int(bet_typ)

    bet_choice = ""

    if bet_typ == 1:
        bet_choice = input("Enter color; red or black: ")
    elif bet_typ == 2:
        bet_choice = input("Enter odd or even: ")
    elif bet_typ == 3:
        bet_choice = input("Enter inside number; 0-36: ")
    elif bet_typ == 0:
        return "done"
    else:
        print("Invalid bet type")
        return "invalid"

    bet_amt = input(
        "Enter bet amount for your chosen bet.\n"
        "Inside bets $100 < $5, Outside bets $1000 < $5: "
    )

    return {"type": bet_typ, "choice": bet_choice, "amount": bet_amt}


# start of main program
bets = []
i = 0

while 1:
    print(f"Enter bet number {i+1}: ")
    bet = get_bet()
    if bet == "done":
        break
    elif bet == "invalid":
        continue

    bets.append(bet)
    i = i + 1

print(bets)
