from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .responses import get_best_response
from .models import Conversation, UploadedFile

# Define the index view to render the chat page
def index(request):
    return render(request, 'chat/chatPage.html')

# Chatbot view to respond to messages
@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '').lower()

        # Get bot response
        bot_response = get_best_response(user_message)

        # Save the conversation in the database
        conversation = Conversation.objects.create(user_message=user_message, bot_response=bot_response)

        return JsonResponse({
            'bot_response': bot_response
        }, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Handle file uploads
@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']

        # Create a conversation record for the file (optional)
        conversation = Conversation.objects.create(user_message="", bot_response="File uploaded")

        # Save the file in the database
        uploaded_file = UploadedFile.objects.create(
            conversation=conversation,
            file=file
        )

        return JsonResponse({
            'success': True,
            'file_id': uploaded_file.id,
            'file_url': uploaded_file.file.url
        })

    return JsonResponse({'success': False, 'error': 'No file uploaded.'})
