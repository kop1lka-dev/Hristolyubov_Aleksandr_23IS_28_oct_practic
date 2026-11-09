import psycopg

print("Скрипт запущен, пробую подключиться...")

минимум = 7

with psycopg.connect(
    dbname="organic_chemistry",
    user="postgres",
    password="Admin",  # <--- ОБЯЗАТЕЛЬНО ЗАМЕНИ НА СВОЙ ПАРОЛЬ
    host="localhost",
    port=5432,
    connect_timeout=5
) as соединение:
    with соединение.cursor() as курсор:
        курсор.execute("""
            SELECT name, formula, carbon_count
            FROM public.alkanes
            WHERE carbon_count >= %s
            ORDER BY carbon_count ASC
        """, (минимум,))
        алканы = курсор.fetchall()

print("Данные получены, вывожу на экран:")

for алкан in алканы:
    print(алкан[0], алкан[1], алкан[2])