from datetime import date, timedelta
import pytest
from model import OrderLine, Batch
# from model import allocate, OrderLine, Batch, OutOfStock


def make_batch_and_line(sku, batch_qty, line_qty):
    return(
        Batch(ref="batch-001", sku=sku, qty=batch_qty, eta=date.today),
        OrderLine(orderid="order-123", sku=sku, qty=line_qty)
    )


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine('order-ref', "SMALL-TABLE", qty=2)
    batch.allocate(line)
    assert batch.available_quantity == 18
