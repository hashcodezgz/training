"""A simple Shell module for manipulating stings."""

from cmd import Cmd

class ListShell(Cmd):
    """A simple Shell class for manipulating lists."""

    list = [1, 2, 3]

    def do_print(self, text):
        """Print the list."""
        args = text.split()
        if not args:
            print(self.list, sep=', ')
        else:
            print('Error: print does not support parameters.')

    def do_append(self, text):
        """Append an integer to the list."""
        args = text.split()
        if len(args) == 1:
            try:
                self.list.append(int(args[0]))
                print(self.list, sep=', ')
            except ValueError:
                print('Error: invalid literal.')
        else:
            print('Error: append takes only one parameter.')

    def do_insert(self, text):
        """Insert in a position of the list an integer."""
        args = text.split()
        if len(args) == 2:
            try:
                pos = int(args[0])
                value = int(args[1])
                self.list.insert(pos, value)
                print(self.list, sep=', ')
            except ValueError:
                print('Error: invalid literal.')
            except IndexError:
                print('Error: invalid position.')
        else:
            print('Error: insert takes two parameters.')

    def do_remove(self, text):
        """Remove an element from the list."""
        args = text.split()
        if len(args) == 1:
            try:
                val = int(args[0])
                self.list.remove(val)
                print(self.list, sep=', ')
            except ValueError:
                print('Error: invalid literal or not found.')
        else:
            print('Error: insert takes two parameters.')

    def do_pop(self, text):
        """Remove the last element from the list."""
        args = text.split()
        if not args:
            try:
                self.list.pop()
                print(self.list, sep=', ')
            except IndexError:
                print('Error: the list is empty.')
        else:
            print('Error: pop does not support parameters.')

    def do_reverse(self, text):
        """Reverse the list."""
        args = text.split()
        if not args:
            self.list.reverse()
            print(self.list, sep=', ')
        else:
            print('Error: reverse does not support parameters.')

    def do_sort(self, text):
        """Reverse the list."""
        args = text.split()
        if not args:
            self.list.sort()
            print(self.list, sep=', ')
        else:
            print('Error: sort does not support parameters.')

    def do_quit(self, unused_text):
        """Quits the program."""
        print('Quitting.')
        raise SystemExit


if __name__ == '__main__':
    PROMPT = ListShell()
    PROMPT.prompt = '> '
    PROMPT.cmdloop('Starting prompt...')
