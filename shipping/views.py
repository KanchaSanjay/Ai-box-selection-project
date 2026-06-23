from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .services import recommend_box


@api_view(['POST'])
def box_recommendation(request):
    product_ids = request.data.get('products', [])
    if not isinstance(product_ids, (list, tuple)):
        return Response({'detail': '`products` must be a list of ids'}, status=400)

    products = Product.objects.filter(id__in=product_ids)

    box = recommend_box(products)

    if not box:
        return Response({
            'message': 'No suitable box found'
        })

    return Response({
        'recommended_box': box.name,
        'cost': str(box.cost)
    })
