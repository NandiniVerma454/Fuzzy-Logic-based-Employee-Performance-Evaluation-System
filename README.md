# 🏢 **Fuzzy Logic-Based Employee Performance Evaluation System**

## 📌 Overview

This project is a Fuzzy Logic-Based Employee Performance Evaluation and Attendance Monitoring System developed using Python and Streamlit.
It evaluates employee performance based on multiple parameters and generates a comprehensive performance report with visualization.
The system mimics human decision-making by using fuzzy logic instead of rigid thresholds, making evaluation more realistic and flexible.

## 🎯 Features

🧾 Employee Details Input (Name, Age, Gender, Job Role, Income)

📊 Performance Evaluation using Fuzzy Logic

## ⚙️ Multiple Input Parameters:

(Attendance,
Work Quality,
Teamwork,
Task Completion,
Job Involvement,
Work-Life Balance)

## 🎯 Performance Score & Category (Poor, Average, Good, Excellent)

📈 Performance Interpretation Graph

📥 Downloadable Report (Excel format)

**The system uses:**

✔ Triangular Membership Functions
(Categories: Low, Medium, High)

✔ Rule-Based System: 20+ fuzzy rules that combines multiple inputs to generate output

✔ Defuzzification: Converts fuzzy output into a crisp performance score

## 📊 Performance Categories

Score Range	Category

0 – 40	Poor

40 – 60	Average

60 – 80	Good

80 – 100	Excellent

## 🖥️ Tech Stack

Python 🐍,

Streamlit 🎨 _(Frontend UI),_

Scikit-Fuzzy 🤖 _(Fuzzy Logic Engine),_

Pandas 📊 _(Data Handling),_

Matplotlib 📈 _(Visualization),_

OpenPyXL 📄 _(Excel Report Generation)_

## 📁 Project Structure

fuzzy_hr_project/

├── app.py              
├── fuzzy_logic.py       
├── dataset/             
├── requirements.txt     
└── README.md           
