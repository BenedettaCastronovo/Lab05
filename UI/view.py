from cProfile import label

import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None
        self._page.scroll = ft.ScrollMode.ADAPTIVE  # Oppure ft.ScrollMode.AUTO

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)


        self._corsi = ft.Dropdown(
            label="corso",
            width=500,
            on_change=self._controller._choiceDDCodins
        )
        self._controller.fillcorsi()

        #ROW with some controls
        # text field for the name

        # button for the "hello" reply
        self.btncercaIscr = ft.ElevatedButton(text="cerca iscritti", on_click=self._controller.cercaIscritti)
        row1 = ft.Row([self._corsi, self.btncercaIscr],)
        self._page.controls.append(row1)

        self._matricola = ft.TextField(
            label="matricola",
            width=200
        )

        self._nome = ft.TextField(label="Nome", read_only= True)
        self._cognome = ft.TextField(label="Cognome", read_only= True)

        row2 = ft.Row([self._matricola, self._nome, self._cognome],)
        self._page.controls.append(row2)

        self._btnStud = ft.ElevatedButton(text="cerca studente",
                                          width=200,
                                          on_click=self._controller.cercaStudente)

        self._btnCorsi = ft.ElevatedButton(text="cerca corso",
                                           width=200,
                                           on_click=self._controller.cercaCorso)

        self._btnIscrivi = ft.ElevatedButton(text="iscrivi",
                                             width=200,
                                             on_click=self._controller.iscrivi)

        row3 = ft.Row([self._btnStud, self._btnCorsi, self._btnIscrivi],)
        self._page.controls.append(row3)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
