from dataclasses import dataclass  # noqa
from datetime import date
from typing import Optional, List, Set  # Support for type hints

# frozen: If true (the default is False), assigning to fields will generate an
# exception. This emulates read-only frozen instances
@dataclass(frozen=True)
class OrderLine:
    """An order line is uniquely identified by its order ID, SKU, and quantity;
    if we change one of those values, we now have a new line.

    Attributes:
        orderid The maximum speed that such a bird can attain.
        sku     A product is identified by a SKU, pronounced "skew", which is
                a short for stock-keeping unit.
        qty     Quantity requested.
    """

    orderid: str
    sku: str
    qty: int


class Batch:
    """The purchasing department orders small batches of stock. A batch of stock
    has a unique ID called a reference, a SKU, and a quantity.

    Attributes:
        ref     Batch unique ID.
        sku     A product is identified by a SKU, pronounced "skew", which is
                short for stock-keeping unit.
        qty     Quantity requested.
        eta     Estimated time of batch arrival.
    """

    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self.available_quantity = qty

    def allocate(self, line: OrderLine):
        self.available_quantity -= line.qty

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
