import asyncio
from cowsay import cowsay, list_cows


clients = {}
cowss = set(list_cows())


async def chat(reader, writer):
    me = None
    flag = True

    send = asyncio.create_task(reader.readline())
    receive = None

    while flag and not reader.at_eof():
        if me is None:
            done, pending = await asyncio.wait([send], return_when=asyncio.FIRST_COMPLETED)
        else:
            done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)

        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                
                text = q.result().decode().strip()

                match text.split():
                    case ['who']:
                        for who in clients.keys():
                            writer.write(who.encode() + b'\n')
                            await writer.drain()
                    case ['cows']:
                        for cow in cowss:
                            writer.write(cow.encode() + b'\n')
                            await writer.drain()
                    case ['login', a] if a in cowss:
                        pass
                    case ['say', cow, *hello] if me is not None and cow in clients.keys():
                        pass
                    case ['yield', *hello] if me is not None:
                        pass
                    case ['quit']:
                        send.cancel()
                        if receive is not None:
                            receive.cancel()

                        writer.close()
                        await writer.wait_closed()
                        
                        if me is not None:
                            del clients[me]
                    case _:
                        writer.write(b'unknown\n')
                        await writer.drain()

            elif q is receive:
                pass


async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())
