import asyncio
from cowsay import cowsay, list_cows


clients = {}
cowss = set(list_cows())


async def chat(reader, writer):
    global cowss
    global clients
    me = None
    flag = True

    while flag and (q := await reader.readline()):
        text = q.decode().strip()

        match text.split():
            case ['who']:
                writer.write(f"{list(clients.keys())}".encode() + b'\n')
                await writer.drain()

            case ['cows']:
                writer.write(f"{list(cowss)}".encode() + b'\n')
                await writer.drain()

            case ['login', a] if a in cowss:
                me = a
                clients[me] = asyncio.Queue()
                writer.write(b'login\n')
                await writer.drain()

                cowss -= {a}
                break

            case ['quit']:
                flag = False
                writer.close()
                await writer.wait_closed()
            case _:
                writer.write(b'unknown\n')
                await writer.drain()

    if flag:
        send = asyncio.create_task(reader.readline())
        receive = asyncio.create_task(clients[me].get())   

    while flag and not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)

        for q in done:
            if q is send:
                text = q.result().decode().strip()

                match text.split():
                    case ['who']:
                        writer.write(f"{list(clients.keys())}".encode() + b'\n')
                        await writer.drain()

                    case ['cows']:
                        writer.write(f"{list(cowss)}".encode() + b'\n')
                        await writer.drain()

                    case ['say', cow, *hello] if me is not None and cow in clients.keys() and cow != me:
                        await clients[cow].put(cowsay(' '.join(hello), me))

                    case ['yield', *hello] if me is not None:
                        for out in clients.values():
                            if out is not clients[me]:
                                await out.put(cowsay(' '.join(hello), me))

                    case ['quit']:
                        flag = False
                        send.cancel()
                        if receive is not None:
                            receive.cancel()

                        writer.close()
                        await writer.wait_closed()
                        
                        del clients[me]
                    case _:
                        writer.write(b'unknown\n')
                        await writer.drain()

                send = asyncio.create_task(reader.readline())

            elif q is receive:
                receive = asyncio.create_task(clients[me].get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()


async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())
