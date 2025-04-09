import random

class Model(object):
    def __init__(self):
        self._numero_massimo = 100
        self._tentativi_massimi = 6
        self._tentativi_rimasti = self._tentativi_massimi
        self._numero_segreto = None

    def reset(self):
        # questo metodo resetta il gioco per iniziare una nuova partita
        self._numero_segreto = random.randint(0, self._numero_massimo)
        self._tentativi_rimasti = self._tentativi_massimi

    def play(self, tentativo):
        """
        gestisce le dinamiche del gioco
        :param tentativo: int
        :return: 0 se si ha vinto, -1 se il numero segreto è più piccolo del tentativo, 1 se il numero segreto è più
        grande del tentativo, 2 se si ha perso (perché le "vite" sono finite)
        """
        # questo metodo gestisce la dinamica di gioco confrontando il numero inserito dall'utente con il numero segreto
        # scelto, randomicamente, dal server
        self._tentativi_rimasti = self._tentativi_rimasti - 1
        if tentativo == self._numero_segreto:
            return 0 # lo zero indica la vittoria
        if self._tentativi_rimasti == 0:
            return 2 # il due indica che la partita è stata persa definitivamente in quanto sono terminate le "vite"
        if tentativo > self._numero_segreto:
            return -1 # il -1 indica che il numero segreto è più piccolo del tentativo inserito dall'utente
        return 1


if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(50))
    print(m.play(10))

# E' sempre una buona prassi testare il modello senza l'interfaccia grafica!