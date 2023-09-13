import asyncio

from file_utils.xml_to_csv import XlsxToCsvConverter


class XlsxToCsvService:
    def __init__(self):
        self.is_running = False
        self.console = ""
        self.folder_path = ""
        self.file_name = ""
        self.xml_names = []


    def start_task(self):
        self.is_running = True
        asyncio.run(self.run_task())

    def stop_task(self):
        self.is_running = False

    async def main_func(self):
        if self.is_running:
            converter = XlsxToCsvConverter()
            converter.make_xlsx(self.folder_path, self.file_name, self.xml_names)
            self.is_running = False

    async def run_task(self):
        tasks = [self.main_func()]
        await asyncio.gather(*tasks)
