from django import forms
from .validators import allow_only_images_validator
from .models import Category, Expatad, Contactme, Interested


class CategoryForm(forms.ModelForm):
    thumbnail = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}), validators=[allow_only_images_validator])
    class Meta:
        model = Category
        fields = '__all__'



class ExpatadForm(forms.ModelForm):
    cover_photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}), validators=[allow_only_images_validator])
    class Meta:
        model = Expatad
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExpatadForm, self).__init__(*args, **kwargs)
        self.fields['areameasurement'].widget.attrs['placeholder'] = 'Sq. ft.,sq.yards,acre,cent'




class ContactmeForm(forms.ModelForm):
    class Meta:
        model = Contactme
        fields = ['fullname', 'contactno', 'email','Description']




class InterestedForm(forms.ModelForm):
    class Meta:
        model = Interested
        fields = ['fullname', 'contactno', 'email','Description']