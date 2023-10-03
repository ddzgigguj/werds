import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS product
        """
    )
    cursor.execute(
        """
       DROP TABLE IF EXISTS category
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS questions (
            rId INTEGER PRIMARY KEY AUTOINCREMENT,
            userId INTEGER
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS product (
            productId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price FLOAT,
            categoryId INTEGER,
            FOREIGN KEY (categoryId) REFERENCES category (id)
        )
        """
    )
    db.commit()


def populate_tables():
    cursor.execute(
        """
        INSERT INTO category (name)
        VALUES ('ФруктыК'), 
                ('ЯгодыК'), 
                ('ОвощиК')
        """
    )
    cursor.execute(
        """
        INSERT INTO product (name, price, categoryId)
        VALUES ('Фрукты', 25.0, 1),
                ('Фрукты2', 25, 1),
                ('Ягоды', 19.0, 2),
                ('Ягоды2', 19.0, 2),
                ('Овощи', 26.0, 3),
                ('Овощи2', 26.0, 3)
        """
    )

def save_question(user_id):
    cursor.execute(
            """
            INSERT INTO questions (userId)
            VALUES (:user_id)
            """,
            {
                "user_id": user_id,
            },
        )
    db.commit()

def select_users():
    cursor.execute("SELECT * FROM questions")
    return cursor.fetchall()

def get_products():
    cursor.execute(
        """
        SELECT p.name, c.name FROM product p JOIN category c ON p.categoryId = c.id
        """
    )
    return cursor.fetchall()

def get_product_by_category(category_id):
    cursor.execute(
        """
        SELECT * FROM product WHERE categoryId = :c_id
        """,
        {"c_id": category_id},
    )
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
