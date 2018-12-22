import requests
import json

class jijin():
    def __init__(self,url):
        self.url=url
        self.jijin_name=""
        self.jijin_id=""
        self.jijin_manager=""
        self.JZ=""
    def Getlist(self):
        self.jijin_id=self.url.split('/')[-1].split('.')[0]
        jj_newlist='http://fundgz.1234567.com.cn/js/'+self.jijin_id+'.js?'
        reponse=requests.get(jj_newlist).text
        #print(reponse)
        JJ_JS=json.loads(reponse.strip("jsonpgz();",))
        self.jijin_name=JJ_JS['name']
        self.JZ=JJ_JS['dwjz']
        #print(self.JZ)
    def JJJZ(self):
        self.jijin_id='002023'
        #data={
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
        cookies={'Cookie':'st_pvi=33021263418532; st_sp=2018-09-12%2009%3A19%3A23; qgqp_b_id=86c4753ea80492c119163b59fc73d967; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; st_si=13664713051492; EMFUND0=null; EMFUND6=12-05%2015%3A38%3A43@%23%24%u4E2D%u6D77%u533B%u836F%u5065%u5EB7%u4EA7%u4E1A%u7CBE%u9009%u6DF7%u5408C@%23%24000879; EMFUND7=12-05%2015%3A42%3A45@%23%24%u666F%u987A%u957F%u57CE%u5185%u9700%u8D30%u53F7%u6DF7%u5408@%23%24260109; EMFUND8=12-05%2015%3A53%3A40@%23%24%u56FD%u6CF0%u667A%u80FD%u88C5%u5907%u80A1%u7968@%23%24001576; st_asi=delete; st_sn=3; st_psi=20181209005735351-117001300541-0586842751; EMFUND9=12-09 02:13:09@#$%u7EA2%u5854%u7EA2%u571F%u7A33%u5065%u56DE%u62A5A@%23%24002023'}
        JJJZ_url='http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery1830347373846943289_1544294277909&fundCode=002023&pageIndex=1&pageSize=20&startDate=&endDate='
        #print(JJJZ_url)
        reponse=requests.get(JJJZ_url,headers=header,cookies=cookies)
        print(reponse.text)
if __name__ ==  '__main__':
    url='http://fund.eastmoney.com/002023.html'
    JJlist=jijin(url).Getlist()
    JJJZList=jijin(url).JJJZ()
