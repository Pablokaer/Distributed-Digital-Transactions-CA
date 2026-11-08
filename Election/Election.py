def show_menu():
    print()
    print("========= VOTING MENU =========")
    print("1 - Show accounts")
    print("2 - Add a voter (owner only)")
    print("3 - Vote")
    print("4 - Show results")
    print("0 - Exit")


def main():
    while True:
        show_menu()
        option = input("Choose an option: ").strip()

        if option == "1":
            print("TODO: show accounts")
        elif option == "2":
            print("TODO: add a voter")
        elif option == "3":
            print("TODO: vote")
        elif option == "4":
            print("TODO: show results")
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
