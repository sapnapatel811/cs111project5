#This Cipher App is created by Sapna Patel for CS 111 @UIC (UIN: 653295462) on 11/13/2024
#This app allows the user to use Caesar Cipher to either encryp or crack a message 

#This is a function that encrypts a message using Caesar Cipher
def caesar_encrypt(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = "" #will store encrypted message

    for letter in message: #loops through each letter in the message to encrypt it
        if letter in alphabet: #for uppercase
            find_pos = alphabet.find(letter)
            new_position = (find_pos + key) % 26 #letter shifts according to the key, wrapping around with % 26
            result += alphabet[new_position]

        elif letter.upper() in alphabet: #for lowercase
            find_pos = alphabet.find(letter.upper())
            new_position = (find_pos + key) % 26
            result += alphabet[new_position].lower()

        else: 
            result += letter #accounts for if punctuation or space to leave it the same
        
    return result #returns encrypted message

#Function to clean the list of words, removing newlines and other sorts
def clean(list_of_words):
    for i in range(len(list_of_words)):
        list_of_words[i] = list_of_words[i].strip()

#Function to find the valid words that match the English words from the given list and finds the percentage of that
def percentage_finder(message , list_of_words):
    words_in_message = message.split()
    count = 0 #this will count valid words

    for user_word in words_in_message: #loops through the word in the message words
        for word_in_list in list_of_words:
            if word_in_list == user_word.lower(): #checks if they match and adds if they do
                count += 1

    percentage = (count / len(words_in_message)) * 100 #calculates percentage of valid words
    return percentage

#Function to decrypt the message by trying and finding the best key shift
def caesar_cracker(message, filename):
    file = open(filename)
    list_of_words = file.readlines()
    clean(list_of_words) #opens the file and reads all lines to clean the list

    percentage_list = []
    key_list = []
    
    for key in range(26): #will loop through all shifts 
        decrypted = caesar_encrypt(message, key) 
        percentage = percentage_finder(decrypted, list_of_words)
        percentage_list.append(percentage) #stores percentage into percentage list
        key_list.append(key) #stores key into key list

    highest_percentage = float(max(percentage_list)) #finds the highest percentage of valid words
    highest_key = key_list[(percentage_list.index(highest_percentage))] #finds the key associated with that highest percentage
    decrypted_message = caesar_encrypt(message, highest_key) #decrypts the message with the highest key

    return 26 - highest_key, decrypted_message

#Main function for user input with a being encryption and b being decryption 
if __name__ == "__main__":
    print("Welcome to the Cipher App")
    print("---------------------------------------------")
    print("This app can help you with one of the following - ")
    print("(A) Encrypt a message with the Caesar Cipher")
    print("(B) Crack a message")
    choice = input("Which would you like to do ?: ")

    if(choice== "A"  or choice == "B"):
        if choice == "A": #if encryption
            print("Your choice is A")
            message = input()
            key = int(input())
            encrypt_message = caesar_encrypt(message, key)
            print("You have chosen to Caesar Encrypt !")
            print(f"Enter your message to be encrypted: Enter the key (one digit number) to be used for the encryption: Your Secret Message is: {encrypt_message}")

        elif choice == "B": #if decryption
            print("Your choice is B")
            print("You have chosen to decrypt !")
            print("You have chosen Caesar Cracking !")
            message = input()
            filename = input()
            key, decrypted_message = caesar_cracker(message, filename)
            print(f"Enter your message to be decrypted: Enter the name of the file to be used to crack the code: Your Secret Message is: {decrypted_message}")
            print(f"The key used to encrypt your message was {key}")
    else: #if invalid choice is entered
        print("Incorrect choice:", choice )
    print("GoodBye!") #ALL DONE :) which will print goodbye to end