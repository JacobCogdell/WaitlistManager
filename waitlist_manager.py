from node import Node
from linkedlist import LinkedList

def waitlist_generator():
    # Create a new linked list instance
    wait_list = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            wait_list.add_front(name)
            
        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            wait_list.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            wait_list.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            wait_list.print_list()
            
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?

I started this project by creating new files for my two new classes.  I know that they could have all 
been in one file, but I wanted to practice working with multiple file projects.  The LinkedList class works 
in collaboration with the Node.  A Node knows which element should follow it and the LinkedList always knows 
where the start of the list is.  As I was working with my LinkedList code, I found myself wanting a previous 
option to go with the next option so that I could traverse the list in both directions.  Modifications to the 
the LinkedList involves setting the next item for each of the nodes.  Removing an element means updating 
the pointer elements so they skip over the element to be deleted.  Adding a new first element means updating 
the head node and then setting the next of the new head node to be the remainder of the list nodes.  Adding 
to the end means finding the last node and then setting its next value to a new node.  I could see an 
engineer using this for any data structure where order mattered.  
'''
