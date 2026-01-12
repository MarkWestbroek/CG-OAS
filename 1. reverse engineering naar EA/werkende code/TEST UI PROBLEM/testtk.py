import tkinter as tk

# 1. Create the main window
root = tk.Tk()
root.title("My First UI")
root.geometry("300x150")

# 2. Add a text label
label = tk.Label(root, text="Hello, World!", font=("Arial", 14))
label.pack(pady=20)

# 3. Add an exit button
button = tk.Button(root, text="Close", command=root.destroy)
button.pack()

# 4. Start the application
root.mainloop()