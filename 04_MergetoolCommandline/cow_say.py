import shlex
import cmd
import cowsay
import readline
import rlcompleter

if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")


class Cow(cmd.Cmd):
    prompt = '>> '

    eyes = ['==', 'XX', '$$', '@@', '**', '--', 'OO', '..']
    tongue = ['U ', ' U']

    def do_list_cows(self, args):
        """Lists all cow file names in the given directory"""
        print(*cowsay.list_cows())


    def do_make_bubble(self, args):
        """
        Wraps text is wrap_text is true, then pads text and sets inside a bubble.
        This is the text that appears above the cows
        """
        print(cowsay.make_bubble(args))


    def do_cowsay(self, args):
        """
        Similar to the cowsay command. Parameters are listed with their
        corresponding options in the cowsay command. Returns the resulting cowsay
        string

        :param message: The message to be displayed
        :param cow: -f – the available cows can be found by calling list_cows
        :param eyes: -e or eye_string
        :param tongue: -T or tongue_string
        """                
        cow = 'default'
        eyes = cowsay.Option.eyes
        tongue = cowsay.Option.tongue
        message = ''

        res = shlex.split(args, 0, 0)

        i = 0

        while i < len(res):
            match res[i]:
                case '-f':
                    cow = res[i + 1]
                    i += 1
                case '-e':
                    eyes = res[i + 1]
                    i += 1
                case '-T':
                    tongue = res[i + 1]
                    i += 1
                case _:
                    if message != '':
                        message += ' '

                    message += res[i]

            i += 1

        print(cowsay.cowsay(message, cow, eyes=eyes, tongue=tongue))

    def complete_cowsay(self, text, line, begidx, endidx):
        res = shlex.split(line[:begidx], 0, 0)

        if res[-1] == '-f':
            return [c for c in cowsay.list_cows() if c.startswith(text)]
        elif res[-1] == '-e':
            return [c for c in self.eyes if c.startswith(text)]
        elif res[-1] == '-T':
            return [c for c in self.tongue if c.startswith(text)]


    def do_cowthink(self, args):
        """
        Similar to the cowthink command. Parameters are listed with their
        corresponding options in the cowthink command. Returns the resulting
        cowthink string

        :param message: The message to be displayed
        :param cow: -f – the available cows can be found by calling list_cows
        :param eyes: -e or eye_string
        :param tongue: -T or tongue_string
        """
        cow = 'default'
        eyes = cowsay.Option.eyes
        tongue = cowsay.Option.tongue
        message = ''

        res = shlex.split(args, 0, 0)

        i = 0

        while i < len(res):
            match res[i]:
                case '-f':
                    cow = res[i + 1]
                    i += 1
                case '-e':
                    eyes = res[i + 1]
                    i += 1
                case '-T':
                    tongue = res[i + 1]
                    i += 1
                case _:
                    if message != '':
                        message += ' '

                    message += res[i]

            i += 1

        print(cowsay.cowthink(message, cow, eyes=eyes, tongue=tongue))


    def complete_cowthink(self, text, line, begidx, endidx):
        res = shlex.split(line[:begidx], 0, 0)

        if res[-1] == '-f':
            return [c for c in cowsay.list_cows() if c.startswith(text)]
        elif res[-1] == '-e':
            return [c for c in self.eyes if c.startswith(text)]
        elif res[-1] == '-T':
            return [c for c in self.tongue if c.startswith(text)]


    def do_EOF(self, args):
        return True


if __name__ == "__main__":
    Cow().cmdloop()
