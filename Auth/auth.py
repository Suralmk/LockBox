import sqlite3
import bcrypt
from cryptography.fernet import Fernet

class LockBoxAuth:
    def __init__(self, db_path="lockbox_auth.db"):
        self.db_path = db_path
        self.key = Fernet.generate_key() 
        self.cipher = Fernet(self.key)
        self._initialize_db()
        self.register_user()

    def _initialize_db(self):
        """
        Initialize the SQLite database and create the users table.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS LockBox (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_location TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            passphrase BLOB, 
            secret_phrase BLOB 
        )
        """)
        conn.commit()
        conn.close()

    def user_exists(self):
        """
        Check if a user exists in the database.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        result = cursor.fetchone()
        conn.close()
        return result[0] > 0  # Returns True if user exists, False if not

    def register_user(self, passphrase="121212", password="123" ):
        """
        Register a new user with hashed password and optional encrypted data.
        """
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        passphrase = self.cipher.encrypt(passphrase.encode('utf-8')) 

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("""
            INSERT INTO users ( password_hash, passphrase)
            VALUES (?, ?)
            """, ( password_hash, passphrase))
            conn.commit()
            print("User registered successfully.")
        except sqlite3.IntegrityError:
            print("Error: Username already exists.")
        finally:
            conn.close()

    def authenticate_user(self, password):
        """
        Authenticate a user by comparing stored hash with the provided password.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT password_hash FROM users ")
        result = cursor.fetchone()
        conn.close()

        print(result)
        if result:
            stored_hash = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                print("Authentication successful!")
                return True
            else:
                print("Authentication failed: Incorrect password.")
        else:
            print("Authentication failed: User not found.")
        return False
