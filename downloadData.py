import hashlib 
import http.cookiejar
import json
import re
import sys
import urllib.request

# check if times to execute is passed as an argument in command line
if len(sys.argv) > 1:
    times = sys.argv[1]
else:
    times = input('How many times do you want to run: ')

try:
    times = int(times)
    print('Downloading...')
except ValueError:
    print('ValueError: Input is not an integer.')
    exit(-1)

for i in range(times):
    # using cookiejar
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    # request login page
    page_content = opener.open('https://www.ais.tku.edu.tw/EleCos/login.aspx').read().decode('utf-8')

    # get the varification code image
    confirm_page = re.findall('confirm.ashx.[^"]*', page_content)
    if len(confirm_page) == 0:
        print('Cannot locate the verification code image.')
        exit(-1)
    varification_code_url = 'https://www.ais.tku.edu.tw/EleCos/BaseData/{0}'.format(confirm_page[0])
    img_binary = opener.open(varification_code_url).read()

    varification_code = ''

    # get the array of hashed varification digits
    varification_code_array = json.loads(opener.open('https://www.ais.tku.edu.tw/EleCos/Handler1.ashx').read().decode('utf-8'))

    # parse each hashed varification code digits back from sha1
    for j in range(len(varification_code_array)):
        for k in range(10):
            sha_1 = hashlib.sha1()
            sha_1.update(str(k).encode('utf8'))
            if sha_1.hexdigest() == varification_code_array[j]:
                varification_code += str(k)
                break

    with open('training/{0}.png'.format(varification_code), 'wb')  as file:
        print('{0} => {1}.png'.format(i + 1, varification_code))
        file.write(img_binary)
