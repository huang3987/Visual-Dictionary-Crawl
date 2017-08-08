import pykeyboard
import pymouse

Mouse = pymouse.PyMouse()

KB = pykeyboard.PyKeyboard()

def Paste():
    KB.press_key(KB.control_l_key)
    KB.press_key('v')
    KB.release_key('v')
    KB.release_key(KB.control_l_key)
