from django.db import models, connection
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    completed = models.BooleanField()
    todo =  models.CharField(max_length=100)
    last_uplate = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "todo"