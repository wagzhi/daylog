#coding=utf-8
__author__ = 'root'
import re
reg_req_url = re.compile("HTTP/1\.[01]\^(http://|www.19lou.com/)[\w./&\-%=:\?#+,]+\^")
reg_refer_url = re.compile("&dm_referer=[\S]+ ")

def __get_match_str(pattern,text):
    m = pattern.search(text)
    if m:
        return m.group(0)
    else:
        return None

def get_req_url(line):
    ms = __get_match_str(reg_req_url,line)
    if ms:
        return ms[9:len(ms)-1]
    else:
        return None

def get_refer_url(line):
    '''&dm_referer=http://www.19lou.com/forum-122-2.html '''
    ms = __get_match_str(reg_refer_url,line)
    if ms:
        return ms[12:len(ms)-1]
    return None

#判断是否是帖子页面
reg_thread_fid_tid=re.compile("http://www\.19lou\.com/forum-(?P<fid>[0-9]+)-thread-(?P<tid>[0-9]+)-[0-9]+-[0-9]+\.html")


def get_thread_fid_tid(url):
    if url is None:
        return None

    m = reg_thread_fid_tid.search(url)
    if m:
        return m.groupdict()
    else:
        return None


URL_TYPES={
    "baidu":re.compile("^http://(www|m|zhidao)\.baidu\.com/"),
    "home": re.compile("^http://www\.19lou\.com([/]?|/\?from=hangzhou)$"),
    "second": re.compile("^http://(ent|love|bb|book|food|baby|house|fashion|home|family)\.19lou\.com[/]?$"),
    "forum": re.compile("^http://www\.19lou\.com/forum-[\d]+-[\d]+\.html"),
    "thread": re.compile("http://www\.19lou\.com/forum-[0-9]+-thread-[0-9]+-[0-9]+-[0-9]+\.html"),
    "board" : re.compile("^http://www\.19lou\.com/(board|r)/"),
    "bq": re.compile("^http://www\.19lou\.com/bq/"),
    "search": re.compile("^http://www\.19lou\.com/search/"),
    "wap": re.compile("^http://www\.19lou\.com/wap/"),
    }

def getUrlType(url):
    if url is not None:
        for type in URL_TYPES.keys():
            pt =  URL_TYPES[type]
            m = pt.search(url)
            if m:
                return type
    return "unknown"



if __name__ == '__main__':
    line='''118.76.227.34^18/Dec/2013:12:00:01 +0800^GET /dm2011_city.gif?channel=hangzhou&host=www.19lou.com&cache_=5871178&pre=&scr=720x1280&rf=&uid=&reg_source=www.19lou.com&reg_kw=&reg_step=151&reg_first=http%253A//m.19lou.com/&dm_sid=08002d176d473ef510083f78d2f65521&dm_s=2899bb3a73de6096bbbe718771e165c9&dm_referer= HTTP/1.1^http://www.19lou.com/wap/forum-26-thread-22301364119625196-979-1.html^Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-N7108 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30^08002d176d473ef510083f78d2f65521^2899bb3a73de6096bbbe718771e165c9^^^www.19lou.com:^1387339201.228^dm_reg=www.19lou.com^^151^http%253A//m.19lou.com/'''
    print get_req_url(line)
    print get_thread_fid_tid(line)


    from demo import exeDemo
    num = 0
    nforum = 0
    nhome,nsecond,nboard,nbq,nsearch,nn = (0,0,0,0,0,0)
    nbaidu = 0
    nthread = 0
    total = 0
    def test(line):
        '''测试分类'''
        global num,nforum,nhome,nbaidu,nthread,nsecond,nboard,nbq,nsearch,nn
        reqUrl=get_req_url(line)


        refUrl=get_refer_url(line)

        if getUrlType(reqUrl) == "thread":
            num=num+1
            #print "ref:  ",refUrl," req: ",reqUrl ,"\n"
            utype =  getUrlType(refUrl)
            if utype == 'baidu':
                nbaidu = nbaidu + 1
            elif utype == 'home':
                nhome = nhome + 1
            elif utype == 'forum':
                nforum = nforum + 1
            elif utype == "thread":
                nthread = nthread+1
            elif utype == "second":
                nsecond = nsecond + 1
            elif utype == "board":
                nboard = nboard + 1
            elif utype == "bq":
                nbq = nbq + 1
            elif utype == "search":
                nsearch = nsearch + 1
            else:
                nn = nn + 1
                print "ref: " , refUrl



    for rurl in exeDemo(test):
        total = total + 1

    print "\ntotal: ",total
    print "\nfrom baidu: ", nbaidu
    print "\nfrom home: ",nhome
    print "\nfrom second", nsecond
    print "\nfrom forum: ",nforum
    print "\nfrom board: ",nboard
    print "\nfrom thread", nthread
    print "\nfrom bq", nbq
    print "\nfrom search", nsearch
    print "\nfrom unkown: " , nn

    print "\nthread total: ",num, " = ", nbaidu+nhome+nsecond+nforum+nboard+nthread+nn