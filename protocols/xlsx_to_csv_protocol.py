from typing import Protocol


class RunServiceProtocol(Protocol):
    def start_task(self):
        ...

    def stop_task(self):
        ...

    async def main_func(self):
        ...

    async def run_task(self):
        ...
