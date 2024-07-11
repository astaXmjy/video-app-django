from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
import json
from .models import RoomMember
from django.views.decorators.csrf import csrf_exempt

def get_token(request):
    appId='27458ea54224470197fbdcdab08e0c3c'
    appCertificate='357f80f0533e40afbd8f2abc03da3720'
    channelName=request.GET.get('channel')
    uid=random.randint(1,230)
    expirationTimeInSeconds=3600*24
    currentTimeStamp=time.time()
    privilegeExpiredTs=currentTimeStamp+expirationTimeInSeconds
    role=1
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token,'uid':uid},safe=False)


def lobby(request):
    return render(request,'vdo/lobby.html')

def room(request):
    return render(request,'vdo/room.html')
@csrf_exempt
def createUser(request):
    data=json.loads(request.body)
    member,created=RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    return JsonResponse({'name':data['name']},safe=False)

def getUser(request):
    uid=request.GET.get('uid')
    room_name=request.GET.get('room_name')

    member=RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )

    return JsonResponse({'name':member.name},safe=False)

@csrf_exempt
def deleteUser(request):
    data=json.loads(request.body)
    member=RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name'],
    )
    member.delete()
    return JsonResponse('member was deleted',safe=False)