filename = "dreams.txt"

while True:
    print("===== FILE MANAGER NI DREAM :) =====")
    print("===== DREAMS FILE MANAGER =====")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file ")
    print("4. Exit")

    choice = input("Enter Your Choice")

    if choice == "1":


        
        try:
            file = open(filename, "r")

            content = file.read()

            print("\n--- Inspiring Messages ---")

            if content == "":
                print("Looks like its Empty")
            else:
                print(content)

            file.close()

        except FileNotFoundError:
            print("File not found.")


    elif choice == "2":

        new_message = input("Enter a new inspiring message: ")

        file = open(filename, "a")
        file.write("\n" + new_message)
        file.close()

        print("Message added successfully!")

    
    elif choice == "3":
        confirm = input("Warning: This will overwrite the file Type YES to continue): ")

        if confirm.lower() == "yes":

            newcontent = input("Write your new set of inspiring messages:")

            file = open(filename, "w")
            file.write(newcontent)
            file.close()

            print("File has been overwritten")

        else:
            print("Rewrite cancelled.")

    elif choice == "4":

        print("You Ended it :(( )")
        break

    # invalid input
    else:
        print("Please try again.")  


    
