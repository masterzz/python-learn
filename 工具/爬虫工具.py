import requests
from bs4 import BeautifulSoup
import urllib.request


class MyCrawler:
    # 找到有指定属性att的下载链接
    def download_by_att(self,html = "",attr = "",save_path = ""):
        page = requests.get(html)
        html_content = page.text
        # 假设html_content是从前面的代码中获取到的HTML页面内容
        soup = BeautifulSoup(html_content, "html.parser")

        # 查找所有的<a>标签
        # links = soup.find_all("a")

        links = soup.select('a[{}]'.format(attr))
        # 根据href属性值,下载到指定路径
        for link in links:
            download_link = link.get("href")
            # 获取文件名
            file_name = link.get_text()
            full_name = save_path + "\\" + file_name
            urllib.request.urlretrieve(download_link, full_name)

if __name__ == '__main__':
    mycla = MyCrawler()
    html = 'http://www.zhaoqing.gov.cn/xxgk/tjxx/tjnj/content/post_2796158.html'
    attr  = "download"
    save_path = "D:\\work\\政企BG\\肇庆-交流\\202310\\预算统计\\统计年鉴"
    mycla.download_by_att(html = html, attr = attr, save_path = save_path)

    # page = requests.get(html)
    # html_content = page.text
    # print(html_content)



