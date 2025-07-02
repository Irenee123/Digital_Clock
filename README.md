---

## 📘 `README.md`

```markdown
# 🕒 Python Digital Clock (Console Version)

A simple digital clock built with Python that displays the current time in the terminal and updates every second.

## 📁 Project Structure

```

python-digitalclock/
├── digital\_clock.py
└── README.md

````

## 🚀 How to Run

### 1. Clone or Create the Project Directory
```bash
mkdir python-digitalclock
cd python-digitalclock
````

### 2. Create the Python File

```bash
touch digital_clock.py
```

Paste the code from `digital_clock.py` into that file.

### 3. Run the Program

Make sure you're using **Python 3**:

```bash
python3 digital_clock.py
```

If using **Python 2**, use the compatible version in this repo.

### ⏹ To Stop the Clock

Press `Ctrl + C` in the terminal.

## 🧠 How It Works

* Uses the built-in `time` module.
* Continuously fetches the current system time.
* Updates the display every second using `sleep(1)` and overwrites the previous time using `\r`.

## 📦 Requirements

No external libraries needed! Just Python.

Tested with:

* Python 3.6+
* Python 2.7 (with modified code)

