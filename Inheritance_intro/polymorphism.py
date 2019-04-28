class AudioFile:
    def __init__(self, name):
        if not name.endswith(self.ext): #polymorphism, because class AudioFile uses self.ext class variable that is not defined in AudioFile but in subclass
            raise Exception('Wrong file extention')

        self.name = name


class MP3File(AudioFile):

    ext = 'mp3'

    def play(self):
        print('Starting file {}'.format(self.name)) #polymorphism - uses self.name from parent class



