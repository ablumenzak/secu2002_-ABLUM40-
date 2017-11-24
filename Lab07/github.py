#Task 4 - writing a code that prints all the commit message from repository
import requests
r = requests.get('https://api.github.com/repos/smeiklej/secu2002_2017/commits')
text = r.json()

#asking the code to print out the commit message for all rows in the text
for row in text:
    print row['commit']['message']
