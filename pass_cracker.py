import hashlib
import threading

# Asking the use for Hash format

print("1. md5\n2. md5\n3. sha1 \n4. sha256\n5. sha512\n")
choice = int(input("Hash format (1-5): "))
match(choice):
    case 1:
        hash_format = "md5"
        print("Hash Format choosen: md5\n")

    case 2:
        hash_format = "md5"
        print("Hash Format choosen: md5\n")

    case 3:
        hash_format = "sha1"
        print("Hash Format choosen: sha1\n")

    case 4:
        hash_format = "sha256"
        print("Hash Format choosen: sha256\n")

    case 5:
        hash_format = "sha512"
        print("Hash Format choosen: sha512\n")


# Taking input Hash from the user for checking  

input_hash = input("Enter the hash to Crack: ")

# Reading the wordlist file

with open('wordlist.txt', 'r') as file:
    wordlist_pass = file.read().splitlines()

# Converting Wordlist password to user specified Hash format 

found = None
items = None
items_found_list = []

def create_hash(input_hash):
    
    for items in wordlist_pass:
        hash_obj= hashlib.new(hash_format)
        current_word = items.encode()
        hash_obj.update(current_word)
        wordlist_pass_hash = hash_obj.hexdigest()
                
            # Check for the correct password
        if input_hash == wordlist_pass_hash:
            items = items
            found = 1
            items_found_list.append(items)
            items_found_list.append(found)
            return(items_found_list)

# Asking user for thread count and implementing threads

thread_count = int(input("\nEnter the number of threads to use (recomended 1-40): "))
print(f"Using {thread_count} threads\n")

threads = []

for i in range(thread_count):
    t = threading.Thread(target=create_hash, args=[input_hash,])
    threads.append(t)
    t.start()

# waiting for all the threads to finish

for t in threads:
    t.join()

# printing the found password

if len(items_found_list)==0:
    print("Passowrd Not Found!")
else:
    items = items_found_list[0]
    found = items_found_list[1]

if(found == 1):
    print(f"PASSWORD FOUND!\nPassword: {items}")

