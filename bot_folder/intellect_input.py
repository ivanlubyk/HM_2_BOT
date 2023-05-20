import time


COMMANDS = ['Phonebook', 'Calendar jubilars', 'Clean folder', 'Note', 'Exit', 
            'Add', 'Change', 'Search info', 'Show all', 'Del', 'Export JSON', 
            'New note', 'Edit note', 'Delete note', 'Print notes', 'Search note']


def recognize_command():
    status = True
    while status == True:        
        text = input('>>>>  ')
        res_dict = {}
        for i in COMMANDS:
            percent = 0
            for y in list(text.lower()):
                if len(list(text)) <= len(i):
                    if y in list(i.lower()):
                        percent += 100 / len(list(i))
                    res_dict[i] = percent
        if len(res_dict) != 0:
            choice = max(res_dict, key=res_dict.get)
        if sum(res_dict.values()) == 0:
            print('Command not recognized. Re-enter? (yes/no)')
            choice_1 = input('>>>>  ')
            if choice_1.lower() == 'no':
                status = False
        else:
            status = False            
    return choice

    
