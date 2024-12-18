from django.urls import path

from workers.views import WorkerDetailView, WorkerListView


urlpatterns = [
    path('api/v1/team/<int:team_id>/WorkerList', WorkerListView.as_view(), name='worker-list'),
    path('api/v1/worker/<int:worker_id>', WorkerDetailView.as_view(), name='worker-detail'),
]
