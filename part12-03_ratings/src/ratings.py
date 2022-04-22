def sort_by_ratings(items: list):
    def order_by_ratings(item: dict):
        return item["rating"]
    return sorted(items, key=order_by_ratings, reverse=True)