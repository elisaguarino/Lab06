import flet as ft
from UI.view import View
from model.model import Autonoleggio
from UI.alert import AlertManager
'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio,alert_manager: AlertManager):
        self._model = model
        self._view = view

        self._alert_manager = alert_manager

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        if not self._model.responsabile:
            self._alert_manager.show_alert("Il campo responsabile non può essere vuoto.")
            return
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra(self,e):
        automobile=self._model.get_automobili()
        for auto in automobile:
            cod=auto[0]
            marca=auto[1]
            modello=auto[2]
            anno=auto[3]
            posti=auto[4]
            if auto[5] == 0:
                disponibile="disponibile"
            else:
                disponibile="non disponibile"
            self._view.lista_auto.controls.append(ft.Text(f"{cod}  |  {marca}  |  {modello}  |  {anno}  |  {disponibile}"))
        print(self._view.lista_auto)
        self._view.update()

    def cerca(self,e):
        self._view.lista_auto_ricerca.controls.clear()
        risultati=[]
        cercata=self._view.input_modello_auto.value
        if not cercata:
            self._alert_manager.show_alert("Inserisci un modello da cercare.")
            self._view.update()
            return

        automobile = self._model.get_automobili()
        for auto in automobile:
            if auto[2] == cercata:
                cod = auto[0]
                marca = auto[1]
                modello = auto[2]
                anno = auto[3]
                posti = auto[4]
                if auto[5] == 0:
                    disponibile = "disponibile"
                else:
                    disponibile = "non disponibile"
                self._view.lista_auto_ricerca.controls.append(ft.Text(f"{cod}  |  {marca}  |  {modello}  |  {anno}  | {posti}  |  {disponibile}"))
                risultati.append(auto)
            if not risultati:
                self._alert_manager.show_alert(f"Nessun veicolo trovato per il modello '{cercata}'.")

        self._view.update()




