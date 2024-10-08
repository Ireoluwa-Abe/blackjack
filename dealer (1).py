# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint

# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
total_value=0
card_count=0

while total_value<17:
    card_rank =randint(1,13)
    card_count += 1

    if card_rank == 11 or card_rank == 12 or card_rank == 13:
    # Jacks, Queens, and Kings are worth 10.
        card_value = 10
    elif card_rank == 1:
    # Aces are worth 11.
        card_value = 11
    else:
    # All other cards are worth the same as
    # their rank.
        card_value = card_rank

    if card_rank == 1:
    # A 1 stands for an ace.
        card_name = "Ace"
    elif card_rank == 11:
    # An 11 stands for a jack.
        card_name = "Jack"
    elif card_rank == 12:
    # A 12 stands for a queen.
        card_name = "Queen"
    elif card_rank == 13:
    # A 13 stands for a king.
        card_name = "King"
    else:
    # All other cards are named by their
    # number, or rank.
        card_name = str(card_rank)

    if card_rank == 1 or card_rank == 8:
        drew_prefix = 'Drew an '
    else:
        drew_prefix = 'Drew a '

    print(drew_prefix + card_name)
    total_value+=card_value

    if total_value < 17 and card_count !=1:
    #if card_count !=1:
        print(f"Dealer has {total_value}.")

print(f"Final hand: {total_value}.")
if total_value==21:
    print("BLACKJACK!")
elif total_value>21:
    print("BUST.")
