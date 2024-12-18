from workers.models import Team, Worker


teams_data = [
    {"id": 1},
    {"id": 2},
]

for team_data in teams_data:
    Team.objects.get_or_create(**team_data)


workers_data = [
    {"id": 1, "last_name": "Иванов", "team_id": 1, "salary": 10000.00, "specialization": "Черновая отделка"},
    {"id": 2, "last_name": "Петров", "team_id": 2, "salary": 12000.00, "specialization": "Чистовая отделка"},
    {"id": 3, "last_name": "Сидоров", "team_id": 1, "salary": 16000.00, "specialization": "Бригадир"},
    {"id": 4, "last_name": "Сергеев", "team_id": 1, "salary": 20000.00, "specialization": "Прораб"},
    {"id": 5, "last_name": "Сергеев", "team_id": 2, "salary": 20000.00, "specialization": "Прораб"},
]

for worker_data in workers_data:
    Worker.objects.get_or_create(**worker_data)
