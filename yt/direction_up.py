import ytp
ytp.load_api(keyboard, mouse, store, system, window, clipboard, highlevel, dialog, engine)

key = '='

def main():
  ytp.move(key, 'up')

if ytp.is_numlock_on():
  keyboard.send_key(key)
else:
  main()
