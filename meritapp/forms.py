from django import forms
from meritapp.models import Request, Touch, Contact1, Modal, Homecontact


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = "__all__"


class TouchForm(forms.ModelForm):
    class Meta:
        model = Touch
        fields = "__all__"


class Contact1Form(forms.ModelForm):
    class Meta:
        model = Contact1
        fields = "__all__"


class ModalForm(forms.ModelForm):
    class Meta:
        model = Modal
        fields = "__all__"


class HomecontactForm(forms.ModelForm):
    class Meta:
        model = Homecontact
        fields = "__all__"
