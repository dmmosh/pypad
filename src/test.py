# solution is based on the example on https://pypi.org/project/pynput/, Global hotkeys

from pynput.keyboard import Controller, Listener, HotKey, Key

c = Controller()


def press_callback():
    try:
        c.release(Key.shift)  # update - undo the shift, otherwise all type will be Uppercase
        c.press(Key.backspace)  # update - Undo the K of the shift-k
        c.type("Kind regards ")
    except AttributeError:
        pass


def for_canonical(f):
    return lambda k: f(l.canonical(k))


hk = HotKey(HotKey.parse('<shift>+k'), on_activate=press_callback)

with Listener(on_press=for_canonical(hk.press), on_release=for_canonical(hk.release)) as l:
    l.join()
