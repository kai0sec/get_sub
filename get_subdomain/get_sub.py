import requests
from bs4 import BeautifulSoup
import user_agent_list
import re
import time
from optparse import OptionParser



url="http://i.links.cn/subdomain/"

def sub_domain(sourl):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)' } 
    data={
        "domain":sourl,
        "bbaidu":"1",
        "b2":"1",
        "b3":"1",
        "b4":"1"
    }
    try:
        zym=requests.post(url=url,headers=user_agent_list.get_user_agent(),data=data,timeout=2).text
        soup=BeautifulSoup(zym,"html.parser")
   
        url_zym=soup.findAll(class_="domain")

        with open("zym.txt",'a') as ok:
            for you_zym in url_zym:
                zym_url=re.sub('(.*?)http',"http",you_zym.text)
                print zym_url
                ok.write(zym_url)
                ok.write('\n')                                                
    except:
        sub_domain(sourl)

def main():
    parser = OptionParser() 
    usage = "usage: %prog [options] arg"  
    parser=OptionParser(usage)
    parser.add_option("-f","--infile",dest="filename",
                      help="please input  file")
    parser.add_option("-u","--url",dest="url",
                      help="please input  url")    
  
    (options,args)=parser.parse_args()
    inputfile=options.filename
    urls=options.url
    if urls:
        sub_domain(urls)
        
        
    if inputfile:
        print inputfile    
        urls=open(inputfile,'r')
        for sourl in urls:
            sourl=sourl.strip('\n')
            sub_domain(sourl)
        
if __name__=="__main__":
    main()



   
    
