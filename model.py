from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set # Support for type hints

# frozen: If true (the default is False), assigning to fields will generate an
# exception. This emulates read-only frozen instances
@dataclass(frozen=True)
class OrderLine:
    """An order line is uniquely identified by its order ID, SKU, and quantity;
    if we change one of those values, we now have a new line.

    Attributes:
        orderid The maximum speed that such a bird can attain.
        sku     A product is identified by a SKU, pronounced "skew", which is 
                short for stock-keeping unit.
        qty     Quantity.
    """
    orderid: str
    sku: str
    qty: int

class Batch:
    def __init__(self, ref: str, sku:str, qty:int, eta:Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self.available_quantity = qty

    def allocate(self, line: OrderLine):
        self.available_quantity -= line.qty
        