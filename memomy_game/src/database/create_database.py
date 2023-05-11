from database.player_database import Database


def create_database():
    database = Database()
    if database.table_exists() is False:
        database.create_table()

    print('"player_database.db" has been created.')


create_database()
