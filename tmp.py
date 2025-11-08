for i in range(0,10):
    print(f"a{i}")


wordlist = open('wordlist.txt', 'r')
wordlist_password = wordlist.read().splitlines()
print(wordlist_password)

for items in wordlist_password:
    print(items)