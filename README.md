# Password Cracker
A simple educational dictionary attack simulator built with Python and Tkinter.  
This tool demonstrates how weak passwords can be cracked using a dictionary attack against MD5 hashes.

---

## Overview

Although modern authentication systems are evolving, passwords remain the most widely used method of identity verification. Weak or commonly used passwords are vulnerable to attacks — one of the most common being the **dictionary attack**.

This project simulates a dictionary attack by:

- Taking a target MD5 hash
- Reading a wordlist file
- Hashing each word using MD5
- Comparing the generated hash with the target
- Displaying the result in a graphical interface

The goal is to provide a simple, visual, and beginner-friendly learning tool for cybersecurity students.

---

##  Features

Simple and intuitive graphical interface (Tkinter)  
Real‑time password attempt display  
Input validation for MD5 hashes  
Case‑insensitive hash comparison  
Error handling for invalid inputs  
Cross‑platform compatibility (Windows, macOS, Linux)

---

## Technologies Used

- **Python 3.11** – Core language  
- **tkinter** – GUI framework  
- **hashlib** – MD5 hashing  
- **os** – File validation  
- **filedialog, messagebox, scrolledtext** – Enhanced GUI components  

No external libraries are required.

---

## Project Structure
```
Password-Cracker/
│
├── dictionary_attack.py
├── wordlist.txt
└── README.md
```

---

## Installation & Setup

### Install Python
Download and install Python from [python.org](https://www.python.org/).  
Verify the installation:

```bash
python --version
```
## Clone the Repository
```
git clone https://github.com/yourusername/Password-Cracker.git
cd Password-Cracker
```
