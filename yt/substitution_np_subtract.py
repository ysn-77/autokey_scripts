

output = system.exec_command("xset -q | grep 'Num Lock:\s*on' || true", getOutput=True)
num_lock_on = (output != '')

key= '-'

def main():
    keyboard.send_keys(':')



if num_lock_on:
    keyboard.send_key(key)
else:
    main()
    


