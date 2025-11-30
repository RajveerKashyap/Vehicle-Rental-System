# ✨ Rentify — Vehicle Rental System 🚗💨

Welcome to **Rentify**, a Python-powered **Vehicle Rental Management System** that brings simplicity, speed, and smart automation to renting vehicles — all inside a clean CLI interface.  
This project was created as part of our **college software development submission**, showcasing design, logic, data handling, and modular Python coding.  

---

## 👥 Team Codestrom
**Batch:** 09  
**Members:**  
- Rajveer Mishra  
- Harsh Raj Singh  
- Vanshika Tyagi  
- Riddhima Mehrotra Singh  
- Harshita  

---

# 🚀 What is Rentify?
Rentify is a menu-driven console application that allows:
- 🧑‍💼 **Customers** to create accounts, log in, rent vehicles, and track them via GPS  
- 🛠️ **Admins** to manage all vehicles, customers, and rentals  
- 🛰️ **GPS Simulation** shows live changing vehicle coordinates  
- 💸 **Smart Pricing** — Base fare + Per-km dynamic cost  
- 🚘 **Wide Vehicle Database** — From SUVs to scooters  

Everything is stored using JSON to keep the system file-based, lightweight, and easy to understand.

---

# 🧭 Features Breakdown (Detailed + Simple)

## 🌟 Customer Features
✔️ Create a new account with a unique Customer ID  
✔️ Secure login using a **6-digit PIN**  
✔️ Rent from categories like:  
- Four-wheelers (SUVs, Sedans, Hatchbacks)  
- Three-wheelers (Autos, E-rickshaws)  
- Two-wheelers (Bikes, Scooters)  
✔️ View pricing **before renting**  
✔️ Realistic **GPS tracking simulation**  
✔️ All rentals saved in your customer history  

---

## 🔐 Admin Features
Admins access the backend using a password.

Admin can:  
✔️ View **all customers**  
✔️ Add new vehicles  
✔️ Edit or delete existing vehicles  
✔️ View **all rented vehicles** with live GPS data  
✔️ Clear entire customer database (with confirmation)  

---

## 🛰️ GPS Tracker Simulation
Every vehicle rented is assigned random coordinates:  
- Latitude: between *19.0 and 19.2*  
- Longitude: between *72.8 and 73.0*  

Location updates randomly when tracking — simulating motion.  
Very cool to show teachers 😉

---

## 💸 Pricing Logic
Every vehicle type has:  
- **Base fare** (fixed)  
- **Per-km price**  

💡 Example:  
Sedan → Base ₹1000 + ₹15/km  
If user travels 10 km → Total = 1000 + (10×15) = **₹1150** (+ deposit ₹500)

---

# ⚙️ Installation & Running the Program

## 🔽 Clone the Repository
```bash
git clone https://github.com/<your-username>/Vehicle-Rental-System.git
cd Vehicle-Rental-System
```
email - rajveermishra2023@gmail.com


