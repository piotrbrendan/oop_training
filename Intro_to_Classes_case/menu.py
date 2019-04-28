import sys
from Intro_to_Classes_case.notebook import Notebook

class Menu:

    def __init__(self, notebook_name):
        self.notebook = Notebook(notebook_name)
        self.choices = {'1': self.show_notes,
                        '3' : self.add_notes,
                        '4' : self.modify_notes,
                        '2' : self.search_notes,
                        '5' : self.quit}

    def display_menu(self):
        print(
            """
                Notebook Menu
                    1. Show all Notes
                    2. Search Notes
                    3. Add Note
                    4. Modify Note
                    5. Quit
             """)

    def show_notes(self, notes = None):
        if notes == None:
            notes = self.notebook.notes_lst

        for note in notes:
            print('memo:{}\n'
                  'tags:{}\n'
                  'date:{}\n'
                  '------'.format(note.memo, note.tags, note.time_of_creation))

    def add_notes(self):
        memo_inp = input('Write memo:')
        tag_inp = input('Add tags:')

        note_kwgs = dict(memo = memo_inp,
                         tag = tag_inp)

        self.notebook.add_note(**note_kwgs)

    def modify_notes(self):

        note_id = input('Provide note_id:')
        memo = input("Enter a memo: ")
        tag = input("Enter tags: ")

        if memo:
            modify = self.notebook.modify_note(note_id, memo)
            if modify == False:
                print('wtf is wrong with you')

        if tag:
            self.notebook.modify_tag(note_id, tag)

            self.show_notes()

    def search_notes(self):
        filter = input('Type which tag/keywords you are looking for:')
        notes = self.notebook.filter_notes(filter)
        self.show_notes(notes)


    def run(self):
        while True:
            self.display_menu()
            choice = input('Enter an option:')
            action = self.choices.get(choice)
            action()
            print('---------------')

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == '__main__':
    name = input('Name notebook:')
    Menu(name).run()
