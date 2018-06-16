from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Registration, InviteCode


class RegistrationCheckForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True
    )

    def clean(self):
        cleaned_data = super(RegistrationCheckForm, self).clean()
        try:
            Registration.objects.get(email=cleaned_data.get('email'))
        except Exception as e:
            raise forms.ValidationError('등록되지 않은 이메일입니다.')
        return cleaned_data


class InviteForm(forms.Form):
    code = forms.CharField(
        label='InviteCode',
        required=True
    )

    def clean(self):
        cleaned_data = super(InviteForm, self).clean()
        reg = None
        try:
            reg = Registration.objects.get(invite_code=cleaned_data.get('code'))
        except Exception:
            pass
        if reg:
            raise forms.ValidationError('유효하지 않은 초청코드입니다.')
        try:
            InviteCode.objects.get(code=cleaned_data.get('code'))
        except Exception:
            raise forms.ValidationError('유효하지 않은 초청코드입니다.')
        return cleaned_data


class RegistrationInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationInfoForm, self).__init__(*args, **kwargs)
        self.fields['invite_code'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['duty'].widget.attrs['readonly'] = True
        self.fields['company'].widget.attrs['readonly'] = True
        self.fields['phone_number'].widget.attrs['readonly'] = True

    class Meta:
        model = Registration
        fields = (
        'invite_code', 'email', 'name', 'duty', 'company', 'phone_number',)
        labels = {
            'name': _('이름'),
            'email': _('이메일'),
            'duty': _('직책'),
            'company': _('소속'),
            'phone_number': _('휴대폰 번호'),
        }


class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['invite_code'].widget.attrs['readonly'] = True
        self.helper = FormHelper()
        self.helper.form_id = 'registration-form'
        self.helper.form_action = '/registration/process'
        self.helper.form_method = 'post'
        self.helper.add_input(
            Submit('submit', _('Submit')))

    class Meta:
        model = Registration
        fields = (
        'invite_code', 'email', 'name', 'duty', 'company', 'phone_number',)
        labels = {
            'name': _('이름'),
            'email': _('이메일'),
            'duty': _('직책'),
            'company': _('소속'),
            'phone_number': _('휴대폰 번호'),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')
        dup = None
        try:
            dup = Registration.objects.get(email=email)
        except Exception:
            pass
        if dup:
            raise forms.ValidationError('이미 등록된 이메일입니다.')
        return cleaned_data
