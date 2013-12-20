import re


def __get_match(text,pattern):
    match=pattern.search(text)
    if match:
        return text[match.start():match.end()]
    else:
        return None

reg_thread=re.compile("HTTP/1\.1\^http://www\.19lou\.com/forum-[0-9]+-thread-[0-9]+-[0-9]+-[0-9]+\.html")








if __name__=='__main__':
    thread_url='''125.122.130.100^18/Dec/2013:12:00:01 +0800^GET /dm2011_city.gif?channel=hangzhou&host=www.19lou.com&cache_=5914874&pre=http%3A//www.19lou.com/forum-122-2.html&scr=768x1024&rf=&uid=28240861_XYZ&reg_source=&reg_kw=&reg_step=&reg_first=&dm_sid=03f3add1bb937e3b0cbf320ae2ae6a9c&dm_s=a62bfb9cf029018a4ceea9901ae51dd8&dm_referer=http://www.19lou.com/forum-122-2.html HTTP/1.1^http://www.19lou.com/forum-122-thread-10631385950470317-1-1.html^Mozilla/5.0(iPad; U;CPU OS 6_1 like Mac OS X; zh-CN; iPad2,5) AppleWebKit/534.46 (KHTML, like Gecko) UCBrowser/2.0.1.280 U3/0.8.0 Safari/7543.48.3^03f3add1bb937e3b0cbf320ae2ae6a9c^a62bfb9cf029018a4ceea9901ae51dd8^28240861_XYZ^^:^1387339201.241^dm_reg=^^^'''

    print __get_match(thread_url,reg_thread)
    print __get_match("ddddd",reg_thread)