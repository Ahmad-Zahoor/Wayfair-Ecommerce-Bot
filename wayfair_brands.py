# coding: utf8
from genericpath import isfile
from tkinter.filedialog import askopenfile, askopenfilename, askopenfilenames, askdirectory
from importlib.machinery import all_suffixes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from asyncio import sleep
from cProfile import label
# from cgitb import text
import csv
from http import server
from itertools import count
import os
from pprint import pprint
# from telnetlib import theNULL
from threading import Thread
import tkinter
from turtle import color
from unicodedata import category, numeric
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from subprocess import CREATE_NO_WINDOW
import time
import re
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import randint
from actions import *
import smtplib
import sys
from datetime import datetime, timedelta
import pytz
import requests
#from PIL import Image, ImageTk
import glob
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.message import EmailMessage
import undetected_chromedriver as uc
import urllib.request
from pathlib import Path
import re
import threading

root = Tk()
root.title("Armand-Store-Wayfair-Products-Data-Software")
# root.iconbitmap("Armand_store.ico")
fram2 = Frame(root)

label6 = Label(fram2, width=55, text="", anchor='w',font=("Helvetica", 10), fg="green")
label6.grid(row=3, column=1, padx=5, pady=5)

running = False

def clock(get_time):
    # pak_date = pytz.timezone("Asia/Karachi")
    # pak_time = datetime.now(pak_date)

    # current_time = pak_time.strftime("%H:%M:%S")
    root.update()
    label6.config(text=get_time)
    label6.after(1000)

def call(getind):
    try:
        root.update()
        emptylabel.configure(text = str(getind))
        root.after(1000)
        #return True
    except tkinter.TclError as e:
        root.destroy()

def furniture_w(driver, hrfs,get_count,create_path,root):

    label3.grid_forget()
    label4.grid_forget()

    driver.get("https://www.wayfair.com/brand/bbb/browse-by-brand")
    sleep(5)

    all_alphanumarics = []

    all_brands = []

    # Scrolling to All Brands A-Z
    try:
        brand_name_scroll = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//h2[@data-hb-id='Heading' and contains(text(), 'All Brands')]")))
        driver.execute_script("arguments[0].scrollIntoView();", brand_name_scroll)
        sleep(1)
    except Exception as e:
        try:
            brand_name_scroll = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-hb-id='Wrapper']/h2")))
            driver.execute_script("arguments[0].scrollIntoView();", brand_name_scroll)
            sleep(1)
        except Exception as e:
            print("Scrolling paths not found")
    
    # Get all Alphanumaric charachters
    try:
        get_alpha_n_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@data-hb-id='Wrapper']/h2[text()='All Brands A-Z']//..//div/button[@data-hb-id='Button' and not(contains(@name, 'Featured Brands'))]/span")))

        for ind2, alpha in enumerate(get_alpha_n_list):
            get_alpha = alpha.text
            if get_alpha not in all_alphanumarics:
                all_alphanumarics.append(get_alpha)
    except Exception as e:
        print("List path not found")
    


    # Code for Vendors list
    for ind, word in enumerate(hrfs):

        if ind<0:
            break

        else:

            vendor_name = word.lower().strip()

            #Get first charachter
            get_f = word[0]

            if get_f.isnumeric():

                # Code for clicking (0-9) in alpha numaric list
                try:
                    nbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-hb-id='Wrapper']/h2[text()='All Brands A-Z']//..//div/button[@name='0-9' and not(contains(@name, 'Featured Brands'))]")))
                    nbtn.click()
                    sleep(5)
                except Exception as e:
                    try:
                        nbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-hb-id='Wrapper']//div/button[@name='0-9']")))
                        driver.execute_script("arguments[0].click();",nbtn)
                        sleep(5)
                    except Exception as e:
                        print("Number not found")
                        break
                
                # Code for Scraping all sub vendor list
                all_sub_vendors = []
                try:
                    sub_vendor_list = driver.find_elements(By.XPATH, "//div[@data-hb-id='Wrapper']/h2[text()='All Brands A-Z']//..//div//a")
                    
                    for ind2, val2 in enumerate(sub_vendor_list, start=1):
                        sub_vendor_name = val2.text
                        #convert_lower2 = dropcatch_domain2.lower()
                        if sub_vendor_name not in all_sub_vendors:
                            all_sub_vendors.append(sub_vendor_name)
                
                except Exception as e:
                    print("Sub Vendor List Path not found")
                
                # Code for looking Vendor name in the list
                try:
                    for new_d in all_sub_vendors:
                        newd1 = new_d.lower().strip()

                        if newd1==vendor_name:
                            try:
                                get_domain2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-hb-id='Wrapper']/h2[text()='All Brands A-Z']//..//div//a//p[text()='"+new_d+"']/parent::a")))
                                get_link = get_domain2.get_attribute("href")

                                if get_link not in all_brands:
                                    all_brands.append(get_link)
                                    print("Found Vendor name:", new_d)
                                #update_data = [new_d,get_link]
                                #writer.writerow(update_data)
                                # print("Vendor name:", new_d)
                                # print("Link is: ", get_link)
                            
                            except Exception as e:
                                print("Get Domain Path Not Found")
                        
                        else:
                            pass
                        
                                        
                except Exception as e:
                    print("Sub Vendor not working")
                
            elif get_f.upper() in all_alphanumarics:

                alph_letter = get_f.upper()

                # Code for clicking Alphabit
                try:
                    alphabtn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-hb-id='Wrapper']/h2[text()='All Brands A-Z']//..//div/button[@name='"+str(alph_letter)+"' and not(contains(@name, 'Featured Brands'))]")))
                    alphabtn.click()
                    sleep(5)
                except Exception as e:
                    try:
                        alphabtn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-hb-id='Wrapper']//div/button[@name='0-9']")))
                        driver.execute_script("arguments[0].click();",alphabtn)
                        sleep(5)
                    except Exception as e:
                        print("Alphabit not found")
                        break
                
                # Code for Scraping all sub vendor list
                all_sub_vendors = []
                try:
                    sub_vendor_list = driver.find_elements(By.XPATH, "//div[@data-hb-id='Wrapper']/h2[text()='All Brands A-Z']//..//div//a")
                    
                    for ind2, val2 in enumerate(sub_vendor_list, start=1):
                        sub_vendor_name = val2.text
                        #convert_lower2 = dropcatch_domain2.lower()
                        if sub_vendor_name not in all_sub_vendors:
                            all_sub_vendors.append(sub_vendor_name)
                
                except Exception as e:
                    print("Sub Vendor List Path not found")
                
                # Code for looking Vendor name in the list
                try:
                    for new_d in all_sub_vendors:
                        newd1 = new_d.lower().strip()

                        if newd1==vendor_name:
                            try:
                                get_domain2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-hb-id='Wrapper']/h2[text()='All Brands A-Z']//..//div//a//p[text()='"+new_d+"']/parent::a")))
                                get_link = get_domain2.get_attribute("href")

                                if get_link not in all_brands:
                                    all_brands.append(get_link)
                                    print("Found Vendor name:", new_d)
                                # update_data = [new_d,get_link]
                                # writer.writerow(update_data)
                                # print("Vendor name:", new_d)
                                # print("Link is: ", get_link)
                            
                            except Exception as e:
                                print("Get Domain Path Not Found")
                                print(e)
                        
                        else:
                            pass
                        
                                        
                except Exception as e:
                    print("Issue in Website Vendor List")
                    print(e)

            else:
                print("First Character of Word Not found in Alphanumaric List")
            
            print("Counter: ",str(ind+1))
        
    
    print("Total Brands Found: ", len(all_brands))
    sleep(1)
    # Code for Opening main Brands
    for ind_b, brand in enumerate(all_brands, start=1):

        if ind_b>0:


            start = time.time()

            driver.get(brand)
            sleep(5)

            Brand_products = []



            try:
                brandName = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//h1/span[@data-cypress-id='BrowseRoadsign']"))).text
            except Exception as e:
                try:
                    brandName = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/h1/span").text
                except Exception as e:
                    print("Brand Name not found")
                    break
            

            if "/" in brandName:
                brandName = brandName.replace("/","")
            
            print(f"Brand {brandName} is in process...")

            # Create Brand Folder

            folderpath = f"{create_path}\{brandName}"

            if not os.path.exists(folderpath):
                os.mkdir(folderpath)



            # Code for Scraping all categories
            # all_categories = []
            try:
                get_categories = driver.find_elements(By.XPATH, "//div/p[text()='Category']//..//..//..//..//div[@class='Filters-filter']//div[@role='grid']/div//input[@data-enzyme-id='BaseToggleInput' or @data-codeception-id='AttributeOptionCheckbox']")
                
                # for ind2, catg in enumerate(get_categories, start=1):
                #     catg_name= catg.get_attribute("href")
                #     if catg_name not in all_categories:
                #         all_categories.append(catg_name)
            
            except Exception as e:
                print("All Categories List Path not found")
                print(e)
            
            # print(f"Brand {brandName} have total categories: ", len(all_categories))
            # sleep(1)
            
            # Code for Scraping categories data
            try:
                for indl, scat in enumerate(get_categories, start=1):

                    if indl >= 0:

                        driver.get(brand)
                        sleep(5)

                        # Click on category check box

                        try:
                            checbtn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div/p[text()='Category']//..//..//..//..//div[@class='Filters-filter']//div[@role='grid']/div["+str(indl)+"]//input[@data-enzyme-id='BaseToggleInput' or @data-codeception-id='AttributeOptionCheckbox']")))
                            checbtn.click()
                            sleep(2)
                        
                        except Exception as e:
                            try:
                                checkbtn = driver.find_element(By.XPATH, "//div/p[text()='Category']//..//..//..//..//div[@class='Filters-filter']//div[@role='grid']/div["+str(indl)+"]//input[@data-enzyme-id='BaseToggleInput' or @data-codeception-id='AttributeOptionCheckbox']")
                                driver.execute_script("arguments[0].click();", checkbtn)
                                sleep(2)
                            except Exception as e:
                                print("Category Checkbox Button not found")


                        # driver.get(scat)
                        # sleep(5)

                        # Code for Category Name
                        try:
                            catname = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h1/span"))).text
                        except Exception as e:
                            try:
                                catname = driver.find_element(By.XPATH,"(//span[@class='BrowseHeaderWithSort-roadsign'])[1]").text
                            except Exception as e:
                                catname = "NAN"
                                print("Category Name Path Not Found")
                                break
                        
                        if catname !="NAN":
                            if "/" in catname:
                                catname = catname.replace("/","")
                                
                            filpathf = f"{folderpath}\{catname}"+".csv"

                            # print(f"Category No: {indl} is in process...")

                            if not os.path.exists(filpathf):

                                headers = ["Wayfair Category Name","Wayfair Product Name","Wayfair Product Link","Wayfair Product SKU","Wayfair Product Price","Armand Price"]

                                with open(filpathf, 'a', newline='',encoding="utf-8") as output:
                                    writer = csv.writer(output)
                                    writer.writerow(headers)
                            
                            with open(filpathf, 'a', newline='',encoding="utf-8") as output:
                                writer = csv.writer(output)

                                counter = 1

                                get_price = ""

                                get_products_links = []

                                while(True):
                                    sleep(3)
                                    
                                    # Clicking on Next Button
                                    try:
                                        try:
                                            sleep(5)
                                            items = driver.find_elements(By.XPATH, "//div[@id='sbprodgrid']//div[@data-hb-id='ProductCard']/a")
                                            
                                            for item_ind, itemn in enumerate(items, start=1):

                                                get_item_link = driver.find_element(By.XPATH, "//div[@id='sbprodgrid']/div/div["+str(item_ind)+"]//a").get_attribute("href")
                                                get_products_links.append(get_item_link)
                                                Brand_products.append(get_item_link)
                                                
                                                    
                                                

                                        except Exception as e:
                                            print("Domains path not found")
                                        
                                        if len(get_products_links)>=48:
                                            print(f"Page No:{counter} Links Scraped")
                                            counter +=1
                                        
                                        nextbtn = check_exists_by_xpath(driver, "//a[@data-enzyme-id='paginationNextPageLink']")
                                        if nextbtn==False:
                                            break
                                        else:
                                            driver.find_element(By.XPATH, "//a[@data-enzyme-id='paginationNextPageLink']").click()
                                            driver.implicitly_wait(50)
                                    except Exception as e:
                                        print("Next btn not found")
                                
                                if len(get_products_links)>0:
                                    print(f"Category No: {indl} have {len(get_products_links)} products and is in process...")
                                    # Code for Products Data Scraping
                                    
                                    for pro_ind, prod_link in enumerate(get_products_links, start=1):

                                        driver.get(prod_link)
                                        sleep(5)

                                        try:
                                            #get_item_link = driver.find_element(By.XPATH, "//div[@id='sbprodgrid']/div/div["+str(item_ind)+"]//a").get_attribute("href")
                                            
                                            #get_item_name = driver.find_element(By.XPATH, "(//header/h1[@data-hb-id='Heading'])[2]").text
                                            get_item_name = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"(//header/h1[@data-hb-id='Heading'])[2]"))).text if check_exists_by_xpath(driver,"(//header/h1[@data-hb-id='Heading'])[2]") else "Null"
                                            #get_item_price = driver.find_element(By.XPATH, "//div[@class='SFPrice']/div/span").text
                                            get_item_price = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='SFPrice']/div/span[contains(text(), '$')]"))).text if check_exists_by_xpath(driver,"//div[@class='SFPrice']/div/span[contains(text(), '$')]") else "Null"
                                            #get_sku_text = driver.find_element(By.XPATH, "//ol[contains(@class,'Breadcrumbs-list')]/li/span[contains(text(), 'SKU')]").text
                                            try:
                                                get_sku_text = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//nav/ol/li/span[contains(text(), 'SKU')]"))).text
                                                get_sku = (get_sku_text.split(":")[1]).strip()
                                            except Exception as e:
                                                try:
                                                    get_sku_text = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//ol[contains(@class,'Breadcrumbs-list')]/li/span[contains(text(), 'SKU')]"))).text
                                                    get_sku = (get_sku_text.split(":")[1]).strip()
                                                except Exception as e:
                                                    get_sku = "Null"
                                            # if get_sku_text=="Null":
                                            #     get_sku = "Null"
                                            #     print("SKU Not found")
                                            # else:
                                                

                                
                                            check_pricen = find_price(driver,get_item_price)

                                            if check_pricen:
                                                armand_price = float(check_pricen) - 5
                                                wayfair_p = float(check_pricen)
                                                new_wayfair_price = "${:,.2f}".format(wayfair_p)
                                                new_armand_price = "${:,.2f}".format(armand_price)
                                                    
                                            else:
                                                print("Price path not found")
                                                new_wayfair_price = "Null"
                                                new_armand_price = "Null"
                                            
                                            get_new_data = [catname,get_item_name,prod_link,get_sku,new_wayfair_price,new_armand_price]
                                            writer.writerow(get_new_data)
                                            output.flush()

                                            print("Link Counter: ",pro_ind)
                                            
                                        
                                        except Exception as e:
                                            print("Product data has an issue")
                                            print(f"Link {pro_ind} has an issue")
                                            print(e)
                                else:
                                    print("Products are not found")
                                    break                     
            except Exception as e:
                print("Issue in Scraping Categories List")
                print(e)
            
            call(str(ind_b))
            
            print(f"Brand {brandName} have {len(Brand_products)} products")
            
            stop = time.time()
            duration = stop-start
            my_time = time.strftime('%H:%M:%S', time.localtime(duration))
            clock(my_time)
        #threading.Thread(target=clock()).start()
        
        


        
    try:
        driver.close()
    except (WebDriverException,NoSuchWindowException) as e:
        pass
    

def stop_w(driver):

    get_val = messagebox.askquestion("Exit", "Do you want to close the program",icon = 'warning')
    try:
        if get_val=='yes':
            root.destroy()
            driver.close()
        else:
            pass
    except (NoSuchWindowException,WebDriverException) as e:
        pass

def close_window():

    global running

    get_val = messagebox.askquestion("Exit", "Do you want to close the program",icon = 'warning')

    try:
        if get_val=='yes' and running:
            root.destroy()
            running.close()
        elif get_val=='yes':
            root.destroy()
    except (WebDriverException,NoSuchWindowException) as e:
        pass


def startBot(ents, root):

    # downloads_path = str(Path.home() / "Downloads")

    # newfolder = "Furniture_data"

    # create_path = os.path.join(downloads_path,newfolder)

    # if not os.path.exists(create_path):
    #     os.mkdir(create_path)
    global running

    b1.config(state="disabled")
    
    startIndex    = ents['Start Index'].get()
    get_file   = ents['Add files'].get()
    get_dir = ents['Output folder'].get()

    if startIndex=="":
        messagebox.showerror('Start Index', "Pleas Enter Value")
        b1.config(state="normal")

    elif startIndex.isnumeric()==False:
        messagebox.showerror('Start Index', "Pleas Enter Only Positive Number")
        b1.config(state="normal")
    
    elif get_file=="":
        messagebox.showerror('Add files', "Pleas Enter File Name")
        b1.config(state="normal")
    
    elif get_file.isnumeric()==True:
        messagebox.showerror('Add files', "Pleas Enter correct file name")
        b1.config(state="normal")
    elif os.path.exists(get_file)==False:
        messagebox.showerror('Add files', "File not found in the direcotry")
        b1.config(state="normal")
    
    elif get_dir=="":
        messagebox.showerror('Folder', "Pleas Select Output Folder")
        b1.config(state="normal")
    
    elif get_dir.isnumeric()==True:
        messagebox.showerror('Folder', "Pleas Enter Correct output path")
        b1.config(state="normal")
    elif os.path.exists(get_file)==False:
        messagebox.showerror('Folder', "Folder path not found")
        b1.config(state="normal")
    
    else:
        startIndex = int(ents['Start Index'].get())

        if startIndex <=0:
            messagebox.showerror('Start Index', "Pleas Enter greater then 0 Number")
            b1.config(state="normal")
        
        else:
            startIndex = int(ents['Start Index'].get())

            name, extensionf = os.path.splitext(get_file)

            data = []
    
            if extensionf=='.xlsx':
                excel_data = pd.read_excel(get_file, header=None, index_col=0)
                
                for row in excel_data.index:
                    if row not in data:
                        sentence = ' '.join(row.split())
                        data.append(sentence)

            else:
                csv_data = pd.read_csv(get_file, header=None, index_col=0)
                for row in csv_data.index:
                    if row not in data:
                        sentence = ' '.join(row.split())
                        data.append(sentence)


            # data = []
                
            # # Open Products file
            # with open(get_file, 'r') as txt_file:
            #     txt_reader = txt_file.readlines()
            #     for row in txt_reader:
            #         if row not in data:
            #             sentence = ' '.join(row.split())
            #             data.append(sentence)
            
            get_lenght = len(data)
            if startIndex >get_lenght:
                messagebox.showerror("Start Index", "Please Enter number between 1 and {}".format(get_lenght))
                b1.config(state="normal")
            else:
                print("Total Vendor are: ")
                print(len(data))
                sleep(1)


                #driver = uc.Chrome(use_subprocess=True,service_creationflags=CREATE_NO_WINDOW)
                driver = uc.Chrome(use_subprocess=True)
                driver.maximize_window()
                time.sleep(5)

                # chrome_options = Options()
                # chrome_options.add_experimental_option("debuggerAddress","localhost:9014")
                # service = Service(executable_path=ChromeDriverManager().install())
                # driver = webdriver.Chrome(service=service,options=chrome_options)
                # #service.creationflags = CREATE_NO_WINDOW
                # driver = webdriver.Chrome(executable_path=r"F:\Furniture\chromedriver.exe",options=chrome_options)
                # driver.maximize_window()
                # sleep(2)

                running = driver

                b1.grid_forget()
                b2 = Button(fram2, text='Stop', command=lambda: stop_w(driver)) #command=root.destroy
                b2.grid(row=4, column=0, padx=5, pady=5)
                
                furniture_w(driver,data[startIndex - 1:], startIndex,get_dir,root)

# def makeform(root, fields):
#     all_ents = {}

#     for field in fields:
#         row = Frame(root)
#         lab = Label(row, width=15, text=field + ": ", anchor='w')
#         ent = Entry(row, width=25)
#         ent.insert(0,"")
#         row.pack(side=TOP, fill=X, padx=5, pady=5)
#         lab.pack(side=LEFT)
#         ent.pack(side=RIGHT, expand=YES, fill=X)
#         all_ents[field] = ent
    
#     return all_ents

def open_file(get_field):
    #os.getcwd()
    # downloads_path = str(Path.home() / "Downloads")
    fileobj = askopenfilename(initialdir=os.getcwd(),title="Open File", filetypes=[('Text Files','*.txt'),('CSV Files', '*.csv'),('Xlsx Files', '*.xlsx')])
    
    if fileobj:
        get_field.set(fileobj)

def open_dir(get_dir):
    # downloads_path = str(Path.home() / "Downloads")
    filedir = askdirectory(initialdir=os.getcwd(),title="Select Folder")
    if filedir:
        get_dir.set(filedir)


def makeform(root, fields):
    
    all_ents = {}

    for field in fields:
        fram1 = Frame(root)
        if field=="Add files":
            label1 = Label(fram1, width=15, text=field + " :", anchor='w')
            label1.pack(side=LEFT, padx=5, pady=5)
            my_str = StringVar()
            ent = Entry(fram1, width=40, textvariable=my_str)
            ent.insert(0, "")
            browsebtn = Button(fram1, text="Browse",state="normal", command=lambda: open_file(my_str))
            browsebtn.pack(side=RIGHT, padx=5, pady=5)
            ent.pack(side=RIGHT, expand=YES, fill=X, padx=50, pady=5)
            fram1.pack(side=TOP, fill=X, padx=5, pady=5)
            all_ents[field] = ent
        elif field=="Output folder":
            label1 = Label(fram1, width=15, text=field + " :", anchor='w')
            label1.pack(side=LEFT, padx=5, pady=5)
            my_dir = StringVar()
            ent = Entry(fram1, width=40, textvariable=my_dir)
            ent.insert(0, "")
            browsebtn = Button(fram1, text="Browse",state="normal", command=lambda: open_dir(my_dir))
            browsebtn.pack(side=RIGHT, padx=5, pady=5)
            ent.pack(side=RIGHT, expand=YES, fill=X, padx=50, pady=5)
            fram1.pack(side=TOP, fill=X, padx=5, pady=5)
            all_ents[field] = ent
        else:
            label1 = Label(fram1, width=15, text=field + " :", anchor='w')
            ent = Entry(fram1, width=40)
            ent.insert(0, "")
            fram1.pack(side=TOP, fill=X, padx=5, pady=5)
            label1.pack(side=LEFT, padx=5, pady=5)
            ent.pack(side=RIGHT, expand=YES, fill=X, padx=50, pady=5)
            all_ents[field] = ent

        # row = Frame(root)
        # lab = Label(row, width=20, text=field + ": ", anchor='w')
        # ent = Entry(row, width=15)
        # ent.insert(0,"")
        # row.pack(side=TOP, fill=X, padx=5, pady=5)
        # lab.pack(side=LEFT)
        # ent.pack(side=RIGHT, expand=YES, fill=X)
        # all_ents[field] = ent
    
    return all_ents


fields = (["Start Index","Add files","Output folder"])

# root = Tk()

entries = makeform(root, fields)


label2 = Label(fram2, width=10, text="Start Counter:", anchor='w')
label2.grid(row=1, column=0, padx=5, pady=5)

emptylabel = Label(fram2, width=10)
emptylabel.grid(row=1, column=1, padx=10, pady=5)

label3 = Label(fram2, width=10, text="Note:", anchor='w', foreground='red')
label3.grid(row=2, column=0, padx=5, pady=5)

label4 = Label(fram2, width=55, text="After You Hit the start button it will start after minimum 50 seconds", anchor='w')
label4.grid(row=2, column=1, padx=5, pady=5)

label5 = Label(fram2, width=10, text="Current Time:", anchor='w')
label5.grid(row=3, column=0, padx=5, pady=5)



# threading.Thread(target=clock()).start()

fram2.pack(side=BOTTOM, padx=5, pady=5)

#command=lambda: threading.Thread(target=run_weekly, args=(parent,), daemon=True).start()

b1 = Button(fram2, text='Start',state="normal", command=lambda: threading.Thread(target=startBot, args=(entries,  root,)).start()) #, daemon=True

#b1 = Button(fram2, text='Start', command=lambda: startBot(entries,  root))
b1.grid(row=4, column=0, padx=5, pady=5)

# b2 = Button(fram2, text='Stop', command=root.destroy)
# b2.grid(row=4, column=1, padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW",close_window)
root.mainloop()