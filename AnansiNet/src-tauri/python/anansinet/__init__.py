from anansinet.models.Host import Host
from anansinet.networking.utils import scan_connected_hosts

from anyio.from_thread import start_blocking_portal
from pytauri import (
    Commands,
    builder_factory,
    context_factory,
)

commands: Commands = Commands()

@commands.command()
async def get_hosts() -> list[Host]:
    return scan_connected_hosts()
    

# --8<-- [end:command]


def main() -> int:
    with start_blocking_portal("asyncio") as portal:  # or `trio`
        app = builder_factory().build(
            context=context_factory(),
            # 👇
            invoke_handler=commands.generate_handler(portal),
            # 👆
        )
        exit_code = app.run_return()
        return exit_code
