class Delivery:
    def __init__(self, order_id, deadline):
        self.order_id = order_id
        self.deadline = deadline

def schedule_deliveries(deliveries):
    # Sort by earliest deadline first
    deliveries.sort(key=lambda x: x.deadline)

    print("Delivery Schedule:")
    for delivery in deliveries:
        print(f"Order {delivery.order_id} -> Deadline {delivery.deadline}")

deliveries = [
    Delivery(1, 4),
    Delivery(2, 2),
    Delivery(3, 1),
    Delivery(4, 3)
]

schedule_deliveries(deliveries)
