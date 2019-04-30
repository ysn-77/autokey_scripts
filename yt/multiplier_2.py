import ytp
ytp.load_api(keyboard, mouse, store, system, window, clipboard, highlevel, dialog, engine)

key = '2'

def main():
  ytp.multiplier(key, key)

if ytp.is_numlock_on():
  keyboard.send_key(key)
else:
  main()
