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
    varification_code_rul = 'https://www.ais.tku.edu.tw/EleCos/BaseData/{0}'.format(re.findall('confirm.ashx.[^"]*', page_content)[0])
    img_binary = opener.open(varification_code_rul).read()

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

    with open('data/{0}.png'.format(varification_code), 'wb')  as file:
        print('{0} => {1}.png'.format(i + 1, varification_code))
        file.write(img_binary)
