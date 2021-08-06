from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerailzer
from .models import Note

@api_view(['GET'])
def get_routes(request):
    routes = [{
        'Endpoint': '/notes/',
        'method': 'GET',
        'body': None,
        'description': 'Returns an array of notes object'
    },
    {
        'Endpoint': '/notes/id',
        'method': 'GET',
        'body': None,
        'description': 'Returns a single note object'
    },
    {
        'Endpoint': '/notes/create',
        'method': 'POST',
        'body': {'body':""},
        'description': 'Creates an existing note with data sent in body'
    },
    {
        'Endpoint': '/notes/id/update',
        'method': 'POST',
        'body': {'body':""},
        'description': 'Updates an existing note with data sent in body'
    },
    {
        'Endpoint': '/notes/id/delete',
        'method': 'POST',
        'body': {'body':""},
        'description': 'Deletes an existing note'
    },
    ]

    return Response(routes)

@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerailzer(notes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_note(request,pk):
    note = Note.objects.get(pk=pk)
    serializer = NoteSerailzer(note,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_note(request):
    data = request.data #returns python dict 
    note = Note.objects.create(body = data['body'])
    serializer = NoteSerailzer(note,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_note(request,pk):
    data = request.data 
    note = Note.objects.get(pk=pk)
    serializer = NoteSerailzer(note,data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_note(request,pk):
    note = Note.objects.get(pk=pk).delete()
    return Response('Note was deleted!')