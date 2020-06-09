import asyncio
import gc
import objgraph
import socket
import websockets

from asyncio.exceptions import CancelledError

sem = asyncio.Semaphore(20)


async def create():
    print(f"Create WS", flush=True)
    uri = "wss://echo.websocket.org"
    try:
        async with websockets.connect(uri) as ws:
            reader_task = asyncio.ensure_future(reader(ws))
            writer_task = asyncio.ensure_future(writer(ws))
            await asyncio.wait(
                [reader_task, writer_task], return_when=asyncio.FIRST_COMPLETED,
            )

            for task in (reader_task, writer_task):
                if not task.done():
                    task.cancel()
                try:
                    await task
                except CancelledError:
                    pass
                except websockets.exceptions.ConnectionClosedError as e:
                    pass
    except socket.gaierror:
        pass

    sem.release()


async def reader(ws):
    while True:
        r = await ws.recv()


async def writer(ws):
    while True:
        await ws.send("hello")
        await asyncio.sleep(2)


async def start_connections():
    while True:
        await sem.acquire()
        asyncio.ensure_future(create())


async def run():
    asyncio.ensure_future(start_connections())

    while True:
        gc.collect()
        print("\n\nDone tasks are: ", flush=True)
        for t in asyncio.Task.all_tasks():
            if t.done():
                print(f"  - {t}", flush=True)

        # print(f"Total: {len(gc.get_objects())}")
        # print("New objects are:")
        # objgraph.show_growth(shortnames=False)
        await asyncio.sleep(10)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


if __name__ == "__main__":
    main()
