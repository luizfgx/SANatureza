    import requests

    url = 'https://docs.google.com/forms/d/e/1FAIpQLSfnlQSpDDHi5S0gf6prRxsl85fE_CfTTu0whdc4LOOhx6K7NA/formResponse'

    data = {
'entry.346969493': 'MAX FREDERICO',
'entry.130963714': 'André Tasca',
'entry.130963714_sentinel': '',
    }

    response = requests.post(url, data=data).text
    
    print(response)