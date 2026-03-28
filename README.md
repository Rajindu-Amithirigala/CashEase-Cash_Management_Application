<div align="center">

# 💵 CashEase

### *Know where your money goes. Before it's gone.*

**A lightweight weekly cash management app built with Python and Tkinter**

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational?style=flat-square)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

</div>

---

## What Is CashEase?

CashEase is a no-fuss desktop app for people who want to keep a close eye on their weekly spending — without the overhead of a full budgeting suite. Log your expenses, watch your remaining cash update in real time, and get warned before you hit zero. Simple, visual, and entirely offline.

No accounts. No subscriptions. No cloud. Just you and your money.

---

## ✨ Features

- **💸 Weekly Expense Tracking** — Log what you spend, when you spend it
- **📊 Visual Reports** — See your expenses broken down in clear, colorful charts
- **🔔 Low Budget Alerts** — Get notified before your cash runs out
- **🎨 Colorful UI** — A clean, friendly interface with background image support
- **💾 Persistent Storage** — All data saved locally to CSV — no database needed

---

## 🖥️ Screenshots

> *Add screenshots of your app here — a picture is worth a thousand budget spreadsheets.*

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8+**
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Rajindu-Amithirigala/CashEase-Cash_Management_Application.git
   cd CashEase-Cash_Management_Application
   ```

2. **Install dependencies**

   ```bash
   pip install pillow pandas
   ```

   > `tkinter` and `os` are part of Python's standard library — no extra install needed.

3. **Make sure these files are in the project root:**

   ```
   CashEase-Cash_Management_Application/
   ├── MainFile.py
   ├── user_data.csv
   └── (background image files)
   ```

4. **Run the app**

   ```bash
   python MainFile.py
   ```

   Or open `MainFile.py` in your IDE (PyCharm, VS Code, etc.) and hit Run.

---

## 📦 Dependencies

| Package | Purpose |
|--------|---------|
| `tkinter` | GUI framework — windows, buttons, forms |
| `pandas` | Reading and writing expense data |
| `Pillow` | Loading and displaying background images |
| `os` | File path handling |
| `csv` | Underlying data storage format |

---

## 📁 Project Structure

```
CashEase-Cash_Management_Application/
├── MainFile.py        # Application entry point
├── user_data.csv      # Persistent expense storage
└── assets/            # Background images and UI resources
```

---

## 🗺️ Roadmap

Possible directions for future versions:

- [ ] **Monthly view** — zoom out beyond weekly tracking
- [ ] **Category tags** — label expenses (food, transport, bills, etc.)
- [ ] **Export reports** — save charts as PDF or PNG
- [ ] **Budget goals** — set weekly targets per category
- [ ] **Dark mode** — because everyone deserves dark mode
- [ ] **Installable executable** — package with PyInstaller for easy distribution

---

## 🤝 Credits & Libraries

- [**Tkinter**](https://docs.python.org/3/library/tkinter.html) — Python's built-in GUI toolkit
- [**Pandas**](https://pandas.pydata.org/) — Data manipulation and CSV handling
- [**Pillow**](https://python-pillow.org/) — Image processing for the UI

---

<div align="center">

Built by [Rajindu Amithirigala](https://github.com/Rajindu-Amithirigala) · Keep it simple. Keep it tracked.

</div>
