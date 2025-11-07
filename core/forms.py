from django import forms

class FeedbackForm(forms.Form):
    first_name = forms.CharField(label='имя 🧡', widget=forms.TextInput(attrs={'placeholder': 'Джон'}))
    text = forms.CharField(label='текст обращения ⏺')
    phone = forms.CharField(max_length=10, label='телефончик ⚡')


    def clean_phone(self):
        """валидация поля телефона"""
        phone = self.cleaned_data['phone']
        if phone[0] != '8':
            raise forms.ValidationError('Номер должен начинаться с 8')
        return phone
