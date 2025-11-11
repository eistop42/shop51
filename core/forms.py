from django import forms

from .models import ProductCategory

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

class AddProductForm(forms.Form):
    name = forms.CharField(label='название')
    price = forms.IntegerField(label='цена', max_value=1000, min_value=50)
    count = forms.IntegerField(label='количество', min_value=1)
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), label='категория')

    def clean_name(self):
        name = self.cleaned_data['name']

        if name.lower() in ['перец']:
            raise forms.ValidationError('это товар запрещен ❌')
        return name


