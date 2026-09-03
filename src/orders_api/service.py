from typing import Any

orders: list[dict[str, Any]] = []


def get_orders():
    return orders


def create_order(customer: str, amount: float):
    order = {
        "id": len(orders) + 1,
        "customer": customer,
        "amount": amount,
    }

    orders.append(order)

    return order


def delete_order(order_id: int):
    global orders

    orders = [
        order
        for order in orders
        if order["id"] != order_id
    ]

    return {
        "message": f"Order {order_id} deleted"
    }