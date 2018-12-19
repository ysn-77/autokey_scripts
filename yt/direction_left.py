import time

output = system.exec_command("xset -q | grep 'Num Lock:\s*on' || true", getOutput=True)
num_lock_on = (output != '')

key= '['
replacement= 'left'

def main():
    seperator=','
    combiner='+'

    escape_sequence= '##$'

    clipboard.fill_selection(escape_sequence)

    keyboard.send_keys("<shift>+<left><shift>+<left>")
    keyboard.send_keys("<right>")
    time.sleep(0.05)

    def move():
        content = clipboard.get_selection()
        if content[-1] == '*' or content[-1] == '.' or content[-1] == '^' or content[-1] == ':' or (content[-1].isdigit() and content[-2] == ':'):
	        return None

        if content != escape_sequence and content[-1] != combiner and content[-1] != seperator:
            keyboard.send_keys(seperator)
        keyboard.send_keys(replacement)

    try:
        move()

    except:
        keyboard.send_key(key)
    

if num_lock_on:
    keyboard.send_key(key)
else:
    main()