from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from predictor import XLS_R
import os
from gtts import gTTS
from .serializers import AudioSerializer
from .models import Audio
from translator import Translator

@api_view(['GET'])
def get_home(request):

    # Obtain all the entires
    entries = Audio.objects.all()
    serializer = AudioSerializer(entries, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def predict(request):

    serializer = AudioSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        obj = XLS_R()
        
        Audio.objects.all().delete()
        path = dict(serializer.data)['file'][1:]
        translator = Translator()
        print(obj.predict(path), '\n\n')
        
        prediction = {'Prediction': translator.translate(obj.predict(path))}

        english = gTTS(text=prediction['Prediction'], lang='en', slow=False)
        english.save(path[:-4] + '_english' + path[-4:])

        os.remove(path)

        return Response(prediction)
        
    print(serializer.is_valid())

    # return Response(serializer.data)