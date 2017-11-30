import os

URL = "https://api.mailgun.net/v3/sandbox6102bd6ccfc243eba66366e170b8b8ad.mailgun.org/messages"
API_KEY = "key-c2308de8f260c0fe45d271d8bf7b5589"
FROM = "<Mailgun Sandbox> postmaster@sandbox6102bd6ccfc243eba66366e170b8b8ad.mailgun.org"
ALERT_TIMEOUT = 1
COLLECTION = "alerts"


URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')
