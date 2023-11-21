import os
import requests

#url = 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2'
url = "https://www.work.ua/"
answer = requests.get(url)
print('Return code ', answer.status_code)
#print('Site:', answer.text)

tempFile = open('./temp.html', 'wb')
tempFile.write(answer.text.encode('utf8'))
tempFile.close()

os.system('start ./temp.html')
