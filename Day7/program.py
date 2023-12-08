from collections import Counter
cards_str = 'AKQT98765432J'

def part2():
    with open('input.txt') as file:
        ans = []
        for line in file.readlines():
            s = line.rstrip().split(' ')
            hand = s[0]
            bet = s[1]
            ans.append([hand, bet])
        ans.sort(key=sort_answer_part2)
        for i, a in enumerate(ans):
            joker_pos = [index for index, char in enumerate([*a[0]]) if char == 'J']
            best_hand_val, best_hand = getBestHandValue(a[0], joker_pos, 0, a[0])
            print(i+1, a[0], '->', best_hand, best_hand_val)
        print(sum((i+1) * int(a[1]) for i, a in enumerate(ans)))

def sort_answer_part1(val):
    print(val)
    card_value = getHandValue(val[0])
    return card_value

def sort_answer_part2(val: str):
    joker_pos = [index for index, char in enumerate([*val[0]]) if char == 'J']
    card_value = getBestHandValue(val[0], joker_pos, 0, val[0])
    print(val[0], card_value[1])
    #print('best val:', card_value)
    return card_value[0]

def getBestHandValue(hand, joker_positions, index, original):
    hand_no_joker = hand.replace('J', '')
    best_hand_val = '-1'
    best_hand = hand
    if index >= len(joker_positions) or len(hand_no_joker) == 0:
        return (getHandValue(hand, original), hand)
    for c in hand_no_joker:
        new_hand = hand[:joker_positions[index]] + c + hand[joker_positions[index] + 1:]
        t_best_hand_val, t_new_hand = getBestHandValue(new_hand, joker_positions, index + 1, original)
        if t_best_hand_val > best_hand_val:
            best_hand_val = t_best_hand_val
            best_hand = t_new_hand
    return (best_hand_val, best_hand)

def part1():
    with open('input.txt') as file:
        ans = []
        for line in file.readlines():
            s = line.rstrip().split(' ')
            hand = s[0]
            bet = s[1]
            ans.append([hand, bet])
        ans.sort(key=sort_answer_part1)
        print(sum((i+1) * int(a[1]) for i, a in enumerate(ans)))

def getHandValue(hand: str, original=None):
    counted_hand = Counter(hand)

    card_hand_value = ''.join(list(map(lambda c: str(len(cards_str) - cards_str.index(c)).zfill(2), [*(original if original is not None else hand)])))
    
    hand_val = -1
    card_vals = list(counted_hand.values())
    #high card
    if len(counted_hand) == 5:
        hand_val = 0
    #one pair
    elif len(counted_hand) == 4:
        hand_val = 1
    #two pair
    elif len(counted_hand) == 3:
        #three of a kind
        if 3 in card_vals:
            hand_val = 3
        else:
            hand_val = 2

    elif len(counted_hand) == 2:
        #full house
        if 3 in card_vals and 2 in card_vals:
            hand_val = 4
        #four of a kind
        elif 4 in card_vals:
            hand_val = 5
    #flush
    elif len(counted_hand) == 1:
        hand_val = 6
    return f'{hand_val}.{card_hand_value}'


part2()