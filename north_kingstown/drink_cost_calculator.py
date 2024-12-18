# calculates price of a single drink (ome ounce/shot)

# example: jim beam orange
# bottle mls: 1 liter
# bottle price: $23.75
# pour cost percent: 14%
# shrinkage percent: 20%
# garnish: 50 cents
# final drink cost: $6.50


class Bottle:
    """
    A base class to represent a liquor bottle.

    Attributes:
        mls (int): The size of the bottle in milliliters.
        price (float): The price of the bottle in dollars.
        
    Methods:
        convert_mls_to_ozs(self) -> float
            Convert the bottle size from milliliters to ounces.
            
        get_cost_per_oz(self) -> float:
            Calculate the cost of liquor per ounce.
    """
    _MLS_TO_OZS = 29.574
    _ROUND_TO = 2
    
    def __init__(self, mls: int, price: float):
        self.mls = mls
        self.price = price
        
    def _convert_mls_to_ozs(self) -> float:
        """Convert the bottle size from milliliters to ounces."""
        return round(self.mls / self._MLS_TO_OZS, self._ROUND_TO)
    
    def _get_cost_per_oz(self) -> float:
        """Get the cost of liquor per ounce."""
        ozs = self._convert_mls_to_ozs()
        return round(self.price / ozs, self._ROUND_TO)
    
    
class DrinkCostCalculator(Bottle):
    """
    A class to calculate the cost of a single drink. 
    Inherits from the Bottle class.

    Attributes:
        pour_cost_percent (float): A percentage to calculate the drink's 
            cost from a proposed profit margin e.g., 0.14 for 14% - 
            means a proposed profit margin of 86%.
        shrinkage_percent (float): The percentage of the drink cost lost due 
            to waste or overpouring e.g., 0.2 for 20%.
        garnish (float): The fixed cost of garnishes for the drink in dollars 
            e.g., $0.50.

    Methods:
        get_base_drink_cost(self) -> float:
            Calculates the base cost of the drink using the cost per ounce of liquor 
            and the desired pour cost percentage. 
        get_shrinkage_cost(self) -> float:
            Calculates the additional cost due to shrinkage (waste or overpouring). 
        get_drink_cost(self) -> str:
            Calculates the final cost of the drink, summing base cost, shrinkage, and garnish, 
            formatted as a string with a dollar sign.
    """
    
    def __init__(self,
                 mls, 
                 price, 
                 pour_cost_percent=0.14,
                 shrinkage_percent=0.2,
                 garnish=0.5):
        super().__init__(mls, price)
        self.pour_cost_percent = pour_cost_percent
        self.shrinkage_percent = shrinkage_percent
        self.garnish = garnish
        
    def _get_base_drink_cost(self) -> float:
        return round(self._get_cost_per_oz() / self.pour_cost_percent, 
                     self._ROUND_TO)
        
    def _get_shrinkage_cost(self) -> float:
        return round(self._get_base_drink_cost() * self.shrinkage_percent, 
                     self._ROUND_TO)
        
    def get_drink_cost(self) -> float:
        return f'''${
            self._get_base_drink_cost() + 
            self._get_shrinkage_cost() + 
            self.garnish
            :.2f}'''
            

jim_bean_orange = DrinkCostCalculator(1000, 23.75)
print(jim_bean_orange.get_drink_cost())