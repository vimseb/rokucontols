import tkinter as tk
import subprocess

print("This is a controler for a roku tv. The device must be in the same network.")
ip = input("Input the ip adress:")
print("Make sure the gui is active a click on it to activate the control")
input("Press Enter to continue...")

def send_request(url):
    command = f"powershell Invoke-WebRequest -Uri \"{url}\" -Method Post > $null"
    subprocess.run(command, shell=True)


def on_key_press(event, ip):
    if event.keysym == 'Up':
        send_request(f"http://{ip}:8060/keypress/up")
    elif event.keysym == 'Down':
        send_request(f"http://{ip}:8060/keypress/down")
    elif event.keysym == 'Left':
        send_request(f"http://{ip}:8060/keypress/left")
    elif event.keysym == 'Right':
        send_request(f"http://{ip}:8060/keypress/right")
    elif event.keysym == 'h':
        send_request(f"http://{ip}:8060/keypress/home")
    elif event.keysym == 'o':
        send_request(f"http://{ip}:8060/keypress/powerOff")
    elif event.keysym == 'f':
        send_request(f"http://{ip}:8060/keypress/powerOn")
    elif event.keysym == 'enter':
        send_request(f"http://{ip}:8060/keypress/select")
    elif event.char == 'q':
        print("Exiting...")
        root.quit()


# Create the main window
root = tk.Tk()
root.title("TV Controls")

# Set the window size
root.geometry('450x400')

# Set the background color
root.configure(bg='black')

# Create the main label to display instructions
main_label = tk.Label(root, text="Roku TV controls", font=('Helvetica', 14), bg='black', fg='white')
main_label.pack(pady=10)

# Create additional labels for directions
direction1 = tk.Label(root, text="Up arrow: Move up", font=('Helvetica', 12), bg='black', fg='white')
direction1.pack()
direction2 = tk.Label(root, text="Down arrow: Move down", font=('Helvetica', 12), bg='black', fg='white')
direction2.pack()
direction3 = tk.Label(root, text="Left arrow: Move left", font=('Helvetica', 12), bg='black', fg='white')
direction3.pack()
direction4 = tk.Label(root, text="Right arrow: Move right", font=('Helvetica', 12), bg='black', fg='white')
direction4.pack()
direction5 = tk.Label(root, text="\'o\' to power on the tv", font=('Helvetica', 12), bg='black', fg='white')
direction5.pack()
direction6 = tk.Label(root, text="\'f\' to power off the tv", font=('Helvetica', 12), bg='black', fg='white')
direction6.pack()

direction7 = tk.Label(root, text="Press 'q' to quit", font=('Helvetica', 12), bg='black', fg='white')
direction7.pack()

# Bind key press events to the on_key_press function
root.bind('<KeyPress>', lambda event: on_key_press(event, ip))

# Run the Tkinter event loop
root.mainloop()

