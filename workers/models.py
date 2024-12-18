from django.db import models



class Team(models.Model):
    id = models.AutoField(primary_key=True, unique=True)


class Worker(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    last_name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.last_name
    