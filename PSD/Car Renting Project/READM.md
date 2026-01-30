# 🚗 Car Rental System

**Course:** MSE800 – Professional Software Engineering  
**Programme:** Master of Software Engineering (Level 8)  
**Institution:** Yoobee College of Creative Innovation  

---

## 📌 Project Overview

The **Car Rental System** is a **console-based application** developed using **Object-Oriented Programming (OOP)** principles in Python.  
It automates the operations of a car rental company by managing **users, cars, and rental bookings** efficiently.

The system uses an **SQLite database**, follows a **modular architecture**, and applies **software engineering best practices**, including separation of concerns and design patterns.

---

## 👥 User Roles

### 👨‍💼 Admin
- Manages cars, customers, and bookings
- Verifies customer profiles
- Approves or rejects bookings
- Receives system notifications

### 👤 Customer
- Registers and logs in
- Views available cars
- Places rental bookings
- Tracks booking status
- Receives notifications

---

## 🎯 Key Features

### 👤 User Management
- User registration and login
- Role-based access control (Admin / Customer)
- Customer verification by Admin

### 🚘 Car Management (Admin)
- Add new cars
- Update existing car details
- Delete cars
- View all cars with availability status

### 📅 Booking Management

**Customer can:**
- View available cars
- Book cars with start and end dates
- View booking status
- Cancel pending bookings

**Admin can:**
- View pending bookings
- Approve or reject bookings
- Provide rejection reasons

### 🔔 Notifications (Innovative Feature)
- **Admin notifications** for:
  - Pending bookings
  - Unverified customers
- **Customer notifications** for:
  - Booking approval
  - Booking rejection with reason

### 🧠 Smart System Behaviour
- Prevents double booking
- Automatically calculates rental duration
- Supports safe database migration without data loss

---

## ⚙️ Installation & Setup Guide

### 🔧 Prerequisites
- Python **3.9** or higher
- No external libraries required

### 📥 Installation Steps

1. Extract the project folder  
2. Open a terminal in the project root directory  
3. Initialize the database:
   ```bash
   python init_db.py
4. Run the application
   python main.py
   
## ▶️ How to Use the System

### 👨‍💼 Admin Workflow
- Login as Admin
- Add, update, or delete cars
- View pending booking requests
- Approve or reject bookings with reasons
- Verify customer profiles
- View admin notifications

### 👤 Customer Workflow
- Register as a customer
- Login to the system
- View available cars
- Book a car by selecting rental dates
- View booking status
- Receive booking notifications

---

## 🗂️ Project Structure

car_rental_system/
│
├── main.py                  # Application entry point
├── init_db.py               # Database initialization & migration
├── README.md                # Project documentation
│
├── src/
│   ├── database/
│   │   ├── db.py            # Database connection (Singleton)
│   │   └── schema.sql       # Database schema
│   │
│   ├── models/              # Entity classes (User, Car, Booking)
│   ├── services/            # Business logic layer
│   │   ├── admin_service.py
│   │   ├── booking_service.py
│   │   └── customer_service.py
│   │
│   ├── utils/               # Helper functions & input validation
│   └── patterns/            # Design pattern implementations
│
└── data/
    └── car_rental.db        # SQLite database


---

## 🧩 Design Patterns Used

### 🔹 Singleton Pattern
Ensures a single shared instance of the database connection across the application.

### 🔹 Observer-Style Notifications
Triggers notifications for admins and customers when booking status changes.

### 🔹 Service Layer Pattern
Separates business logic from the user interface, improving maintainability and scalability.

---

## 🐞 Known Issues & Limitations
- Console-based user interface (no graphical UI)
- Passwords are stored without encryption (kept simple for academic purposes)
- Limited input validation for some edge cases

These limitations are documented and can be addressed in future versions.

---

## 🔐 License
This project is released under the **MIT License**.  
It may be used, modified, and distributed for **educational purposes**.

---

## 👨‍💻 Developer Credits

- **Name:** Md. Jihad  
- **Programme:** Master of Software Engineering  
- **Institution:** Yoobee College of Creative Innovation  
- **Role:** Sole Developer  

---

## 📈 Future Enhancements
- Graphical or web-based user interface
- Payment gateway integration
- Email and SMS notification support
- Extended role-based permissions
- RESTful API implementation
