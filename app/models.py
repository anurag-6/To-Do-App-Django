from django.db import models

class Users(models.Model):
    
    def __str__(self):
        return str(self.id)



class Todo(models.Model):
    title = models.CharField(max_length = 20,blank = False)
    body = models.TextField(blank =True , null = True)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank = False)
    is_done  = models.BooleanField(default = False)
    completed_on = models.DateTimeField(blank= True, null =True)
    user_id = models.ForeignKey(Users,on_delete = models.CASCADE)


