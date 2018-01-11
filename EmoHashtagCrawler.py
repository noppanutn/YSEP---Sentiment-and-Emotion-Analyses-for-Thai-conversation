# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:06:39 2018

@author: nop
"""
import csv
from TwitterSearch import *
try:
    searchObject = {}
    keywords = ['#ทึ่ง','#อึ้ง','#ว้าว']
#    keywords = ['#คาดคะเน','#หวังว่า','#ปรารถนา','#ปรารถนาว่า','#ระแวดระวัง','#ระวัง','#รอบคอบ','#ความรอบคอบ','#ไม่ประมาท',]
#    keywords = ['#รำคาน','#ลำคาน','#ลำคาญ','#กัว',]
#    keywords = ['#สนใจ','#ความสนใจ',
#                '#ดึงดูด','#น่าดึงดูด','#ดึงดูดใจ','#น่าดึงดูดใจ','#อยากรู้','#เดา','#เดามั่ว','#เดาสุ่ม','#รอ',]
#    keywords = ['#ความปิติยินดี','#ความปิติ','#ความยินดี','#ปิติ','#ยินดี','#ความรื่นเริง','#รื่นเริง','#ความดีอกดีใจ','#ความดีใจ',
#                '#ดีใจ','#ความสุขสบาย','#ความสุข','#ความสบาย','#สุข','#สบาย','#ความสนุกสนาน','#ความสนุก','#สนุก',
#                '#ปลาบปลื้ม','#ปลื้ม',]
#                
#    keywords = ['#ความเศร้าใจ','#เศร้าใจ','#ความเสียใจ','#เสียใจ','#เสียใจด้วย','#ความเศร้าโศก','#ความโศกเศร้า','#โศกเศร้า',
#                '#เศร้าโศก','#ความตรอมใจ','#ตรอมใจ','#ความรวดร้าว','#รวดร้าว','#ความรันทด','#รันทด','#ความสลด','#สลด',
#                '#ความหกหู่','#หดหู่',]
#                
#    keywords = ['#วางใจ','#ไว้เนื้อเชื่อใจ','#เชื่อใจ','#ไว้ใจได้','#ความมั่นใจ','#มั่นใจ','#ความเชื่อถือไว้วางใจ','#ความเชื่อถือ',
#                '#ความไว้วางใจ','#ไว้วางใจ','#ยอมรับ','#ยอมใจ','#น่าชื่นชม','#ชื่นชม','#น่ายกย่อง','#น่านับถือ','#นับถือ',
#                '#เคารพ','#น่าเชื่อถือ','#เชื่อถือ','#เชื่อมั่น','#ความหวัง','#หวัง','#ไว้ใจ','#ให้ใจ','#มั่นใจ','#แลกใจ','#ยอมรับ',
#                '#ยอม',]
#                
#    keywords = ['#ทำให้รังเกียจ','#รังเกียจ','#ทำให้สะอิดสะเอียน','#สะอิดสะเอียน','#น่าเกลียด','#เกลียด','#เดียด','#ความรังเกียจ',
#                '#ความสะอิดสะเอียน',]
#                
#    keywords = ['#กลัว','#เกรง','#เกรงขาม','#หวั่นหวาด','#หวั่นกลัว','#หวั่นเกรง','#หวั่นวิตก','#วิตกกังวล','#วิตก','#กังวล',
#                '#หวาดกลัว','#วิตกจริต','#ความกลัว','#ความวิตกกังวล','#ความหวาดกลัว','#กัว','#สยอง','#ไม่กล้า','#สับสน',
#                '#น่าสงสัย','#สงสัย','#เกรงกลัว','#คิดมาก','#ระแวง','#หวาดระแวง','#ความระแวง','#ไม่แน่ใจ','#เคลือบแคลงใจ',
#                '#รู้สึกกลัว',]
#                
#    keywords = ['#โทสะ','#วิโรธ','#ความโกรธ','#โกรธ','#ความฉุนเฉียว','#ฉุนเฉียว','#ความขัดเคือง','#เคือง','#ขัดแค้น','#แค้น',
#                '#ขึ้งเคียด','#ขึ้งโกรธ','#ดาลเดือด','#เดือด','#ทำให้โกรธ','#ทำให้ฉุนเฉียว','#ทำให้เกิดโทสะ','#ยั่วโมโห','#โมโห',
#                '#หลงใหล','#ความหลงใหล','#ไม่พอใจ','#ความไม่พอใจ','#โกด','#ความรำคาญ','#รำคาญ','#รบกวน',
#                '#น่ารำคาญ','#หงุดหงิด','#อารมณ์เสีย','#เสียอารมณ์','#อารมณ์ไม่ดี','#อารมณ์บูด']
#                
#    keywords = ['#อัศจรรย์','#ตะลึง','#ทำให้ประหลาดใจ','#ประหลาดใจ','#แปลกใจ','#รู้สึกประหลาดใจ','#ความแปลกใจ','#ว้าวุ่น',
#                '#ว้าวุ่นใจ','#วุ่นใจ','#วอกแวก','#รบกวน','#น่าทึ่ง','#ทึ่ง','#น่าตะลึง','#ตกตะลึง','#ข้องใจ','#งง','#งงงวย',
#                '#ไม่เข้าใจ','#ไม่เก็ต',]
#                
#    keywords = ['#ตั้งตาคอย','#คอย','#คาดหมาย','#ความคาดหมาย','#มุ่งหวัง','#หวัง','#คาดคิด','#คาดหวัง','#ความคาดหวัง',
#                '#คาดเดา','#ความคาดเดา','#ตั้งตารอ','#ประมาณการณ์','#มาดหมาย','#เป็นที่คาดหวัง','#สนใจ','#ความสนใจ',
#                '#ดึงดูด','#น่าดึงดูด','#ดึงดูดใจ','#น่าดึงดูดใจ','#อยากรู้','#เดา','#เดามั่ว','#เดาสุ่ม','#รอ',]
    for i in range(len(keywords)):
        print(keywords[i])
        tsoo = TwitterSearchOrder()
        tsoo.set_keywords([keywords[i]])
#        tsoo.set_language('th')
        tsoo.set_include_entities(False)
        searchObject[keywords[i]] = tsoo
    #print(searchObject)
    
#    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
#    tso.set_keywords(['#โกรธ']) # let's define all words we would like to have a look for
#    tso.set_language('th') # we want to see German tweets only
#    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'fYAPx1MbDj9ks8EASP0BxImaC',
        consumer_secret = 'rtWToH82d2rpnKfChef064CzBTDzC01LpgmjheV8FWWgfLlptI',
        access_token = '2527864249-GKLOuOg026HcQm6ffjfy5XXv27UKuUEVhn4HyXU',
        access_token_secret = 'LcoXOTLQ2El5BcjcYVoIkpwSiUlqB6TVIA2lZrI8THpXx'
     )
    
     # this is where the fun actually starts :)
    j = 1
#    myData = [['Tweet','Emotion']]
    myData = []
    for i in range(len(keywords)):
#        print(searchObject[keywords[i]])
        tso = searchObject[keywords[i]]
        for tweet in ts.search_tweets_iterable(tso):    
    #        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            if(tweet['text'][0] is not 'R' and tweet['truncated'] == False):
                print(j,tweet['text'])
                print('--------------------')
                j = j+1
                myData.append([tweet['text'].replace('\n',' '),keywords[i]])
    
    myFile = open('try.csv', 'w', encoding='utf8')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)
     
    print("Writing complete")

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)