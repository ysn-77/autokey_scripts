import time

def load_api(api_keyboard, api_mouse, api_store, api_system, api_window, api_clipboard, api_highlevel, api_dialog, api_engine):
  global keyboard, mouse, store, system, window, clipboard, highlevel, dialog, engine  # Define the API class instances as globals
  # then put the given instances into the script globals
  keyboard = api_keyboard
  mouse = api_mouse
  store = api_store
  system = api_system
  window = api_window
  clipboard = api_clipboard
  highlevel = api_highlevel
  dialog = api_dialog
  engine = api_engine


muliplier_symbol          = '*'
seperator_symbol          = ','
combiner_symbol           = '+'
hold_symbol               = '!'
argument_seperator_symbol = ':'
group_multipler_symbol    = '^'
decimal_point_symbol      = '.'

touch_command_last_charecter = 't'

escape_sequence = '##$'
seconds_to_wait = 0.05



def is_numlock_on():
  output = system.exec_command("xset -q | grep 'Num Lock:\s*on' || true", getOutput=True)
  return (output != '')


def multiplier(key, multiple):
  clipboard.fill_selection(escape_sequence)
  keyboard.send_keys("<shift>+<left><shift>+<left><shift>+<left><right>")
  time.sleep(seconds_to_wait)
  try:
    content = clipboard.get_selection()
    if (content == escape_sequence or 
        content[-1] == combiner_symbol or 
        content[-1] == seperator_symbol
      ):
      return
    if (len(content) >= 3 and (
        content[-2] == argument_seperator_symbol or 
        content[-3] == argument_seperator_symbol)
      ):
      keyboard.send_keys(muliplier_symbol+multiple)
    else:
      keyboard.send_keys(multiple)
  except:
    keyboard.send_key(key)


def move(key, direction_string):
  clipboard.fill_selection(escape_sequence)
  keyboard.send_keys("<shift>+<left><right>")
  time.sleep(seconds_to_wait)
  try:
    content = clipboard.get_selection()
    if (content[-1] == muliplier_symbol or
        content[-1] == decimal_point_symbol or
        content[-1] == group_multipler_symbol or
        content[-1] == argument_seperator_symbol
      ):
      return
    if (content != escape_sequence and
        content[-1] != combiner_symbol and
        content[-1] != seperator_symbol and
        content[-1] != hold_symbol
      ):
      keyboard.send_keys(seperator_symbol+direction_string)
    else:
      keyboard.send_keys(direction_string)
  except:
    keyboard.send_key(key)


def button(key, button_string):
  clipboard.fill_selection(escape_sequence)
  keyboard.send_keys("<shift>+<left><right>")
  time.sleep(seconds_to_wait)
  try:
    content = clipboard.get_selection()
    if (content != escape_sequence and
        content[-1] != combiner_symbol and
        content[-1] != seperator_symbol and
        content[-1] != hold_symbol
      ):
      keyboard.send_keys(seperator_symbol+button_string)
    else:
      keyboard.send_keys(button_string)
  except:
    keyboard.send_key(key)

def numpad(key):
  clipboard.fill_selection(escape_sequence)
  keyboard.send_keys("<shift>+<left><shift>+<left><shift>+<left><shift>+<left><right>")
  time.sleep(seconds_to_wait)
  try:
    content = clipboard.get_selection()
    if (len(content) >= 4 and 
        content[-3] == argument_seperator_symbol
      ):
      if content[-4] == touch_command_last_charecter:
        keyboard.send_keys(argument_seperator_symbol+key)
      else:
        keyboard.send_keys(muliplier_symbol+key)
    else:
      keyboard.send_key(key)
  except:
    keyboard.send_key(key)



