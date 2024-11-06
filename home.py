import tkinter as tk
from tkinter import ttk, messagebox
from time import strftime, time
import datetime
from threading import Timer as ThreadingTimer

# Initialize the main window
root = tk.Tk()
root.title("Interactive Clock Application")
root.geometry("600x400")

# Tab Control
tab_control = ttk.Notebook(root)

# Clock Tab
clock_tab = ttk.Frame(tab_control)
tab_control.add(clock_tab, text='Clock')

# Stopwatch Tab
stopwatch_tab = ttk.Frame(tab_control)
tab_control.add(stopwatch_tab, text='Stopwatch')

# Timer Tab
timer_tab = ttk.Frame(tab_control)
tab_control.add(timer_tab, text='Timer')

# Alarm Tab
alarm_tab = ttk.Frame(tab_control)
tab_control.add(alarm_tab, text='Alarm')

# Weather Tab
weather_tab = ttk.Frame(tab_control)
tab_control.add(weather_tab, text='Weather')

tab_control.pack(expand=1, fill="both")

# Clock Function
def update_time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

time_label = tk.Label(clock_tab, font=('calibri', 50, 'bold'), background='purple', foreground='white')
time_label.pack(anchor='center', pady=20)
update_time()

# Stopwatch Functionality
stopwatch_running = False
stopwatch_start_time = 0
def start_stopwatch():
    global stopwatch_running, stopwatch_start_time
    if not stopwatch_running:
        stopwatch_start_time = time()
        stopwatch_running = True
        update_stopwatch()

def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False

def reset_stopwatch():
    global stopwatch_start_time
    stopwatch_start_time = time()
    stopwatch_label.config(text="00:00:00")

def update_stopwatch():
    if stopwatch_running:
        elapsed_time = int(time() - stopwatch_start_time)
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        root.after(1000, update_stopwatch)

# Stopwatch Controls
stopwatch_label = tk.Label(stopwatch_tab, font=('calibri', 30), text="00:00:00", foreground="blue")
stopwatch_label.pack(pady=20)
ttk.Button(stopwatch_tab, text="Start", command=start_stopwatch).pack(side="left", padx=5, pady=5)
ttk.Button(stopwatch_tab, text="Stop", command=stop_stopwatch).pack(side="left", padx=5, pady=5)
ttk.Button(stopwatch_tab, text="Reset", command=reset_stopwatch).pack(side="left", padx=5, pady=5)

# Timer Functionality
timer_running = False
timer_seconds = 0
def start_timer():
    global timer_running
    if not timer_running and timer_seconds > 0:
        timer_running = True
        update_timer()

def stop_timer():
    global timer_running
    timer_running = False

def reset_timer():
    global timer_seconds
    timer_seconds = 0
    timer_label.config(text="00:00:00")

def set_timer():
    global timer_seconds
    timer_seconds = int(timer_entry.get())
    minutes, seconds = divmod(timer_seconds, 60)
    timer_label.config(text=f"{minutes:02}:{seconds:02}")

def update_timer():
    global timer_seconds, timer_running
    if timer_running and timer_seconds > 0:
        minutes, seconds = divmod(timer_seconds, 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        timer_seconds -= 1
        root.after(1000, update_timer)
    else:
        timer_running = False
        if timer_seconds == 0:
            messagebox.showinfo("Timer Finished", "Your timer is up!")

# Timer Controls
timer_label = tk.Label(timer_tab, font=('calibri', 30), text="00:00:00", foreground="green")
timer_label.pack(pady=20)
timer_entry = tk.Entry(timer_tab, font=('calibri', 15), width=5)
timer_entry.pack(pady=5)
ttk.Button(timer_tab, text="Set Timer", command=set_timer).pack()
ttk.Button(timer_tab, text="Start Timer", command=start_timer).pack(side="left", padx=5, pady=5)
ttk.Button(timer_tab, text="Stop Timer", command=stop_timer).pack(side="left", padx=5, pady=5)
ttk.Button(timer_tab, text="Reset Timer", command=reset_timer).pack(side="left", padx=5, pady=5)

# Alarm Functionality
def set_alarm():
    alarm_time = alarm_entry.get()
    alarm_label.config(text=f"Alarm set for {alarm_time}")
    try:
        alarm_timer = ThreadingTimer((datetime.datetime.strptime(alarm_time, "%H:%M") - datetime.datetime.now()).seconds, trigger_alarm)
        alarm_timer.start()
    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter time in HH:MM format")

def trigger_alarm():
    alarm_label.config(text="Alarm ringing!")
    messagebox.showinfo("Alarm", "Your alarm is ringing!")

# Alarm Controls
alarm_entry = tk.Entry(alarm_tab, font=('calibri', 15), width=5)
alarm_entry.pack(pady=10)
ttk.Button(alarm_tab, text="Set Alarm (HH:MM)", command=set_alarm).pack()
alarm_label = tk.Label(alarm_tab, font=('calibri', 15), foreground="red")
alarm_label.pack()

# Weather Functionality (Placeholder)
def get_weather():
    weather_label.config(text="Weather: 25°C, Clear skies")

# Weather Controls
ttk.Button(weather_tab, text="Get Weather", command=get_weather).pack(pady=10)
weather_label = tk.Label(weather_tab, font=('calibri', 15), foreground="black")
weather_label.pack()

# Exit Fullscreen Binding
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

# Run the Application
root.mainloop()


