
def success_response(data=None,status=True, message="success"):
    if data is None:
        data = []
    return {
        "status": status,
        "message": message,
        "data": data
    }

# custom serializer for Sell model
def custom_sell_data(sell):
    return {
        "id": sell.id,
        "facture_number": sell.facture_number,
        "date_sold": sell.date_sold,
        "user_id": sell.user_id,
        "status": sell.status,
        "user": {
            "id": sell.user.id,
            "name": sell.user.name
        },
        "sell_items": [
            {
                "id": item.id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "price_per_unit": item.price_per_unit,
                "total_price": item.total_price,
                "product": {
                    "id": item.product.id,
                    "name": item.product.name
                }
            }
            for item in sell.sell_items
        ]
    }