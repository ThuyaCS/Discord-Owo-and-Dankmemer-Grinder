# Made by ThuyaCS

import pyautogui
import time
import random

# List of commands with their respective cooldowns
# `owo_commands` have a 25-second cooldown
owo_commands = ["owob", "owoh"]

# `pls_commands` has variable cooldowns:
# - "Pls hunt" and "Pls dig" have a 35-second cooldown
# - "Pls beg" and "owoz" have a 45-second cooldown
pls_commands = ["Pls hunt", "Pls dig", "Pls beg", "owoz"]

# Initialize the last command times
# Set the start times to past values to ensure commands can be sent immediately on the first loop
last_owo_times = {cmd: time.time() - 25 for cmd in owo_commands}
last_pls_times = {
    "Pls hunt": time.time() - 35,
    "Pls dig": time.time() - 35,
    "Pls beg": time.time() - 45,
    "owoz": time.time() - 45
}

def type_commands():
    """
    Function to type commands randomly from the `owo_commands` and `pls_commands` lists,
    adhering to their respective cooldowns.
    """
    while True:
        current_time = time.time()  # Get the current time

        # Randomly pick and type an `owo` command if its cooldown is up
        random_owo_command = random.choice(owo_commands)
        if current_time - last_owo_times[random_owo_command] >= 25:
            print(f"Typing owo command: {random_owo_command} at {time.strftime('%H:%M:%S')}")
            pyautogui.write(random_owo_command)
            pyautogui.hotkey('ctrl', 'enter')
            last_owo_times[random_owo_command] = current_time
        else:
            print(f"Cooldown for owo command: {random_owo_command}, time remaining: {25 - (current_time - last_owo_times[random_owo_command]):.2f} seconds")

        # Randomly pick and type a `Pls` command if its cooldown is up
        random_pls_command = random.choice(pls_commands)
        cooldown = 35 if random_pls_command in ["Pls hunt", "Pls dig"] else 45
        if current_time - last_pls_times[random_pls_command] >= cooldown:
            print(f"Typing Pls command: {random_pls_command} at {time.strftime('%H:%M:%S')}")
            pyautogui.write(random_pls_command)
            pyautogui.hotkey('ctrl', 'enter')
            last_pls_times[random_pls_command] = current_time
        else:
            print(f"Cooldown for Pls command: {random_pls_command}, time remaining: {cooldown - (current_time - last_pls_times[random_pls_command]):.2f} seconds")

        time.sleep(1)  # Sleep for a short time before checking again

# Allow a 5-second delay to switch to the target window
time.sleep(5)
print("Starting the script...")
type_commands()
