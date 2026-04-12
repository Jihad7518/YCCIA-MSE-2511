-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('admin', 'customer'))
);

-- Cars table
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    mileage INTEGER NOT NULL,
    available INTEGER NOT NULL CHECK(available IN (0,1)),
    daily_rate REAL NOT NULL,
    description TEXT
);

-- Bookings table
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    car_id INTEGER NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    total_cost REAL NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('pending', 'approved', 'rejected')),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(car_id) REFERENCES cars(id)
);

-- Customer Profiles table
CREATE TABLE IF NOT EXISTS customer_profiles (
    user_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    id_type TEXT NOT NULL CHECK(id_type IN ('Passport', 'License')),
    id_number TEXT NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    verified INTEGER DEFAULT 0 CHECK(verified IN (0,1)),
    FOREIGN KEY(user_id) REFERENCES users(id)
);

-- ALTER TABLE bookings ADD COLUMN notified INTEGER DEFAULT 0;
-- ALTER TABLE bookings ADD COLUMN rejection_reason TEXT;

-- CREATE TABLE IF NOT EXISTS profiles (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     user_id INTEGER UNIQUE,
--     full_name TEXT,
--     id_type TEXT,
--     id_number TEXT,
--     country TEXT,
--     phone TEXT,
--     email TEXT,
--     verified INTEGER DEFAULT 0,
--     FOREIGN KEY (user_id) REFERENCES users(id)
-- );


-- -- Users table
-- CREATE TABLE IF NOT EXISTS users (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     username TEXT UNIQUE NOT NULL,
--     password TEXT NOT NULL,
--     role TEXT NOT NULL CHECK(role IN ('admin', 'customer'))
-- );

-- -- Cars table
-- CREATE TABLE IF NOT EXISTS cars (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     make TEXT NOT NULL,
--     model TEXT NOT NULL,
--     year INTEGER NOT NULL,
--     mileage INTEGER NOT NULL,
--     available INTEGER NOT NULL CHECK(available IN (0,1)),
--     daily_rate REAL NOT NULL
-- );

-- -- Bookings table
-- CREATE TABLE IF NOT EXISTS bookings (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     user_id INTEGER NOT NULL,
--     car_id INTEGER NOT NULL,
--     start_date TEXT NOT NULL,
--     end_date TEXT NOT NULL,
--     total_cost REAL NOT NULL,
--     status TEXT NOT NULL CHECK(status IN ('pending', 'approved', 'rejected')),
--     FOREIGN KEY(user_id) REFERENCES users(id),
--     FOREIGN KEY(car_id) REFERENCES cars(id)
-- );