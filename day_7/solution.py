from functools import cmp_to_key
from itertools import product

card_order_desc = 'AKQJT98765432'

def is_five_of_a_kind(hand):
    return all(map(lambda x: x == hand[0], hand))

def is_four_of_a_kind(hand):
    return hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4
def is_full_house(hand):
    card_counts = {}
    for card in hand:
        if card in card_counts:
            continue
        card_counts[card] = hand.count(card)
    return len(card_counts) == 2 and 2 in card_counts.values()

def is_three_of_a_kind(hand):
    card_counts = {}
    for card in hand:
        if card in card_counts:
            continue
        card_counts[card] = hand.count(card)
    return 3 in card_counts.values() and 1 in card_counts.values()

def is_two_pairs(hand):
    card_counts = {}
    for card in hand:
        if card in card_counts:
            continue
        card_counts[card] = hand.count(card)
    return len(card_counts) == 3 and 1 in card_counts.values() and 2 in card_counts.values()

def is_pair(hand):
    pair_found = False
    for card in hand:
        if hand.count(card) > 2:
            return False
        pair_found = pair_found or hand.count(card) == 2
    return pair_found
    
def cmp_plays(play1, play2):
    
    
    hand1, hand2 = play1[0], play2[0]
    
    constellation_checks = [is_five_of_a_kind, is_four_of_a_kind, is_full_house,\
                            is_three_of_a_kind, is_two_pairs, is_pair]
    for constellation_check in constellation_checks:
        check = (constellation_check(hand1), constellation_check(hand2))
        if check == (False, False):
            continue
        elif check == (True, False):
            return 1
        elif check == (False, True):
            return -1
        else:
            break
    
    # Hands are the same constellation
    for cards in zip(hand1, hand2):
        difference = card_order_desc.find(cards[0]) - card_order_desc.find(cards[1])
        if difference == 0:
            continue
        elif difference < 0:
            return 1
        else:
            return -1
    
    # Hands are exactly the same
    return 0

def cmp_plays_2(play1, play2):
    hand1, hand2 = play1[0], play2[0]
    
    replaces1 = product('AKQT98765432', repeat=hand1.count('J'))
    replaces2 = product('AKQT98765432', repeat=hand2.count('J'))
    possible_plays1, possible_plays2 = [play1], [play2]
    for replacement in replaces1:
        new_hand = list(hand1)
        tuple_index = 0
        for j, c in enumerate(new_hand):
            if c != 'J':
                continue
            new_hand[j] = replacement[tuple_index]
            tuple_index += 1
        possible_plays1.append((''.join(new_hand), play1[1]))
    check_hand1 = max(possible_plays1, key=cmp_to_key(cmp_plays))[0]
    for replacement in replaces2:
        new_hand = list(hand2)
        tuple_index = 0
        for j, c in enumerate(new_hand):
            if c != 'J':
                continue
            new_hand[j] = replacement[tuple_index]
            tuple_index += 1
        possible_plays2.append((''.join(new_hand), play2[1]))
    check_hand2 = max(possible_plays2, key=cmp_to_key(cmp_plays))[0]
    
    constellation_checks = [is_five_of_a_kind, is_four_of_a_kind, is_full_house,\
                            is_three_of_a_kind, is_two_pairs, is_pair]
    for constellation_check in constellation_checks:
        check = (constellation_check(check_hand1), constellation_check(check_hand2))
        if check == (False, False):
            continue
        elif check == (True, False):
            return 1
        elif check == (False, True):
            return -1
        else:
            break
    
    # Hands are the same constellation
    for cards in zip(hand1, hand2):
        difference = card_order_desc.find(cards[0]) - card_order_desc.find(cards[1])
        if difference == 0:
            continue
        elif difference < 0:
            return 1
        else:
            return -1
    
    # Hands are exactly the same
    return 0

def task_one(lines):
    plays = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]
    plays.sort(key=cmp_to_key(cmp_plays))
    scores = [(i+1)*play[1] for i, play in enumerate(plays)]
    return sum(scores)

def task_two(lines):
    plays = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]
    plays.sort(key=cmp_to_key(cmp_plays_2))
    scores = [(i+1)*play[1] for i, play in enumerate(plays)]
    return sum(scores)

if __name__ == '__main__':
    # Read input.txt
    with open('day_7/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    solution_one = task_one(lines)
    card_order_desc = 'AKQT98765432J'
    solution_two = task_two(lines)
    print(f'Task one:\n{solution_one}')
    print()
    print(f'Task two:\n{solution_two}')