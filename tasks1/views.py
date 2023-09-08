from django.http import JsonResponse
from .models import Slack

# Create your views here.

def my_api(request):
    data = {
        'data': list(Slack.objects.values()),
    }
    return JsonResponse(data)
