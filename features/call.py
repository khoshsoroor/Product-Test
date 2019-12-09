import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


# region TRUNCATE cities
def delete_cities():
    try:
        ps_connection = psycopg2.connect(user=os.getenv("PGADMIN_USER"),
                                         password=os.getenv("PGADMIN_PASSWORD"),
                                         host=os.getenv("HOST"),
                                         port=os.getenv("PORT"),
                                         database=os.getenv("DATABASE"))
        cursor = ps_connection.cursor()
        cursor.execute("TRUNCATE TABLE cities cascade;")
        ps_connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")


# endregion


# region TRUNCATE services
def delete_services():
    try:
        ps_connection = psycopg2.connect(user=os.getenv("PGADMIN_USER"),
                                         password=os.getenv("PGADMIN_PASSWORD"),
                                         host=os.getenv("HOST"),
                                         port=os.getenv("PORT"),
                                         database=os.getenv("DATABASE"))
        cursor = ps_connection.cursor()
        cursor.execute("TRUNCATE TABLE services cascade;")
        ps_connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()


# endregion
# region TRUNCATE categories
def delete_categories():
    try:
        ps_connection = psycopg2.connect(user=os.getenv("PGADMIN_USER"),
                                         password=os.getenv("PGADMIN_PASSWORD"),
                                         host=os.getenv("HOST"),
                                         port=os.getenv("PORT"),
                                         database=os.getenv("DATABASE"))
        cursor = ps_connection.cursor()
        cursor.execute("TRUNCATE TABLE categories cascade;")
        ps_connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()


# endregion
# region TRUNCARE zones
def delete_zones():
    try:
        ps_connection = psycopg2.connect(user=os.getenv("PGADMIN_USER"),
                                         password=os.getenv("PGADMIN_PASSWORD"),
                                         host=os.getenv("HOST"),
                                         port=os.getenv("PORT"),
                                         database=os.getenv("DATABASE"))
        cursor = ps_connection.cursor()
        cursor.execute("TRUNCATE TABLE zones cascade;")
        ps_connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()
# endregion


# region TRUNCATE services
def delete_city_services():
    try:
        ps_connection = psycopg2.connect(user=os.getenv("PGADMIN_USER"),
                                         password=os.getenv("PGADMIN_PASSWORD"),
                                         host=os.getenv("HOST"),
                                         port=os.getenv("PORT"),
                                         database=os.getenv("DATABASE"))
        cursor = ps_connection.cursor()
        cursor.execute("TRUNCATE TABLE city_services cascade;")
        ps_connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()


# endregion


# region TRUNCATE category services
def delete_cat_services():
    try:
        ps_connection = psycopg2.connect(user=os.getenv("PGADMIN_USER"),
                                         password=os.getenv("PGADMIN_PASSWORD"),
                                         host=os.getenv("HOST"),
                                         port=os.getenv("PORT"),
                                         database=os.getenv("DATABASE"))
        cursor = ps_connection.cursor()
        cursor.execute("TRUNCATE TABLE category_services cascade;")
        ps_connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()


# endregion


# region TRUNCATE offices
def delete_offices():
    try:
        ps_connection = psycopg2.connect(user=os.getenv("PGADMIN_USER"),
                                         password=os.getenv("PGADMIN_PASSWORD"),
                                         host=os.getenv("HOST"),
                                         port=os.getenv("PORT"),
                                         database=os.getenv("DATABASE"))
        cursor = ps_connection.cursor()
        cursor.execute("TRUNCATE TABLE offices cascade;")
        ps_connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()


# endregion


# region TRUNCATE facilities
def delete_facilities():
    try:
        ps_connection = psycopg2.connect(user=os.getenv("PGADMIN_USER"),
                                         password=os.getenv("PGADMIN_PASSWORD"),
                                         host=os.getenv("HOST"),
                                         port=os.getenv("PORT"),
                                         database=os.getenv("DATABASE"))
        cursor = ps_connection.cursor()
        cursor.execute("TRUNCATE TABLE facilities cascade;")
        ps_connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()


# endregion


# region TRUNCATE service facilities
def delete_facility_service():
    try:
        ps_connection = psycopg2.connect(user=os.getenv("PGADMIN_USER"),
                                         password=os.getenv("PGADMIN_PASSWORD"),
                                         host=os.getenv("HOST"),
                                         port=os.getenv("PORT"),
                                         database=os.getenv("DATABASE")
                                         )
        cursor = ps_connection.cursor()
        cursor.execute("TRUNCATE TABLE service_facilities cascade;")
        ps_connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection
        if (ps_connection):
            cursor.close()
            ps_connection.close()
# endregion
