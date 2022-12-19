from .flight import Flight
from bs4.element import Tag

class AzAirFlight(Flight):
    def __init__(self, flight_div: Tag, is_two_way: bool) -> None:
        super().__init__(flight_div, is_two_way)
        self._set_flight_info_paragraph()
        self._set_overall_flight_price()
        self._set_flight_depature_ariport_code()
        self._set_flight_depature_hour()
        self._set_flight_arrival_airport_code()
        self._set_flight_arrival_hour()
        self._set_flight_date()
        if is_two_way:
            self._set_return_flight_date()
            self._set_return_flight_depature_hour()
            self._set_return_flight_arrival_hour()

    def _set_flight_info_paragraph(self) -> None:
        # I should refactor later. Will do for now.
        paragraphs = self.flight_div.find_all("p")
        self._flight_info_paragraph = [paragraph for paragraph in paragraphs if paragraph.find("span", class_="caption tam") is not None][0]
        if self.is_two_way:
            self._return_flight_info_paragraph = [paragraph for paragraph in paragraphs if paragraph.find("span", class_="caption sem") is not None][0]

    def _set_overall_flight_price(self) -> None:
        price_div = self.flight_div.find("div", class_="totalPrice")
        self.price = price_div.find("span", class_="tp").text

    def _set_flight_depature_ariport_code(self) -> None:
        from_span = self._flight_info_paragraph.find("span", class_="from")
        self.depature_airport_code = from_span.find("span", class_="code").text
    
    def _set_flight_arrival_airport_code(self) -> None:
        to_span = self._flight_info_paragraph.find("span", class_="to")
        self.arrival_airport_code = to_span.find("span", class_="code").text
    
    def _set_flight_date(self) -> None:
        self.date = self._flight_info_paragraph.find("span", class_="date").text
    
    def _set_flight_depature_hour(self) -> None:
        depature_info = self._flight_info_paragraph.find("span", class_="from").text
        self.depature_hour = depature_info.split(" ")[0]

    def _set_flight_arrival_hour(self) -> None: 
        arrival_info = self._flight_info_paragraph.find("span", class_="to").text
        self.arrival_hour = arrival_info.split(" ")[0]

    def _set_return_flight_date(self) -> None:
        self.return_date = self._return_flight_info_paragraph.find("span", class_="date").text

    def _set_return_flight_arrival_hour(self) -> None:
        return_arrival_info = self._return_flight_info_paragraph.find("span", class_="to").text
        self.return_arrival_hour = return_arrival_info.split(" ")[0]

    def _set_return_flight_depature_hour(self) -> None:
        return_depature_info = self._return_flight_info_paragraph.find("span", class_="from").text
        self.return_depature_hour = return_depature_info.split(" ")[0]

    # # dunder methods
    # def __str__(self) -> str:
    #     return f"{self.price}, {self.date}, {self.depature_airport_code}, {self.depature_hour}, {self.arrival_airport_code}, {self.arrival_hour}"