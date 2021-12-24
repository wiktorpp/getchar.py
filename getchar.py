import sys
import tty
import termios

def getchar():
    tattr = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno(), termios.TCSANOW)
    out = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSANOW, tattr)
    return out
