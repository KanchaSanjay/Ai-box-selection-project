from .models import Box


def recommend_box(products):
    """Simple recommendation: find smallest-cost box that fits products stacked by height."""

    products = list(products)
    if not products:
        return None

    total_weight = sum(p.weight for p in products)

    max_length = max(p.length for p in products)
    max_width = max(p.width for p in products)
    total_height = sum(p.height for p in products)

    suitable_boxes = []

    for box in Box.objects.all():
        if (
            box.length >= max_length and
            box.width >= max_width and
            box.height >= total_height and
            box.max_weight >= total_weight
        ):
            suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    suitable_boxes.sort(key=lambda b: b.cost)

    return suitable_boxes[0]
