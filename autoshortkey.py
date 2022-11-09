from command import *

def on_activate_exit():
    print('exit')
    exit()

with keyboard.GlobalHotKeys({
        '<ctrl_l>+l': login_cisco,
        '<ctrl_l>+q': on_activate_exit}) as h:
    h.join()