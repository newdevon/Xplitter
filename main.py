import os
from splitCheck import splitCheck
import os

def set_shorter_esc_delay_in_os():
    os.environ.setdefault('ESCDELAY', '2500')

if __name__ == "__main__":
    set_shorter_esc_delay_in_os()
    splitCheck()