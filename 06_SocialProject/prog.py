import shlex
import cmd
import cowsay
import readline
import rlcompleter
import threading
import socket


if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

host = "localhost"
port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
event = threading.Event()
event.set()


def serv(cmdl, event):
    try:
        while msg := s.recv(1024).rstrip().decode():
            if event.is_set():
                print(f"\n{msg}\n{cmdl.prompt}{readline.get_line_buffer()}", end='', flush=True)
            else:
                print(msg, flush=True)
                event.set()
    except Exception as ex:
        pass


class NCC(cmd.Cmd):
    prompt = ">> "

    def do_who(self, args):
        event.clear()
        s.sendall("who\n".encode())
        event.wait()


    def do_cows(self, args):
        event.clear()
        s.sendall("cows\n".encode())
        event.wait()


    def do_login(self, args):
        event.clear()
        s.sendall(f"login {args}\n".encode())
        event.wait()


    def do_say(self, args):
        s.sendall(f"say {args}\n".encode())


    def do_yield(self, args):
        s.sendall(f"yield {args}\n".encode())


    def do_quit(self, args):
        s.sendall(f"quit\n".encode())


    def complete_login(self, text, line, begidx, endidx):
        pass


    def complete_say(self, text, line, begidx, endidx):
        pass


    def do_EOF(self, args):
        print()
        return True

            
if __name__ == "__main__":
    cmdl = NCC()
    serv_talk = threading.Thread(target=serv, args=(cmdl, event))
    serv_talk.start()
    cmdl.cmdloop()
    s.close()
