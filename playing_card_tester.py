# playing_card_tester.py

from playing_cards import Card, Deck


c = Card(1, 1)

# encapsulation (private + getter or setter)


print (c)

d = Deck()
d.shuffle()
d.display()


print (d.deal())
print (d.deal())
print (d.deal())
print (d.deal())
print (d.deal())


print ("=" * 30)
#c.set_value(99)
print (c)
c.__value = 99 # this statement doesn't do anything.
c.display()