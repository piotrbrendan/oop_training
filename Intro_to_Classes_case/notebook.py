import datetime

last_id = 0

class Note:

    def __init__(self, memo, tags='',**kwgs):
    '''note that memo and tags here are redundand at this moment, but I will leave them as they are
      available kwargs are memo and tags'''
        for key,val in kwgs.items():
            self.key = val


        global last_id
        last_id+=1
        self.id = last_id
        self.time_of_creation = datetime.datetime.today()

    def match(self,filter):

        return filter in self.memo or filter in self.tags



class Notebook:

    def __init__(self, name ):
        self.notes_lst =[]
        self.name = name

    def add_note(self, **kwgs) -> object:
        return self.notes_lst.append(Note(**kwgs))

    def _find_note(self,note_id):

        for note in self.notes_lst:
            if str(note.id) == str(note_id):
                return note

            return None

    def modify_note(self,note_id, new_memo):
        note = self._find_note(note_id)
        if note:
            note.memo=new_memo
            return True
        return False

    def modify_tag(self, note_id, new_tag):
        note = self._find_note(note_id)
        if note:
            note.tag = new_tag
            return True
        return False

    def filter_notes(self,filter):
        return [note for note in self.notes_lst if note.match(filter)]
