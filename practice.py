def check_straight(card1, card2, card3):
    val1 = 0
    val2 = 0
    val3 = 0
    for x in range(len(cards)):
        if card1 == cards[x]:
            val1 = card_value[x]
    for x in range(len(cards)):
        if card2 == cards[x]:
            val2 = card_value[x]
    for x in range(len(cards)):
        if card3 == cards[x]:
            val3 = card_value[x]
    if val1 + 1 == val2 and val2 + 1 == val3:
        highest = val3
        return highest
    elif val1 + 1 == val3 and val3 + 1 == val2:
        highest = val2
        return highest
    else:
        return 0


def check_3ofa_kind(card1, card2, card3):
    if card1 == card2 == card3:
        for x in range(len(cards)):
            if card1 == cards[x]:
                val1 = card_value[x]
                return val1
    else:
        # print("not equal")
        return 0


def check_royal_flush(card1, card2, card3):
    return check_straight(card1, card2, card3)


def play_cards(left1, left2, left3, right1, right2, right3):
    player1 = 0
    player2 = 0
    for x in range(3):
        if check_3ofa_kind(left1, left2, left3):
            player1 = check_3ofa_kind(left1, left2, left3)+10
        elif check_straight(left1, left2, left3):
            player1 = check_straight(left1, left2, left3)+20
        elif check_royal_flush(left1, left2, left3):
            player1 = check_royal_flush(left1, left2, left3)+30

        if check_3ofa_kind(right1, right2, right3):
            player2 = check_3ofa_kind(right1, right2, right3)+10
        elif check_straight(right1, right2, right3):
            player2 = check_straight(right1, right2, right3)+20
        elif check_royal_flush(left1, left2, left3):
            player2 = check_royal_flush(right1, right2, right3)+30
            print(player1, player2)
    if player1 > player2:
        return -1
    elif player1 == player2:
        return 0
    else:
        return 1


cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')
card_value = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

#
# def check_royal_flush(card1, card2, card3):
#     pass
# def check_3ofa_kind(card1, card2, card3):
#     if card1 == card2 and card2 == card3:
#         pass


# print(check_3ofa_kind("S2", "S2", "S3"))
