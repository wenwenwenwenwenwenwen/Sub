# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2025/3/23 21:55
import base64
import sys
import time
import json
import requests
import hmac
import hashlib
import re  # 新增导入re模块
sys.path.append('..')
from base.spider import Spider
class Spider(Spider):
    def getName(self):
        return "Litv"

    def init(self, extend):
        self.extend = extend
        try:
            self.extendDict = json.loads(extend)
        except:
            self.extendDict = {}

        proxy = self.extendDict.get('proxy', None)
        if proxy is None:
            self.is_proxy = False
        else:
            self.proxy = proxy
            self.is_proxy = True
        pass

    def getDependence(self):
        return []

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def natural_sort_key(self, s):
        """
        自然排序辅助函数
        """
        return [
            int(part) if part.isdigit() else part.lower()
            for part in re.split(r'(\d+)', s)
        ]
    def get_channel_url(channel_id):
        # 内嵌的JSON数据
        CHANNEL_DATA = '''
        [{
          "channelId": "1244",
          "channelName": "CCTV-1 综合 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207222407598d36991a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1-HD/index.m3u8"
        }, {
          "channelId": "1245",
          "channelName": "CCTV-2 财经 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/2022120722241710bbebd40c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-2-HD/index.m3u8"
        }, {
          "channelId": "1246",
          "channelName": "CCTV-3 综艺 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/146/146/20221207222354748308bcc68.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-3-HD/index.m3u8"
        }, {
          "channelId": "1247",
          "channelName": "CCTV-4 中文国际 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222343276fff5efce.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-4-HD/index.m3u8"
        }, {
          "channelId": "1248",
          "channelName": "CCTV-5 体育 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/122/122/2022120722233126f882be7d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-5-HD/index.m3u8"
        }, {
          "channelId": "1249",
          "channelName": "CCTV-6 电影 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223198181b4f5e72.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-6-HD/index.m3u8"
        }, {
          "channelId": "1250",
          "channelName": "CCTV-7 国防军事 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223077319f73617a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-7-HD/index.m3u8"
        }, {
          "channelId": "1251",
          "channelName": "CCTV-8 电视剧 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222256669c3e1d6b7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-8-HD/index.m3u8"
        }, {
          "channelId": "1252",
          "channelName": "CCTV-9 纪录 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/152/152/20221207222244929b8d4b7bc.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-9-HD/index.m3u8"
        }, {
          "channelId": "1254",
          "channelName": "CCTV-10 科教 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/20221207222231504fb7ce4d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-10-HD/index.m3u8"
        }, {
          "channelId": "1255",
          "channelName": "CCTV-11 戏曲 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/198/198/202212072222188594550f71c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-11-HD/index.m3u8"
        }, {
          "channelId": "1256",
          "channelName": "CCTV-12 社会与法 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/117/117/20221207222207220284c9fc8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-12-HD/index.m3u8"
        }, {
          "channelId": "1358",
          "channelName": "CCTV-13 新闻 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072221151304eb5505e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13-HD/index.m3u8"
        }, {
          "channelId": "1257",
          "channelName": "CCTV-14 少儿 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/182/182/20221207222155328049fb5a6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-14-HD/index.m3u8"
        }, {
          "channelId": "1258",
          "channelName": "CCTV-15 音乐 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/2022120722214390791fff94f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-15-HD/index.m3u8"
        }, {
          "channelId": "1259",
          "channelName": "CCTV-17 农业农村 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/20221207222132202539afab9.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cctv17-HD/index.m3u8"
        }, {
          "channelId": "6",
          "channelName": "CGTN",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/165/165/202212072041501851b94c9ec.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-NEWS/index.m3u8"
        }, {
          "channelId": "1502",
          "channelName": "陕西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/101/101/2024110509445978929c3937c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxws-HD/index.m3u8"
        }, {
          "channelId": "1260",
          "channelName": "东方卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720351191821898b11.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dfws-HD/index.m3u8"
        }, {
          "channelId": "1261",
          "channelName": "湖南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720352634886bbc892.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws-HD/index.m3u8"
        }, {
          "channelId": "1262",
          "channelName": "江苏卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/20221207203538852325a2b88.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jsws-HD/index.m3u8"
        }, {
          "channelId": "1263",
          "channelName": "浙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/20221207203552131534a252f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zjws-HD/index.m3u8"
        }, {
          "channelId": "1264",
          "channelName": "北京卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/137/137/202212072036065012d2a1d95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/bjws-HD/index.m3u8"
        }, {
          "channelId": "1265",
          "channelName": "广东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/162/162/20221207203627511f5e13d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gdws-HD/index.m3u8"
        }, {
          "channelId": "1266",
          "channelName": "深圳卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/180/180/20221207203640583e63fa438.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SZWS-HD/index.m3u8"
        }, {
          "channelId": "1267",
          "channelName": "黑龙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/134/134/20221207203656198d014c1cb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HLJWS-HD/index.m3u8"
        }, {
          "channelId": "1268",
          "channelName": "湖北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/151/151/202212072037118302177fa1b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws-HD/index.m3u8"
        }, {
          "channelId": "1269",
          "channelName": "山东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072037277168582433.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sdws-HD/index.m3u8"
        }, {
          "channelId": "1270",
          "channelName": "四川卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/191/191/20221207203742205af521b1d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SCWS-HD/index.m3u8"
        }, {
          "channelId": "1271",
          "channelName": "安徽卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/20221207203758233936ea70e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ahws-HD/index.m3u8"
        }, {
          "channelId": "1272",
          "channelName": "重庆卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/20221207203811940c62dadbb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CQWS-HD/index.m3u8"
        }, {
          "channelId": "1273",
          "channelName": "天津卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/154/154/20221207203824509804022ef.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/tjws-HD/index.m3u8"
        }, {
          "channelId": "1274",
          "channelName": "东南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/202212072038382189fea09ed.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/DNWS-HD/index.m3u8"
        }, {
          "channelId": "1275",
          "channelName": "河南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/150/150/202212072038523111d3231a0.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HENWS-HD/index.m3u8"
        }, {
          "channelId": "1276",
          "channelName": "江西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/110/110/202212072039081329dfdd5c7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JXWS-HD/index.m3u8"
        }, {
          "channelId": "1277",
          "channelName": "吉林卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/189/189/2022120720392130600be9a05.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JLWS-HD/index.m3u8"
        }, {
          "channelId": "150",
          "channelName": "山西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/184/184/20190626140149321f61f2260.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ssxws/index.m3u8"
        }, {
          "channelId": "1278",
          "channelName": "贵州卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/140/140/2022031617152978797823af.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/GZWS-HD/index.m3u8"
        }, {
          "channelId": "58",
          "channelName": "甘肃",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/177/177/2022120720125423223d7812a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gsws/index.m3u8"
        }, {
          "channelId": "137",
          "channelName": "宁夏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/114/114/20190626140114540c491b02b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nxws/index.m3u8"
        }, {
          "channelId": "64",
          "channelName": "广西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/110/110/20190626134452888ce96a0da.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gxws/index.m3u8"
        }, {
          "channelId": "1279",
          "channelName": "辽宁卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/158/158/2022031617162098005a2d260.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/LNWS-HD/index.m3u8"
        }, {
          "channelId": "144",
          "channelName": "青海",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/179/179/20190626142941540a41135bd.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/qhws/index.m3u8"
        }, {
          "channelId": "181",
          "channelName": "西藏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/166/166/2019062614371060936aa124b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xzws/index.m3u8"
        }, {
          "channelId": "136",
          "channelName": "内蒙古",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/158/158/20190626142907384b6e2e7f6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nmgws/index.m3u8"
        }, {
          "channelId": "189",
          "channelName": "新疆",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/144/144/20190626135855225fd8af02c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xjws/index.m3u8"
        }, {
          "channelId": "1280",
          "channelName": "河北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/115/115/20220316171717176a4d4dd90.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HEBWS-HD/index.m3u8"
        }, {
          "channelId": "216",
          "channelName": "云南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/147/147/20190626135941353f5c1b0d5.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ynws/index.m3u8"
        }, {
          "channelId": "24",
          "channelName": "兵团",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/173/173/2019062614062666486fe05ad.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/btws/index.m3u8"
        }, {
          "channelId": "1232",
          "channelName": "CETV1",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/2/134/134/202203021435319329091931c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zgjy/index.m3u8"
        }, {
          "channelId": "132",
          "channelName": "海南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/2/120/120/2022030214370034042ae2842.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/lyws/index.m3u8"
        }, {
          "channelId": "1418",
          "channelName": "CETV4 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2023/11/7/106/106/202311071622482947994370c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CETV4/index.m3u8"
        }, {
          "channelId": "1503",
          "channelName": "陕西新闻资讯高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/136/136/20241105094553201e0f4bef4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t-HD/index.m3u8"
        }, {
          "channelId": "1504",
          "channelName": "陕西都市青春高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/133/133/20241105094621650945717c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx2t-HD/index.m3u8"
        }, {
          "channelId": "1505",
          "channelName": "陕西银龄高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/174/174/202411050946409130aaf53.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx3t-HD/index.m3u8"
        }, {
          "channelId": "1507",
          "channelName": "陕西秦腔高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/104/104/202411050947225294228c5f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx5t-HD/index.m3u8"
        }, {
          "channelId": "1508",
          "channelName": "陕西乐家购物高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/20241105100935425e14700d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx6t-HD/index.m3u8"
        }, {
          "channelId": "1509",
          "channelName": "陕西体育休闲高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/102/102/20241105100958274114a58f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx7t-HD/index.m3u8"
        }, {
          "channelId": "1510",
          "channelName": "西部电影高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/202411051010176160b28c230.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx8t-HD/index.m3u8"
        }, {
          "channelId": "1511",
          "channelName": "农林卫视高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/124/124/20241105101047340918e4dba.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nlws-HD/index.m3u8"
        }, {
          "channelId": "116",
          "channelName": "金鹰卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/202212072017014723ac246e0.jpeg",
          "channelUrl": "http://shanxiunicom.vshk.wasu.tv/jykt/index.m3u8?"
        }, {
          "channelId": "1235",
          "channelName": "卡酷少儿",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/150/150/2022120720324331063869b5d.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/kkdh/index.m3u8"
        }, {
          "channelId": "210",
          "channelName": "优漫卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/149/149/202212072020296680ed40b1c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ymkt/index.m3u8"
        }, {
          "channelId": "1237",
          "channelName": "炫动卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/168/168/2022120720325885681b6d47.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xdkt/index.m3u8"
        }, {
          "channelId": "103",
          "channelName": "嘉佳卡通 ",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/115/115/2022120720160881888186c24.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jjkt/index.m3u8"
        }, {
          "channelId": "264",
          "channelName": "综合",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/161/161/20221207202335888ecb9e4f8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1/index.m3u8"
        }, {
          "channelId": "458",
          "channelName": "财经",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/171/171/2022120720251563281358835.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-2/index.m3u8"
        }, {
          "channelId": "250",
          "channelName": "综艺",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/175/175/202212072021412061bd30e71.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-3/index.m3u8"
        }, {
          "channelId": "259",
          "channelName": "中文国际",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/118/118/202212072023057650110df4c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-4/index.m3u8"
        }, {
          "channelId": "460",
          "channelName": "体育",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207202533705c32d9f7a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-5/index.m3u8"
        }, {
          "channelId": "246",
          "channelName": "电影",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/202212072021081992442044c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-6/index.m3u8"
        }, {
          "channelId": "248",
          "channelName": "国防军事",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/2022120720212810862048e4c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-7/index.m3u8"
        }, {
          "channelId": "238",
          "channelName": "电视剧",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/196/196/20221207202054957c69ebde3.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-8/index.m3u8"
        }, {
          "channelId": "450",
          "channelName": "纪录",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/110/110/20221207202456195c3023d87.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-9/index.m3u8"
        }, {
          "channelId": "256",
          "channelName": "科教",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/199/199/20221207202235273a48669ed.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-10/index.m3u8"
        }, {
          "channelId": "258",
          "channelName": "戏曲",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/166/166/2022120720225137155a2a639.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-11/index.m3u8"
        }, {
          "channelId": "254",
          "channelName": "社会与法",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/193/193/202212072022137535e830337.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-12/index.m3u8"
        }, {
          "channelId": "263",
          "channelName": "新闻",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/202212072023214584b918a95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13/index.m3u8"
        }, {
          "channelId": "252",
          "channelName": "少儿",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207202154432b84b8335.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-14/index.m3u8"
        }, {
          "channelId": "266",
          "channelName": "音乐",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/137/137/20221207202352875c6a02c69.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-15/index.m3u8"
        }, {
          "channelId": "1233",
          "channelName": "农业农村",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/199/199/202212072032281723a250285.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cctv17/index.m3u8"
        }, {
          "channelId": "151",
          "channelName": "陕西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720185319499a21b3c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxwshz/index.m3u8"
        }, {
          "channelId": "38",
          "channelName": "东方",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207201227834eb28be0e.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dfws/index.m3u8"
        }, {
          "channelId": "480",
          "channelName": "湖南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/148/148/202212072026411559f439aa9.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws35/index.m3u8"
        }, {
          "channelId": "110",
          "channelName": "江苏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/100/100/202212072016253704df286ff.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jsws/index.m3u8"
        }, {
          "channelId": "475",
          "channelName": "浙江",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/133/133/202212072026219499bf03cdb.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zjws/index.m3u8"
        }, {
          "channelId": "467",
          "channelName": "北京",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/106/106/20221207202605186e334c7ae.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/bjws/index.m3u8"
        }, {
          "channelId": "62",
          "channelName": "广东",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/196/196/202212072014072922475ccfe.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gdws/index.m3u8"
        }, {
          "channelId": "154",
          "channelName": "深圳",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/170/170/20221207201912336c6462663.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/szws/index.m3u8"
        }, {
          "channelId": "86",
          "channelName": "黑龙江",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/147/147/202212072015259882baf55c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hljws/index.m3u8"
        }, {
          "channelId": "88",
          "channelName": "湖北",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/154/154/202212072015419210fd26e24.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws/index.m3u8"
        }, {
          "channelId": "148",
          "channelName": "山东",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/164/164/2022120720183062322708f40.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sdws/index.m3u8"
        }, {
          "channelId": "166",
          "channelName": "四川",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/20221207201928317495b7204.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/scws/index.m3u8"
        }, {
          "channelId": "1290",
          "channelName": "安徽",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/176/176/20221207204017183231d683.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ahws/index.m3u8"
        }, {
          "channelId": "268",
          "channelName": "重庆",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/163/163/2022120720242221995842d54.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cqws/index.m3u8"
        }, {
          "channelId": "170",
          "channelName": "天津",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/159/159/20221207201955482ffe5c63d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/tjws/index.m3u8"
        }, {
          "channelId": "42",
          "channelName": "东南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/20221207201241849264a8255.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dnws/index.m3u8"
        }, {
          "channelId": "84",
          "channelName": "河南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720150952252fbd3b6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws/index.m3u8"
        }, {
          "channelId": "112",
          "channelName": "江西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/171/171/2022120720164150348a07e03.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jxws/index.m3u8"
        }, {
          "channelId": "99",
          "channelName": "吉林",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/167/167/201906261346568355d6927df.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jlws/index.m3u8"
        }, {
          "channelId": "65",
          "channelName": "贵州",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/186/186/20190626134516827358cde83.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gzws/index.m3u8"
        }, {
          "channelId": "129",
          "channelName": "辽宁",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/12/4/164/164/20191204165502140909cd681.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/lnws/index.m3u8"
        }, {
          "channelId": "82",
          "channelName": "河北",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/116/116/20190626134532472ef3227c7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws33/index.m3u8"
        }, {
          "channelId": "1221",
          "channelName": "陕西新闻资讯",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/141/141/20221207202837557645acc5d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t/index.m3u8"
        }, {
          "channelId": "1222",
          "channelName": "陕西都市青春",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/181/181/2022120720285482607e62ce8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx2t/index.m3u8"
        }, {
          "channelId": "1223",
          "channelName": "陕西银龄",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/187/187/20221207202939895f2e3be02.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx3t/index.m3u8"
        }, {
          "channelId": "1225",
          "channelName": "陕西秦腔",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/100/100/20221207203025395322f59ca.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx5t/index.m3u8"
        }, {
          "channelId": "1226",
          "channelName": "陕西乐家购物",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2023/3/29/183/183/20230329103934380c7ab8bd6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx6t/index.m3u8"
        }, {
          "channelId": "1227",
          "channelName": "陕西体育休闲",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/159/159/202212072031008521aeb99f4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx7t/index.m3u8"
        }, {
          "channelId": "1228",
          "channelName": "西部电影",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/175/175/20221207203121934da21c433.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx8t/index.m3u8"
        }, {
          "channelId": "1229",
          "channelName": "农林卫视",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/167/167/202212072031375384ae96eae.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nlws/index.m3u8"
        }, {
          "channelId": "1244",
          "channelName": "CCTV-1 综合 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207222407598d36991a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1-HD/index.m3u8"
        }, {
          "channelId": "1245",
          "channelName": "CCTV-2 财经 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/2022120722241710bbebd40c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-2-HD/index.m3u8"
        }, {
          "channelId": "1246",
          "channelName": "CCTV-3 综艺 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/146/146/20221207222354748308bcc68.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-3-HD/index.m3u8"
        }, {
          "channelId": "1247",
          "channelName": "CCTV-4 中文国际 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222343276fff5efce.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-4-HD/index.m3u8"
        }, {
          "channelId": "1248",
          "channelName": "CCTV-5 体育 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/122/122/2022120722233126f882be7d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-5-HD/index.m3u8"
        }, {
          "channelId": "1249",
          "channelName": "CCTV-6 电影 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223198181b4f5e72.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-6-HD/index.m3u8"
        }, {
          "channelId": "1250",
          "channelName": "CCTV-7 国防军事 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223077319f73617a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-7-HD/index.m3u8"
        }, {
          "channelId": "1251",
          "channelName": "CCTV-8 电视剧 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222256669c3e1d6b7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-8-HD/index.m3u8"
        }, {
          "channelId": "1252",
          "channelName": "CCTV-9 纪录 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/152/152/20221207222244929b8d4b7bc.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-9-HD/index.m3u8"
        }, {
          "channelId": "1254",
          "channelName": "CCTV-10 科教 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/20221207222231504fb7ce4d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-10-HD/index.m3u8"
        }, {
          "channelId": "1255",
          "channelName": "CCTV-11 戏曲 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/198/198/202212072222188594550f71c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-11-HD/index.m3u8"
        }, {
          "channelId": "1256",
          "channelName": "CCTV-12 社会与法 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/117/117/20221207222207220284c9fc8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-12-HD/index.m3u8"
        }, {
          "channelId": "1358",
          "channelName": "CCTV-13 新闻 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072221151304eb5505e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13-HD/index.m3u8"
        }, {
          "channelId": "1257",
          "channelName": "CCTV-14 少儿 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/182/182/20221207222155328049fb5a6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-14-HD/index.m3u8"
        }, {
          "channelId": "1258",
          "channelName": "CCTV-15 音乐 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/2022120722214390791fff94f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-15-HD/index.m3u8"
        }, {
          "channelId": "1259",
          "channelName": "CCTV-17 农业农村 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/20221207222132202539afab9.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cctv17-HD/index.m3u8"
        }, {
          "channelId": "6",
          "channelName": "CGTN",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/165/165/202212072041501851b94c9ec.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-NEWS/index.m3u8"
        }, {
          "channelId": "264",
          "channelName": "综合",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/161/161/20221207202335888ecb9e4f8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1/index.m3u8"
        }, {
          "channelId": "458",
          "channelName": "财经",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/171/171/2022120720251563281358835.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-2/index.m3u8"
        }, {
          "channelId": "250",
          "channelName": "综艺",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/175/175/202212072021412061bd30e71.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-3/index.m3u8"
        }, {
          "channelId": "259",
          "channelName": "中文国际",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/118/118/202212072023057650110df4c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-4/index.m3u8"
        }, {
          "channelId": "460",
          "channelName": "体育",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207202533705c32d9f7a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-5/index.m3u8"
        }, {
          "channelId": "246",
          "channelName": "电影",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/202212072021081992442044c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-6/index.m3u8"
        }, {
          "channelId": "248",
          "channelName": "国防军事",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/2022120720212810862048e4c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-7/index.m3u8"
        }, {
          "channelId": "238",
          "channelName": "电视剧",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/196/196/20221207202054957c69ebde3.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-8/index.m3u8"
        }, {
          "channelId": "450",
          "channelName": "纪录",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/110/110/20221207202456195c3023d87.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-9/index.m3u8"
        }, {
          "channelId": "256",
          "channelName": "科教",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/199/199/20221207202235273a48669ed.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-10/index.m3u8"
        }, {
          "channelId": "258",
          "channelName": "戏曲",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/166/166/2022120720225137155a2a639.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-11/index.m3u8"
        }, {
          "channelId": "254",
          "channelName": "社会与法",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/193/193/202212072022137535e830337.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-12/index.m3u8"
        }, {
          "channelId": "263",
          "channelName": "新闻",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/202212072023214584b918a95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13/index.m3u8"
        }, {
          "channelId": "252",
          "channelName": "少儿",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207202154432b84b8335.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-14/index.m3u8"
        }, {
          "channelId": "266",
          "channelName": "音乐",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/137/137/20221207202352875c6a02c69.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-15/index.m3u8"
        }, {
          "channelId": "1233",
          "channelName": "农业农村",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/199/199/202212072032281723a250285.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cctv17/index.m3u8"
        }, {
          "channelId": "1502",
          "channelName": "陕西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/101/101/2024110509445978929c3937c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxws-HD/index.m3u8"
        }, {
          "channelId": "1260",
          "channelName": "东方卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720351191821898b11.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dfws-HD/index.m3u8"
        }, {
          "channelId": "1261",
          "channelName": "湖南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720352634886bbc892.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws-HD/index.m3u8"
        }, {
          "channelId": "1262",
          "channelName": "江苏卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/20221207203538852325a2b88.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jsws-HD/index.m3u8"
        }, {
          "channelId": "1263",
          "channelName": "浙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/20221207203552131534a252f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zjws-HD/index.m3u8"
        }, {
          "channelId": "1264",
          "channelName": "北京卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/137/137/202212072036065012d2a1d95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/bjws-HD/index.m3u8"
        }, {
          "channelId": "1265",
          "channelName": "广东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/162/162/20221207203627511f5e13d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gdws-HD/index.m3u8"
        }, {
          "channelId": "1266",
          "channelName": "深圳卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/180/180/20221207203640583e63fa438.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SZWS-HD/index.m3u8"
        }, {
          "channelId": "1267",
          "channelName": "黑龙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/134/134/20221207203656198d014c1cb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HLJWS-HD/index.m3u8"
        }, {
          "channelId": "1268",
          "channelName": "湖北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/151/151/202212072037118302177fa1b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws-HD/index.m3u8"
        }, {
          "channelId": "1269",
          "channelName": "山东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072037277168582433.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sdws-HD/index.m3u8"
        }, {
          "channelId": "1270",
          "channelName": "四川卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/191/191/20221207203742205af521b1d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SCWS-HD/index.m3u8"
        }, {
          "channelId": "1271",
          "channelName": "安徽卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/20221207203758233936ea70e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ahws-HD/index.m3u8"
        }, {
          "channelId": "1272",
          "channelName": "重庆卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/20221207203811940c62dadbb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CQWS-HD/index.m3u8"
        }, {
          "channelId": "1273",
          "channelName": "天津卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/154/154/20221207203824509804022ef.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/tjws-HD/index.m3u8"
        }, {
          "channelId": "1274",
          "channelName": "东南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/202212072038382189fea09ed.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/DNWS-HD/index.m3u8"
        }, {
          "channelId": "1275",
          "channelName": "河南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/150/150/202212072038523111d3231a0.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HENWS-HD/index.m3u8"
        }, {
          "channelId": "1276",
          "channelName": "江西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/110/110/202212072039081329dfdd5c7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JXWS-HD/index.m3u8"
        }, {
          "channelId": "1277",
          "channelName": "吉林卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/189/189/2022120720392130600be9a05.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JLWS-HD/index.m3u8"
        }, {
          "channelId": "150",
          "channelName": "山西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/184/184/20190626140149321f61f2260.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ssxws/index.m3u8"
        }, {
          "channelId": "1278",
          "channelName": "贵州卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/140/140/2022031617152978797823af.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/GZWS-HD/index.m3u8"
        }, {
          "channelId": "58",
          "channelName": "甘肃",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/177/177/2022120720125423223d7812a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gsws/index.m3u8"
        }, {
          "channelId": "137",
          "channelName": "宁夏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/114/114/20190626140114540c491b02b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nxws/index.m3u8"
        }, {
          "channelId": "64",
          "channelName": "广西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/110/110/20190626134452888ce96a0da.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gxws/index.m3u8"
        }, {
          "channelId": "1279",
          "channelName": "辽宁卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/158/158/2022031617162098005a2d260.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/LNWS-HD/index.m3u8"
        }, {
          "channelId": "144",
          "channelName": "青海",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/179/179/20190626142941540a41135bd.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/qhws/index.m3u8"
        }, {
          "channelId": "181",
          "channelName": "西藏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/166/166/2019062614371060936aa124b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xzws/index.m3u8"
        }, {
          "channelId": "136",
          "channelName": "内蒙古",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/158/158/20190626142907384b6e2e7f6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nmgws/index.m3u8"
        }, {
          "channelId": "189",
          "channelName": "新疆",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/144/144/20190626135855225fd8af02c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xjws/index.m3u8"
        }, {
          "channelId": "1280",
          "channelName": "河北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/115/115/20220316171717176a4d4dd90.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HEBWS-HD/index.m3u8"
        }, {
          "channelId": "216",
          "channelName": "云南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/147/147/20190626135941353f5c1b0d5.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ynws/index.m3u8"
        }, {
          "channelId": "24",
          "channelName": "兵团",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/173/173/2019062614062666486fe05ad.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/btws/index.m3u8"
        }, {
          "channelId": "1232",
          "channelName": "CETV1",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/2/134/134/202203021435319329091931c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zgjy/index.m3u8"
        }, {
          "channelId": "132",
          "channelName": "海南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/2/120/120/2022030214370034042ae2842.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/lyws/index.m3u8"
        }, {
          "channelId": "1418",
          "channelName": "CETV4 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2023/11/7/106/106/202311071622482947994370c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CETV4/index.m3u8"
        }, {
          "channelId": "151",
          "channelName": "陕西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720185319499a21b3c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxwshz/index.m3u8"
        }, {
          "channelId": "38",
          "channelName": "东方",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207201227834eb28be0e.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dfws/index.m3u8"
        }, {
          "channelId": "480",
          "channelName": "湖南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/148/148/202212072026411559f439aa9.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws35/index.m3u8"
        }, {
          "channelId": "110",
          "channelName": "江苏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/100/100/202212072016253704df286ff.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jsws/index.m3u8"
        }, {
          "channelId": "475",
          "channelName": "浙江",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/133/133/202212072026219499bf03cdb.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zjws/index.m3u8"
        }, {
          "channelId": "467",
          "channelName": "北京",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/106/106/20221207202605186e334c7ae.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/bjws/index.m3u8"
        }, {
          "channelId": "62",
          "channelName": "广东",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/196/196/202212072014072922475ccfe.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gdws/index.m3u8"
        }, {
          "channelId": "154",
          "channelName": "深圳",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/170/170/20221207201912336c6462663.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/szws/index.m3u8"
        }, {
          "channelId": "86",
          "channelName": "黑龙江",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/147/147/202212072015259882baf55c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hljws/index.m3u8"
        }, {
          "channelId": "88",
          "channelName": "湖北",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/154/154/202212072015419210fd26e24.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws/index.m3u8"
        }, {
          "channelId": "148",
          "channelName": "山东",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/164/164/2022120720183062322708f40.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sdws/index.m3u8"
        }, {
          "channelId": "166",
          "channelName": "四川",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/20221207201928317495b7204.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/scws/index.m3u8"
        }, {
          "channelId": "1290",
          "channelName": "安徽",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/176/176/20221207204017183231d683.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ahws/index.m3u8"
        }, {
          "channelId": "268",
          "channelName": "重庆",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/163/163/2022120720242221995842d54.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cqws/index.m3u8"
        }, {
          "channelId": "170",
          "channelName": "天津",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/159/159/20221207201955482ffe5c63d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/tjws/index.m3u8"
        }, {
          "channelId": "42",
          "channelName": "东南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/20221207201241849264a8255.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dnws/index.m3u8"
        }, {
          "channelId": "84",
          "channelName": "河南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720150952252fbd3b6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws/index.m3u8"
        }, {
          "channelId": "112",
          "channelName": "江西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/171/171/2022120720164150348a07e03.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jxws/index.m3u8"
        }, {
          "channelId": "99",
          "channelName": "吉林",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/167/167/201906261346568355d6927df.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jlws/index.m3u8"
        }, {
          "channelId": "65",
          "channelName": "贵州",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/186/186/20190626134516827358cde83.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gzws/index.m3u8"
        }, {
          "channelId": "129",
          "channelName": "辽宁",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/12/4/164/164/20191204165502140909cd681.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/lnws/index.m3u8"
        }, {
          "channelId": "82",
          "channelName": "河北",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/116/116/20190626134532472ef3227c7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws33/index.m3u8"
        }, {
          "channelId": "1358",
          "channelName": "CCTV-13 新闻 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072221151304eb5505e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13-HD/index.m3u8"
        }, {
          "channelId": "1502",
          "channelName": "陕西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/101/101/2024110509445978929c3937c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxws-HD/index.m3u8"
        }, {
          "channelId": "1503",
          "channelName": "陕西新闻资讯高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/136/136/20241105094553201e0f4bef4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t-HD/index.m3u8"
        }, {
          "channelId": "263",
          "channelName": "新闻",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/202212072023214584b918a95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13/index.m3u8"
        }, {
          "channelId": "151",
          "channelName": "陕西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720185319499a21b3c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxwshz/index.m3u8"
        }, {
          "channelId": "1221",
          "channelName": "陕西新闻资讯",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/141/141/20221207202837557645acc5d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t/index.m3u8"
        }, {
          "channelId": "1502",
          "channelName": "陕西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/101/101/2024110509445978929c3937c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxws-HD/index.m3u8"
        }, {
          "channelId": "1503",
          "channelName": "陕西新闻资讯高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/136/136/20241105094553201e0f4bef4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t-HD/index.m3u8"
        }, {
          "channelId": "1504",
          "channelName": "陕西都市青春高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/133/133/20241105094621650945717c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx2t-HD/index.m3u8"
        }, {
          "channelId": "1505",
          "channelName": "陕西银龄高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/174/174/202411050946409130aaf53.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx3t-HD/index.m3u8"
        }, {
          "channelId": "1507",
          "channelName": "陕西秦腔高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/104/104/202411050947225294228c5f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx5t-HD/index.m3u8"
        }, {
          "channelId": "1508",
          "channelName": "陕西乐家购物高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/20241105100935425e14700d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx6t-HD/index.m3u8"
        }, {
          "channelId": "1509",
          "channelName": "陕西体育休闲高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/102/102/20241105100958274114a58f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx7t-HD/index.m3u8"
        }, {
          "channelId": "1510",
          "channelName": "西部电影高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/202411051010176160b28c230.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx8t-HD/index.m3u8"
        }, {
          "channelId": "1511",
          "channelName": "农林卫视高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/124/124/20241105101047340918e4dba.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nlws-HD/index.m3u8"
        }, {
          "channelId": "151",
          "channelName": "陕西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720185319499a21b3c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxwshz/index.m3u8"
        }, {
          "channelId": "1221",
          "channelName": "陕西新闻资讯",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/141/141/20221207202837557645acc5d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t/index.m3u8"
        }, {
          "channelId": "1222",
          "channelName": "陕西都市青春",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/181/181/2022120720285482607e62ce8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx2t/index.m3u8"
        }, {
          "channelId": "1223",
          "channelName": "陕西银龄",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/187/187/20221207202939895f2e3be02.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx3t/index.m3u8"
        }, {
          "channelId": "1225",
          "channelName": "陕西秦腔",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/100/100/20221207203025395322f59ca.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx5t/index.m3u8"
        }, {
          "channelId": "1226",
          "channelName": "陕西乐家购物",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2023/3/29/183/183/20230329103934380c7ab8bd6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx6t/index.m3u8"
        }, {
          "channelId": "1227",
          "channelName": "陕西体育休闲",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/159/159/202212072031008521aeb99f4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx7t/index.m3u8"
        }, {
          "channelId": "1228",
          "channelName": "西部电影",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/175/175/20221207203121934da21c433.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx8t/index.m3u8"
        }, {
          "channelId": "1229",
          "channelName": "农林卫视",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/167/167/202212072031375384ae96eae.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nlws/index.m3u8"
        }, {
          "channelId": "1244",
          "channelName": "CCTV-1 综合 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207222407598d36991a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1-HD/index.m3u8"
        }, {
          "channelId": "1245",
          "channelName": "CCTV-2 财经 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/2022120722241710bbebd40c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-2-HD/index.m3u8"
        }, {
          "channelId": "1246",
          "channelName": "CCTV-3 综艺 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/146/146/20221207222354748308bcc68.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-3-HD/index.m3u8"
        }, {
          "channelId": "1247",
          "channelName": "CCTV-4 中文国际 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222343276fff5efce.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-4-HD/index.m3u8"
        }, {
          "channelId": "1248",
          "channelName": "CCTV-5 体育 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/122/122/2022120722233126f882be7d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-5-HD/index.m3u8"
        }, {
          "channelId": "1249",
          "channelName": "CCTV-6 电影 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223198181b4f5e72.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-6-HD/index.m3u8"
        }, {
          "channelId": "1250",
          "channelName": "CCTV-7 国防军事 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223077319f73617a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-7-HD/index.m3u8"
        }, {
          "channelId": "1251",
          "channelName": "CCTV-8 电视剧 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222256669c3e1d6b7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-8-HD/index.m3u8"
        }, {
          "channelId": "1252",
          "channelName": "CCTV-9 纪录 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/152/152/20221207222244929b8d4b7bc.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-9-HD/index.m3u8"
        }, {
          "channelId": "1254",
          "channelName": "CCTV-10 科教 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/20221207222231504fb7ce4d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-10-HD/index.m3u8"
        }, {
          "channelId": "1255",
          "channelName": "CCTV-11 戏曲 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/198/198/202212072222188594550f71c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-11-HD/index.m3u8"
        }, {
          "channelId": "1256",
          "channelName": "CCTV-12 社会与法 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/117/117/20221207222207220284c9fc8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-12-HD/index.m3u8"
        }, {
          "channelId": "1358",
          "channelName": "CCTV-13 新闻 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072221151304eb5505e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13-HD/index.m3u8"
        }, {
          "channelId": "1257",
          "channelName": "CCTV-14 少儿 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/182/182/20221207222155328049fb5a6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-14-HD/index.m3u8"
        }, {
          "channelId": "1258",
          "channelName": "CCTV-15 音乐 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/2022120722214390791fff94f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-15-HD/index.m3u8"
        }, {
          "channelId": "1259",
          "channelName": "CCTV-17 农业农村 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/20221207222132202539afab9.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cctv17-HD/index.m3u8"
        }, {
          "channelId": "1502",
          "channelName": "陕西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/101/101/2024110509445978929c3937c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxws-HD/index.m3u8"
        }, {
          "channelId": "1260",
          "channelName": "东方卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720351191821898b11.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dfws-HD/index.m3u8"
        }, {
          "channelId": "1261",
          "channelName": "湖南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720352634886bbc892.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws-HD/index.m3u8"
        }, {
          "channelId": "1262",
          "channelName": "江苏卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/20221207203538852325a2b88.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jsws-HD/index.m3u8"
        }, {
          "channelId": "1263",
          "channelName": "浙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/20221207203552131534a252f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zjws-HD/index.m3u8"
        }, {
          "channelId": "1264",
          "channelName": "北京卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/137/137/202212072036065012d2a1d95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/bjws-HD/index.m3u8"
        }, {
          "channelId": "1265",
          "channelName": "广东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/162/162/20221207203627511f5e13d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gdws-HD/index.m3u8"
        }, {
          "channelId": "1266",
          "channelName": "深圳卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/180/180/20221207203640583e63fa438.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SZWS-HD/index.m3u8"
        }, {
          "channelId": "1267",
          "channelName": "黑龙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/134/134/20221207203656198d014c1cb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HLJWS-HD/index.m3u8"
        }, {
          "channelId": "1268",
          "channelName": "湖北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/151/151/202212072037118302177fa1b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws-HD/index.m3u8"
        }, {
          "channelId": "1269",
          "channelName": "山东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072037277168582433.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sdws-HD/index.m3u8"
        }, {
          "channelId": "1270",
          "channelName": "四川卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/191/191/20221207203742205af521b1d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SCWS-HD/index.m3u8"
        }, {
          "channelId": "1271",
          "channelName": "安徽卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/20221207203758233936ea70e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ahws-HD/index.m3u8"
        }, {
          "channelId": "1272",
          "channelName": "重庆卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/20221207203811940c62dadbb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CQWS-HD/index.m3u8"
        }, {
          "channelId": "1273",
          "channelName": "天津卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/154/154/20221207203824509804022ef.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/tjws-HD/index.m3u8"
        }, {
          "channelId": "1274",
          "channelName": "东南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/202212072038382189fea09ed.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/DNWS-HD/index.m3u8"
        }, {
          "channelId": "1275",
          "channelName": "河南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/150/150/202212072038523111d3231a0.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HENWS-HD/index.m3u8"
        }, {
          "channelId": "1276",
          "channelName": "江西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/110/110/202212072039081329dfdd5c7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JXWS-HD/index.m3u8"
        }, {
          "channelId": "1277",
          "channelName": "吉林卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/189/189/2022120720392130600be9a05.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JLWS-HD/index.m3u8"
        }, {
          "channelId": "1278",
          "channelName": "贵州卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/140/140/2022031617152978797823af.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/GZWS-HD/index.m3u8"
        }, {
          "channelId": "1279",
          "channelName": "辽宁卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/158/158/2022031617162098005a2d260.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/LNWS-HD/index.m3u8"
        }, {
          "channelId": "1280",
          "channelName": "河北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/115/115/20220316171717176a4d4dd90.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HEBWS-HD/index.m3u8"
        }, {
          "channelId": "1418",
          "channelName": "CETV4 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2023/11/7/106/106/202311071622482947994370c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CETV4/index.m3u8"
        }, {
          "channelId": "1503",
          "channelName": "陕西新闻资讯高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/136/136/20241105094553201e0f4bef4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t-HD/index.m3u8"
        }, {
          "channelId": "1504",
          "channelName": "陕西都市青春高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/133/133/20241105094621650945717c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx2t-HD/index.m3u8"
        }, {
          "channelId": "1505",
          "channelName": "陕西银龄高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/174/174/202411050946409130aaf53.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx3t-HD/index.m3u8"
        }, {
          "channelId": "1507",
          "channelName": "陕西秦腔高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/104/104/202411050947225294228c5f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx5t-HD/index.m3u8"
        }, {
          "channelId": "1508",
          "channelName": "陕西乐家购物高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/20241105100935425e14700d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx6t-HD/index.m3u8"
        }, {
          "channelId": "1509",
          "channelName": "陕西体育休闲高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/102/102/20241105100958274114a58f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx7t-HD/index.m3u8"
        }, {
          "channelId": "1510",
          "channelName": "西部电影高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/202411051010176160b28c230.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx8t-HD/index.m3u8"
        }, {
          "channelId": "1511",
          "channelName": "农林卫视高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/124/124/20241105101047340918e4dba.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nlws-HD/index.m3u8"
        }, {
          "channelId": "116",
          "channelName": "金鹰卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/202212072017014723ac246e0.jpeg",
          "channelUrl": "http://shanxiunicom.vshk.wasu.tv/jykt/index.m3u8?"
        }, {
          "channelId": "1235",
          "channelName": "卡酷少儿",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/150/150/2022120720324331063869b5d.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/kkdh/index.m3u8"
        }, {
          "channelId": "210",
          "channelName": "优漫卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/149/149/202212072020296680ed40b1c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ymkt/index.m3u8"
        }, {
          "channelId": "1237",
          "channelName": "炫动卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/168/168/2022120720325885681b6d47.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xdkt/index.m3u8"
        }, {
          "channelId": "103",
          "channelName": "嘉佳卡通 ",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/115/115/2022120720160881888186c24.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jjkt/index.m3u8"
        }]
        '''
        data = json.loads(CHANNEL_DATA)

        for channel in data:
            if channel["channelId"] == channel_id:
                return channel["channelUrl"]
        return "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1-HD/index.m3u8"
    def generate_real_url(channel_url):
        key = "12b3da27-c3c8-4683-a824-c83f338ac84d"
        E = int(time.time()) + 36000
        sign_str = channel_url.replace("http://shanxiunicom-new.livestr.wasu.tv/", "")
        sign_str += f"?&E={E}&U=5d919b&A=2&K=5&P=01111&S="
        S = hmac.new(key.encode(), sign_str.encode(), hashlib.md5).hexdigest()
        real_url = f"{channel_url}?&E={E}&U=5d919b&A=2&K=5&P=01111&S={S}"
        return real_url
    def liveContent(self, url):
        # 内嵌的JSON数据
        CHANNEL_DATA = '''
        [{
          "channelId": "1244",
          "channelName": "CCTV-1 综合 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207222407598d36991a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1-HD/index.m3u8"
        }, {
          "channelId": "1245",
          "channelName": "CCTV-2 财经 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/2022120722241710bbebd40c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-2-HD/index.m3u8"
        }, {
          "channelId": "1246",
          "channelName": "CCTV-3 综艺 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/146/146/20221207222354748308bcc68.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-3-HD/index.m3u8"
        }, {
          "channelId": "1247",
          "channelName": "CCTV-4 中文国际 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222343276fff5efce.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-4-HD/index.m3u8"
        }, {
          "channelId": "1248",
          "channelName": "CCTV-5 体育 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/122/122/2022120722233126f882be7d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-5-HD/index.m3u8"
        }, {
          "channelId": "1249",
          "channelName": "CCTV-6 电影 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223198181b4f5e72.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-6-HD/index.m3u8"
        }, {
          "channelId": "1250",
          "channelName": "CCTV-7 国防军事 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223077319f73617a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-7-HD/index.m3u8"
        }, {
          "channelId": "1251",
          "channelName": "CCTV-8 电视剧 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222256669c3e1d6b7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-8-HD/index.m3u8"
        }, {
          "channelId": "1252",
          "channelName": "CCTV-9 纪录 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/152/152/20221207222244929b8d4b7bc.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-9-HD/index.m3u8"
        }, {
          "channelId": "1254",
          "channelName": "CCTV-10 科教 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/20221207222231504fb7ce4d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-10-HD/index.m3u8"
        }, {
          "channelId": "1255",
          "channelName": "CCTV-11 戏曲 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/198/198/202212072222188594550f71c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-11-HD/index.m3u8"
        }, {
          "channelId": "1256",
          "channelName": "CCTV-12 社会与法 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/117/117/20221207222207220284c9fc8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-12-HD/index.m3u8"
        }, {
          "channelId": "1358",
          "channelName": "CCTV-13 新闻 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072221151304eb5505e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13-HD/index.m3u8"
        }, {
          "channelId": "1257",
          "channelName": "CCTV-14 少儿 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/182/182/20221207222155328049fb5a6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-14-HD/index.m3u8"
        }, {
          "channelId": "1258",
          "channelName": "CCTV-15 音乐 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/2022120722214390791fff94f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-15-HD/index.m3u8"
        }, {
          "channelId": "1259",
          "channelName": "CCTV-17 农业农村 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/20221207222132202539afab9.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cctv17-HD/index.m3u8"
        }, {
          "channelId": "6",
          "channelName": "CGTN",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/165/165/202212072041501851b94c9ec.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-NEWS/index.m3u8"
        }, {
          "channelId": "1502",
          "channelName": "陕西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/101/101/2024110509445978929c3937c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxws-HD/index.m3u8"
        }, {
          "channelId": "1260",
          "channelName": "东方卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720351191821898b11.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dfws-HD/index.m3u8"
        }, {
          "channelId": "1261",
          "channelName": "湖南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720352634886bbc892.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws-HD/index.m3u8"
        }, {
          "channelId": "1262",
          "channelName": "江苏卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/20221207203538852325a2b88.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jsws-HD/index.m3u8"
        }, {
          "channelId": "1263",
          "channelName": "浙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/20221207203552131534a252f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zjws-HD/index.m3u8"
        }, {
          "channelId": "1264",
          "channelName": "北京卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/137/137/202212072036065012d2a1d95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/bjws-HD/index.m3u8"
        }, {
          "channelId": "1265",
          "channelName": "广东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/162/162/20221207203627511f5e13d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gdws-HD/index.m3u8"
        }, {
          "channelId": "1266",
          "channelName": "深圳卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/180/180/20221207203640583e63fa438.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SZWS-HD/index.m3u8"
        }, {
          "channelId": "1267",
          "channelName": "黑龙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/134/134/20221207203656198d014c1cb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HLJWS-HD/index.m3u8"
        }, {
          "channelId": "1268",
          "channelName": "湖北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/151/151/202212072037118302177fa1b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws-HD/index.m3u8"
        }, {
          "channelId": "1269",
          "channelName": "山东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072037277168582433.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sdws-HD/index.m3u8"
        }, {
          "channelId": "1270",
          "channelName": "四川卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/191/191/20221207203742205af521b1d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SCWS-HD/index.m3u8"
        }, {
          "channelId": "1271",
          "channelName": "安徽卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/20221207203758233936ea70e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ahws-HD/index.m3u8"
        }, {
          "channelId": "1272",
          "channelName": "重庆卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/20221207203811940c62dadbb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CQWS-HD/index.m3u8"
        }, {
          "channelId": "1273",
          "channelName": "天津卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/154/154/20221207203824509804022ef.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/tjws-HD/index.m3u8"
        }, {
          "channelId": "1274",
          "channelName": "东南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/202212072038382189fea09ed.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/DNWS-HD/index.m3u8"
        }, {
          "channelId": "1275",
          "channelName": "河南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/150/150/202212072038523111d3231a0.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HENWS-HD/index.m3u8"
        }, {
          "channelId": "1276",
          "channelName": "江西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/110/110/202212072039081329dfdd5c7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JXWS-HD/index.m3u8"
        }, {
          "channelId": "1277",
          "channelName": "吉林卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/189/189/2022120720392130600be9a05.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JLWS-HD/index.m3u8"
        }, {
          "channelId": "150",
          "channelName": "山西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/184/184/20190626140149321f61f2260.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ssxws/index.m3u8"
        }, {
          "channelId": "1278",
          "channelName": "贵州卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/140/140/2022031617152978797823af.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/GZWS-HD/index.m3u8"
        }, {
          "channelId": "58",
          "channelName": "甘肃",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/177/177/2022120720125423223d7812a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gsws/index.m3u8"
        }, {
          "channelId": "137",
          "channelName": "宁夏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/114/114/20190626140114540c491b02b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nxws/index.m3u8"
        }, {
          "channelId": "64",
          "channelName": "广西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/110/110/20190626134452888ce96a0da.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gxws/index.m3u8"
        }, {
          "channelId": "1279",
          "channelName": "辽宁卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/158/158/2022031617162098005a2d260.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/LNWS-HD/index.m3u8"
        }, {
          "channelId": "144",
          "channelName": "青海",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/179/179/20190626142941540a41135bd.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/qhws/index.m3u8"
        }, {
          "channelId": "181",
          "channelName": "西藏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/166/166/2019062614371060936aa124b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xzws/index.m3u8"
        }, {
          "channelId": "136",
          "channelName": "内蒙古",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/158/158/20190626142907384b6e2e7f6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nmgws/index.m3u8"
        }, {
          "channelId": "189",
          "channelName": "新疆",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/144/144/20190626135855225fd8af02c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xjws/index.m3u8"
        }, {
          "channelId": "1280",
          "channelName": "河北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/115/115/20220316171717176a4d4dd90.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HEBWS-HD/index.m3u8"
        }, {
          "channelId": "216",
          "channelName": "云南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/147/147/20190626135941353f5c1b0d5.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ynws/index.m3u8"
        }, {
          "channelId": "24",
          "channelName": "兵团",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/173/173/2019062614062666486fe05ad.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/btws/index.m3u8"
        }, {
          "channelId": "1232",
          "channelName": "CETV1",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/2/134/134/202203021435319329091931c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zgjy/index.m3u8"
        }, {
          "channelId": "132",
          "channelName": "海南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/2/120/120/2022030214370034042ae2842.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/lyws/index.m3u8"
        }, {
          "channelId": "1418",
          "channelName": "CETV4 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2023/11/7/106/106/202311071622482947994370c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CETV4/index.m3u8"
        }, {
          "channelId": "1503",
          "channelName": "陕西新闻资讯高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/136/136/20241105094553201e0f4bef4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t-HD/index.m3u8"
        }, {
          "channelId": "1504",
          "channelName": "陕西都市青春高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/133/133/20241105094621650945717c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx2t-HD/index.m3u8"
        }, {
          "channelId": "1505",
          "channelName": "陕西银龄高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/174/174/202411050946409130aaf53.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx3t-HD/index.m3u8"
        }, {
          "channelId": "1507",
          "channelName": "陕西秦腔高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/104/104/202411050947225294228c5f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx5t-HD/index.m3u8"
        }, {
          "channelId": "1508",
          "channelName": "陕西乐家购物高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/20241105100935425e14700d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx6t-HD/index.m3u8"
        }, {
          "channelId": "1509",
          "channelName": "陕西体育休闲高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/102/102/20241105100958274114a58f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx7t-HD/index.m3u8"
        }, {
          "channelId": "1510",
          "channelName": "西部电影高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/202411051010176160b28c230.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx8t-HD/index.m3u8"
        }, {
          "channelId": "1511",
          "channelName": "农林卫视高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/124/124/20241105101047340918e4dba.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nlws-HD/index.m3u8"
        }, {
          "channelId": "116",
          "channelName": "金鹰卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/202212072017014723ac246e0.jpeg",
          "channelUrl": "http://shanxiunicom.vshk.wasu.tv/jykt/index.m3u8?"
        }, {
          "channelId": "1235",
          "channelName": "卡酷少儿",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/150/150/2022120720324331063869b5d.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/kkdh/index.m3u8"
        }, {
          "channelId": "210",
          "channelName": "优漫卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/149/149/202212072020296680ed40b1c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ymkt/index.m3u8"
        }, {
          "channelId": "1237",
          "channelName": "炫动卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/168/168/2022120720325885681b6d47.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xdkt/index.m3u8"
        }, {
          "channelId": "103",
          "channelName": "嘉佳卡通 ",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/115/115/2022120720160881888186c24.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jjkt/index.m3u8"
        }, {
          "channelId": "264",
          "channelName": "综合",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/161/161/20221207202335888ecb9e4f8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1/index.m3u8"
        }, {
          "channelId": "458",
          "channelName": "财经",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/171/171/2022120720251563281358835.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-2/index.m3u8"
        }, {
          "channelId": "250",
          "channelName": "综艺",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/175/175/202212072021412061bd30e71.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-3/index.m3u8"
        }, {
          "channelId": "259",
          "channelName": "中文国际",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/118/118/202212072023057650110df4c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-4/index.m3u8"
        }, {
          "channelId": "460",
          "channelName": "体育",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207202533705c32d9f7a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-5/index.m3u8"
        }, {
          "channelId": "246",
          "channelName": "电影",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/202212072021081992442044c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-6/index.m3u8"
        }, {
          "channelId": "248",
          "channelName": "国防军事",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/2022120720212810862048e4c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-7/index.m3u8"
        }, {
          "channelId": "238",
          "channelName": "电视剧",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/196/196/20221207202054957c69ebde3.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-8/index.m3u8"
        }, {
          "channelId": "450",
          "channelName": "纪录",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/110/110/20221207202456195c3023d87.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-9/index.m3u8"
        }, {
          "channelId": "256",
          "channelName": "科教",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/199/199/20221207202235273a48669ed.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-10/index.m3u8"
        }, {
          "channelId": "258",
          "channelName": "戏曲",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/166/166/2022120720225137155a2a639.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-11/index.m3u8"
        }, {
          "channelId": "254",
          "channelName": "社会与法",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/193/193/202212072022137535e830337.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-12/index.m3u8"
        }, {
          "channelId": "263",
          "channelName": "新闻",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/202212072023214584b918a95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13/index.m3u8"
        }, {
          "channelId": "252",
          "channelName": "少儿",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207202154432b84b8335.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-14/index.m3u8"
        }, {
          "channelId": "266",
          "channelName": "音乐",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/137/137/20221207202352875c6a02c69.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-15/index.m3u8"
        }, {
          "channelId": "1233",
          "channelName": "农业农村",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/199/199/202212072032281723a250285.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cctv17/index.m3u8"
        }, {
          "channelId": "151",
          "channelName": "陕西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720185319499a21b3c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxwshz/index.m3u8"
        }, {
          "channelId": "38",
          "channelName": "东方",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207201227834eb28be0e.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dfws/index.m3u8"
        }, {
          "channelId": "480",
          "channelName": "湖南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/148/148/202212072026411559f439aa9.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws35/index.m3u8"
        }, {
          "channelId": "110",
          "channelName": "江苏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/100/100/202212072016253704df286ff.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jsws/index.m3u8"
        }, {
          "channelId": "475",
          "channelName": "浙江",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/133/133/202212072026219499bf03cdb.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zjws/index.m3u8"
        }, {
          "channelId": "467",
          "channelName": "北京",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/106/106/20221207202605186e334c7ae.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/bjws/index.m3u8"
        }, {
          "channelId": "62",
          "channelName": "广东",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/196/196/202212072014072922475ccfe.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gdws/index.m3u8"
        }, {
          "channelId": "154",
          "channelName": "深圳",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/170/170/20221207201912336c6462663.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/szws/index.m3u8"
        }, {
          "channelId": "86",
          "channelName": "黑龙江",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/147/147/202212072015259882baf55c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hljws/index.m3u8"
        }, {
          "channelId": "88",
          "channelName": "湖北",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/154/154/202212072015419210fd26e24.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws/index.m3u8"
        }, {
          "channelId": "148",
          "channelName": "山东",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/164/164/2022120720183062322708f40.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sdws/index.m3u8"
        }, {
          "channelId": "166",
          "channelName": "四川",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/20221207201928317495b7204.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/scws/index.m3u8"
        }, {
          "channelId": "1290",
          "channelName": "安徽",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/176/176/20221207204017183231d683.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ahws/index.m3u8"
        }, {
          "channelId": "268",
          "channelName": "重庆",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/163/163/2022120720242221995842d54.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cqws/index.m3u8"
        }, {
          "channelId": "170",
          "channelName": "天津",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/159/159/20221207201955482ffe5c63d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/tjws/index.m3u8"
        }, {
          "channelId": "42",
          "channelName": "东南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/20221207201241849264a8255.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dnws/index.m3u8"
        }, {
          "channelId": "84",
          "channelName": "河南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720150952252fbd3b6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws/index.m3u8"
        }, {
          "channelId": "112",
          "channelName": "江西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/171/171/2022120720164150348a07e03.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jxws/index.m3u8"
        }, {
          "channelId": "99",
          "channelName": "吉林",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/167/167/201906261346568355d6927df.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jlws/index.m3u8"
        }, {
          "channelId": "65",
          "channelName": "贵州",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/186/186/20190626134516827358cde83.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gzws/index.m3u8"
        }, {
          "channelId": "129",
          "channelName": "辽宁",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/12/4/164/164/20191204165502140909cd681.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/lnws/index.m3u8"
        }, {
          "channelId": "82",
          "channelName": "河北",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/116/116/20190626134532472ef3227c7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws33/index.m3u8"
        }, {
          "channelId": "1221",
          "channelName": "陕西新闻资讯",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/141/141/20221207202837557645acc5d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t/index.m3u8"
        }, {
          "channelId": "1222",
          "channelName": "陕西都市青春",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/181/181/2022120720285482607e62ce8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx2t/index.m3u8"
        }, {
          "channelId": "1223",
          "channelName": "陕西银龄",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/187/187/20221207202939895f2e3be02.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx3t/index.m3u8"
        }, {
          "channelId": "1225",
          "channelName": "陕西秦腔",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/100/100/20221207203025395322f59ca.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx5t/index.m3u8"
        }, {
          "channelId": "1226",
          "channelName": "陕西乐家购物",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2023/3/29/183/183/20230329103934380c7ab8bd6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx6t/index.m3u8"
        }, {
          "channelId": "1227",
          "channelName": "陕西体育休闲",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/159/159/202212072031008521aeb99f4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx7t/index.m3u8"
        }, {
          "channelId": "1228",
          "channelName": "西部电影",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/175/175/20221207203121934da21c433.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx8t/index.m3u8"
        }, {
          "channelId": "1229",
          "channelName": "农林卫视",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/167/167/202212072031375384ae96eae.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nlws/index.m3u8"
        }, {
          "channelId": "1244",
          "channelName": "CCTV-1 综合 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207222407598d36991a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1-HD/index.m3u8"
        }, {
          "channelId": "1245",
          "channelName": "CCTV-2 财经 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/2022120722241710bbebd40c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-2-HD/index.m3u8"
        }, {
          "channelId": "1246",
          "channelName": "CCTV-3 综艺 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/146/146/20221207222354748308bcc68.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-3-HD/index.m3u8"
        }, {
          "channelId": "1247",
          "channelName": "CCTV-4 中文国际 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222343276fff5efce.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-4-HD/index.m3u8"
        }, {
          "channelId": "1248",
          "channelName": "CCTV-5 体育 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/122/122/2022120722233126f882be7d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-5-HD/index.m3u8"
        }, {
          "channelId": "1249",
          "channelName": "CCTV-6 电影 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223198181b4f5e72.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-6-HD/index.m3u8"
        }, {
          "channelId": "1250",
          "channelName": "CCTV-7 国防军事 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223077319f73617a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-7-HD/index.m3u8"
        }, {
          "channelId": "1251",
          "channelName": "CCTV-8 电视剧 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222256669c3e1d6b7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-8-HD/index.m3u8"
        }, {
          "channelId": "1252",
          "channelName": "CCTV-9 纪录 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/152/152/20221207222244929b8d4b7bc.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-9-HD/index.m3u8"
        }, {
          "channelId": "1254",
          "channelName": "CCTV-10 科教 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/20221207222231504fb7ce4d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-10-HD/index.m3u8"
        }, {
          "channelId": "1255",
          "channelName": "CCTV-11 戏曲 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/198/198/202212072222188594550f71c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-11-HD/index.m3u8"
        }, {
          "channelId": "1256",
          "channelName": "CCTV-12 社会与法 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/117/117/20221207222207220284c9fc8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-12-HD/index.m3u8"
        }, {
          "channelId": "1358",
          "channelName": "CCTV-13 新闻 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072221151304eb5505e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13-HD/index.m3u8"
        }, {
          "channelId": "1257",
          "channelName": "CCTV-14 少儿 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/182/182/20221207222155328049fb5a6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-14-HD/index.m3u8"
        }, {
          "channelId": "1258",
          "channelName": "CCTV-15 音乐 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/2022120722214390791fff94f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-15-HD/index.m3u8"
        }, {
          "channelId": "1259",
          "channelName": "CCTV-17 农业农村 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/20221207222132202539afab9.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cctv17-HD/index.m3u8"
        }, {
          "channelId": "6",
          "channelName": "CGTN",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/165/165/202212072041501851b94c9ec.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-NEWS/index.m3u8"
        }, {
          "channelId": "264",
          "channelName": "综合",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/161/161/20221207202335888ecb9e4f8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1/index.m3u8"
        }, {
          "channelId": "458",
          "channelName": "财经",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/171/171/2022120720251563281358835.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-2/index.m3u8"
        }, {
          "channelId": "250",
          "channelName": "综艺",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/175/175/202212072021412061bd30e71.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-3/index.m3u8"
        }, {
          "channelId": "259",
          "channelName": "中文国际",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/118/118/202212072023057650110df4c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-4/index.m3u8"
        }, {
          "channelId": "460",
          "channelName": "体育",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207202533705c32d9f7a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-5/index.m3u8"
        }, {
          "channelId": "246",
          "channelName": "电影",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/202212072021081992442044c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-6/index.m3u8"
        }, {
          "channelId": "248",
          "channelName": "国防军事",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/2022120720212810862048e4c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-7/index.m3u8"
        }, {
          "channelId": "238",
          "channelName": "电视剧",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/196/196/20221207202054957c69ebde3.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-8/index.m3u8"
        }, {
          "channelId": "450",
          "channelName": "纪录",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/110/110/20221207202456195c3023d87.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-9/index.m3u8"
        }, {
          "channelId": "256",
          "channelName": "科教",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/199/199/20221207202235273a48669ed.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-10/index.m3u8"
        }, {
          "channelId": "258",
          "channelName": "戏曲",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/166/166/2022120720225137155a2a639.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-11/index.m3u8"
        }, {
          "channelId": "254",
          "channelName": "社会与法",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/193/193/202212072022137535e830337.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-12/index.m3u8"
        }, {
          "channelId": "263",
          "channelName": "新闻",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/202212072023214584b918a95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13/index.m3u8"
        }, {
          "channelId": "252",
          "channelName": "少儿",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207202154432b84b8335.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-14/index.m3u8"
        }, {
          "channelId": "266",
          "channelName": "音乐",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/137/137/20221207202352875c6a02c69.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-15/index.m3u8"
        }, {
          "channelId": "1233",
          "channelName": "农业农村",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/199/199/202212072032281723a250285.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cctv17/index.m3u8"
        }, {
          "channelId": "1502",
          "channelName": "陕西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/101/101/2024110509445978929c3937c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxws-HD/index.m3u8"
        }, {
          "channelId": "1260",
          "channelName": "东方卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720351191821898b11.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dfws-HD/index.m3u8"
        }, {
          "channelId": "1261",
          "channelName": "湖南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720352634886bbc892.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws-HD/index.m3u8"
        }, {
          "channelId": "1262",
          "channelName": "江苏卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/20221207203538852325a2b88.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jsws-HD/index.m3u8"
        }, {
          "channelId": "1263",
          "channelName": "浙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/20221207203552131534a252f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zjws-HD/index.m3u8"
        }, {
          "channelId": "1264",
          "channelName": "北京卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/137/137/202212072036065012d2a1d95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/bjws-HD/index.m3u8"
        }, {
          "channelId": "1265",
          "channelName": "广东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/162/162/20221207203627511f5e13d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gdws-HD/index.m3u8"
        }, {
          "channelId": "1266",
          "channelName": "深圳卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/180/180/20221207203640583e63fa438.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SZWS-HD/index.m3u8"
        }, {
          "channelId": "1267",
          "channelName": "黑龙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/134/134/20221207203656198d014c1cb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HLJWS-HD/index.m3u8"
        }, {
          "channelId": "1268",
          "channelName": "湖北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/151/151/202212072037118302177fa1b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws-HD/index.m3u8"
        }, {
          "channelId": "1269",
          "channelName": "山东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072037277168582433.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sdws-HD/index.m3u8"
        }, {
          "channelId": "1270",
          "channelName": "四川卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/191/191/20221207203742205af521b1d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SCWS-HD/index.m3u8"
        }, {
          "channelId": "1271",
          "channelName": "安徽卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/20221207203758233936ea70e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ahws-HD/index.m3u8"
        }, {
          "channelId": "1272",
          "channelName": "重庆卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/20221207203811940c62dadbb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CQWS-HD/index.m3u8"
        }, {
          "channelId": "1273",
          "channelName": "天津卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/154/154/20221207203824509804022ef.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/tjws-HD/index.m3u8"
        }, {
          "channelId": "1274",
          "channelName": "东南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/202212072038382189fea09ed.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/DNWS-HD/index.m3u8"
        }, {
          "channelId": "1275",
          "channelName": "河南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/150/150/202212072038523111d3231a0.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HENWS-HD/index.m3u8"
        }, {
          "channelId": "1276",
          "channelName": "江西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/110/110/202212072039081329dfdd5c7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JXWS-HD/index.m3u8"
        }, {
          "channelId": "1277",
          "channelName": "吉林卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/189/189/2022120720392130600be9a05.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JLWS-HD/index.m3u8"
        }, {
          "channelId": "150",
          "channelName": "山西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/184/184/20190626140149321f61f2260.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ssxws/index.m3u8"
        }, {
          "channelId": "1278",
          "channelName": "贵州卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/140/140/2022031617152978797823af.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/GZWS-HD/index.m3u8"
        }, {
          "channelId": "58",
          "channelName": "甘肃",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/177/177/2022120720125423223d7812a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gsws/index.m3u8"
        }, {
          "channelId": "137",
          "channelName": "宁夏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/114/114/20190626140114540c491b02b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nxws/index.m3u8"
        }, {
          "channelId": "64",
          "channelName": "广西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/110/110/20190626134452888ce96a0da.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gxws/index.m3u8"
        }, {
          "channelId": "1279",
          "channelName": "辽宁卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/158/158/2022031617162098005a2d260.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/LNWS-HD/index.m3u8"
        }, {
          "channelId": "144",
          "channelName": "青海",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/179/179/20190626142941540a41135bd.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/qhws/index.m3u8"
        }, {
          "channelId": "181",
          "channelName": "西藏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/166/166/2019062614371060936aa124b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xzws/index.m3u8"
        }, {
          "channelId": "136",
          "channelName": "内蒙古",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/158/158/20190626142907384b6e2e7f6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nmgws/index.m3u8"
        }, {
          "channelId": "189",
          "channelName": "新疆",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/144/144/20190626135855225fd8af02c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xjws/index.m3u8"
        }, {
          "channelId": "1280",
          "channelName": "河北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/115/115/20220316171717176a4d4dd90.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HEBWS-HD/index.m3u8"
        }, {
          "channelId": "216",
          "channelName": "云南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/147/147/20190626135941353f5c1b0d5.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ynws/index.m3u8"
        }, {
          "channelId": "24",
          "channelName": "兵团",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/173/173/2019062614062666486fe05ad.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/btws/index.m3u8"
        }, {
          "channelId": "1232",
          "channelName": "CETV1",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/2/134/134/202203021435319329091931c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zgjy/index.m3u8"
        }, {
          "channelId": "132",
          "channelName": "海南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/2/120/120/2022030214370034042ae2842.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/lyws/index.m3u8"
        }, {
          "channelId": "1418",
          "channelName": "CETV4 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2023/11/7/106/106/202311071622482947994370c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CETV4/index.m3u8"
        }, {
          "channelId": "151",
          "channelName": "陕西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720185319499a21b3c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxwshz/index.m3u8"
        }, {
          "channelId": "38",
          "channelName": "东方",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207201227834eb28be0e.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dfws/index.m3u8"
        }, {
          "channelId": "480",
          "channelName": "湖南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/148/148/202212072026411559f439aa9.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws35/index.m3u8"
        }, {
          "channelId": "110",
          "channelName": "江苏",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/100/100/202212072016253704df286ff.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jsws/index.m3u8"
        }, {
          "channelId": "475",
          "channelName": "浙江",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/133/133/202212072026219499bf03cdb.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zjws/index.m3u8"
        }, {
          "channelId": "467",
          "channelName": "北京",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/106/106/20221207202605186e334c7ae.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/bjws/index.m3u8"
        }, {
          "channelId": "62",
          "channelName": "广东",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/196/196/202212072014072922475ccfe.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gdws/index.m3u8"
        }, {
          "channelId": "154",
          "channelName": "深圳",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/170/170/20221207201912336c6462663.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/szws/index.m3u8"
        }, {
          "channelId": "86",
          "channelName": "黑龙江",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/147/147/202212072015259882baf55c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hljws/index.m3u8"
        }, {
          "channelId": "88",
          "channelName": "湖北",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/154/154/202212072015419210fd26e24.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws/index.m3u8"
        }, {
          "channelId": "148",
          "channelName": "山东",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/164/164/2022120720183062322708f40.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sdws/index.m3u8"
        }, {
          "channelId": "166",
          "channelName": "四川",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/20221207201928317495b7204.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/scws/index.m3u8"
        }, {
          "channelId": "1290",
          "channelName": "安徽",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/176/176/20221207204017183231d683.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ahws/index.m3u8"
        }, {
          "channelId": "268",
          "channelName": "重庆",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/163/163/2022120720242221995842d54.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cqws/index.m3u8"
        }, {
          "channelId": "170",
          "channelName": "天津",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/159/159/20221207201955482ffe5c63d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/tjws/index.m3u8"
        }, {
          "channelId": "42",
          "channelName": "东南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/20221207201241849264a8255.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dnws/index.m3u8"
        }, {
          "channelId": "84",
          "channelName": "河南",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720150952252fbd3b6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws/index.m3u8"
        }, {
          "channelId": "112",
          "channelName": "江西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/171/171/2022120720164150348a07e03.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jxws/index.m3u8"
        }, {
          "channelId": "99",
          "channelName": "吉林",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/167/167/201906261346568355d6927df.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jlws/index.m3u8"
        }, {
          "channelId": "65",
          "channelName": "贵州",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/186/186/20190626134516827358cde83.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gzws/index.m3u8"
        }, {
          "channelId": "129",
          "channelName": "辽宁",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/12/4/164/164/20191204165502140909cd681.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/lnws/index.m3u8"
        }, {
          "channelId": "82",
          "channelName": "河北",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2019/6/26/116/116/20190626134532472ef3227c7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws33/index.m3u8"
        }, {
          "channelId": "1358",
          "channelName": "CCTV-13 新闻 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072221151304eb5505e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13-HD/index.m3u8"
        }, {
          "channelId": "1502",
          "channelName": "陕西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/101/101/2024110509445978929c3937c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxws-HD/index.m3u8"
        }, {
          "channelId": "1503",
          "channelName": "陕西新闻资讯高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/136/136/20241105094553201e0f4bef4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t-HD/index.m3u8"
        }, {
          "channelId": "263",
          "channelName": "新闻",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/202212072023214584b918a95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13/index.m3u8"
        }, {
          "channelId": "151",
          "channelName": "陕西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720185319499a21b3c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxwshz/index.m3u8"
        }, {
          "channelId": "1221",
          "channelName": "陕西新闻资讯",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/141/141/20221207202837557645acc5d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t/index.m3u8"
        }, {
          "channelId": "1502",
          "channelName": "陕西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/101/101/2024110509445978929c3937c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxws-HD/index.m3u8"
        }, {
          "channelId": "1503",
          "channelName": "陕西新闻资讯高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/136/136/20241105094553201e0f4bef4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t-HD/index.m3u8"
        }, {
          "channelId": "1504",
          "channelName": "陕西都市青春高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/133/133/20241105094621650945717c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx2t-HD/index.m3u8"
        }, {
          "channelId": "1505",
          "channelName": "陕西银龄高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/174/174/202411050946409130aaf53.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx3t-HD/index.m3u8"
        }, {
          "channelId": "1507",
          "channelName": "陕西秦腔高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/104/104/202411050947225294228c5f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx5t-HD/index.m3u8"
        }, {
          "channelId": "1508",
          "channelName": "陕西乐家购物高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/20241105100935425e14700d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx6t-HD/index.m3u8"
        }, {
          "channelId": "1509",
          "channelName": "陕西体育休闲高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/102/102/20241105100958274114a58f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx7t-HD/index.m3u8"
        }, {
          "channelId": "1510",
          "channelName": "西部电影高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/202411051010176160b28c230.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx8t-HD/index.m3u8"
        }, {
          "channelId": "1511",
          "channelName": "农林卫视高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/124/124/20241105101047340918e4dba.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nlws-HD/index.m3u8"
        }, {
          "channelId": "151",
          "channelName": "陕西",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/2022120720185319499a21b3c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxwshz/index.m3u8"
        }, {
          "channelId": "1221",
          "channelName": "陕西新闻资讯",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/141/141/20221207202837557645acc5d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t/index.m3u8"
        }, {
          "channelId": "1222",
          "channelName": "陕西都市青春",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/181/181/2022120720285482607e62ce8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx2t/index.m3u8"
        }, {
          "channelId": "1223",
          "channelName": "陕西银龄",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/187/187/20221207202939895f2e3be02.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx3t/index.m3u8"
        }, {
          "channelId": "1225",
          "channelName": "陕西秦腔",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/100/100/20221207203025395322f59ca.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx5t/index.m3u8"
        }, {
          "channelId": "1226",
          "channelName": "陕西乐家购物",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2023/3/29/183/183/20230329103934380c7ab8bd6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx6t/index.m3u8"
        }, {
          "channelId": "1227",
          "channelName": "陕西体育休闲",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/159/159/202212072031008521aeb99f4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx7t/index.m3u8"
        }, {
          "channelId": "1228",
          "channelName": "西部电影",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/175/175/20221207203121934da21c433.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx8t/index.m3u8"
        }, {
          "channelId": "1229",
          "channelName": "农林卫视",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/167/167/202212072031375384ae96eae.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nlws/index.m3u8"
        }, {
          "channelId": "1244",
          "channelName": "CCTV-1 综合 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/20221207222407598d36991a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-1-HD/index.m3u8"
        }, {
          "channelId": "1245",
          "channelName": "CCTV-2 财经 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/2022120722241710bbebd40c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-2-HD/index.m3u8"
        }, {
          "channelId": "1246",
          "channelName": "CCTV-3 综艺 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/146/146/20221207222354748308bcc68.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-3-HD/index.m3u8"
        }, {
          "channelId": "1247",
          "channelName": "CCTV-4 中文国际 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222343276fff5efce.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-4-HD/index.m3u8"
        }, {
          "channelId": "1248",
          "channelName": "CCTV-5 体育 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/122/122/2022120722233126f882be7d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-5-HD/index.m3u8"
        }, {
          "channelId": "1249",
          "channelName": "CCTV-6 电影 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223198181b4f5e72.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-6-HD/index.m3u8"
        }, {
          "channelId": "1250",
          "channelName": "CCTV-7 国防军事 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/202212072223077319f73617a.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-7-HD/index.m3u8"
        }, {
          "channelId": "1251",
          "channelName": "CCTV-8 电视剧 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/120/120/20221207222256669c3e1d6b7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-8-HD/index.m3u8"
        }, {
          "channelId": "1252",
          "channelName": "CCTV-9 纪录 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/152/152/20221207222244929b8d4b7bc.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-9-HD/index.m3u8"
        }, {
          "channelId": "1254",
          "channelName": "CCTV-10 科教 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/197/197/20221207222231504fb7ce4d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-10-HD/index.m3u8"
        }, {
          "channelId": "1255",
          "channelName": "CCTV-11 戏曲 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/198/198/202212072222188594550f71c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-11-HD/index.m3u8"
        }, {
          "channelId": "1256",
          "channelName": "CCTV-12 社会与法 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/117/117/20221207222207220284c9fc8.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-12-HD/index.m3u8"
        }, {
          "channelId": "1358",
          "channelName": "CCTV-13 新闻 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072221151304eb5505e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-13-HD/index.m3u8"
        }, {
          "channelId": "1257",
          "channelName": "CCTV-14 少儿 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/182/182/20221207222155328049fb5a6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-14-HD/index.m3u8"
        }, {
          "channelId": "1258",
          "channelName": "CCTV-15 音乐 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/2022120722214390791fff94f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CCTV-15-HD/index.m3u8"
        }, {
          "channelId": "1259",
          "channelName": "CCTV-17 农业农村 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/125/125/20221207222132202539afab9.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/cctv17-HD/index.m3u8"
        }, {
          "channelId": "1502",
          "channelName": "陕西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/101/101/2024110509445978929c3937c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sxws-HD/index.m3u8"
        }, {
          "channelId": "1260",
          "channelName": "东方卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720351191821898b11.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/dfws-HD/index.m3u8"
        }, {
          "channelId": "1261",
          "channelName": "湖南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/2022120720352634886bbc892.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hnws-HD/index.m3u8"
        }, {
          "channelId": "1262",
          "channelName": "江苏卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/192/192/20221207203538852325a2b88.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jsws-HD/index.m3u8"
        }, {
          "channelId": "1263",
          "channelName": "浙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/139/139/20221207203552131534a252f.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/zjws-HD/index.m3u8"
        }, {
          "channelId": "1264",
          "channelName": "北京卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/137/137/202212072036065012d2a1d95.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/bjws-HD/index.m3u8"
        }, {
          "channelId": "1265",
          "channelName": "广东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/162/162/20221207203627511f5e13d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/gdws-HD/index.m3u8"
        }, {
          "channelId": "1266",
          "channelName": "深圳卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/180/180/20221207203640583e63fa438.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SZWS-HD/index.m3u8"
        }, {
          "channelId": "1267",
          "channelName": "黑龙江卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/134/134/20221207203656198d014c1cb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HLJWS-HD/index.m3u8"
        }, {
          "channelId": "1268",
          "channelName": "湖北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/151/151/202212072037118302177fa1b.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/hbws-HD/index.m3u8"
        }, {
          "channelId": "1269",
          "channelName": "山东卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/119/119/202212072037277168582433.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sdws-HD/index.m3u8"
        }, {
          "channelId": "1270",
          "channelName": "四川卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/191/191/20221207203742205af521b1d.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/SCWS-HD/index.m3u8"
        }, {
          "channelId": "1271",
          "channelName": "安徽卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/107/107/20221207203758233936ea70e.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ahws-HD/index.m3u8"
        }, {
          "channelId": "1272",
          "channelName": "重庆卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/129/129/20221207203811940c62dadbb.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CQWS-HD/index.m3u8"
        }, {
          "channelId": "1273",
          "channelName": "天津卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/154/154/20221207203824509804022ef.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/tjws-HD/index.m3u8"
        }, {
          "channelId": "1274",
          "channelName": "东南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/190/190/202212072038382189fea09ed.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/DNWS-HD/index.m3u8"
        }, {
          "channelId": "1275",
          "channelName": "河南卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/150/150/202212072038523111d3231a0.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HENWS-HD/index.m3u8"
        }, {
          "channelId": "1276",
          "channelName": "江西卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/110/110/202212072039081329dfdd5c7.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JXWS-HD/index.m3u8"
        }, {
          "channelId": "1277",
          "channelName": "吉林卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/189/189/2022120720392130600be9a05.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/JLWS-HD/index.m3u8"
        }, {
          "channelId": "1278",
          "channelName": "贵州卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/140/140/2022031617152978797823af.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/GZWS-HD/index.m3u8"
        }, {
          "channelId": "1279",
          "channelName": "辽宁卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/158/158/2022031617162098005a2d260.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/LNWS-HD/index.m3u8"
        }, {
          "channelId": "1280",
          "channelName": "河北卫视 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/3/16/115/115/20220316171717176a4d4dd90.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/HEBWS-HD/index.m3u8"
        }, {
          "channelId": "1418",
          "channelName": "CETV4 高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2023/11/7/106/106/202311071622482947994370c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/CETV4/index.m3u8"
        }, {
          "channelId": "1503",
          "channelName": "陕西新闻资讯高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/136/136/20241105094553201e0f4bef4.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx1t-HD/index.m3u8"
        }, {
          "channelId": "1504",
          "channelName": "陕西都市青春高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/133/133/20241105094621650945717c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx2t-HD/index.m3u8"
        }, {
          "channelId": "1505",
          "channelName": "陕西银龄高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/174/174/202411050946409130aaf53.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx3t-HD/index.m3u8"
        }, {
          "channelId": "1507",
          "channelName": "陕西秦腔高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/104/104/202411050947225294228c5f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx5t-HD/index.m3u8"
        }, {
          "channelId": "1508",
          "channelName": "陕西乐家购物高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/20241105100935425e14700d6.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx6t-HD/index.m3u8"
        }, {
          "channelId": "1509",
          "channelName": "陕西体育休闲高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/102/102/20241105100958274114a58f2.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx7t-HD/index.m3u8"
        }, {
          "channelId": "1510",
          "channelName": "西部电影高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/105/105/202411051010176160b28c230.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/sx8t-HD/index.m3u8"
        }, {
          "channelId": "1511",
          "channelName": "农林卫视高清",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2024/11/5/124/124/20241105101047340918e4dba.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/nlws-HD/index.m3u8"
        }, {
          "channelId": "116",
          "channelName": "金鹰卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/124/124/202212072017014723ac246e0.jpeg",
          "channelUrl": "http://shanxiunicom.vshk.wasu.tv/jykt/index.m3u8?"
        }, {
          "channelId": "1235",
          "channelName": "卡酷少儿",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/150/150/2022120720324331063869b5d.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/kkdh/index.m3u8"
        }, {
          "channelId": "210",
          "channelName": "优漫卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/149/149/202212072020296680ed40b1c.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/ymkt/index.m3u8"
        }, {
          "channelId": "1237",
          "channelName": "炫动卡通",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/168/168/2022120720325885681b6d47.jpeg",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/xdkt/index.m3u8"
        }, {
          "channelId": "103",
          "channelName": "嘉佳卡通 ",
          "channelPic": "http://sxlt-pic.obmp.wasu.tv/pc/nlz/mams/pic/2022/12/7/115/115/2022120720160881888186c24.png",
          "channelUrl": "http://shanxiunicom-new.livestr.wasu.tv/jjkt/index.m3u8"
        }]
        '''
        # 初始化默认M3U内容（至少包含EXTM3U声明）
        a = ['#EXTM3U']

        try:

            data = json.loads(CHANNEL_DATA)
            channels = [
                element
                #for item in data.get('list', [])
                for item in data
                for element in (
                    f'#EXTINF:-1 tvg-id="{item["channelId"]}" tvg-name="{item["channelName"]}" '
                    f'tvg-logo="{item["channelPic"]}" group-title="",'
                    f'{item["channelName"]}',
                    f'http://127.0.0.1:9978/proxy?do=py&type=real_url&pid={item["channelId"]}',
                )
            ]
            a += channels  # 合并到初始化的a中

        except requests.exceptions.RequestException as e:
            print(f"网络请求失败: {e}")
            a.append('# 错误：无法获取频道列表')
        except KeyError as e:
            print(f"数据解析错误，缺少字段: {e}")
            a.append('# 错误：数据格式异常')
        except json.JSONDecodeError:
            print("响应内容不是有效的JSON")
            a.append('# 错误：无效的API响应')

        return '\n'.join(a)

    def homeContent(self, filter):
        return {}

    def homeVideoContent(self):
        return {}

    def categoryContent(self, cid, page, filter, ext):
        return {}

    def detailContent(self, did):
        return {}

    def searchContent(self, key, quick, page='1'):
        return {}

    def searchContentPage(self, keywords, quick, page):
        return {}

    def playerContent(self, flag, pid, vipFlags):
        return {}

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        if params['type'] == "ts":
            return self.get_ts(params)
        if params['type'] == "real_url":
            pid = params['pid']
            channel_url = self.get_channel_url(pid)
            real_url = self.generate_real_url(channel_url)
            m3u8_text = f'#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-STREAM-INF:BANDWIDTH=4000000,RESOLUTION=1280x720\n{real_url}\n'
            return m3u8_text
        return [302, "text/plain", None, {'Location': 'https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4'}]
    def proxyM3u8(self, params):
        pid = params['pid']
        info = pid.split(',')
        a = info[0]
        b = info[1]
        c = info[2]
        timestamp = int(time.time() / 4 - 355017625)
        t = timestamp * 4
        m3u8_text = f'#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:4\n#EXT-X-MEDIA-SEQUENCE:{timestamp}\n'
        for i in range(10):
            url = f'https://ntd-tgc.cdn.hinet.net/live/pool/{a}/litv-pc/{a}-avc1_6000000={b}-mp4a_134000_zho={c}-begin={t}0000000-dur=40000000-seq={timestamp}.ts'
            if self.is_proxy:
                url = f'http://127.0.0.1:9978/proxy?do=py&type=ts&url={self.b64encode(url)}'

            m3u8_text += f'#EXTINF:4,\n{url}\n'
            timestamp += 1
            t += 4
        return [200, "application/vnd.apple.mpegurl", m3u8_text]

    def get_ts(self, params):
        url = self.b64decode(params['url'])
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, stream=True, proxies=self.proxy)
        return [206, "application/octet-stream", response.content]

    def destroy(self):
        return '正在Destroy'

    def b64encode(self, data):
        return base64.b64encode(data.encode('utf-8')).decode('utf-8')

    def b64decode(self, data):
        return base64.b64decode(data.encode('utf-8')).decode('utf-8')

if __name__ == '__main__':
    pass
