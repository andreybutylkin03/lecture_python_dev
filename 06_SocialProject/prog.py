import shlex
import cmd
import cowsay
import readline
import rlcompleter
import threading


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


if __name__ == "__main__":
    NCC().cmdloop()
