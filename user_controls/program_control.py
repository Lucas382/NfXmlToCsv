import os
import flet as ft

from protocols.xlsx_to_csv_protocol import RunServiceProtocol
from services.timer_service import Count
from user_controls.program_console import ProgramConsole


text_field_label = "CSV file name"


def verify_file_xlsx(directory_path):
    try:
        files = os.listdir(directory_path)
    except FileNotFoundError:
        return []
    except PermissionError:
        return []
    return [file for file in files if file.endswith('.xml')]


class ProgramController(ft.UserControl):
    def __init__(self, controller: RunServiceProtocol):
        super().__init__()
        self.run_controller = controller

    def save(self, name, directory_path):
        dic = verify_file_xlsx(directory_path)
        if not directory_path:
            self.console.update_console("No XML directory specified.")
            self.console.set_console_color("red")

        elif not dic:
            self.console.update_console("No XML file in the selected folder.")
            self.console.set_console_color("red")

        else:
            self.running_timer.start_count()
            self.run_controller.folder_path = directory_path
            self.run_controller.file_name = name
            self.run_controller.xml_names = dic
            self.console.set_console_color("cyan")
            self.console.update_console("Conversion started, please wait...")
            self.run_controller.start_task()
            self.running_timer.stop_counter()
            self.console.set_console_color("green")
            self.console.update_console("XLSX successfully converted!")

    def build(self):
        self.running_timer = Count()
        self.console = ProgramConsole()
        self.file_name = ft.TextField(label=text_field_label)

        return ft.Column(
            [
                ft.Divider(),
                self.console,
                self.running_timer,
                ft.Divider()
            ],
            expand=True,
        )
