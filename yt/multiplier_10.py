import ytp
ytp.load_api(keyboard, mouse, store, system, window, clipboard, highlevel, dialog, engine)

key = '0'

def main():
  ytp.multiplier(key, '10')

if ytp.is_numlock_on():
  keyboard.send_key(key)
else:
  main()
