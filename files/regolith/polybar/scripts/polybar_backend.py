#!/usr/bin/env python3
import asyncio
import os

from aiorun import run


async def setup():
    # Setup delegate
    print(os.getpid())
    await setup_unix_server()


async def setup_unix_server():
    server = await asyncio.start_unix_server(task_client_connected, path='/tmp/polybar_backend.sock')
    try:
        # Run until cancelled.
        while True:
            await asyncio.sleep(60)
    except asyncio.CancelledError:
        await shutdown_unix_server(server)


async def shutdown_unix_server(server):
    server.close()
    await server.wait_closed()


async def task_client_connected(reader, writer):
    data = await reader.readline()
    message = data.decode().strip()
    print(f'Received {message}')
    print("Closed the client socket")
    writer.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run(setup())