from .models import Todo
from django import forms


class AddTask(forms.ModelForm):

    due_date = forms.CharField(widget=forms.TextInput(attrs={'type':'datetime-local'}))



    class Meta:
        model = Todo
        fields = ['title','body','due_date']
