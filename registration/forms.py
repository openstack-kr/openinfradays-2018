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
    invite_code = forms.CharField(
        label='초청 코드',
        required=True
    )

    def clean(self):
        cleaned_data = super(RegistrationCheckForm, self).clean()
        try:
            reg = Registration.objects.get(email=cleaned_data.get('email'))
            if reg.invite_code != cleaned_data.get('invite_code'):
                raise forms.ValidationError('등록되지 않은 정보입니다.')
        except Exception as e:
            raise forms.ValidationError('등록되지 않은 정보입니다.')
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
        self.fields['team'].widget.attrs['readonly'] = True
        self.fields['phone_number'].widget.attrs['readonly'] = True
        self.fields['company_phone_number'].widget.attrs['readonly'] = True
        self.fields['term_agreed'].widget.attrs['readonly'] = True
        self.fields['term_agreed'].widget.attrs['checked'] = True

    class Meta:
        model = Registration
        fields = ('term_agreed', 'invite_code', 'email', 'name', 'company', 'team', 'duty', 'company_phone_number',
                  'phone_number', 'participant_dates',)
        labels = {
            'invite_code': _('초청 코드'),
            'name': _('이름'),
            'email': _('이메일'),
            'duty': _('직책'),
            'company': _("소속 (없으시면 '없음'으로 기재해 주세요)"),
            'team': _('부서'),
            'company_phone_number': _('사무실 전화번호'),
            'phone_number': _('휴대폰 번호'),
            'term_agreed': _('개인정보 제3자 제공 동의'),
            'participant_dates': _('참가 일정'),
        }


class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['invite_code'].widget.attrs['readonly'] = True
        self.fields['term_agreed'].required = True
        self.fields['name'].required = True
        self.fields['company'].required = True
        self.fields['team'].required = True
        self.fields['duty'].required = True
        self.fields['phone_number'].required = True
        self.fields['company_phone_number'].required = False
        self.fields['participant_dates'].required = False
        self.helper = FormHelper()
        self.helper.form_id = 'registration-form'
        self.helper.form_action = '/registration/process'
        self.helper.form_method = 'post'
        self.helper.add_input(
            Submit('submit', _('Submit')))

    class Meta:
        model = Registration
        fields = ('term_agreed', 'invite_code', 'email', 'name', 'company', 'team', 'duty', 'company_phone_number',
                  'phone_number', 'participant_dates',)
        labels = {
            'invite_code': _(
                '초청 코드'),
            'name': _('이름'),
            'email': _('이메일'),
            'duty': _('직책'),
            'company': _("소속 (없으시면 '없음'으로 기재해 주세요)"),
            'team': _('부서'),
            'company_phone_number': _('사무실 전화번호'),
            'phone_number': _('휴대폰 번호'),
            'term_agreed': _('개인정보 제3자 제공 동의'),
            'participant_dates': _('참가 일정')
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')
        dup = None
        try:
            dup = Registration.objects.get(invite_code=invite_code)
        except Exception:
            pass
        if dup:
            raise forms.ValidationError('이미 등록된 초청코드입니다.')
        return cleaned_data
