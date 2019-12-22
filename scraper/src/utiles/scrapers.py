import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
import re

class scraper_test:
  def __init__(self):
    print ("init")

  def scraping(self, url):
    response = requests.get(url)

    print (response.content)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find('title')
    # text_lines = soup.findAll('text')


    #１．初めの検索したtagをreturn
    p_line = soup.find('p')
    print(p_line)
    print(p_line.string)
    print(p_line.get_text())

    #２． tagにあるidで検索
    title_data =  soup.find(id='title')
    print (title_data)
    print (title_data.string)
    print (title_data.get_text())

    #３．html tagとcss　classを利用して必要なデータをもらう方法
    paraGraph_data = soup.file('p', class_ = 'cssstyle')
    print(paraGraph_data)
    print(paraGraph_data.string)
    print(paraGraph_data.get_text())

    #4．html tagとcss　classを利用して必要なデータをもらう方法
    paraGraph_data = soup.file('p', 'cssstyle')
    print(paraGraph_data)
    print(paraGraph_data.string)
    print(paraGraph_data.get_text())

    #５．html tagとtagにあるattributeを利用して必要なデータをもらう方法
    paraGraph_data =  soup.find('p', attrs = {'align':'center'})
    print (paraGraph_data)
    print (paraGraph_data.string)
    print (paraGraph_data.get_text())

    #6.find_all()すべてのデータをリスト形態でもらうmethod
    paragraph_data = soup.find_all('p')
    print (paraGraph_data)

    for array_data in paraGraph_data:
      print ('配列データ　＝',array_data) 

    print (title.get_text())

  def search_scraping(self, search):
    # 7.BeautifulSoup　libraryを利用したstring検索
    #tagじゃなくて文字列で検索
    #文字列,  いろな方法で検索可能
    # 文字列検索の場合tag内の文字列をexat mathchingだけもらう
    re_search = re_search_string(search)
    url = "http://www.google.com/search?q="+re_search
    print ("url = ", url)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    image_url = ""
    print ("parsing data")
    # print (soup)
    # copy_div_id = soup.select('div#hdtb-msb-vis')  
    datas = soup.find_all("div", class_="hdtb-mitem")
    # datas = soup.findAll('a')
    for line in datas:
      print (line)
      # if "画像" == line.get_text():
      #   image_url = line['href']
    
    print(image_url)

    file1 = open("myfile.txt","w")       
    # file1.write() 
    file1.writelines(str(soup)) 
    file1.close() #to change file access modes 

  # url image all get
  def search_image_scraping(self, url): 
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')   
    images = soup.find_all('img',{'src':re.compile('.jpg')})
    count = 0
    for image in images:
      count += 1
      print(image['src'] + "\n")
      image_name = "image_{}.jpg".format(count)
      url_link = image['src']
      url_image_download(image_name, url_link)


# google search
def re_search_string(search):
  re_search = search
  if ' ' in search:
    re_search = ""
    serach_split = search.split(' ')
    for num in range(len(serach_split)):
      if num + 1 < len(serach_split):
        re_search += "{}+".format(serach_split[num])
      else:
        re_search += "{}".format(serach_split[num])
  return re_search


# url get image
def url_image_download(img_name, pic_url):
  directory = "./images/" 
  
  if not os.path.exists(directory):
    os.makedirs(directory)
  
  with open(directory + img_name,'wb') as handle:
    response = requests.get (pic_url,  stream =True)

    if not response.ok:
      print (response)
    
    for block in response.iter_content(1024):
      if not block:
        break

      handle.write(block)  




# print (text_lines)
if __name__ == "__main__":
  # url ="https://www.google.com/search?q=amazon&rlz=1C1CHBD_jaJP786JP786&oq=amazon&aqs=chrome..69i57j69i59l2j69i60l5.5058j0j8&sourceid=chrome&ie=UTF-8"
  # search_name = "abe shinzo"
  # scraper = scraper_test()
  # scraper.search_scraping(search_name)
  url = "https://unsplash.com/s/photos/tree"
  scraper = scraper_test()
  scraper.search_image_scraping(url)
