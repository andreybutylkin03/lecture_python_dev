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

    def do_list_cows(self, args):
        """Lists all cow file names in the given directory"""
        pass

    def complete_list_cows(self, text, line, begidx, endidx):
        pass

    def do_make_bubble(self, args):
        """
        Wraps text is wrap_text is true, then pads text and sets inside a bubble.
        This is the text that appears above the cows
        """
        pass

    def complete_make_bubble(self, text, line, begidx, endidx):
        pass

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
        pass

    def complete_cowsay(self, text, line, begidx, endidx):
        pass

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
        pass

    def complete_cowthink(self, text, line, begidx, endidx):
        pass

    def do_EOF(self, args):
        return True


if __name__ == "__main__":
    Cow().cmdloop()
