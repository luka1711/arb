import sqlite3

def test_connection():
    conn = None
    try:
        conn = sqlite3.connect('/Users/luka/PycharmProjects/ods_extract_new/odds_extract.db')
        cursor = conn.cursor()
        print("Connection successful!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    test_connection()