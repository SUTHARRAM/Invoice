from django.http import JsonResponse
from django.db import connection

def fetch_data_from_postgres(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT UserID, UserName FROM userdetail")
        rows = cursor.fetchall()
    # Convert rows to JSON response
    data = [{'UserID': row[0], 'UserName': row[1]} for row in rows]
    return JsonResponse(data, safe=False)
