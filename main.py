while True:

    user_prompt = """
1. ADD CONTACT
2. DELETE CONTACT
3. EDIT CONTACT
4. VIEW CONTACT
5. EXIT
"""

    print(user_prompt)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        contact_file = open("contact_info.txt", "a")

        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contact_file.write(f"{name} {phone} {email}\n")
        contact_file.close()

    elif choice == 2:
        try:
            contact_file = open("contact_info.txt", "r")
            contacts = contact_file.readlines()
            contact_file.close()

            print("----------- CONTACT LIST -------------")

            serial_no = 1
            for contact in contacts:
                print(f"{serial_no}. {contact.strip("\n")}")
                serial_no += 1

            line_no = int(input("Enter line no. to delete the particular contact: "))

            if line_no > len(contacts):
                print("Line number doesn't exist: ")
            else:
                del contacts[line_no - 1]
                print("Contact deleted successfully")

                contact_file = open("contact_info.txt", "w")
                contact_file.writelines(contacts)
                contact_file.close()
            
        except:
            print("You don't have any contact list")

    elif choice == 3:
        try:
            contact_file = open("contact_info.txt", "r")
            contacts = contact_file.readlines()
            contact_file.close()

            print("----------- CONTACT LIST -------------")

            serial_no = 1
            for contact in contacts:
                print(f"{serial_no}. {contact.strip("\n")}")
                serial_no += 1

            line_no = int(input("Enter line no. to edit the particular contact: "))

            contact = contacts[line_no - 1].strip("\n")   

            if line_no > len(contacts):
                print("Line number doesn't exist: ")
            else:
                user_prompt = "What do you want to edit?\n1. NAME\n2. PHONE NO.\n3. EMAIL"
                print(user_prompt)

                edit_choice = int(input("Enter your choice: "))

                contact_file = open("contact_info.txt", "w")

                if edit_choice == 1:
                    name = input("Enter your name: ")
                    contact = contact.split(" ")
                    contact[0] = name

                    edited_contact = ""

                    for i in contact:
                        edited_contact += i + " "
                    
                    contacts[line_no - 1] = edited_contact + "\n"

                    contact_file.writelines(contacts)
                    contact_file.close()
                    
                    print("Changes saved successfully")
                
                elif choice == 2:
                    phone = input("Enter your phone number: ")
                    contact = contact.split(" ")
                    contact[1] = phone

                    edited_contact = ""

                    for i in contact:
                        edited_contact += i + " "
                    
                    contacts[line_no - 1] = edited_contact + "\n"

                    contact_file.writelines(contacts)
                    contact_file.close()

                    print("Changes saved successfully")

                elif choice == 3:
                    email = input("Enter your email: ")
                    contact = contact.split(" ")
                    contact[2] = email

                    edited_contact = ""

                    for i in contact:
                        edited_contact += i + " "
                    
                    contacts[line_no - 1] = edited_contact + "\n"

                    contact_file.writelines(contacts)
                    contact_file.close()

                    print("Changes saved successfully")

                else:
                    print("Invalid Input")
                    contact_file.close()
        except:
            print("You don't have any contact list")
        
    elif choice == 4: 
        try:
            contact_file = open("contact_info.txt", "r")
            contacts = contact_file.readlines()
            contact_file.close()

            print("----------- CONTACT LIST -------------")

            serial_no = 1
            for contact in contacts:
                print(f"{serial_no}. {contact.strip("\n")}")
                serial_no += 1
        except:
            print("You don't have any contact list")

    elif choice == 5:
        break

    else:
        print("Invalid Input")