from django.core.mail import EmailMessage
from django.conf import settings


def send_email(name, date, email):
    txt = """
    <html>
<body>
<table cellpadding='0' cellspacing='0' width='100%' border='0'>
    <tbody>
    <tr>
        <td style='word-wrap:break-word;font-size:0px;padding:0px;padding-bottom:10px' align='left'>
            <div style='color:#000000;font-family:Spoqa Han Sans,sans-serif;font-size:20px;line-height:22px;letter-spacing:-0.8px;text-align:left'>
                안녕하세요 <span style='color:#3832D8'>{0}</span> 님,
            </div>
        </td>
    </tr>
    <tr>
        <td style='word-wrap:break-word;font-size:0px;padding:0px;padding-bottom:10px' align='left'>
            <div style='color:#000000;font-family:Spoqa Han Sans,sans-serif;font-size:30px;line-height:1.3;letter-spacing:-1.1px; text-align:left'>
                OpenInfra Days Korea 2018
            </div>
        </td>
    </tr>
    <tr>
        <td style='word-wrap:break-word;font-size:0px;padding:0px;padding-bottom:30px' align='left'>
            <div style='color:#000000;font-family:Spoqa Han Sans,sans-serif;font-size:20px;line-height:22px;letter-spacing:-0.8px;text-align:left'>
                초청 티켓 등록이 완료되었습니다.
            </div>
        </td>
    </tr>
    <tr>
        <td style='word-wrap:break-word;font-size:0px;padding:0px;padding-bottom:30px' align='left'>
            <div style='color:#000000;font-family:Spoqa Han Sans,sans-serif;font-size:20px;line-height:22px;letter-spacing:-0.8px;text-align:left'>
                참가 일자 : {1}
            </div>
        </td>
    </tr>
    <tr>
        <td style='word-wrap:break-word;font-size:0px;padding:0px' align='left'>
            <div style='color:#000000;font-family:Spoqa Han Sans,sans-serif;font-size:20px;line-height:22px;letter-spacing:-0.8px;text-align:left'>
                <a href="http://invite.openinfradays.kr">티켓 확인</a>
            </div>
        </td>
    </tr>
    </tbody>
</table>
</body>
</html>

    """.format(name, date)
    email = EmailMessage(settings.EMAIL_TITLE, txt, to=(email,))
    email.content_subtype = "html"
    return email.send()

