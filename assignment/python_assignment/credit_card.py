import re
pattern = re.compile(r'[4-6][0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4}[-]?[0-9]{4}')

def check_consecutive(credit_card):
    card_length = len(credit_card)
    ch = credit_card[0]
    count = 1
    length = 1
    for i in xrange(1, card_length):
      if credit_card[i] == '-':
        continue
      if credit_card[i] == ch:
        count += 1
        length += 1
        if count == 4:
          return False
      else:
        length += 1
        ch = credit_card[i]
        count = 1
    return True if length == 16 else False

try:
  number_of_credit_cards = int(raw_input("Enter number of cards: "))
  credit_card = [None] * number_of_credit_cards
  for i in xrange(number_of_credit_cards):
    credit_card[i] = raw_input().strip()
  for i in xrange(number_of_credit_cards):
    if pattern.match(credit_card[i]) and check_consecutive(credit_card[i]):
      print 'Valid'
    else:
      print 'Invalid'
except Exception as e:
  print(e)