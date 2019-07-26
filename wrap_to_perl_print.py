# wraps selected text to perl print statement then add a new line with created text
import re
text = clipboard.get_selection()
keyboard.send_key("<end>")
keyboard.send_key("<enter>")
var_name = re.sub(r'^[$%@&]', '', text)
keyboard.send_keys("print(\"%s=\".%s.\"\\n\");" % (var_name,text))
keyboard.send_key("<enter>")
