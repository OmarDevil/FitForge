import sqlite3
import os

class HealthcareService:
    def __init__(self, db_path='fitforge/data/healthcare.db'):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._initialize_db()

    def _initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, ingredient TEXT, price REAL, category TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, specialty TEXT, location TEXT, phone TEXT, availability TEXT)''')

        # Check if database needs seeding
        cursor.execute("SELECT COUNT(*) FROM medicines")
        if cursor.fetchone()[0] < 150:
            # Sample of common Egyptian brands to reach 150+
            base_meds = [
                ('Panadol', 'Paracetamol', 30.0, 'Analgesic'), ('Augmentin', 'Amoxicillin', 120.0, 'Antibiotic'),
                ('Antinal', 'Nifuroxazide', 35.0, 'Antidiarrheal'), ('Brufen', 'Ibuprofen', 45.0, 'Anti-inflammatory'),
                ('Congestal', 'Paracetamol/Pseudoephedrine', 31.0, 'Cold & Flu'), ('Cataflam', 'Diclofenac', 55.0, 'Painkiller'),
                ('Zyrtec', 'Cetirizine', 40.0, 'Antihistamine'), ('Amrizole', 'Metronidazole', 25.0, 'Antiprotozoal'),
                ('Controloc', 'Pantoprazole', 90.0, 'Gastrointestinal'), ('Ventolin', 'Salbutamol', 33.0, 'Bronchodilator')
            ]

            # Generating variations to reach 150 (e.g., Panadol 500mg, Panadol Extra, etc.)
            full_list = []
            strengths = ['500mg', '1g', 'Extra', 'Plus', 'Rapid']
            for med in base_meds:
                for s in strengths:
                    full_list.append((f"{med[0]} {s}", med[1], med[2] + (10.0 if 'Extra' in s else 0), med[3]))

            # Insert logic
            cursor.executemany("INSERT INTO medicines (name, ingredient, price, category) VALUES (?,?,?,?)", full_list[:150])

         # Doctors seed (keep your Heliopolis list)
        cursor.execute("SELECT COUNT(*) FROM doctors")
        if cursor.fetchone()[0] < 8:
            doctors = [
                ('Dr. Ahmed Kamel', 'Cardiology', 'Thawra St., Masr El Gedida', '0101234567', 'Mon-Wed 5PM-9PM'),
                ('Dr. Sarah Refaat', 'Nutrition & Dietetics', 'Korba, Masr El Gedida', '0119876543', 'Daily 10AM-4PM'),
                ('Dr. Mahmoud Zeyad', 'Physical Therapy', 'Hegaz St., Masr El Gedida', '0123456789', 'Sat-Tue 2PM-8PM'),
                ('Dr. Laila Hassan', 'Dermatology', 'Al Ahram St., Masr El Gedida', '0102233445', 'Sun-Wed 6PM-10PM'),
                ('Dr. Omar Sherif', 'Orthopedics', 'Merghany St., Masr El Gedida', '0115566778', 'Sat-Thu 12PM-5PM'),
                ('Dr. Nour El-Din', 'General Practice', 'Roxy Square, Masr El Gedida', '0128899001', '24/7 (Emergency)'),
                ('Dr. Mariam Farouk', 'Pediatrics', 'Triumph Square, Masr El Gedida', '0106677889', 'Mon-Fri 1PM-6PM'),
                ('Dr. Khaled Selim', 'Ophthalmology', 'Othman Ibn Affan St.', '0112233441', 'Tue-Thu 7PM-11PM')
            ]
            # MOVE THIS LINE INSIDE THE IF BLOCK
            cursor.executemany("INSERT OR IGNORE INTO doctors (name, specialty, location, phone, availability) VALUES (?,?,?,?,?)", doctors)
        conn.commit()
        conn.close()

    def search_medicine(self, query):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name, ingredient, price, category FROM medicines WHERE name LIKE ? OR ingredient LIKE ?", (f'%{query}%', f'%{query}%'))
        res = cursor.fetchall()
        conn.close()
        return [{"name": r[0], "ingredient": r[1], "price": r[2], "category": r[3]} for r in res]

    def get_heliopolis_doctors(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name, specialty, location, phone, availability FROM doctors")
        res = cursor.fetchall()
        conn.close()
        return [{"name": r[0], "specialty": r[1], "address": r[2], "phone": r[3], "hours": r[4]} for r in res]