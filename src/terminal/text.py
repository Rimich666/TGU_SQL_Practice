class Text(object):
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    default = "\033[39m" + "\033[22m"
    bold = "\033[1m"
    thin = "\033[22m"
    head = yellow + bold
    line = white + bold
    title = green + bold
