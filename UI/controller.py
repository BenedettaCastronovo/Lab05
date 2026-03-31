import flet as ft
from networkx.classes import non_edges


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._corsi = None
        self._mappa_corsi = {}
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._nome = None
        self._cognome = None


    def fillcorsi(self):
        for c in self._model.getAllCorsi():
            self._mappa_corsi[c.codins] = c
            self._view._corsi.options.append(ft.dropdown.Option(
                key = c.codins,
                text = str(c)
                #on_select = self._choiceDDCodins
            ) )
        self._view.update_page()

    def _choiceDDCodins(self, e):
        # Cerchiamo l'opzione che ha la chiave uguale a quella selezionata
        codice_selezionato = self._view._corsi.value
        if self._view._corsi.value is None:
            self._corsiValue = None
            return
        if codice_selezionato in self._mappa_corsi:
            self._corsiValue = self._mappa_corsi[codice_selezionato]
            print(f"Corso recuperato: {self._corsiValue.nome}")


    def cercaIscritti(self,e):
        if self._corsiValue is None:
            self._view.create_alert("Per favore, seleziona un corso dal menu!")
            return
        iscritti = self._model.getIscrittiCorso(self._corsiValue)
        self._view.txt_result.controls.clear()
        if not iscritti:
            self._view.txt_result.controls.append(ft.Text("Non ci sono iscritti a questo corso."))
        else:
            self._view.txt_result.controls.append(ft.Text(f" ci sono {len(iscritti)} iscritti al corso"))
            for s in iscritti:
                self._view.txt_result.controls.append(ft.Text(s))

        self._view.update_page()

    def cercaStudente(self, e):
        self._matr = self._view._matricola.value.strip()
        if self._matr is None:
            self._view.create_alert("Inserisci matricola")
            return

        self._nome, self._cognome = self._model.cercaStudente(self._matr)

        if self._nome is None or self._cognome is None:
            self._view.create_alert("non trovata")
            self._view._nome.value = ""
            self._view._cognome.value = ""
        else:
            self._view._nome.value = self._nome
            self._view._cognome.value = self._cognome

        self._view.update_page()

        #self.set_nome(self._nome)
        #self.set_cognome(self._cognome)

    def cercaCorso(self, e):
        self._matr = self._view._matricola.value.strip()
        if self._matr is None:
            self._view.create_alert("Inserisci matricola valida")
            return
        self._corsi = self._model.getCorso(self._matr)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Risultano {len(self._corsi)} corsi"))
        for s in self._corsi:
            self._view.txt_result.controls.append(ft.Text(s))
        self._view.update_page()

    def iscrivi(self, e):
        matr = self._view._matricola.value.strip()
        corso = self._corsiValue
        self._model.iscrivi(matr, corso)
        self._view.txt_result.controls.append(ft.Text(f"studente {matr} iscritto al corso {corso.codins}"))
        self._view.update_page()
