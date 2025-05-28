import psycopg2
from psycopg2 import extras

connection = psycopg2.connect(dbname='films')

try:
    with connection:
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute("""SELECT genre, count(id) FROM films
                            WHERE duration < 110
                                GROUP BY genre""")
            counts = cursor.fetchall()
finally:
    connection.close()

print(counts)
for genre, count in counts:
    print(f'{genre}: {count}')
