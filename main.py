import tkinter as tk
from tkinter import messagebox
import random

# Define the network scenarios
scenarios = [
    {
        "issue": "Users cannot connect to the Wi-Fi network.",
        "choices": [
            "Check if the Wi-Fi router is powered on.",
            "Reboot the user's computer.",
            "Replace the Wi-Fi router.",
            "Check if the user has entered the correct Wi-Fi password."

        ],
        "correct_choice": 0
    },
    {
        "issue": "Website is loading very slowly for all users.",
        "choices": [
            "Check if the web server is overloaded.",
            "Check the users' internet speed.",
            "Restart the web server.",
            "Clear the browser cache for all users."
        ],
        "correct_choice": 0
    },
    {
        "issue": "Emails are not being sent or received.",
        "choices": [
            "Check if the email server is running.",
            "Reboot the users' computers.",
            "Check the email server's storage capacity.",
            "Ensure the users are using the correct email client."
        ],
        "correct_choice": 0
    },
    {
        "issue": "A specific user cannot access shared network drives.",
        "choices": [
            "Check the user's network permissions.",
            "Reboot the user's computer.",
            "Reboot the network drive server.",
            "Replace the user's network cable."
        ],
        "correct_choice": 0
    },
    {
        "issue": "DNS server is not resolving domain names.",
        "choices": [
            "Check if DNS server IP is correctly configured on the client.",
            "Check if DNS server is reachable from the client.",
            "Restart DNS server service.",
            "Replace the DNS server."
        ],
        "correct_choice": 0
    },
    {
        "issue": "VoIP calls are choppy and dropping.",
        "choices": [
            "Check network bandwidth and quality of service settings.",
            "Reboot VoIP phone devices.",
            "Check for interference from other network devices.",
            "Replace the VoIP gateway."
        ],
        "correct_choice": 0
    },
    {
        "issue": "VPN connection fails to establish.",
        "choices": [
            "Check if VPN server is running and accessible.",
            "Check VPN client configuration.",
            "Check for firewall rules blocking VPN traffic.",
            "Upgrade VPN client software."
        ],
        "correct_choice": 0
    }
]

# Initialize the game state
attempts = 3

# Function to handle the user's choice
def handle_choice(choice_index):
    global attempts
    if choice_index == scenario["correct_choice"]:
        messagebox.showinfo("Correct!", "You have resolved the issue.")
        attempts = 2
        select_new_scenario()

    else:
        attempts -= 1
        if attempts > 0:
            messagebox.showwarning("Incorrect", f"Incorrect. You have {attempts} attempts remaining. Try again.")
        else:
            messagebox.showerror("Game Over", f"Sorry, you have used all your attempts. The correct solution was:\n{scenario['choices'][scenario['correct_choice']]}")
            attempts = 2
            select_new_scenario()

# Function to select a new scenario
def select_new_scenario():
    global scenario_label, choice_buttons, scenario
    scenario = random.choice(scenarios)
    scenario_label.config(text=f"Issue: {scenario['issue']}")
    for i in range(len(choice_buttons)):
        choice_buttons[i].config(text=scenario['choices'][i])

# Set up the main application window
root = tk.Tk()
root.title("Network Troubleshooting Simulation")

# Display the network issue
scenario = random.choice(scenarios)
scenario_label = tk.Label(root, text=f"Issue: {scenario['issue']}", wraplength=500, justify="left", font=("Arial", 14))
scenario_label.pack(pady=10)

# Display the choices as buttons
choice_buttons = []
for index, choice in enumerate(scenario["choices"]):
    button = tk.Button(root, text=choice, command=lambda i=index: handle_choice(i), wraplength=500, justify="left", font=("Arial", 12))
    button.pack(pady=5, padx=10, ipady=5, fill=tk.X)
    choice_buttons.append(button)

# Start the GUI event loop
root.mainloop()