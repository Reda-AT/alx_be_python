def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    a=0
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item=input("what do you want to add:")
            shopping_list[a] = item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            shopping_list
            Rm=input("what item do you want to remove?")
            shopping_list.remove(Rm)
            pass
        elif choice == '3':
            shopping_list
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()