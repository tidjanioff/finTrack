# 💰 FinTrack

**FinTrack** is a terminal-based financial tracking app written in Python. It helps you monitor your **incomes**, **expenses**, and provides **detailed monthly and yearly summaries**. Simple and efficient, it's built to give you clear insights into your financial activity.

<p align="center">
  <img src="assets/FINTRACK3.png">
</p>

---

## 📊 Features Overview

- Add new **income** and **expense** entries directly from the terminal.
- Generate **monthly** or **yearly summaries**:
  - Total Income
  - Total Expenses
  - Net Balance
- View **detailed breakdowns** of all transactions.
- All data is stored in easy-to-read `.csv` files for each month.

---

## 🎬 Live Demo

🎥 [Watch the live demo on YouTube](https://youtu.be/k4D-Yvv9-KU)


---

## 🎯 Objectives

- 📥 Track all your financial inflows and outflows.
- 📆 Get a month-by-month or yearly overview of your finances.
- 🧾 Access detailed transaction logs.
- 📈 Improve personal budgeting and financial awareness.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/tidjanioff/finTrack.git
```

### 2. Install Dependencies
```bash
pip install -r assets/requirements.txt 
```

### 3. Run the App

Navigate to the project folder:

```bash
cd finTrack
```

Then launch the app:
```bash
python3 project.py
```
✅ **Make sure the `income/` and `expenses/` folders are present, each containing `.csv` files for every month** (these are included in this repo).

---

## 📁 Project Structure

- `fintrack/`
  - `income/` – Monthly income CSV files  
  - `expenses/` – Monthly expense CSV files  
  - `project.py` – Main application script  
  - `months.py` – Utility module for month handling  
  - `README.md` – Project documentation  


---

## 🧩 Technologies Used

- **Python 3**
- **CSV** (data storage)
- **tabulate** (table rendering in terminal)
- **simple_colors** (colored output for better UX)

---

## 📝 Example Usage

Upon launch, you’ll see:  
→ Tap **1** to add a new income  <br>
→ Tap **2** to add a new expense  <br>
→ Tap **3** to display a summary of your `[current month]`'s finances  <br>
→ Tap **4** to display a summary of any month's finances  <br>
→ Tap **5** to display a summary of this year's finances  <br>
→ Tap **6** to get access to the details of your `[current month]`'s finances  <br>
→ Tap **7** to get access to the details of any month's finances  <br>
→ Tap **0** to end the program


---

© 2024 **FinTrack** | Built by Tidjani. All rights reserved.
