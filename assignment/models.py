from django.db import models, connection

# Create your models here.
class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    completed = models.BooleanField()
    todo =  models.CharField(max_length=100)
    last_uplate = models.DateTimeField()

    class Meta:
        db_table = "Todo"