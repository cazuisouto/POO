class Musica:
    def __init__(self, nome, artista, album):
        self.nome = nome
        self.artista = artista
        self.album = album
    
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    
    def set_artista(self, artista):
        self.artista = artista
    def get_artista(self):
        return self.artista
    
    def set_album(self, album):
        self.album = album
    def get_album(self):
        return self.album
    
    def __str__(self):
        return f" Nome: {self.nome}, Artista: {self.artista}, Album: {self.album}"

class PlayList:
    def __init__(self, nome, descrição):
        self.nome = nome
        self.descrição = descrição
        self.musicas = []
    
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    
    def set_descrição(self, descrição):
        self.descrição = descrição
    def get_descrição(self):
        return self.descrição
    
    def inserir_musica(self, musica):
        self.musicas.append(musica)
    
    def listar_musicas(self):
        for musica in self.musicas:
            print(musica)
    
    def __str__(self):
        return f" A quantidade de músicas na playlist é: {len(self.musicas)} \n"
    

musica1 = Musica("Shape of You", "Ed Sheeran", "Divide")
musica2 = Musica("Blinding Lights", "The Weeknd", "After Hours")
musica3 = Musica("Levitating", "Dua Lipa", "Future Nostalgia")

playlist = PlayList("Top Hits", "As melhores músicas do momento")
playlist.inserir_musica(musica1)
playlist.inserir_musica(musica2)
playlist.inserir_musica(musica3)

print(playlist)
playlist.listar_musicas()