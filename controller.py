from math import log2

from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNMax(self):
        return self._model.numero_massimo

    def getTMax(self):
        return self._model.tentativi_massimi

    def reset(self, e):
        self._model.reset()
        self._view._txtOutT.value = self._model.tentativi_rimasti
        self._view._lv.controls.clear()
        self._view._btnPlay.disabled = False
        self._view._txtIn.disabled = False
        self._view._lv.controls.append(ft.Text("Indovina a quale numero sto pensando...!"))
        self._view.update()

    def play(self, e):
        tentativoStr = self._view._txtIn.value
        self._view._txtIn.value = ""
        self._view._txtOutT.value = self._model.tentativi_rimasti - 1
        if tentativoStr == "":
            self._view._lv.controls.append(ft.Text("Attenzione! Inserisci un valore numerico da testare.",
                                                   color="red"))
            self._view.update()
            return
        try:
            tentativoInt = int(tentativoStr)
        except ValueError:
            self._view._lv.controls.append(ft.Text("Attenzione: il valore inserito non è un intero!",
                                                   color="red"))
            self._view.update()
            return
        risultato = self._model.play(tentativoInt)
        if risultato == 0:
            self._view._lv.controls.append(ft.Text(f"Fantastico... hai vinto! Il numero segreto era {tentativoInt}.",
                                           color="green"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif risultato == 2:
            self._view._lv.controls.append(ft.Text(f"Peccato... hai finito le vite. Il numero segreto era {self._model.numero_segreto}.",
                                           color="blue"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return

        elif risultato == -1:
            self._view._lv.controls.append(ft.Text(f"Il numero segreto è più piccolo di {tentativoInt}"))
            self._view.update()
        else:
            self._view._lv.controls.append(ft.Text(f"Il numero segreto è più grande di {tentativoInt}"))
            self._view.update()