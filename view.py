import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2025 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text(value="Indovina il numero",
                               color="blue",
                               size=24)
        self._txtOutNMax = ft.TextField(label="Numero massimo",
                                        disabled=True,
                                        width=200,
                                        value=self._controller.getNMax())
        self._txtOutTMax = ft.TextField(label="Tentativi massimi",
                                        disabled=True,
                                        width=200,
                                        value=self._controller.getTMax())
        self._txtOutT = ft.TextField(label="Tentativi rimanenti",
                                     disabled=True,
                                     width=200)
        self._txtIn = ft.TextField(label="Valore",
                                   width=200,
                                   disabled=True)
        self._btnReset = ft.ElevatedButton(text="Nuova partita",
                                           width=200,
                                           on_click=self._controller.reset) # non vengono messe le parentesi perché non
                                                                            # si vuole eseguire il metodo, ma si vuole
                                                                            # chiamare il metodo --> non si vuole la
                                                                            # sua return
        self._btnPlay = ft.ElevatedButton(text="Gioca",
                                          width=200,
                                          disabled=True,
                                          on_click=self._controller.play)
        self._lv = ft.ListView(expand=True) # expand=True permette di scrollare la finestra
        row_01 = ft.Container(self._titolo,
                              alignment=ft.alignment.center) # l'allignamento avviene in maniera diversa rispetto alla
                                                             # riga
        row_02 = ft.Row([self._txtOutNMax, self._txtOutTMax, self._txtOutT],
                        alignment=ft.MainAxisAlignment.CENTER)
        row_03 = ft.Row([self._btnReset, self._txtIn, self._btnPlay],
                        alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row_01, row_02, row_03, self._lv)
        self._page.update()

    def setController(self,controller):
        self._controller = controller

    def update(self):
        self._page.update()