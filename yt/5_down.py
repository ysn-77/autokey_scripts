import ytp
ytp.load_api(keyboard, mouse, store, system, window, clipboard, highlevel, dialog, engine)

key = '5'

def main():
  ytp.numpad(key)

if ytp.is_numlock_on():
  keyboard.send_key(key)
else:
  main()
