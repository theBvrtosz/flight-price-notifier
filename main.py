from utils import get_flights_div_list
from flight_data import AzAirFlight

if __name__ == '__main__':
    flights_list = get_flights_div_list()

    for flight_div in flights_list:
        azair_flight = AzAirFlight(flight_div=flight_div, is_two_way=False)
        