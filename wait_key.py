import os
import sys


class Key(object):
    left = 'left'
    right = 'right'
    down = 'down'
    up = 'up'
    enter = 'enter'
    close = 'close'

    @staticmethod
    def wait():
        key = None
        while key is None:
            key = Key._wait()
        return key

    @staticmethod
    def _wait():
        """ Wait for a key press on the console and return it. """
        result = None
        if os.name == 'nt':
            import msvcrt
            code = ord(msvcrt.getch())
            print(code)
            if code == 13:
                result = Key.enter
            elif code == 3:
                result = Key.close
            elif code == 0 or 0xe0 or 3:
                code = ord(msvcrt.getch())
                print(code)
                if code == 72:
                    result = Key.up
                elif code == 80:
                    result = Key.down
                elif code == 75:
                    result = Key.left
                elif code == 77:
                    result = Key.right

        else:
            import termios
            fd = sys.stdin.fileno()

            old_term = termios.tcgetattr(fd)
            new_attr = termios.tcgetattr(fd)
            new_attr[3] = new_attr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, new_attr)

            try:
                code = ord(sys.stdin.read(1))

                if code == 10:
                    result = Key.enter
                if code == 27:
                    code = ord(sys.stdin.read(2)[1])
                    print(code)
                    if code == 65:
                        result = Key.up
                    elif code == 66:
                        result = Key.down
                    elif code == 68:
                        result = Key.left
                    elif code == 67:
                        result = Key.right
            except IOError:
                pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

        return result


if __name__ == '__main__':
    key = Key.wait()
    print(key)
