from db import db_cur

def get_flights_board():
    with db_cur(dictionary=True) as cursor:
        cursor.execute("Select flight_id, departure_date, origin_airport, destination_airport from flights Where flight_status='Active'")
        flights_data = cursor.fetchall()
        return flights_data
