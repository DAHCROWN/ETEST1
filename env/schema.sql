DROP TABLE IF EXISTS test_users;
DROP TABLE IF EXISTS testquestion;
DROP TABLE IF EXISTS admins;

CREATE TABLE test_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    otp TEXT NOT NULL,
    score INTEGER NOT NULL,
    statuss BOOLEAN NOT NULL,
);
CREATE TBALE testquestion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    optiona TEXT NOT NULL,
    optionb TEXT NOT NULL,
    optionc TEXT NOT NULL,
    optiond TEXT NOT NULL,
    correct TEXT NOT NULL,
);
CREATE TABLE admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_id TEXT NOT NULL,
    password TEXT NOT NULL,
    );