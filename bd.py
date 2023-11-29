import sqlite3
import os
import bcrypt


def create_database():
    if not os.path.exists('bd.db'):
        conn = sqlite3.connect('bd.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user TEXT NOT NULL,
                      password TEXT NOT NULL)''')
        c.execute('''CREATE TABLE t_productos
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      t_producto TEXT NOT NULL)''')
        c.execute('''CREATE TABLE productos
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      producto TEXT NOT NULL,
                      t_producto TEXT NOT NULL)''')
        c.execute('''CREATE TABLE entradas
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      tipo TEXT NOT NULL,
                      nombre TEXT NOT NULL,
                      cantidad REAL NOT NULL,
                      p_unitario REAL NOT NULL,
                      p_total REAL NOT NULL,
                      fecha_entrada TEXT NOT NULL,
                      u_m TEXT NOT NULL)''')
        c.execute('''CREATE TABLE salidas
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      tipo TEXT NOT NULL,
                      nombre TEXT NOT NULL,
                      cantidad REAL NOT NULL,
                      fecha_salida TEXT NOT NULL,
                      u_m TEXT NOT NULL)''')
        conn.commit()
        conn.close()
        print('Database created successfully.')
    else:
        print('Database already exists.')


def get_user(username,password):
    conn = sqlite3.connect('bd.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user = ?", (username,))
    user = c.fetchone()
    conn.close()
    if user is None:
        return None
    hashed_password = user[2]
    password_encoded = password.encode('utf-8')
    if bcrypt.checkpw(password_encoded, hashed_password):
        return user
    else:
        return None


def has_users():
    conn = sqlite3.connect('bd.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM users")
    count = c.fetchone()[0]
    conn.close()

    return count > 0


def insert_user(username, password):
    conn = sqlite3.connect('bd.db')
    c = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    c.execute("INSERT INTO users (user, password) VALUES (?, ?)",(username, hashed_password))
    conn.commit()
    conn.close()
