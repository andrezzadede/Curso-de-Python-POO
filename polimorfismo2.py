# Segunda parte poliformismo 

class AudioFile:
    def __init__(self, filename):
        
        if not filename.endswith(self.ext): # Caso eu nao encontre a extensão
            raise Exception('Formato invalido')

        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print('Tocando arquivo mp3')

class WavFile(AudioFile):
    ext = 'wav'
    def play(self):
        print('Tocando arquivo wav')

class OggFile(AudioFile):
    ext = 'ogg'
    def play(self):
        print('Tocando arquivo OGG')


mp3 = MP3File('musica.mp3')
mp3.play()
ogg = OggFile('musica.ogg')
ogg.play()

