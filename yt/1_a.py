import time

output = system.exec_command("xset -q | grep 'Num Lock:\s*on' || true", getOutput=True)
num_lock_on = (output != '')

key= '1'
replacement= 'a'

def main():
	seperator=','
	combiner='+'

	escape_sequence= '##$'

	clipboard.fill_selection(escape_sequence)

	keyboard.send_keys("<shift>+<left><shift>+<left>")
	keyboard.send_keys("<right>")
	time.sleep(0.05)


	try:
	    content = clipboard.get_selection()
	    if content[-1] == '*' or content[-1] == '.' or content[-1] == '^' or content[-1] == ':' or (content[-1].isdigit() and content[-2] == ':'):
		    keyboard.send_key(key)
	    else:
	        if content != escape_sequence and content[-1] != combiner and content[-1] != seperator and content[-1] != '!':
	            keyboard.send_keys(seperator)
	        keyboard.send_keys(replacement)
	            
	except:
	    keyboard.send_key(key)

if num_lock_on:
    keyboard.send_key(key)
else:
    main()

