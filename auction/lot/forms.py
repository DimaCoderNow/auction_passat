from django import forms
from .models import Bid, Message  # Импортируем модель Bid


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['user_name', 'amount', 'phone']

    user_name = forms.CharField(max_length=20)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    phone = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user_name'].widget.attrs.update({'class': 'input',
                                                      'placeholder': ' '})
        self.fields['amount'].widget.attrs.update({'class': 'input',
                                                   'placeholder': ' '})
        self.fields['phone'].widget.attrs.update({'class': 'input',
                                                  'placeholder': ' ',
                                                  'inputmode': 'tel'})


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'phone', 'text']

    name = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'input',
                                                 'placeholder': ' '})
        self.fields['phone'].widget.attrs.update({'class': 'input',
                                                  'placeholder': ' ',
                                                  'inputmode': 'tel'})
        self.fields['text'].widget.attrs.update({'class': 'input',
                                                 'placeholder': ' '})
