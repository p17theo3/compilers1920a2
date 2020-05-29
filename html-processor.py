import re

def function(m): #replace &amp, &gt, &lt kai &nbsp

    if (m.group(0)=='&amp;'):
        return '&'
    elif (m.group(0)=='&gt;'):
        return '>'
    elif (m.group(0)=='&lt;'):
        return '<'
    else:
        return ' '  


#Erotimata

rexp = re.compile('<title>(.+?)</title>') #teriazi <title></title>
rexp2 = re.compile('<!--.*?-->',re.DOTALL) #apalifi sxolion
rexp3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL)
rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)#auto einai gia to <a></a> kai href
rexp5-1 = re.compile(r'<.+?>|</.+?>',re.DOTALL) # tags <>
rexp5-2 = re.compile(r'<.+?/>',re.DOTALL) # tags </>
rexp6 = re.compile(r'&(amp|gt|lt|nbsp);') #auto einai gia == &amp, &gt, &lt kai &nbsp
rexp7 = re.compile(r'\s+') #whitespaces



with open('testpage.txt','r') as fp: 
    text = fp.read() #reading  testpage.txt
    m = rexp.search(text)
    print(m.group(1))
    text = rexp2.sub(' ',text)
    text = rexp3.sub(' ',text)
    for m in rexp4.finditer(text):
        print('{}    {}'.format(m.group(1),m.group(2)))
    text = rexp5-1.sub(' ',text)
    text = rexp5-2.sub(' ',text)
    text = rexp6.sub(function,text)
    text = rexp7.sub(' ',text)
    print(text)
    
