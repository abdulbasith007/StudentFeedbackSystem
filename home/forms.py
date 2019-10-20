from django import forms
from .models import Feedbacks
class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedbacks
        fields=['feedback_content']