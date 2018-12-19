import time

output = system.exec_command("xset -q | grep 'Num Lock:\s*on' || true", getOutput=True)
num_lock_on = (output != '')

key= '8'
replacement= '*' + key

def main():
    seperator=','
    combiner='+'

    escape_sequence= '##$'

    clipboard.fill_selection(escape_sequence)

    keyboard.send_keys("<shift>+<left><shift>+<left>")
    keyboard.send_keys("<right>")
    time.sleep(0.05)

    def multiply():
        content = clipboard.get_selection()
        if content == escape_sequence or content[-1] == combiner or content[-1] == seperator:
            return None

        if content[-1] == '.':
            keyboard.send_keys('<left>*<right>' + key)
        elif content[-1] == '*' or content[-1] == '^':
            keyboard.send_key(key)
        else:
            keyboard.send_keys(replacement)

    try:
        multiply()

    except:
        keyboard.send_key(key)


if num_lock_on:
    keyboard.send_key(key)
else:
    main()
    
