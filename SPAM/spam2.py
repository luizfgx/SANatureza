import requests
i=0;
while(1):
	url = 'https://docs.google.com/forms/d/e/1FAIpQLSfnlQSpDDHi5S0gf6prRxsl85fE_CfTTu0whdc4LOOhx6K7NA/formResponse'

	form_data = {
        'entry.346969493'   : 'MAX FREDERICO',
        'entry.130963714'   : 'André Tasca',
        'entry.130963714_sentinel'  : '',
		}
	user_agent ={
		'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSfnlQSpDDHi5S0gf6prRxsl85fE_CfTTu0whdc4LOOhx6K7NA/viewform',
		'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
		}
	r = requests.post(url, data=form_data, headers=user_agent)
	i=i+1
	if(i%3==0):
		print(r)
		print('\nTotal Count = ')
		print(i)
		print('\n')