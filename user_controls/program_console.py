import flet as ft


class ProgramConsole(ft.UserControl):
    def build(self):
        self.console = ft.TextField(value="No conversion started...", text_align=ft.TextAlign.LEFT, disabled=True, color="white", label="Console")
        return self.console

    def update_console(self, value):
        self.console.value = value
        self.update()

    def set_console_color(self, color):
        self.console.color = color
        self.update()