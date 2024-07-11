from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder

token = RtcTokenBuilder.buildTokenWithAccount(appId,appCertificate, channelName, account, role, privilegeExpiredTs)





def lobby(request):
    return render(request,'vdo/lobby.html')

def room(request):
    return render(request,'vdo/room.html')

