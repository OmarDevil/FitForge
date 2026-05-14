import sqlite3
import os

class MedicineService:
    def __init__(self, db_path='fitforge/data/healthcare.db'):
        self.db_path = db_path
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._initialize_db()

    def _initialize_db(self):
        """Creates the medicine table and seeds it with initial Egyptian data."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS medicines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                active_ingredient TEXT,
                price_egp REAL,
                category TEXT
            )
        ''')

        # Seed initial data (Common Egyptian Medications)
        medicines = [
            ('Panadol Advance', 'Paracetamol', 30.0, 'Analgesic'),
            ('Augmentin 1g', 'Amoxicillin + Clavulanic Acid', 120.0, 'Antibiotic'),
            ('Concor 5mg', 'Bisoprolol', 45.0, 'Cardiovascular'),
            ('Antinal', 'Nifuroxazide', 35.0, 'Antidiarrheal'),
            ('Brufen 400mg', 'Ibuprofen', 40.0, 'NSAID')
        ]

        # Only insert if empty to avoid duplicates
        cursor.execute("SELECT COUNT(*) FROM medicines")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO medicines (name, active_ingredient, price_egp, category) VALUES (?, ?, ?, ?)",
                medicines
            )

        conn.commit()
        conn.close()

    def search_medicine(self, query):
        """Searches by name or active ingredient."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        search_term = f"%{query}%"
        cursor.execute('''
            SELECT name, active_ingredient, price_egp, category
            FROM medicines
            WHERE name LIKE ? OR active_ingredient LIKE ?
        ''', (search_term, search_term))

        results = cursor.fetchall()
        conn.close()

        return [{"name": r[0], "ingredient": r[1], "price": r[2], "type": r[3]} for r in results]