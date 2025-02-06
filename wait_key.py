import os
import sys


class Key(object):
    left = 'left'
    right = 'right'
    down = 'down'
    up = 'up'
    enter = 'enter'
    close = 'close'
    back = 'backspace'
    delete = 'delete'
    home = 'home'
    end = 'end'

    edit = [back, delete, home, end, enter, close, left, right]

    @staticmethod
    def control(key):
        return key in [Key.left, Key.right, Key.down, Key.up, Key.enter, Key.close]

    @staticmethod
    def number(key):
        return key in [str(i) for i in range(10)] + ['.'] + Key.edit

    @staticmethod
    def chars(key):
        return ord(key) > 31 or key in Key.edit

    @staticmethod
    def wait(check=control):
        # key = None
        # while key is None:
        key = Key._wait()
        if not check(key):
            key = None
        return key

    @staticmethod
    def _wait():
        """ Wait for a key press on the console and return it. """
        result = None
        if os.name == 'nt':
            import msvcrt
            key = msvcrt.getch()
            code = ord(key)
            print(code)
            if code == 13:
                result = Key.enter
            elif code == 3:
                result = Key.close
            elif code == 8:
                result = Key.back
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
                elif code == 83:
                    result = Key.delete
                elif code == 71:
                    result = Key.home
                elif code == 79:
                    result = Key.end
            elif code > 31:
                result = key

        else:
            import termios
            fd = sys.stdin.fileno()

            old_term = termios.tcgetattr(fd)
            new_attr = termios.tcgetattr(fd)
            new_attr[3] = new_attr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, new_attr)

            try:
                key = sys.stdin.read(1)
                code = ord(key)
                print('code1', code)
                if code == 10:
                    result = Key.enter
                elif code == 127:
                    result = Key.back
                elif code == 27:
                    code = ord(sys.stdin.read(2)[1])
                    print('code2', code)
                    if code == 65:
                        result = Key.up
                    elif code == 51:
                        result = Key.delete
                    elif code == 66:
                        result = Key.down
                    elif code == 68:
                        result = Key.left
                    elif code == 67:
                        result = Key.right
                    elif code == 72:
                        result = Key.home
                    elif code == 70:
                        result = Key.end
                elif code > 31:
                    result = key
            except IOError:
                pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

        return result


if __name__ == '__main__':
    key = Key.wait(Key.control)
    print('выход', key)
    key2 = Key.wait(Key.number)
    print('выход', key2)
