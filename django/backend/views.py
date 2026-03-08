from django.http import JsonResponse
import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="database", user="root", password="secret", database="myapp"
    )

def get_users(request):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return JsonResponse(users, safe=False)
