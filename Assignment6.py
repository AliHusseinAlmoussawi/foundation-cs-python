#Stack and Queues
#Exercise 1:
def isPalindrome(word):
    stack = []
    str = ''
    for char in word:
        if char.isalnum():
            str+=char
    print(str)
    for char in str:
            stack.append(char)

    reversedStr = ''
    while stack:
        reversedStr += stack.pop()

    return str == reversedStr


word = input("Input your string: ")

result = isPalindrome(word)

if result == True:
    print(word + " is palindrome.")
else:
    print(word + " is not palindrome.")

#Stack MIB Exercise:
def decodeMibMessage(message):
    stack = []
    decodedMessage = ''

    for char in message:
        if char.isalpha() or char==' ':
            stack.append(char)
        elif char == '*':
            if len(stack)!=0:
                decodedMessage += stack.pop()

    # If there are remaining characters in the stack, pop them out
    while stack:
        decodedMessage += stack.pop()

    return decodedMessage

mibMessage = input("Men in black message:  ")
decodedMessage = decodeMibMessage(mibMessage)
print("Decoded message: "+ decodedMessage)


#Linked Lists Exercise:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_at_location(self, location):
        if not self.head:
            print("Error: Linked list is empty.")
            return

        # If location is 0, delete the head
        if location == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0

        # Traverse to the node just before the target location
        while count < location - 1 and current.next:
            current = current.next
            count += 1

        # Check if the location is valid
        if count < location - 1 or not current.next:
            print("Invalid location.")
            return

        # Skip over the node at the specified location
        current.next = current.next.next



