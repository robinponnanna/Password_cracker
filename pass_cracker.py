import hashlib

# Asking the use for Hash format

print("1. md5\n2. md5\n3. sha1 \n4. sha256\n5. sha512\n")
choice = int(input("Hash format (1-5): "))
match(choice):
    case 1:
        hash_format = "md5"
        print("Hash Format choosen: md5")

    case 2:
        hash_format = "md5"
        print("Hash Format choosen: md5")

    case 3:
        hash_format = "sha1"
        print("Hash Format choosen: sha1")

    case 4:
        hash_format = "sha256"
        print("Hash Format choosen: sha256")

    case 5:
        hash_format = "sha512"
        print("Hash Format choosen: sha512")


# Taking input Hash from the user for checking  

input_hash = input("Enter the hash to Crack: ")

# Reading the wordlist file

wordlist = open('wordlist.txt', 'r')
wordlist_pass = wordlist.read().splitlines()
wordlist.close()

# Converting Wordlist password to user specified Hash format 

found = 0

for items in wordlist_pass:
    hash_obj= hashlib.new(hash_format)
    current_word = items.encode()
    hash_obj.update(current_word)
    wordlist_pass_hash = hash_obj.hexdigest()

            
        # Check for the correct password
    if input_hash == wordlist_pass_hash:
        found = 1
        break

if(found == 1):
    print(f"PASSWORD FOUND!\nPassword: {items}")
else:
    print("Passowrd Not Found!")

