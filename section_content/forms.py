from django import forms

from .models import Reservation

class ContactForm(forms.Form):
    pass 

# class ReservationForm(forms.Form):
#     name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control"}))
#     email = forms.EmailField()
#     phone = forms.CharField(max_length=100)
#     date = forms.DateField()
#     time = forms.TimeField()
#     guests = forms.IntegerField()
#     message = forms.CharField(widget=forms.Textarea)

    # widgets = {
    #         "name": CharField(attrs={"cols": 80, "rows": 20}),
    #     }

class ReservationForm(forms.ModelForm):
    model = Reservation
    class Meta:
        model = Reservation
        # customer_name = models.CharField(max_length=100)
        # email = models.EmailField(max_length=100)
        # phone_number = models.CharField(max_length=20)
        # date = models.CharField(max_length=100)
        # time = models.CharField(max_length=100)
        # guests = models.IntegerField(default=0)
        # message = models.TextField(blank=True)

        # fields = '__all__'
        fields = ['customer_name', 'email', 'phone_number', 'date', 'time', 'guests', 'message']

        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'data-rule' : "minlen:4",
                'data-msg' : "Please enter at least 4 chars",
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'data-rule' : "email",
                'data-msg' : "Please enter a valid email",
                }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone',
                'data-rule' : "minlen:4",
                'data-msg' : "Please enter at least 4 chars",
                }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type' : 'date',
                'placeholder': 'Date',
                'title' : 'Select the date',
                }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'title': 'Select the time',
                'type' : "time",
                'data-msg' : "Please enter at least 4 chars",
                }),
            'guests': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '# of people',
                'data-rule' : "minlen:1",
                'data-msg' : "Please enter at least 1 chars",
                'required' : 'required',
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'rows' : "5",
                }),
        }

