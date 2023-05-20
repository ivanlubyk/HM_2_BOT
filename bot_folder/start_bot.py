
try:
    import bot_folder.export_func as basic
    import bot_folder.module_classes_2 as class_exp
    import bot_folder.module_classes_note as class_note
    from bot_folder.intellect_input import recognize_command as neurone
    from bot_folder.clean_folder import main as clean
except ModuleNotFoundError:
    import export_func as basic
    import module_classes_2 as class_exp
    import module_classes_note as class_note
    from intellect_input import recognize_command as neurone
    from clean_folder import main as clean
import time
import os
import json
from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def show_contacts(self, contacts):
        pass
    
    @abstractmethod
    def show_notes(self, notes):
        pass
    
    @abstractmethod
    def show_help(self, commands):
        pass

class ConsoleInterface(Interface):
    def show_contacts(self, contacts):
        print("=== Contacts ===")
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            
    
    def show_notes(self, notes):
        print("=== Notes ===")
        for note in notes:
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
           
    
    def show_help(self, commands):
        print("=== Help ===")
        for command in commands:
            print(f"{command['name']}: {command['description']}")
            

class CommandLineInterface(Interface):
    def show_contacts(self, contacts):
        print("=== Contacts ===")
        for contact in contacts:
            print(f"{contact['name']}\t{contact['phone']}\t{contact['email']}")
    
    def show_notes(self, notes):
        print("=== Notes ===")
        for note in notes:
            print(f"{note['title']}\t{note['content']}")
    
    def show_help(self, commands):
        print("=== Help ===")
        for command in commands:
            print(f"{command['name']}\t{command['description']}")

#Створюємо екземпляри класів телефкниги та нотаток
book = class_exp.Record()
note = class_note.Record()


def main_menu():

    os.system('CLS')
    print('==== main menu ====')
    print('How can I help you?')
    print('"Phonebook" - opening phonebook menu\n"Calendar jubilars" - opening calendar\n'
          '"Clean Folder" - opening a file sorting application\n'
          '"Note" - opening a notebook\n'
          '"Export JSON" - Export data to JSON\n'
          '"Exit" - exit from the program\n'
          'Your chois (enter a command from the above list):')

    chois = neurone()    
    if chois == 'Phonebook':        
        phone_menu()
    elif chois == 'Calendar jubilars':        
        calendar_menu()
    elif chois == 'Clean folder':
        response =clean()
        if response == None:
            main_menu()
    elif chois == 'Note':        
        note_menu()
    elif chois == 'Exit':
        basic.input_output(chois)
    elif chois == 'Export JSON':
        json_menu()       
    else:
        main_menu()


def phone_menu():

    os.system('CLS')
    print('==== phonebook menu ====')
    print('"Add" - adding a contact to the phonebook\n"Change" - change an existing contact'
          '\n"Search info" - search contact information by name\n"Show all" - list of all contacts\n'
          '"Del" - deleting a contact from the phonebook\n"Exit" - exit to main menu'
          '\nYour chois (enter a command from the above list):')

    
    chois = neurone()
    if chois == 'Add':
        os.system('CLS')
        print('==== adding contact ===')
        
        print('Enter contact name(Name Surname (cannot be empty))')
        name_contact = input('>>>> ')
        res = basic.check_name(name_contact)
        if res[0] == True:
            name = class_exp.Name()
            name.name = res[1]
            print(f'Name {res[1]} added success')
        print('=' * 30)
        print('Add additional data ? (phone number, email, date of birth) (yes/no)')
        chois = input('>>>>  ')
        if chois.lower() == 'yes':
            print('Enter phone number \nun the format +380672972960 (may be empty)')
            number_contact = input('>>>>  ')
            res = basic.check_number(number_contact)
            if res[0] == True and len(res[1]) > 0:
                phone = class_exp.Phone()
                phone.phone = res[1]
                print(f'Phone number {res[1]} added success')

            print('Add email address un the format "post@mail.com" (may be empty)')
            email_contact = input('>>>>  ')
            res = basic.check_email(email_contact)
            if res[0] == True and len(res[1]) > 0:
                email = class_exp.Email()
                email.email = res[1]
                print(f'E-mail {res[1]} added success')

            print("Add contact's date of the birth un the format 'dd-mm-yyyy'(may be empty)")
            date_birth = input('>>>>  ')
            res = basic.check_birthdate(date_birth)
            if res[0] == True and len(res[1]) > 0:
                date_birth = class_exp.DateBirth()
                date_birth.date_birth = res[1]
                print(f'Date of the birth "{res[1]}" added success')
            
        else:
            phone = class_exp.Phone()            
            email = class_exp.Email()
            date_birth = class_exp.DateBirth()
                        
        book.add_record(name.name, phone.phone, email.email, date_birth.date_birth)
        print(f'Contact details "{name.name}" added successfully')
        time.sleep(3)
        phone_menu()           


    elif chois == 'Change':
        status = True        
        
        while status == True:
            os.system('CLS')
            print('==== contact change ====')
            print('Enter contact name')
            name_contact = input('>>>>  ')
            result = book.search_kontakts(name_contact)
            if len(result) == 0:
                print(f'Name "{name_contact}" not found. Re-enter? ( yes / no)')
                chois_1 = input ('>>>>  ')
                if chois_1.lower() == 'no':
                    status =False
                    phone_menu()
                
            else:  
                os.system('CLS')
                print('==== contact change ====')
                count = 1
                for name, number in result.items():
                    count_1 = 1
                    print(count,' : ',name)
                    for i in number:                        
                        for key, value in i.items():                            
                            if type(value) == list:
                                print(count_1, ' : ',key, " : ", (', ').join(value))
                                count_1 +=1
                            else:
                                print(count_1, ' : ',key, " : ", value)
                    print("*" * 34)
                    count_1 =1
                    count +=1

                if count > 2:
                    print('Enter the number of the contact you want to change')
                    num_change = input('>>>>  ')
                    print('Enter the number of the value contact you want to change')
                    num_value = input('>>>>  ')
                else:
                    num_change = 1 
                    print('Enter the number of the value contact you want to change')
                    num_value = input('>>>>  ')
                print(
                    f'Enter a new value "{list(list(result.values())[int(num_change)-1][int(num_value) -1].keys())[0]}" for contact "{list(result.keys())[int(num_change)-1]}"')
                new_value = input('>>>>  ')
                book.change_record(list(result.keys())[int(num_change)-1], new_value, list(
                    list(result.values())[int(num_change)-1][int(num_value) - 1].keys())[0])
                print(
                    f'Value "{new_value}" added to contact "{list(result.keys())[int(num_change)-1]}"')
                time.sleep(3)
                phone_menu()



            

    elif chois == 'Search info':

        os.system('CLS')       

        status = True
        while status == True:
            print('==== search contact information ====')
            print('enter contact name')
            name_contact = input ('>>>>  ')
            result_names = book.search_kontakts(name_contact)

            os.system('CLS')
            print('='*10, 'Result search', '='*10)
            for name_book, number_book in result_names.items():
                print(name_book)
                for i in number_book:
                    for key, value in i.items():
                        if type(value) == list:
                            print(key, " : ", (', ').join(value))
                        else:
                            print(key, " : ", value)
                print("*" * 34)
            print('Return in phone menu ? (yes / no)')
            chois = input('>>>>  ')
            if chois.lower() == 'yes':
                status = False
                phone_menu()
            else:
                os.system('CLS')

            if len(result_names) == 0:
                print('Contacts with such data were not found. Repeat search? (yes/no)')
                response = input('>>>>  ')
                if response.lower() == 'no':
                    search = False
                    phone_menu()
            
                

        print('Return in menu phonebook ?(yes/no)')
        if input('>>>>  ').lower() == 'yes':
            phone_menu()
        else:
            main_menu()

    elif chois == 'Show all':
        book.show_all_record()
        print('Return in menu phonebook ?(yes/no)')
        if input('>>>>  ').lower() == 'yes':
            phone_menu()
        else:
            main_menu()

    elif chois == 'Del':
        status = True
        while status == True: 
            os.system('CLS')
            print('==== delete change ====')
            print('Enter contact name')
            name_contact = input('>>>>  ')
            result = book.search_kontakts(name_contact)    
            if len(result) == 0:
                print('Contacts with such data were not found. Repeat search? (yes/no)')
                chois = input('>>>>  ')
                if chois.lower() == 'no': 
                    status = False               
                    phone_menu()
            else:
                count = 1
                count = 1
                for name, number in result.items():
                        count_1 = 1
                        print(count, ' : ', name)
                        for i in number:
                            for key, value in i.items():
                                if type(value) == list:
                                    print(count_1, ' : ', key,
                                            " : ", (', ').join(value))
                                    count_1 += 1
                                else:
                                    print(count_1, ' : ', key, " : ", value)
                        print("*" * 34)
                        count_1 = 1
                        count += 1
                if count >2:
                    print('Enter the number of the contact you want to delete')
                    num_change = input('>>>>  ')
                else:
                    num_change = 1
                print(
                    f'Contact "{list(result.keys())[int(num_change)-1]}" entry will be deleted from the phonebook.(yes/no)\nYour choice')
                chois = input('>>>>  ')
                if chois.lower() == 'yes':
                    book.delete_record(list(result.keys())[int(num_change)-1])
                    print(
                        f'Record "{list(result.keys())[int(num_change)-1]}" deleted from phone book')
                else:
                    print(f'Operation canceled')
                print('Return in menu phonebook ?(yes/no)')
                chois = input('>>>>  ')
                if chois.lower() == 'yes':
                    status = False                
                    phone_menu()
                else:
                    status = False
                    main_menu()                    

    elif chois == 'Exit':
        main_menu()

    else:
        print('Incorrect chois...')
        time.sleep(3)
        phone_menu() 
        

def calendar_menu():
    print('==== calendar menu ====')
    print('Calendar menu options here')
    os.system('CLS')
    book.get_jubilars()
    print('*'*56)
    print('Return in main menu (yes/no)')
    chois_2 = input('>>>>  ')
    if chois_2.lower() == 'yes':
        main_menu()
    else:
        basic.input_output('goodbye')


def json_menu():
    print('==== JSON menu ====')
    print('JSON menu options here')
    os.system('CLS')
    print('=' * 30)
    print('Select data to export')
    print('=' * 30)
    print('Phonebook\nNote\nYour chois (enter a command from the above list):')
    choice = neurone()
    if choice == 'Phonebook':
        basic.export_json(book.book.data, choice)
    else:
        basic.export_json(note.notes, choice)
        pass
    print('Data upload was successful')
    time.sleep(3)
    main_menu()


#Логіка роботи з нотатками
def note_menu():
    os.system('CLS')
    while True:
        print('==== note menu ====')
        print('Note menu options here')
        print("Choose an action:")
        print("1. New note - create a new note >>> press 1 ")
        print("2. Change note - edit an existing note >>> press 2")
        print("3. Search note - search for an existing note >>> press 3")
        print("4. Delete note - delete an existing note >>> press 4")
        print("5. Print notes - print notes by topic >>> press 5")
        print("6. Return to the main menu >>> press 6")
        choice = input("Your choice: ").strip()
        if choice == '1':
            print('Choose an option:')
            print('1. Enter note manually')
            print('2. Load note from a file')
            note_choice = input('Your choice: ').strip()
            if note_choice == '1':
                note.add_note()
            elif note_choice == '2':
                file_path = input('Enter file path: ')
                try:
                    note.load_notes_from_file(file_path)
                except FileNotFoundError:
                    print('File not found')
                except json.JSONDecodeError:
                    print('Invalid JSON format')
            else:
                print('Incorrect choice')
        elif choice == '2':
            title = input("Enter the title of the note you want to edit: ")
            note.edit_note(title)
        elif choice == '3':
            tags = input("Enter tags to search for (comma-separated): ").split(",")
            result_notes = note.search_notes_by_tags([tag.strip() for tag in tags])
            print('Return in menu note?(yes/no)')
            chois = input('>>>>  ')
            if chois.lower() == 'yes':
               note_menu()
        elif choice == '4':
            title = input("Enter the title of the note you want to delete: ")
            note.delete_note(title)
        elif choice == '5':
           note.print_notes(note.notes)
           print('Return in menu note?(yes/no)')
           chois = input('>>>>  ')
           if chois.lower() == 'yes':
               note_menu()
        elif choice == '6':
            break
        else:
            print('Incorrect choice')
        time.sleep(2)

    #Можливість повренутися) у головне меню
    print('Return in main menu ? (yes/no)')
    choice = input('>>>>  ')
    if choice.lower() == 'yes':
        main_menu()
    else:
        note_menu()



def main():
    os.system('CLS')
    print('Hello! I am a bot.\nEnter "hello" to get started or any other word to exit.')
    chois = input('>>>>  ').lower()
    chois = basic.input_output(chois)
    if chois == True:        
        main_menu()

if __name__ == '__main__':
    main()

