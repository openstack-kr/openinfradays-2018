from django.core.mail import EmailMessage
from django.conf import settings


def send_auth_email(request, token):
    txt = 'http://%s/login/process/%s' % (request.get_host(), token.token)
    email = EmailMessage(settings.EMAIL_TITLE, txt, to=(token.email,))
    return email.send()

