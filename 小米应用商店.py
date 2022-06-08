import requests
from lxml import etree
from multiprocessing.dummy import Pool
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}
urls=[]
for i in range(1,4):
    url=f'https://app.mi.com/allHotList?page={i}'
    urls.append(url)
appName=[]
def getAppData(url):
    page_text=requests.get(url=url,headers=headers).text
    tree=etree.HTML(page_text)
    app_data=tree.xpath('//ul[@class="applist"]/li/h5/a/text()')
    # print(app_data)
    list(filter(addAppData,app_data))
    # appName.append(app_data)
def addAppData(name):
    # print(name)
    appName.append(name)
pool=Pool(len(urls))
pool.map(getAppData,urls)
pool.close()
pool.join()
print(appName)



# url='https://app.mi.com/allHotList?page=1'
# page_text=requests.get(url=url,headers=headers).text
# tree=etree.HTML(page_text)
# app_data=tree.xpath('//ul[@class="applist"]/li/h5/a/text()')
# print(app_data)