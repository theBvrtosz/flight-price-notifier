from bs4.element import Tag

class Flight:
    def __init__(self, flight_div: Tag, is_two_way: bool) -> None:
        self.flight_div: Tag = flight_div
        self.is_two_way = is_two_way
        
    def _set_overall_flight_price(self) -> None:
        raise NotImplementedError
    
    def _set_flight_depature_ariport_code(self) -> None:
        raise NotImplementedError
    
    def _set_flight_arrival_airport_code(self) -> None:
        raise NotImplementedError
    
    def _set_flight_date(self) -> None:
        raise NotImplementedError
    
    # def set_flight_number(self) -> None:
    #     raise NotImplementedError
    
    def _set_flight_depature_hour(self) -> None:
        raise NotImplementedError
    
    def _set_flight_arrival_hour(self) -> None: 
        raise NotImplementedError
    
    def _set_return_flight_date(self) -> None:
        raise NotImplementedError
    
    # def set_return_flight_number(self) -> None:
    #     raise NotImplementedError
    
    def _set_return_flight_depature_hour(self) -> None:
        raise NotImplementedError
    
    def _set_return_flight_arrival_hour(self) -> None: 
        raise NotImplementedError
