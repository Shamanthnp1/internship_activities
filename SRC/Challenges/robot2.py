import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import math
from datetime import datetime

# ---------------- Main Window ----------------
window = tk.Tk()
window.title("🤖 RoboController 3.0")
window.geometry("700x700")
window.configure(bg="#eef5ff")

# ---------------- Style ----------------
style = ttk.Style()
style.theme_use("clam")
style.configure("TProgressbar", thickness=20)

# ---------------- State ----------------
state = {
    "name": "",
    "total_distance": 0,
    "remaining_distance": 0,
    "distance_travelled": 0,
    "speed": 0,
    "battery": 100,
    "checkpoints": [],
    "start_time": None
}

# ---------------- Helper Functions ----------------
def decide_speed(distance):
    if distance > 150:
        return 30
    elif 80 <= distance <= 150:
        return 20
    return 10

def write_output(text):
    output.insert(tk.END, text + "\n")
    output.see(tk.END)

def animate():
    x = robot_label.winfo_x()
    if x < 550:
        robot_label.place(x=x + 20, y=420)

# ---------------- Start Robot ----------------
def start_robot():
    try:
        state["name"] = name_entry.get()
        state["total_distance"] = float(distance_entry.get())
        state["remaining_distance"] = state["total_distance"]
        state["distance_travelled"] = 0
        state["battery"] = 100
        state["speed"] = decide_speed(state["total_distance"])
        state["checkpoints"] = ["Start"]
        state["start_time"] = datetime.now()

        progress["maximum"] = state["total_distance"]
        progress["value"] = 0

        robot_label.place(x=20, y=420)

        output.delete(1.0, tk.END)
        write_output("🚀 Robot Mission Started!")
        write_output(f"Speed: {state['speed']} m/step")
        write_output(f"Start Time: {state['start_time'].strftime('%H:%M:%S')}")
        write_output("-" * 50)

        move_robot()

    except ValueError:
        messagebox.showerror("Error", "Enter valid numeric distance")

# ---------------- Auto Movement ----------------
def move_robot():

    if state["remaining_distance"] <= 0:
        finish_mission()
        return

    if state["battery"] <= 0:
        write_output("🔋 Battery drained! Mission Failed.")
        return

    obstacle = obstacle_var.get()

    write_output(f"Remaining Distance: {math.ceil(state['remaining_distance'])} m")

    if obstacle == "human":
        write_output("👤 Human detected. Waiting...")
        state["checkpoints"].append("Waited (Human)")

    elif obstacle == "wall":
        turn = random.choice(["Left", "Right"])
        write_output(f"🧱 Wall detected. Turned {turn}")
        state["checkpoints"].append(f"Turned {turn}")

    else:
        write_output("Moving Forward...")
        state["checkpoints"].append("Forward")

    state["remaining_distance"] -= state["speed"]
    state["distance_travelled"] += state["speed"]
    state["battery"] -= 2

    progress["value"] = state["distance_travelled"]
    battery_label.config(text=f"Battery: {state['battery']}%")

    animate()
    write_output("-" * 40)

    window.after(1000, move_robot)  # Auto move every 1 sec

# ---------------- Finish Mission ----------------
def finish_mission():
    end_time = datetime.now()
    duration = (end_time - state["start_time"]).seconds

    write_output("\n🎯 TARGET REACHED!")
    write_output(f"End Time: {end_time.strftime('%H:%M:%S')}")
    write_output(f"Total Duration: {duration} seconds")
    write_output("\n===== TRIP SUMMARY =====")
    write_output(f"Robot Name         : {state['name']}")
    write_output(f"Total Distance     : {state['total_distance']} m")
    write_output(f"Distance Travelled : {state['distance_travelled']} m")
    write_output(f"Battery Remaining  : {state['battery']}%")
    write_output("Checkpoints:")
    for cp in state["checkpoints"]:
        write_output(f"  ➤ {cp}")
    write_output("=" * 50)

# ---------------- UI ----------------
title = tk.Label(window, text="🤖 RoboController 3.0",
                 font=("Segoe UI", 22, "bold"),
                 bg="#eef5ff")
title.pack(pady=15)

frame = tk.Frame(window, bg="#eef5ff")
frame.pack(pady=10)

tk.Label(frame, text="Robot Name:", bg="#eef5ff").grid(row=0, column=0, pady=5)
name_entry = tk.Entry(frame, width=20)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Distance (meters):", bg="#eef5ff").grid(row=1, column=0, pady=5)
distance_entry = tk.Entry(frame, width=20)
distance_entry.grid(row=1, column=1)

tk.Label(frame, text="Obstacle:", bg="#eef5ff").grid(row=2, column=0, pady=5)
obstacle_var = tk.StringVar(value="none")
ttk.Combobox(frame, textvariable=obstacle_var,
             values=["none", "human", "wall"],
             state="readonly").grid(row=2, column=1)

tk.Button(window, text="Start Mission 🚀",
          font=("Segoe UI", 11, "bold"),
          bg="#4da6ff",
          command=start_robot).pack(pady=10)

progress = ttk.Progressbar(window, length=550)
progress.pack(pady=10)

battery_label = tk.Label(window, text="Battery: 100%",
                         font=("Segoe UI", 11),
                         bg="#eef5ff")
battery_label.pack()

robot_label = tk.Label(window, text="🤖", font=("Arial", 40),
                       bg="#eef5ff")

output = tk.Text(window, height=14, width=80, font=("Consolas", 10))
output.pack(pady=15)

window.mainloop()
