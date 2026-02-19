a = 'Make a lot of money'
b = 'buy now'
c = 'suscribe this'
d = 'click this'

msg  = input('Enter your message: ')

if ((a in msg) or (b in msg) or (c in msg) or (d in msg) ):
    print("This is spam msg")

else:
    print("This comment is not spammm")