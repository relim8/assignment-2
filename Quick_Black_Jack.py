import random

def game():
    #player and dealer hands
    dealer_cards = []
    player_cards = []

    #player hand
    if len(player_cards) != 2:
        player_cards.append(random.randint(1, 10))
        player_cards.append(random.randint(1, 10))
      #dealer hands
    if len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        dealer_cards.append(random.randint(1, 11))
    print('\n')
    #showing the player their cards
    print(f"you have {player_cards} for a total of {str(sum(player_cards))}")
    print('\n')
    #showing dealer card
    print(f"Dealer Has a {dealer_cards[1]} and X")
    print('\n')

    while True:
        # h_or_s = Hit or Stand
        h_or_s = str(input(f"Do you want to Stay or Hit (H/S): ")).upper()
        print('\n')

        #if the user says hit we will give them a card
        if h_or_s in ["H"]:
            player_cards.append(random.randint(1, 10))
            print(f"you now have a total {str(sum(player_cards))} from these cards {player_cards}  ")
            print('\n')

        #if the player decided to stay I will prompt the user the dealers cards and from there decides a winner
        elif h_or_s in ['S', 'Stay'] or sum(player_cards) == 21:
            print('You have choosen to stay')
            print('\n')
            print(f" you now have a total of  {str(sum(player_cards))} with {player_cards}")
            print('\n')
            if sum(dealer_cards) < 21:
                print(f"The dealer has reavealed his hand! {dealer_cards} a total of {str(sum(dealer_cards))}")
                while sum(dealer_cards) <= 16:
                    print('\n')
                    print('Dealer Hits!')
                    dealer_cards.append(random.randint(1, 10))
                    print('\n')
                    print(f"The Dealer has now {dealer_cards} for a total of {str(sum(dealer_cards))}")

            #comparing values between the dealer and player
            #this is if both the player and the dealer have the same values dealer wins
            if sum(player_cards) == sum(dealer_cards):
                print('Boom! Dealer Wins!, Dealer wins all the ties! HAHHAAHA')
                break
            #if the dealer gets over 21
            elif sum(dealer_cards) > 21:
                print('Dealer BUSTS, You win...')
                break

            #if the sum of the player cards is greater than the dealers cards
            elif sum(player_cards) > sum(dealer_cards):
                print('You win!, You cheated!! ')
                break
            #if the sum of the dealer cards is greater than 21 then player wins
            elif sum(player_cards) < sum(dealer_cards):
                print('Boom! Dealer Wins!!!')
                break
        elif h_or_s not in ['H', 'S']:
            print('Sorry I didn\'t understand!')

        if sum(player_cards) > 21:
            print(f"The dealer has a total of {str(sum(dealer_cards))} with {dealer_cards}")
            print('\n')
            print("HAHAH you BUSTED! Dealer Wins!")
            break


game()

# asking the user if they want to play again till they say no
while True:
    print('\n')
    again = input("Would you like to play again? (Y/N): ").upper()
    if again in ['Y']:
        game()
    elif again in ['N']:
        print(f"Till next time! ")
        exit()
    elif again not in ['Y', 'N']:
        print("I'm sorry I didn't understand!")
        continue


if __name__ == '__main__':
    game()
