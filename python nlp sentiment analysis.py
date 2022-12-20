# python nlp sentiment analysis

# Ex: LAST OF US PART II
# https://www.metacritic.com/game/playstation-4/the-last-of-us-part-ii/user-reviews

# 爬取所有评论
# 根据评论进行NLP情感分析，归因争议原因

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

path_to_driver = "/Users/bill/Documents/python/chromedriver"
driver = webdriver.Chrome(executable_path =
                          path_to_driver)
driver.get("https://www.metacritic.com/game/playstation-4/the-last-of-us-part-ii/user-reviews")

# manual refresh
print(driver.title)

# run for the first page

expand_num = len(driver.find_elements(By.XPATH,"//*[text()='Expand']"))

while expand_num > 0:
    try: 
        driver.find_elements(By.XPATH,"//*[text()='Expand']")[0].click()
        print(len(driver.find_elements(By.XPATH,"//*[text()='Expand']")))
    except selenium.common.exceptions.ElementClickInterceptedException:
        pass
    except IndexError:
        break
    time.sleep(0.01)
    
review_section = driver.find_elements(By.XPATH,"//ol[@class = 'reviews user_reviews']")
review_section_list = []
for i in range(len(review_section)): # 把抓取到的数据convert成文本，合并成一个list
    review_section_list.append(str(review_section[i].text))
print(review_section_list[-1])

driver.find_elements(By.XPATH,"//*[text()='next']")[0].click()

# run for remaining pages, until list index out of range

expand_num = len(driver.find_elements(By.XPATH,"//*[text()='Expand']"))
last_page = int(driver.find_elements(By.XPATH,"//a[@class = 'page_num']")[-1].text)

for i in range(last_page-1): #可以考虑查询总页数
    while expand_num > 0:
        try: 
            driver.find_elements(By.XPATH,"//*[text()='Expand']")[0].click()
            print(len(driver.find_elements(By.XPATH,"//*[text()='Expand']")))
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        except IndexError:
            break
        time.sleep(0.01)
    try:
        review_section = driver.find_elements(By.XPATH,"//ol[@class = 'reviews user_reviews']")
        review_section_list = []
        for i in range(len(review_section)): # 把抓取到的数据convert成文本，合并成一个list
            review_section_list.append(str(review_section[i].text))
        print(review_section_list[-1])
        # print("Page" + str(i)) 
        driver.find_elements(By.XPATH,"//*[text()='next']")[0].click()
    except IndexError:
        break

print(review_section_list[-1])
print(review_section_list[0])

len(review_section_list)

with open("each_comment.txt", "w") as file:
    file.write(str(review_section))

# 分别对每一个输出进行切分
# 利用/n进行切分，并保存成df

driver.get(url)
driver.find_elements(By.XPATH,"//label[@class= 'clamp-list-expand-label']")[0].click()
page1 = driver.find_elements(By.XPATH,"//td[@class = 'clamp-summary-wrap']")
print(page1[0].text)

review_section[0].text

len(review_section)

a = review_section[0]
b = a.split("\n")
print(b)
len(b)
new_df = pd.DataFrame([b],columns=["Username", "Name", "Platform", "Release Date", "Background", "Metascore_drop", "Metascore", "Userscore_drop", "Userscore"])
print(new_df)


import numpy as np
import pandas as pd

df = pd.DataFrame(columns=["No.", "Name", "Platform", "Release Date", "Background", "Metascore_drop", "Metascore", "Userscore_drop", "Userscore"])

for element in total_list:
    splited = element.split("\n")
    new_df = pd.DataFrame([splited], columns=["No.", "Name", "Platform", "Release Date", "Background", "Metascore_drop", "Metascore", "Userscore_drop", "Userscore"])
    df = pd.concat([df, new_df]) 
df = df.reset_index().drop(["index", "Metascore_drop", "Userscore_drop"], axis='columns')

df.head()
df.duplicated()

df['Metascore'] = pd.to_numeric(df['Metascore'])/10
df['Userscore'] = pd.to_numeric(df['Userscore'], errors='coerce').fillna(0)
df['Platform'] = df['Platform'].str.replace("Platform: ", "")

high_critic = df[df['Metascore'] > 8]
controversial = high_critic[high_critic['Metascore'] - 3 > high_critic['Userscore']]

controversial

df.to_csv('out2020.csv')

# 设定其他争议游戏的筛选机制，例如评价数量，评分分布，评测分布
# 争议游戏时间序列编年史

# comment.txt
    # list
# 去除高频元素
    # \n，
    # \n140 of 240 users found this helpful
    # \nAll this user\'s reviews\n
    
# user_name, date, user_rate, user_review, possible_collapse, xx_of_xx_user_helpful, all_reviews
# [2:-3]

my_file = open("/Users/bill/Documents/python/Metacritic Project/comment.txt", "r")
data = my_file.read()[2:-3]
data_into_list = data.split("\\nAll this user\\\'s reviews\'")
len(data_into_list)
data_into_list[0]

# len(data_into_list)
comment_list = []
for i in range(len(data_into_list)):
    element = data_into_list[i].split("\\nAll this user\\\'s reviews\\n")
    for i in range(len(element)):
        comment_list.append(element[i].split("\\n"))

len(comment_list)

comment_list[0]

abc = comment_list[-1]
len(abc)
for i in range(len(abc)):
    print(i)
    print(abc[i])

# abc = all_comments_elements[-1]
# for i in range(len(abc)):
#     print(i)
#     print(abc[i])
    
comment_list[-1] = comment_list[-1][:-1]

# user_name, date, user_rate, user_review, possible_collapse, xx_of_xx_user_helpful, all_reviews
user_name = []
date = []
user_rate = []
user_review = []
xx_of_xx_user_helpful = []

for i in range(len(comment_list)):
    user_name.append(comment_list[i][0])
    date.append(comment_list[i][1])
    user_rate.append(comment_list[i][2])
    user_review.append(comment_list[i][3:-1])
    xx_of_xx_user_helpful.append(comment_list[i][-1])

len(user_name)
len(date)
len(user_rate)
len(user_review)
len(xx_of_xx_user_helpful)

print(user_review[-3])

import pandas as pd
user_name_df = pd.DataFrame(user_name)
date_df = pd.DataFrame(date)
user_rate_df = pd.DataFrame(user_rate)
user_review_df = pd.DataFrame(user_review).fillna("").agg('-'.join, axis=1)
xx_of_xx_user_helpful_df = pd.DataFrame(xx_of_xx_user_helpful)

df = pd.concat([user_name_df, date_df, user_rate_df, user_review_df, xx_of_xx_user_helpful_df], join = 'outer', axis = 1)
df.columns = ['user_name', 'date', "user_rate", "user_review", "xx_of_xx_user_helpful"]

# df.to_csv('all_comments_new.csv')

user_review_df.iloc[0]

print(df.head())

# 下一步开始拆解 user_review_df, 进行语义分析
# 挑选出英文评论 / 通过观察csv文件，非英语字符显示为乱码
# 对格式进行整理 / spoiler,collapse, ""
# 使用text vectorization，通过训练模型得到采样数据中rating与text的关系
    # 使用分类算法，汇总各类评论观点
# 将模型应用到其他来源(exp. Twitter)的评论中，得到Predicted Sentiment

from sklearn.feature_extraction.text import CountVectorizer
# from nltk.corpus import stopwords 

vectorizer = CountVectorizer()
df["text_vectors"] = ""
# df["feature_names"] = ""

for i in range(df.shape[0]):
    corpus = user_review[i]
    try:
        X = vectorizer.fit_transform(corpus)
    except ValueError:
        df = df.drop(index=i) # drop rows with meaningless reviews
    # df["feature_names"] = vectorizer.get_feature_names()
    vectorizer.get_feature_names()
    result = X.toarray() 
    df["text_vectors"].iloc[i] = result
    
len(df)
df.iloc[0]
df["text_vectors"].iloc[-1]

text_vectors = pd.DataFrame(text_vectors)
df = pd.concat([df,text_vectors_df])

# 对格式进行整理 / spoiler,collapse, ""

# df[user_review].replace("")
# knn
# .str.startswith(('This review contains spoilers.'))

# how to pick comments in English?
# seelct("the")

corpus = user_review
X = vectorizer.fit_transform(corpus)
# df["feature_names"] = vectorizer.get_feature_names()
vectorizer.get_feature_names()
X.toarray() [0]

# 创建总feature_name，得到word freq

corpus = ""
for i in user_review:
    print(i)
    corpus += i[0]
    
print(user_review[2])