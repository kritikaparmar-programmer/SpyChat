# We are here to make a SPY CHAT.
# Importing necessary module to hide and read messages from an image.
from steganography.steganography import Steganography
from datetime import datetime

# Adding Default status messages
Status_Messages = ["My name is Mr. Detective!", "Live and let live!", "Just Love the way I am", "I am surprised!"]


# Making Class Spy and chat message.
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.count = 0


class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.sent_by_me = sent_by_me
        self.time = datetime.now()


# Adding a default user spy
spy = Spy(" ", " ", 19, 4.5)
spy.name = 'K'
spy.salutation = 'Ms.'

# adding friends
friend_first = Spy('Aki', 'Mr.', 20, 4.7)
friend_second = Spy('Anita', 'Ms.', 20, 4.8)
friends = [friend_first, friend_second]

print("WELCOME TO THE SPY CHAT\n Let's get started!!")
print("Do you want to continue as DEFAULT USER or create a NEW USER?(Y/N): ")
answer = input("Enter your choice: ")


# Making Menu as a function.
def menu():
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do?\n 1. What's Your Status?\n 2. Add a Spy\n" \
                       " 3. Send a message\n 4. Read a message\n 5. Read Chat History\n 6. Close App "
        print(menu_choices)
        choice_of_you = input("Enter any choice acc. to you: ")
        # to check whether the user has inputted the menu choice according to him or not.
        if len(choice_of_you) > 0:
            choice_of_you = int(choice_of_you)

            if choice_of_you == 1:
                # Set your current status
                add_status()

            elif choice_of_you == 2:
                # Add a new friend
                add_friend()

            elif choice_of_you == 3:
                # Send a secret message
                send_a_message()

            elif choice_of_you == 4:
                # Read the secret message sent by your friend
                read_a_message()

            elif choice_of_you == 5:
                # Read the chat history
                read_chat_history()

            elif choice_of_you == 6:
                # Close the app
                print("Successfully closed!!")
                show_menu = False

            else:
                print("Wrong Choice entered by you!")


# Adding of the status
def add_status():
    updated_status_message = None
    adding = int(input("What do you want?\n1. Add Status Update\n2. Choose From Existing Status\n3. Go back to "
                       "Menu\nEnter your choice: "))

    if adding == 1:
        new_status = input("Write the status you want:  ")
        if len(new_status) > 0:
            Status_Messages.append(new_status)
            updated_status_message = new_status

    elif adding == 2:
        print(Status_Messages)
        choosing_status = int(input("Choose the index of the status: "))
        if len(Status_Messages) >= choosing_status:
            updated_status_message = Status_Messages[choosing_status - 1]

    elif adding == 3:
        menu()

    else:
        print("The option is not valid!!")

    if updated_status_message:
        print("Your updates status is:\n ")
        print(updated_status_message)

    else:
        print("SORRY!\n Your status is not updated")


# Adding A SPY
def add_friend():
    a = int(input("Whats next you want?:\n1. Continue adding a friend\n2. Go back to main menu\nEnter your choice: "))
    new_friend = Spy(" ", " ", 0, 0.0)
    new_friend.name = input('Please Enter your friend name: \n')
    new_friend.salutation = input('Are they MR. or MS. : \n')
    new_friend.age = int(input("Enter the age of your friend: \n"))
    new_friend.rating = float(input("Please enter the SPY Rating: \n"))
    if a == 1:
        if len(new_friend.name) > 0 and 12 < new_friend.age < 50 and new_friend.rating >= spy.rating:
            friends.append(new_friend)
            print("Friend Added")

        else:
            print("Sorry!\n The Friend cannot be a SPY")
    else:
        menu()

    return len(friends)


# selecting a friend
def select_friend():
    index_number = 0
    for friend in friends:
        print(index_number + 1, ". ", friend.salutation, " ", friend.name, " aged ", friend.age, "  with rating ",
              friend.rating, " is online. ")
        index_number += 1

    choose_friend = int(input("Choose the index no. of the friend: "))

    friend_choice_position = int(choose_friend) - 1

    # Check if the user chooses index out of range
    if friend_choice_position + 1 > len(friends):
        print("Sorry,This friend is not present.")
        exit()

    else:
        # returns the selected friend to perform the options
        return friend_choice_position


# sending message
def send_a_message():
    friend_choose = select_friend()
    original_image = input("What is the name of the image that you want to encode the secret message with? ")
    output_path = "output.jpg"
    text = input("What is the secret message you want to hide with the image? ")
    Steganography.encode(original_image, output_path, text)
    new_chat = ChatMessage(text, True)
    friends[friend_choose].chats.append(new_chat)
    print("Hey Dude! \n Your secret 'MESSAGE- IMAGE' is ready.")


# Reading messages
def read_a_message():
    sender = select_friend()
    output_path = input("What is the name of the image file from which yo want to decode the message from? ")
    # error handling (there may be a secret message and may be not)
    try:
        secret_text = Steganography.decode(output_path)
        print("The secret message you got: ")
        print(secret_text)
        words = secret_text.split()
        friends[sender].count += len(words)
        new_chat = ChatMessage(secret_text, False)
        friends[sender].chats.append(new_chat)
        print("Your secret message is saved!")

        # Delete a spy from your list of spies if they are speaking too much
        if len(words) > 100:
            print(friends[sender].name, 'blue'),
            print("Removed from friends list. What a chatter box! What a drag!!!", "yellow")
            # Removes that chatterbox friend
            friends.remove(friends[sender])

    except TypeError:
        print("Nothing to decode from the image as it contains no secret message!")


# Reading of chat history
def read_chat_history():
    friend_select = select_friend()
    print('\n')

    for chat in friends[friend_select].chats:
        if chat.sent_by_me:
            print(chat.time.strftime("%d %B %Y %A %H:%M"))
            print("You said: *", str(chat.message), "*")

        else:
            print(chat.time.strftime("%d %B %Y %A %H:%M"))
            print(str(friends[friend_select].name) + " said : " + str(chat.message))


def start_chat():
    spy.name = spy.salutation + " " + spy.name

    if 12 < spy.age < 50:
        print("WELCOME", spy.name, "\nYour age: ", spy.age, "\nYour rating: ", spy.rating)

        menu()

    else:
        if spy.age < 12:
            print("Sorry , you are too young to become a Spy.")
        elif spy.age >= 50:
            print("Sorry , you are too old to become a Spy.")


# if the user chooses default spy
if answer.upper() == "Y":
    start_chat()

elif answer.upper() == "N":
    spy = Spy(" ", " ", 0, 0.0)

    spy.name = input("What is your Spy name? \n")

    if len(spy.name) > 0 and spy.name.isdigit() is False:
        spy.salutation = input("What should we call you? MR. or Ms.: \n")
        if len(spy.salutation) > 0:
            spy.age = int(input("Enter your age: \n"))
            if 12 <= spy.age < 50:
                print("Welcome to SPY community!")
                spy.rating = (input("Please Enter your Spy rating: \n"))
                if len(spy.rating) > 0:
                    spy.rating = float(spy.rating)
                    if spy.rating >= 4.5:
                        print("Great !")
                    elif 3.5 <= spy.rating < 4.5:
                        print("You are very good at this!")
                    elif 2.5 <= spy.rating < 3.5:
                        print("You can do Better!")
                    else:
                        print("You Need some help!")

                    start_chat()

                else:
                    print("Enter a valid rating..")

            else:
                if spy.age < 12:
                    print("Sorry , you are too young to become a Spy.")
                elif spy.age >= 50:
                    print("Sorry , you are too old to become a Spy.")
                else:
                    print("Enter a valid age..")

        else:
            print("Please enter a valid salutation")

    else:
        print("Please enter a valid name.")

else:
    print("You did not replied with a Y or N")
    exit()
