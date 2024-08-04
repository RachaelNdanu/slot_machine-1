import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROW = 3
COLS = 3 

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        #lines = input("Enter the amount of lines you would you like to bet on(1-" + str(MAX_LINES) +")? ")
        lines = input(f"Enter the amount of lines you would you like to bet on 1-{MAX_LINES}? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <=MAX_LINES:
                break
            else:
                print("Enter a valid amount of lines.")

        else:
            print("Please enter a number.")

    return lines

def get_bet ():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:

                break
            else:
                print(f"Amount must be between ${MIN_BET}- ${MAX_BET}.")

        else:
            print("Please enter a number.")

    return amount
    


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:

        bet = get_bet()
        total_bet = bet *lines

        if total_bet > balance:
            print(f"You do not have insufficient money to bet that amount.Your current balance is ${balance}")

        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total amount of bet is:${total_bet}")


main()


'''symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8

}
     '''
     


    


     
    



    
