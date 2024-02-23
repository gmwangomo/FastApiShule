import mysql.connector

def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user = "root",
        password="Mwangomo#1",
        database="fastApiShule"
    )