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


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line(sku="ELEGANTLAMP", batch_qty=20, line_qty=2)
    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = make_batch_and_line(sku="ELEGANTLAMP", batch_qty=2, line_qty=20)
    assert small_batch.can_allocate(large_line) is False


def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line(sku="ELEGANT-LAMP", batch_qty=2, line_qty=2)
    assert batch.can_allocate(line)


def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
    different_sku_line = OrderLine("order-123", "EXPENSIVETOASTER", 10)
    assert batch.can_allocate(different_sku_line) is False
