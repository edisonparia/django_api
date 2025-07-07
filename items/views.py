from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

items = []

@csrf_exempt
def items_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode() or '{}')
        except json.JSONDecodeError:
            data = {}
        name = data.get('name')
        if not name:
            return JsonResponse({'error': 'name is required'}, status=400)
        item = {'id': len(items) + 1, 'name': name}
        items.append(item)
        return JsonResponse(item, status=201)
    return JsonResponse(items, safe=False)
