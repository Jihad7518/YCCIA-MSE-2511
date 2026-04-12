# Notification System – Factory Design Pattern Example

## Overview
This project demonstrates a notification system implemented in two ways:
1. Without using the Factory Design Pattern
2. Using the Factory Design Pattern

The system supports Email, SMS, and Push notifications, where the notification type is selected at runtime.

---

## Version 1: Without Factory Pattern
- Object creation logic is written directly in the client code.
- Client code depends on concrete notification classes.
- Adding a new notification type requires modifying the client code.

**Disadvantages:**
- Tight coupling
- Poor scalability
- Harder maintenance

---

## Version 2: With Factory Pattern
- Object creation logic is moved to a factory class.
- Client code depends only on the factory.
- New notification types can be added without modifying client code.

**Advantages:**
- Loose coupling
- Better maintainability
- Improved scalability
- Follows Open/Closed Principle

---

## How to Run

Navigate to either version folder and run:

```bash
python main.py
