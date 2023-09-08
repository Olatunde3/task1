from  rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Slack
from .serializer import Slackserializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    slack = Slack.objects.all()
    serializer = Slackserializer(slack, many=True)
    return Response(serializer.data)