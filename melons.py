"""Classes for melon orders."""
import random
from datetime import datetime

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):

        price = random.randint(5,9)
        now = datetime.now()
        hour = now.hour
        day = datetime.date(now)
        day_of_the_week = day.weekday()

        if day_of_the_week < 5 and hour >= 8 and hour < 11:
            price = price + 4
            
        return price
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True







    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    # order_type = None
    # tax = 0

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__( species, qty, "domestic", 0.08)
        """Initialize melon order attributes."""



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__( species, qty, "international", 0.17)

        self.country_code = country_code
       

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
    
    def get_total(self):
        total = super().get_total()
        if self.qty < 10:
            total = total + 3

        return total

    

class GovernmentMelonOrder(AbstractMelonOrder): 
    def __init__(self, species, qty):
        super().__init__( species, qty, "government", 0.00)

        self.passed_inspection = False

    def mark_inspection(self, passed):
        
        self.passed_inspection = passed

    

# dom = DomesticMelonOrder("cren", 5)
# print(dom.get_base_price())