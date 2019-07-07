import ytp
ytp.load_api(keyboard, mouse, store, system, window, clipboard, highlevel, dialog, engine)

key = '0'

def main():
  ytp.numpad(key)

if ytp.is_numlock_on():
  keyboard.send_keys(key)
else:
  main()
