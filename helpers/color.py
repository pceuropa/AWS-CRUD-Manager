import os

ATTRIBUTES = {'bold': 1, 'dark': 2, 'underline': 4, 'blink': 5, 'reverse': 7, 'concealed': 8}
COLORS = {'grey': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37}
HIGHLIGHTS = {'on_grey': 40, 'on_red': 41, 'on_green': 42, 'on_yellow': 43, 'on_blue': 44, 'on_magenta': 45, 'on_cyan': 46, 'on_white': 47}
END = '\033[0m'


def colored(text, color=None, on_color=None, attrs=None):
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        s = '\033[%dm%s'
        if color is not None:
            text = s % (COLORS[color], text)

        if on_color is not None:
            text = s % (HIGHLIGHTS[on_color], text)

        if attrs is not None:
            for attr in attrs:
                text = s % (ATTRIBUTES[attr], text)

        text += END
    return text


def yel(string, activate=True):
    if activate:
        return colored(string, 'yellow')

    return str(string)


def gre(string):
    return colored(string, 'green')


def red(string, activate=True):
    if activate:
        return colored(string, 'red')

    return str(string)


def cyan(string):
    return colored(string, 'cyan')


def grey(string):
    return colored(string, 'grey')


def magenta(string):
    return colored(string, 'magenta')


def alert(string, negative=True):
    if negative:
        return colored(str(string), 'green' if string else 'red')
    return colored(str(string), 'red' if string else 'green')


''' √ ■ ▲▼ ☺☻♥♦
♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂Çüéâäà
åçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒáíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·ⁿ²■ '''
