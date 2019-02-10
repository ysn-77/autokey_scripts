import time

output = system.exec_command("xset -q | grep 'Num Lock:\s*on' || true", getOutput=True)
num_lock_on = (output != '')

key= '1'
replacement= '1'

def main():
    seperator=','
    combiner='+'

    escape_sequence= '##$'

    clipboard.fill_selection(escape_sequence)

    keyboard.send_keys('<home>')
    keyboard.send_keys("<shift>+<end>")
    time.sleep(0.05)

    def action():
        content = clipboard.get_selection()
        keyboard.send_keys(content.replace(',', ''))
    try:
        action()

    except:
        keyboard.send_key(key)


if num_lock_on:
    keyboard.send_key(key)
else:
    main()
    
