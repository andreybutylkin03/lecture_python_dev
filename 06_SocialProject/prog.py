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


class NCC(cmd.Cmd):
    prompt = ">> "

    def do_who(self, args):
        pass


    def do_cows(self, args):
        pass


    def do_login(self, args):
        pass


    def do_say(self, args):
        pass


    def do_yield(self, args):
        pass


    def do_quit(self, args):
        pass


    def complete_login(self, text, line, begidx, endidx):
        pass


    def complete_say(self, text, line, begidx, endidx):
        pass


    def do_EOF(self, args):
        print()
        return True


def serv(cmdl):
    host = "localhost" 
    port = 1337
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while msg := s.recv(1024).rstrip().decode():
            print(f"\n{msg}\n{cmdl.prompt}{readline.get_line_buffer()}", end='', flush=True)
            
if __name__ == "__main__":
    cmdl = NCC()
    serv_talk = threading.Thread(target=serv, args=(cmdl, ))
    serv_talk.start()
    cmdl.cmdloop()
