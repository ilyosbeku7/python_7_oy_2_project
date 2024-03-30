from django import forms
from .models import Comment

class PlaceCommentForm(forms.ModelForm):
   star_given=forms.IntegerField(max_value=5, min_value=1)
   comment_text=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control' ,'rows':4, }))
   class Meta:
         model=Comment
         fields=('comment_text', 'star_given' )