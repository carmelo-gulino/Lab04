import flet as ft
from time import sleep

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        #Row1
        self._lang = ft.Dropdown(label="Select language", width=450, on_change=self.__controller.selectLanguage)
        self.fillLang()
        row1 = ft.Row([self._lang])

        #Row2
        self._searchType = ft.Dropdown(label="Search type", width=150, on_change=self.__controller.selectType)
        self.fillSearch()
        self._txtIn = ft.TextField(label="Add your sentence here", width=750)
        self._SpChBtn = ft.ElevatedButton(text="Spell Check", on_click=self.__controller.handleSpellCheck)
        row2 = ft.Row([self._searchType, self._txtIn, self._SpChBtn])

        self.page.add(row1, row2)
        self.page.update()

    def fillLang(self):
        langs = ["italian", "english", "spanish"]
        for lang in langs:
            self._lang.options.append(ft.dropdown.Option(lang))
        return self._lang

    def fillSearch(self):
        types = ["Default", "Linear", "Dichotomic"]
        for type in types:
            self._searchType.options.append(ft.dropdown.Option(type))
        return self._searchType

    def confirmLang(self):
        self._msg = ft.ListView()
        self._msg.controls.append(ft.Text("Language confirmed", color="blue"))
        self.page.add(self._msg)
        self.page.update()
        self.sleep()

    def confirmType(self):
        self._msg = ft.ListView()
        self._msg.controls.append(ft.Text("Search type confirmed", color="blue"))
        self.page.add(self._msg)
        self.page.update()
        self.sleep()

    def handleMissingFields(self):
        self._errorMsg = ft.ListView()
        self._errorMsg.controls.append(ft.Text("All the fields are required", color="red", size=20))
        self.page.add(self._errorMsg)
        self.page.update()
        self.sleep()

    def sleep(self):
        sleep(0.5)
        self.page.add()
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def cleanFields(self):
        self._searchType.value = None
        self._lang.value = None
        self._txtIn.value = None
        self.update()

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    def printWrong(self, txt, output):
        self._msg = ft.ListView()
        self._msg.controls.append(ft.Text(f"Frase inserita: {txt}\n"
                                          f"Parole errate: - {output[0]}\n"
                                          f"Tempo richiesto dalla ricerca: {output[1]}"))
        self.page.add(self._msg)
        self.page.update()