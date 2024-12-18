from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from workers.models import Worker
from workers.serializers import WorkerSerializer



class WorkerListView(APIView):
    def get(self, request, team_id):
        workers = Worker.objects.select_related('team').filter(team_id=team_id)
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class WorkerDetailView(APIView):
    def get(self, request, worker_id):
        try:
            worker = Worker.objects.get(id=worker_id)
            serializer = WorkerSerializer(worker)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Worker.DoesNotExist:
            return Response({'error': 'Worker not found'}, status=status.HTTP_404_NOT_FOUND)
