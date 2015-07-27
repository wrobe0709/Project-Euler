import random
suits = ['d','h','s','c']
ranks = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

def build_deck():
	deck = []
	for r in ranks:
		for s in suits:
			mytuple = (r, s)
			deck.append(mytuple)
	return deck

def deal_cards(player_hand):
	deck = build_deck()
	card = random.choice(deck)
	deck.remove(card)
	card2 = random.choice(deck)
	deck.remove(card2)
	player_hand.append(card)
	player_hand.append(card2)
	return player_hand

def hand_value(hand):
	total = 0
	rank = [i[0] for i in hand]
	for c in rank:
		total += ranks[c]
	return total

def palindrome_compare(string1, string2):
	if isinstance(string1, basestring) == True and isinstance(string2, basestring) == True:
		string1 = sorted(string1)
		string2 = sorted(string2)
		if string1 == string2:
			return True
		else:
			return False
	else:
		raise Exception("Warning! Not a String")

def large_sum():
	return str(sum(map(int,([line.strip('\n') for line in open("string_of_100_numbers") if line.strip() and not line.startswith("\'") and not line.startswith("s")]))))[:10]


if __name__ == '__main__':
	large_sum()
	#palindrome_compare('hello','world')
	#build_deck()
	#for x in range(0,1000):
	#	hand_value(deal_cards([]))
