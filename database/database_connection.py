import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="aimlb3",
        database="hospital_db"
    )

    return connection