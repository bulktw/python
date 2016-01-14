from django import forms
from .models import Allowlist

class AllowlistForm(forms.ModelForm):
	class Meta:
		model = Allowlist
		fields = ('employeeid', 'employeedept', 'employeename', 'purpose',)