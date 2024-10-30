import mysql.connector
import Config

def connect_to_db():
 
    try:
        mydb = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        if mydb.is_connected():
            print("Ture")
            return mydb
    except mysql.connector.Error as e:
        print(e)
        return None
    return None

def add_expense_to_db(category, amount, date):
    mydb = connect_to_db()
    if mydb:
        try:
            cursor = mydb.cursor()
            sql_insert = "INSERT INTO Expense (Category, Amount, Date) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert, (category, amount, date))
            mydb.commit()
            cursor.close()
        except mysql.connector.Error as e:
            return str(e)
    return None

def get_summary_by_category():
    mydb = connect_to_db()
    if mydb:
        try:
            cursor = mydb.cursor()
            cursor.execute("SELECT Category, SUM(Amount) FROM Expense GROUP BY Category")
            data = cursor.fetchall()
            cursor.close()
            return data
        except mysql.connector.Error as e:
            return str(e)
    return []

def delete_entry_from_db(category, amount):
    mydb = connect_to_db()
    if mydb:
        try:
            cursor = mydb.cursor()
            sql_delete = "DELETE FROM Expense WHERE Category = %s AND Amount = %s"
            cursor.execute(sql_delete, (category, amount))
            mydb.commit()
            cursor.close()
        except mysql.connector.Error as e:
            return str(e)
    return None

connect_to_db()