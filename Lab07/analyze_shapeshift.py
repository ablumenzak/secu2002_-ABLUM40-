import pickle
shapeshift = pickle.load(open('shapeshift.p', 'rb'))

print shapeshift

#how many transactions have ethereum (code ETH) as the input currency:
count = 0
for x in shapeshift:
    if x['curIn'] == 'ETH':
        count += 1
print count, 'transactions have Ethereum as the input currency.'

count1 = 0
for x in shapeshift:
    if x['curOut'] == 'BTC':
        count1 += 1
print count1, 'transactions have Bitcoins has the output currency.'

count2 = 0
for x in shapeshift:
    if x['curIn'] == 'ZEC' and x['curOut'] == 'BTC':
        count2 +=1
print count2, 'transactions are trading Zcash to Bitcoins'

