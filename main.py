

from cmath import log
from email import message
from lib2to3.pgen2 import token
from logging import exception
from bs4 import BeautifulSoup
import requests
import jwt
import base64
import time
import datetime
import random
from binance.client import Client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import os
from aiogram import Bot, Dispatcher, executor, types, asyncio
from binance_api import Binance
from selenium.webdriver.common.keys import Keys
link_login = 'https://msk.trendagent.ru/login'


options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
driver.get(url= link_login)
time.sleep(3)
number_input = driver.find_element_by_class_name('text-field__element')
number_input.clear()
number_input.send_keys('79690838446')
time.sleep(2)
password_input = driver.find_element_by_name('password')
password_input.clear()
password_input.send_keys('x4KYWwv')
time.sleep(2)
password_input.send_keys(Keys.ENTER)
time.sleep(20)
with open('index.html','w') as file:
    file.write(driver.page_source)

with open('index.html') as file:
    src = file.read()
    soup = BeautifulSoup(src,"lxml")
    links = soup.find_all('div','files-item')

for i in links:
    i = i.text
    print(i)
# print(soup.find_all('files-item__btn-content'))
# driver.close()
# driver.quit()
# print(soup.find(''))




# def jwts():
#     private_key = 'LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcEFJQkFBS0NBUUVBcld3YTdkRjVWMEVOdWxiZjJ5Y0pZSEdYOVAxa1hTaUxDallEckEzeHNVVmltelptCkFrOXRHVGM3Sk9aMDYzTHJkTkxZLzZWbjJ3bEs3VysySE16ZmxPei9ZYjI3TDFxTjlNNXFsMGxMd0gwbFlwbnIKaVVQUGxsSGFlNUNyeS8zeC9sSk9PSlliVnVLY0JzRFg2UmhqNERQV29GZUkyNk1SdFlramZKckdVRnpGRHZmeQp0SDhaVjNabUpHVlZGa1pzeHJpUkFmYy9peUpKUDQrT2cxSHVWRjF2aUVnSWVBNWtvbE9QWGdiNUpObXpOMjhsCjdlOENVSWpUV3R1QmNtQTlRYVRsWFJvQ3Noc3hDOUN0bEcwY2svd2N4anIrZmZ4ZHIzRnFQSTNNWGdqcGRDRGwKZmlZZWQrTmlNR2xKbXp5MFBFY2NYanBjU01tWDlmeW9iQ3kySHdJREFRQUJBb0lCQUROYllGNHRPcEhzWWZSYwo1YzR3c1VZdVhhSGZxR2t1S0g3Tm9DakR1RitXL0t5YVgzc3ZxazlkVzlhQnFQNVErZ21PcDFTTjEwTzJiTW9ECjJ4cU1VV241QldnY2wrSmVIc3Z3bFFCWVpHYU1xUldhSDNaMjduTEZxcjROQ2ROUFVPclAxUHBNK2F1eFVDTnYKMklEZkNEVE5KVEkydWdEUk9kMVl6M21ISEZPUHFMeVh2VUtWNFNkYVdmVldnNXRGd1ExSGQzbmRRQVZkUm5XQQo3dnoxVWpUZDZPRnQyZDV6T1ZqYUU4VnJTMkNTT2wxOTBwRVlNdlpFeDNtZ2UvYlJSMHdZT1pmY1VrK05Ob3VBCkpGMyt2ZjJkK012ZDc3UjIrUThBdDZza2lRaVdTN3RzUHREeDQ4RU9tU0taNTVoTHhENm5BUGxQQ1BxTWdzSXgKdHhLYkhnRUNnWUVBMWI0TldndzFsdGs1Rk84b3cvS25lRmp4QTVLRVFGa1hQaGZsR0dyY0c3MTI3RHpoMm9iZgp5SWZOUmcwNUFuMjVuMFkxOGx6R1B1OVk2M1QyWnpwZXc1cDRLNStpZjYvUTZUUGh5dmxYNXFwNjUxN29zcnozClRwZzNTY0UreHRhbmNrR201SHA1bVk1dENSY1Bua3BmVFlYS1l2SUgrNi9zQU92bllyQmFNTzhDZ1lFQXo3VmUKVk1aczZwTm5URnVrRXJMTVlOM3hzdnZ4dEtsU0FxMHBQY1lZVnY0WjA3WlBxTkg4UnhwNnVTMWNhT0pBQTBYMAowa25rOXE4c0l3TWdIekFGdUpSbDJDRTJ6QlhzZnMvVFBXRnREeUNrS0daamN2b2dHd3FsZGppcSs2WEh4RFRuClp2eXpOZkVIYWZlSzYzSDBjM01EekoreEw3Z0hNNmRCREVXYmJkRUNnWUExOHppdmgvRm0yQUYrZFRkVzdrS3oKTDgvMTFOK28xbFAxaWxaN0tVM1JlcXN2eWRaQU1GYi82TGM1ZlZEc2ZndUNWbGg3aWt0SHkyWW9XR2R4ZXR3OApoeHJaOS9zdU81U0JxR1RQdE13cEh0TFMzN1BnbWEzYW1yVXAycXNieVVhT29sK2J3QVk5YWlPL2JhQzFsWlFrCm55YU1md2JnMG5EQmNzbitzUUN5NVFLQmdRQzAvQk03Q1Q4RVV2WnlhWE9ZdTJVc2pwZTVYcURveTVUak1pRTYKYTI3djlpOW84M1dMNDVUUUcvbU5lMElIUGdXTEZKelQwNEdIbFhGKy9JMHp2N05zZHhvYTdpNENQS1E2aHpwSQpSS2t6d2p4bjIzZVNTdkpJdmNrWkx4MkZjcG1UbEltQmluVlpiakVJbTZMWHJ3N1N2Z2cwZDMxNzEvMm1lM2xKCmlTbDYwUUtCZ1FDZ3I5Y1dBdWx0TXJDbEVJQ25YeVUrL0x0enZ6VlE5czJGb3B3VzJrU1k2SEdaTHRaOFBaQ2QKOGtpUWZLaUlnY2lzRzQ4K0M3dzBlVi9sRHEzbWkvcmszdTRTZG81aVFFenF3WTdyOUpra1FjdHpKYTFmVkVlawpDWExNRmlzMnBhVU95Z3pFdTFLM0JKSURJYjF1LzZlYU1wdVoycVAxMDVQdi9pRFZ3Z2NMSlE9PQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQo='
#     uid = '09c4f8a7-e075-46e4-9a5a-9a6cc42ed2e3'

#     host = 'garantex.io'

#     key = base64.b64decode(private_key)
#     iat = int(time.mktime(datetime.datetime.now().timetuple()))

#     claims = {
#         "exp": iat + 1*60*60,  # JWT Request TTL in seconds since epoch
#         "jti": hex(random.getrandbits(12)).upper()
#     }

#     jwt_token = jwt.encode(claims, key, algorithm="RS256")
#     ret = requests.post('https://dauth.' + host + '/api/v1/sessions/generate_jwt',  json={'kid': uid, 'jwt_token': jwt_token})
#     token = ret.json().get('token')
#     return token

# host = 'garantex.io'
# ret = requests.get('https://' + host + '/api/v2/depth?market=usdtrub', headers={'Authorization': 'Bearer ' + jwts()})


# api_key = 'EL1JVTvDCDbMHERkYIp1tHp7sACSrEgHRhy69ZmHaR9ra63pXlCnjjavx6MDnoFl'
# api_secret = 'gEqQy3tBAwA4fuiqeFX6PTilKYNoqbn9zgZHQyzrxawsSyvOVMm7WsmdmlzGmI87'
# client = Binance(api_key, api_secret)
# client.depth(symbol='USDTRUB')


# link_bestc_sell = 'https://bestcoin.cc/?refer_id=22&cur_from=USDTTRC20&cur_to=TCSBRUB&lng=ru'
# link_alfa_buy = 'https://alfabit.exchange/ru/exchange/TCSBRUB/USDTBEP20'

# p2p_link_b_raif = 'https://p2p.binance.com/ru/trade/RaiffeisenBankRussia/USDT?fiat=RUB'
# p2p_link_s_raif = 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=RaiffeisenBankRussia'
# p2p_link_b_qiwi = 'https://p2p.binance.com/ru/trade/QIWI/USDT?fiat=RUB'
# p2p_link_s_qiwi = 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=QIWI'

# def bestcoin():
#     options = Options()
#     #options.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
#     driver.get(url= link_bestc_sell)
#     time.sleep(3)
#     soup = BeautifulSoup(driver.page_source,"lxml")
#     driver.close()
#     driver.quit()
#     return soup.find('aside').text

# def alfa_b():
#     options = Options()
#     #options.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
#     driver.get(url= link_alfa_buy)
#     time.sleep(5)
#     soup = BeautifulSoup(driver.page_source,"lxml")
#     driver.close()
#     driver.quit()
#     return soup.find('div','text-center').text

# print(alfa_b()[20:25])

# p2p_link_b = 'https://p2p.binance.com/ru/trade/RosBank/USDT?fiat=RUB'
# p2p_link_b_t='https://p2p.binance.com/ru/trade/Tinkoff/USDT?fiat=RUB'
# p2p_link_s_tink = 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=Tinkoff'
# p2p_link_s_rosb = 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payent=RosBank&payment=RosBank'

# def p2p_b():
#     options = Options()
#     #options.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
#     driver.get(url= p2p_link_b)
#     time.sleep(5)
#     driver.find_element_by_id('onetrust-accept-btn-handler').click()
#     time.sleep(3)
#     driver.find_element_by_class_name('css-1pcqseb').click()
#     time.sleep(2)
#     soup = BeautifulSoup(driver.page_source,"lxml")
#     driver.close()
#     driver.quit()
#     # print(soup.find("div", 'css-1rhb69f').text, ' ',soup.find("div", 'css-1a0u4z7').text, ' ',soup.find("div", 'css-19crpgd').text, '\n',"Цена ",soup.find("div", 'css-1kj0ifu').text, '\n',soup.find("div", 'css-3v2ep2').text," ",soup.find("div", 'css-16w8hmr').text )
#     return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 
    
# def p2p_b_t():
#     options = Options()
#     #options.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
#     driver.get(url= p2p_link_b_t)
#     time.sleep(5)
#     driver.find_element_by_id('onetrust-accept-btn-handler').click()
#     time.sleep(3)
#     driver.find_element_by_class_name('css-1pcqseb').click()
#     time.sleep(2)
#     soup = BeautifulSoup(driver.page_source,"lxml")
#     driver.close()
#     driver.quit()
#     # print(soup.find("div", 'css-1rhb69f').text, ' ',soup.find("div", 'css-1a0u4z7').text, ' ',soup.find("div", 'css-19crpgd').text, '\n',"Цена ",soup.find("div", 'css-1kj0ifu').text, '\n',soup.find("div", 'css-3v2ep2').text," ",soup.find("div", 'css-16w8hmr').text )
#     return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

# def p2p_s_rosb():
#     options = Options()
#     #options.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
#     driver.get(url= p2p_link_s_rosb)
#     time.sleep(5)
#     driver.find_element_by_id('onetrust-accept-btn-handler').click()
#     time.sleep(3)
#     driver.find_element_by_class_name('css-1pcqseb').click()
#     time.sleep(2)
#     soup = BeautifulSoup(driver.page_source,"lxml")
#     driver.close()
#     driver.quit()
#     # print(soup.find("div", 'css-1rhb69f').text, ' ',soup.find("div", 'css-1a0u4z7').text, ' ',soup.find("div", 'css-19crpgd').text, '\n',"Цена ",soup.find("div", 'css-1kj0ifu').text, '\n',soup.find("div", 'css-3v2ep2').text," ",soup.find("div", 'css-16w8hmr').text )
#     return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

# def p2p_s_tink():
#     options = Options()
#     #options.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
#     driver.get(url= p2p_link_s_tink)
#     time.sleep(5)
#     driver.find_element_by_id('onetrust-accept-btn-handler').click()
#     time.sleep(3)
#     driver.find_element_by_class_name('css-1pcqseb').click()
#     time.sleep(2)
#     soup = BeautifulSoup(driver.page_source,"lxml")
#     driver.close()
#     driver.quit()
#     # print(soup.find("div", 'css-1rhb69f').text, ' ',soup.find("div", 'css-1a0u4z7').text, ' ',soup.find("div", 'css-19crpgd').text, '\n',"Цена ",soup.find("div", 'css-1kj0ifu').text, '\n',soup.find("div", 'css-3v2ep2').text," ",soup.find("div", 'css-16w8hmr').text )
#     return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

# def p2p_b_raif():
#     options = Options()
#     #options.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
#     driver.get(url= p2p_link_b_raif)
#     time.sleep(5)
#     driver.find_element_by_id('onetrust-accept-btn-handler').click()
#     time.sleep(3)
#     driver.find_element_by_class_name('css-1pcqseb').click()
#     time.sleep(2)
#     soup = BeautifulSoup(driver.page_source,"lxml")
#     driver.close()
#     driver.quit()
#     return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

# def p2p_s_raif():
#     options = Options()
#     #options.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
#     driver.get(url= p2p_link_s_raif)
#     time.sleep(5)
#     driver.find_element_by_id('onetrust-accept-btn-handler').click()
#     time.sleep(3)
#     driver.find_element_by_class_name('css-1pcqseb').click()
#     time.sleep(2)
#     soup = BeautifulSoup(driver.page_source,"lxml")
#     driver.close()
#     driver.quit()
#     return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

# def p2p_b_qiwi():
#     options = Options()
#     #options.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
#     driver.get(url= p2p_link_b_qiwi)
#     time.sleep(5)
#     driver.find_element_by_id('onetrust-accept-btn-handler').click()
#     time.sleep(3)
#     driver.find_element_by_class_name('css-1pcqseb').click()
#     time.sleep(2)
#     soup = BeautifulSoup(driver.page_source,"lxml")
#     driver.close()
#     driver.quit()
#     return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

# def p2p_s_qiwi():
#     options = Options()
#     #options.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path='/Users/svrnsergey/Desktop/python — копия/chromedriver', options=options)
#     driver.get(url= p2p_link_s_qiwi)
#     time.sleep(5)
#     driver.find_element_by_id('onetrust-accept-btn-handler').click()
#     time.sleep(3)
#     driver.find_element_by_class_name('css-1pcqseb').click()
#     time.sleep(2)
#     soup = BeautifulSoup(driver.page_source,"lxml")
#     driver.close()
#     driver.quit()
#     return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 








# def main():
#     p2p_buy = p2p_b()
#     p2p_buy_t = p2p_b_t()
#     p2p_sell_t = p2p_s_tink()
#     p2p_sell_r = p2p_s_rosb()
#     bestcoin_sell = bestcoin()
#     garantex_buy = ret.json().pop("bids")[0].pop("price")
#     garantex_sell = ret.json().pop("asks")[0].pop("price")
#     bnb = client.depth(symbol='USDTRUB').pop("bids")[0][0][:5]
#     bns = client.depth(symbol='USDTRUB').pop("asks")[0][0][:5]
#     alfa_br = alfa_b()[14:23]
#     p2p_buy_raif = p2p_b_raif()
#     p2p_sell_raif = p2p_s_raif()
#     p2p_buy_qiwi = p2p_b_qiwi()
#     p2p_sell_qiwi = p2p_s_qiwi()
#     return p2p_buy, p2p_buy_t, p2p_sell_t, p2p_sell_r, bestcoin_sell, garantex_buy, garantex_sell, bnb, bns, alfa_br, p2p_buy_raif, p2p_sell_raif, p2p_buy_qiwi, p2p_sell_qiwi




# TOKEN = "5369544605:AAFe1ZMEdGQgBJm__rQ4N5exYln2QoL_Hz8"
# bot = Bot(token = TOKEN)
# dp = Dispatcher(bot)

# s= [] 

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.reply("What's up Doc?\n Let's do everything right now!")
#     chat_id = (message.chat.id)
#     s.append(chat_id)



# spread = 1.007
# spread_with_garantex = 1.01

# async def svyazki():
#     while True:
        
#             temp = main()
#             p2p_buyer = float(temp[0][0][:5])
#             p2p_buyer_t = float(temp[1][0][:5])
#             p2p_seller_t = float(temp[2][0][:5])
#             p2p_seller_r = float(temp[3][0][:5])
#             bestcoin_seller = float(temp[4][-10:-5])
#             garantex_buyer = float(temp[5])*1.002
#             garantex_seller = float(temp[6])*0.998
#             binance_buyer = float(temp[7])*1.15
#             binance_seller = float(temp[8])
#             alfa_buyer = float(temp[9]) 
#             p2p_buyer_raif = float(temp[10][0][:5])
#             p2p_seller_raif = float(temp[11][0][:5])
#             p2p_buyer_qiwi = float(temp[12][0][:5])
#             p2p_seller_qiwi = float(temp[13][0][:5])
            
#             if bestcoin_seller/garantex_buyer>=spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,'*Buy Garantex -> Sell Bestcoin*✅' +f'\nGarantex_price = {garantex_buyer} ₽\nBestcoin_price = {bestcoin_seller} ₽\n*SPREAD* = {round(bestcoin_seller/garantex_buyer,3)} 🔥', parse_mode="Markdown")
                
#             if p2p_seller_r/garantex_buyer>=spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy Garantex -> Sell p2p Росбанк</b>✅\nGarantex_price = {garantex_buyer} ₽\nP2P_Rosbank_price = {p2p_seller_r} ₽\n<b>SPREAD</b> = {round(p2p_seller_r/garantex_buyer,3)} 🔥 ', parse_mode="HTML")
                
#             if p2p_seller_t/garantex_buyer>=spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy Garantex -> Sell p2p Тинькофф</b>✅' + f'\nGarantex_price = {garantex_buyer} ₽\nP2P_Tinkoff_price = {p2p_seller_t} ₽\n<b>SPREAD</b> = {round(p2p_seller_t/garantex_buyer,3)} 🔥', parse_mode="HTML")
            
#             if garantex_seller/p2p_buyer>=spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy p2p Росбанк -> Sell Garantex</b>✅ \nP2P_Rosbank_price = {p2p_buyer} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/p2p_buyer,3)} 🔥',parse_mode="HTML" )

#             if garantex_seller/p2p_buyer_t>=spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy p2p Тинькофф -> Sell Garantex</b>✅ \nP2P_Tinkoff_price = {p2p_buyer_t} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/p2p_buyer_t,3)} 🔥',parse_mode="HTML" )   
        
#             if bestcoin_seller/p2p_buyer>=spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy p2p Росбанк -> Sell Bestcoin</b>✅ \nP2P_Rosbank_price = {p2p_buyer} ₽\nBestcoin_price = {bestcoin_seller} ₽\n<b>SPREAD</b> = {round(bestcoin_seller/p2p_buyer,3)} 🔥',parse_mode="HTML" )
            
#             if bestcoin_seller/p2p_buyer_t>=spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy p2p Тинькофф -> Sell Bestcoin</b>✅ \nP2P_Tinkoff_price = {p2p_buyer_t} ₽\nBestcoin_price = {bestcoin_seller} ₽\n<b>SPREAD</b> = {round(bestcoin_seller/p2p_buyer_t,3)} 🔥',parse_mode="HTML" )
        
#             if garantex_seller/binance_buyer >= spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell Garantex</b>✅ \nBinance_price (с учетом покупки рублей на p2p) = {binance_buyer} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/binance_buyer,3)} 🔥',parse_mode="HTML" )
        
#             if garantex_seller/alfa_buyer >= spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy AlfaBit -> Sell Garantex</b>✅ \nAlfaBit_price = {alfa_buyer} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/alfa_buyer,3)} 🔥',parse_mode="HTML" )
        
#             if p2p_seller_r/alfa_buyer >= spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy AlfaBit -> Sell p2p Росбанк</b>✅ \nAlfaBit_price = {alfa_buyer} ₽\nP2P_Rosbank_price = {p2p_seller_r} ₽\n<b>SPREAD</b> = {round(p2p_seller_r/alfa_buyer,3)} 🔥',parse_mode="HTML" )
                
#             if bestcoin_seller/binance_buyer>= spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell Bestcoin</b>✅ \nBinance_price = {binance_buyer} ₽\nBestcoin_price = {bestcoin_seller} ₽\n<b>SPREAD</b> = {round(bestcoin_seller/binance_buyer,3)} 🔥',parse_mode="HTML")

#             if p2p_seller_r/binance_buyer>= spread:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell P2P Росбанк</b>✅ \nBinance_price = {binance_buyer} ₽\nP2P_Rosbank_price = {p2p_buyer} ₽\n<b>SPREAD</b> = {round(p2p_seller_r/binance_buyer,3)} 🔥',parse_mode="HTML")

#             if p2p_seller_t/binance_buyer>= spread and p2p_seller_t != 74.81:
#                     for i in range(1):
#                         await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell P2P Тинькофф</b>✅ \nBinance_price = {binance_buyer} ₽\nP2P_Tinkoff_price = {p2p_buyer_t} ₽\n<b>SPREAD</b> = {round(p2p_seller_t/binance_buyer,3)} 🔥',parse_mode="HTML")
        
#             if p2p_seller_raif/binance_buyer >= spread and p2p_seller_raif != 74.81:
#                     for i in range(1):
#                         await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell P2P Raif</b>✅ \nBinance_price (с учетом покупки рублей на p2p) = {binance_buyer} ₽\nP2P_Raif_price = {p2p_seller_raif} ₽\n<b>SPREAD</b> = {round(p2p_seller_raif/binance_buyer,3)} 🔥',parse_mode="HTML")

#             if p2p_seller_qiwi/binance_buyer>= spread and p2p_seller_qiwi != 74.81:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell P2P Qiwi</b>✅ \nBinance_price (с учетом покупки рублей на p2p) = {binance_buyer} ₽\nP2P_Qiwi_price = {p2p_seller_qiwi} ₽\n<b>SPREAD</b> = {round(p2p_seller_qiwi/binance_buyer,3)} 🔥',parse_mode="HTML")

#             if p2p_seller_raif/alfa_buyer >= spread and p2p_seller_raif != 74.81:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy AlfaBit -> Sell p2p Raif</b>✅ \nAlfaBit_price = {alfa_buyer} ₽\nP2P_Raif_price = {p2p_seller_raif} ₽\n<b>SPREAD</b> = {round(p2p_seller_raif/alfa_buyer,3)} 🔥',parse_mode="HTML" )

#             if p2p_seller_qiwi/alfa_buyer >= spread and p2p_seller_qiwi != 74.81:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy AlfaBit -> Sell p2p Qiwi</b>✅ \nAlfaBit_price = {alfa_buyer} ₽\nP2P_Qiwi_price = {p2p_seller_qiwi} ₽\n<b>SPREAD</b> = {round(p2p_seller_qiwi/alfa_buyer,3)} 🔥',parse_mode="HTML" )

#             if bestcoin_seller/p2p_buyer_raif>=spread and p2p_buyer_raif != 74.81:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy p2p Raif -> Sell Bestcoin</b>✅ \nP2P_Raif_price = {p2p_buyer_raif} ₽\nBestcoin_price = {bestcoin_seller} ₽\n<b>SPREAD</b> = {round(bestcoin_seller/p2p_buyer_raif,3)} 🔥',parse_mode="HTML" )

#             if bestcoin_seller/p2p_buyer_qiwi>=spread and p2p_buyer_qiwi != 74.81:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy p2p Qiwi -> Sell Bestcoin</b>✅ \nP2P_Qiwi_price = {p2p_buyer_qiw} ₽\nBestcoin_price = {bestcoin_seller} ₽\n<b>SPREAD</b> = {round(bestcoin_seller/p2p_buyer_qiwi,3)} 🔥',parse_mode="HTML" )

#             if garantex_seller/p2p_buyer_raif>=spread_with_garantex and p2p_buyer_raif != 74.81:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy p2p raif -> Sell Garantex</b>✅ \nP2P_Raif_price = {p2p_buyer_raif} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/p2p_buyer_raif,3)} 🔥',parse_mode="HTML" )   

#             if garantex_seller/p2p_buyer_qiwi>=spread_with_garantex and p2p_buyer_qiwi != 74.81:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy p2p Qiwi -> Sell Garantex</b>✅ \nP2P_Qiwi_price = {p2p_buyer_qiwi} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/p2p_buyer_qiwi,3)} 🔥',parse_mode="HTML" )   

#             if p2p_seller_raif/garantex_buyer>=spread_with_garantex and p2p_seller_raif != 74.81:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy Garantex -> Sell p2p Raif</b>✅\nGarantex_price = {garantex_buyer} ₽\nP2P_Raif_price = {p2p_seller_raif} ₽\n<b>SPREAD</b> = {round(p2p_seller_raif/garantex_buyer,3)} 🔥 ', parse_mode="HTML")

#             if p2p_seller_qiwi/garantex_buyer>=spread_with_garantex and p2p_seller_qiwi != 74.81:
#                 for i in range(1):
#                     await bot.send_message(-1001762743594,f'<b>Buy Garantex -> Sell p2p Qiwi</b>✅\nGarantex_price = {garantex_buyer} ₽\nP2P_Qiwi_price = {p2p_seller_qiwi} ₽\n<b>SPREAD</b> = {round(p2p_seller_qiwi/garantex_buyer,3)} 🔥 ', parse_mode="HTML")

        
#             await asyncio.sleep(5)


# if __name__ == "__main__":
#     asyncio.run(svyazki())
#     executor.start_polling(dp, skip_updates=True)



