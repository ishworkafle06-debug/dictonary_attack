import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import hashlib
import os

def browse_file():
    filename = filedialog.askopenfilename(title="Select Dictionary File",
                                          filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)

def start_attack():
    target = hash_entry.get().strip()
    dict_file = file_entry.get().strip()

    # Validate inputs
    if not target:
        messagebox.showerror("Error", "Please enter a target MD5 hash.")
        return
    if len(target) != 32 or not all(c in '0123456789abcdefABCDEF' for c in target):
        messagebox.showerror("Error", "Invalid MD5 hash. Must be 32 hex characters.")
        return
    if not dict_file or not os.path.isfile(dict_file):
        messagebox.showerror("Error", "Please select a valid dictionary file.")
        return
    # Clear output and disable button
    output_area.delete(1.0, tk.END)
    start_btn.config(state=tk.DISABLED, text="Cracking...")
    root.update()  # Force GUI update

    target = target.lower()
    found = False

    try:
        with open(dict_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                word = line.strip()
                if not word:
                    continue

                # Show progress
                output_area.insert(tk.END, f"Trying word {line_num}: {word[:30]}...\n")
                output_area.see(tk.END)
                root.update()  # Update GUI after each line

                # Compute hash and compare
                word_hash = hashlib.md5(word.encode('utf-8')).hexdigest()
                if word_hash == target:
                    output_area.insert(tk.END, f"\n[+] Password found: {word}\n")
                    found = True
                    messagebox.showinfo("Success", f"Password found: {word}")
                    break

        if not found:
            output_area.insert(tk.END, "\n[-] Password not found in dictionary.\n")
            messagebox.showinfo("Result", "Password not found.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    # Re-enable button
    start_btn.config(state=tk.NORMAL, text="Start Attack")

# Create main window
root = tk.Tk()
root.title("Simple Dictionary Attack")
root.geometry("550x400")

# Target hash
tk.Label(root, text="Target MD5 Hash:").pack(pady=(10,0))
hash_entry = tk.Entry(root, width=60)
hash_entry.pack(pady=5)

# Dictionary file
tk.Label(root, text="Dictionary File:").pack()
file_frame = tk.Frame(root)
file_frame.pack(pady=5, fill=tk.X, padx=10)
file_entry = tk.Entry(file_frame, width=50)
file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Button(file_frame, text="Browse", command=browse_file).pack(side=tk.RIGHT, padx=5)

# Start button
start_btn = tk.Button(root, text="Start Attack", command=start_attack, bg="lightblue")
start_btn.pack(pady=10)

# Output area
output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
output_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()
