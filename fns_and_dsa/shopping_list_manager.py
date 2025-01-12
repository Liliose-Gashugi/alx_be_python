def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                item = input("Enter the name of an item to add: ").strip()
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")


            elif choice == 2:
                item = input("Enter the name of an item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the shopping list.")
                else:
                    print(f"'{item}' is not in the shopping list.")



            elif choice == 3:
                if shopping_list:
                    print("\n Current Shopping List:")
                    for i, item in enumerate(shopping_list, start=1):
                        print(f"{i}. {item}")
                else:
                    print("The shopping List is currently empty.")




            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()