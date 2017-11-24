import requests
url = ('https://shapeshift.io/recenttx/50')
r = requests.get(url)

print r.text

import pickle
filename = 'shapeshift.p'
pickle.dump(r.json(), open(filename, 'wb'))

