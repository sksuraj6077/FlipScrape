#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request



def Flipkart_Data_Scraping(page_no):
    page_num = str(page_no)
    mydict = {"mobilename":[],'rating':[],'price':[],'details':[]}
    
    final_data = pd.DataFrame()
    all_link = [
        "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlJlYWxtZSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_Realme_mobile-phones-store_Q1PDG4YW86MF_wp3&fm=neo%2Fmerchandising&iid=M_e5d92eae-4868-449c-82db-0e5695f98d9d_5.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=apvwjhjqww0000001692796013110&page={}".format(page_num),
        "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DPOCO&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_6d4a2f3d-ccc6-437f-8808-a65f84c117b1_5.O1WYX08RHODP&ppt=clp&ppn=mobile-phones-store&ssid=a6p32j7fts0000001691832642564&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlBPQ08iXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&otracker=clp_metro_expandable_2_5.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp3&fm=neo%2Fmerchandising&iid=M_b9e3a456-6fcb-4e9b-b2b5-c37b413eaff4_5.O1WYX08RHODP&ppt=browse&ppn=browse&ssid=gxlbamfptc0000001692796083581&page={}".format(page_num),
        "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DAPPLE&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_f7915cda-a0a8-404b-95b3-a34cb988bdbf_5.92RED14GXPXF&ppt=browse&ppn=browse&ssid=mq3li68ipc0000001691833314257&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbImlQaG9uZSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&otracker=clp_metro_expandable_6_5.metroExpandable.METRO_EXPANDABLE_iPhone_mobile-phones-store_92RED14GXPXF_wp3&fm=neo%2Fmerchandising&iid=M_62bf87c8-89d8-4635-b402-83b67a39cfcb_5.92RED14GXPXF&ppt=browse&ppn=browse&ssid=h7pgemre800000001692796439638&page={}".format(page_num),
        "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_0e4af7c1-3171-4c02-b8ab-7e22c885ef69_5.TY6OUL5ASJ9P&ppt=browse&ppn=browse&ssid=gtrep4frxc0000001691833161754&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNBTVNVTkciXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&otracker=clp_metro_expandable_4_5.metroExpandable.METRO_EXPANDABLE_SAMSUNG_mobile-phones-store_TY6OUL5ASJ9P_wp3&fm=neo%2Fmerchandising&iid=M_6bc4b063-70a9-4a6e-ade2-30f59ab1ec4f_5.TY6OUL5ASJ9P&ppt=browse&ppn=browse&ssid=vfry3e35io0000001692796325998&page={}".format(page_num),
        "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Dvivo&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlZJVk8iXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&fm=neo%2Fmerchandising&iid=M_ff06eb92-ad05-4d09-a381-5cba295ff50a_5.3Z3SLACO8AXE&ppt=browse&ppn=browse&ssid=6oox7isl400000001691833159604&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlZJVk8iXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&otracker=clp_metro_expandable_3_5.metroExpandable.METRO_EXPANDABLE_VIVO_mobile-phones-store_3Z3SLACO8AXE_wp3&fm=neo%2Fmerchandising&iid=M_0f0b09d1-8b42-44ba-ade0-acfaa95c44eb_5.3Z3SLACO8AXE&ppt=browse&ppn=browse&ssid=slhop2h8800000001692796252560&page={}".format(page_num),
        "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIm1vdG9yb2xhIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_7_5.metroExpandable.METRO_EXPANDABLE_motorola_mobile-phones-store_G1WUJ6Y1ZZV9_wp3&fm=neo%2Fmerchandising&iid=M_3b409924-6c43-401c-bc63-fedaf4a51f42_5.G1WUJ6Y1ZZV9&ppt=browse&ppn=browse&ssid=3asizx0s5s0000001692796534432&page={}".format(page_num)
    ]
    for link in all_link:
        
        webpage = requests.get(link)
        if webpage == None:
            continue
        soup = BeautifulSoup(webpage.text, "html.parser")

        url_1 = [] 
        link = soup.find_all("div",attrs={'class':'_1AtVbE col-12-12'})
        for x in link:
            for l1 in x.find_all('a',attrs={'class':'_1fQZEK'},href=True):
                url_1.append("https://www.flipkart.com"+l1["href"])  

        for z in url_1:
            webpage1 = requests.get(z)
            soup1 = BeautifulSoup(webpage1.text,"html.parser")
            mobile_name = soup1.find_all("span",attrs={'class':'B_NuCI'})
            m = mobile_name[0].text.strip()
            mydict['mobilename'].append(m)


            rating = soup1.find_all("div",attrs={'class':'_3LWZlK'})
            r = rating[0].text.strip()
            mydict['rating'].append(r)

            price = soup1.find_all("div",attrs={'class':'_30jeq3 _16Jk6d'})
            p = price[0].text.strip()
            mydict['price'].append(p)

            details = soup1.find_all("li",attrs={'class':'_21Ahn-'})
            d = details[0].text.strip()
            mydict['details'].append(d)

        data = pd.DataFrame(mydict)
        
        final_data = pd.concat([final_data,data],ignore_index=True)
    mydict.clear()
    return final_data




def run(start,end):
    final = pd.DataFrame()
    #start = int(input('Enter Starting Page No : '))
    #end = int(input("Enter Ending Page No : "))
    for i in range(start,end+1):
        d = Flipkart_Data_Scraping(i)
        final = pd.concat([final,d],ignore_index=True)
    return final    #.to_csv("PhonesInfoPage{}to{}.csv".format(start,end))


