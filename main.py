import flet as ft

from file_utils.json_utils import save_file_data, is_file_exists, get_file_data
from user_controls.program_control import ProgramController
from protocols.xlsx_to_csv_protocol import RunServiceProtocol
from services.xlsx_to_csv_service import XlsxToCsvService


def main(page: ft.Page):
    page.title = "App Controller"
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    run_controller: RunServiceProtocol = XlsxToCsvService()
    controller = ProgramController(run_controller)

    def save_file_result(e: ft.FilePickerResultEvent):
        save_file_path = e.path if e.path else ""
        if save_file_path:
            controller.save(save_file_path, directory_path.value)

    save_file_dialog = ft.FilePicker(on_result=save_file_result)
    directory_path = ft.Text()

    def get_directory_result(e: ft.FilePickerResultEvent):
        directory_path.value = e.path if e.path else ""
        if directory_path.value:
            save_file_data("dir_path", directory_path.value, "configs", "dir_path")
            directory_path.update()

    get_directory_dialog = ft.FilePicker(on_result=get_directory_result)

    page.overlay.extend([get_directory_dialog, save_file_dialog])

    if is_file_exists("configs", "dir_path"):
        data = get_file_data(folder="configs", file_name="dir_path")
        if data and "dir_path" in data:
            directory_path.value = data["dir_path"]

    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                [
                    ft.Container(
                        margin=ft.margin.Margin(0, 10, 0, 0),
                        alignment=ft.alignment.bottom_center,
                        content=ft.ElevatedButton(
                            "Select a XML files directory",
                            bgcolor="#494b4f",
                            height=45,
                            width=280,
                            icon=ft.icons.FOLDER_OPEN,
                            on_click=lambda _: get_directory_dialog.get_directory_path(dialog_title="XML Folder files"),
                            disabled=page.web,
                        ),
                    ),
                    ft.Container(
                        margin=ft.margin.Margin(0, 0, 0, 10),
                        alignment=ft.alignment.top_center,
                        content=directory_path,
                    ),
                ]
            )
        ),
        ft.Container(
            alignment=ft.alignment.center,
            padding=10,
            content=ft.ElevatedButton(
                        "Save CSV",
                        bgcolor="#494b4f",
                        height=45,
                        width=280,
                        icon=ft.icons.SAVE,
                        on_click=lambda _: save_file_dialog.save_file(dialog_title="Save XLSX File"),
                        disabled=page.web,
            ),
        )
    )

    page.add(controller)


ft.app(target=main)
