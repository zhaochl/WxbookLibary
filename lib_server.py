#!/usr/bin/env python
# coding=utf-8
import sys
import json
import werobot
from book_util import *

import requests
reload(sys)  
sys.setdefaultencoding('utf8')
import re
import traceback
from pdb import *
from book_dao import *

token="NageLxLS32W0OyeWXtJoxrcax841uE8k-8TGPR8oOpCkmkdAGU-_gpQslFvJqqqc_agPQlU4Sbt8vnNyissXxqvyr7fncup-y7Rty5Mbe1EFMhHUGYZqJu4CRl6yN7RDTWFeADAFIR"

robot = werobot.WeRoBot(token=token)

robot.config["APP_ID"] = ""
robot.config["APP_SECRET"] = ""
client = robot.client
def init_menu1():
    client.create_menu({
    "button":[{
         "type": "click",
         "name": "今日歌曲",
         "key": "music"
    }]
    })

def init_menu():
    client.create_menu({
    "button":[
        {
            "name":"查询",
            "sub_button":[
                {
                    "type":"click",
                    "name":"书名查询",
                    "key":"search_book_by_title"
                },
                {
                    "type":"click",
                    "name":"作者查询",
                    "key":"search_book_by_author"
                }
                
            ]
        },
        {
            "name":"我的",
            "sub_button":[
                {
                    "type":"click",
                    "name":"在借图书",
                    "key":"view_my_borrow"
                },
                {
                    "type":"click",
                    "name":"预约图书",
                    "key":"view_my_order"
                },
                {
                    "type":"click",
                    "name":"查看信息",
                    "key":"view_my_info"
                }
            ]
        }
        ,{
            "type":"click",
            "name":"关于",
            "key":"about_us"
        }
    ]})

#@robot.text
#def articles(message):
#    article =  [
#        [
#            "title",
#            "description",
#            "##",
#            "##"
#        ],
#        [
#            "whtsky",
#            "I wrote WeRoBot",
#            "##","##"
#        ]
#    ]
#    return article

@robot.key_click("about_us")
def about_us(message):
    content = show_about()
    return content


#print 'token:',client.get_access_token()
#@robot.key_click("music")
#def music(message):
#    return '你点击了“今日歌曲”按钮'

@robot.key_click("search_book_by_title")
def search_book_by_title(message):
    content = """请输入:书名{空格} {关键字}进行查询
            例如: 书名 Java
            """
    return content

@robot.key_click("search_book_by_author")
def search_book_by_author(message):
    content ="""请输入:作者{空格}{作者名}进行查询
            例如:作者 张三
            """
    return content

@robot.filter(re.compile("作者.*"))
def show_search_book_by_author(message):
    openId = message.source
    keyword = message.content.strip("作者").strip(" ")
    if keyword=="":
        return "您输入有误，请重新输入"
    content = """
    你搜索的作者为:{}
    """.format(keyword)
    books = get_books_by_author(keyword)
    content = build_books_info(books)
    return content

@robot.filter(re.compile("书名.*"))
def show_search_book_by_title(message):
    openId = message.source
    set_trace()
    keyword = message.content.strip("书名").strip(" ")
    if keyword=="":
        return "您输入有误，请重新输入"
    content = """
    你搜索的书名为:{}
    """.format(keyword)
    books = get_books_by_title(keyword)
    content = build_books_info(books)
    return content


@robot.key_click("search_book")
def search_book(message):
    content = show_menu()
    return content


@robot.key_click("view_my_borrow")
def view_my_borrow(message):
    source = message.source
    books =get_my_borrow_books(source)
    content = build_my_borrow_book_info(books)

    #content = "select * from userid where openId="+source
    return content


@robot.key_click("view_my_order")
def view_my_order(message):
    source = message.source
    books =get_my_order_books(source)
    content = build_my_order_book_info(books)

    #content = "select * from userid where openId="+source
    return content


@robot.subscribe
def subscribe(message):
    source = message.source
    print source+'添加了关注'
    content = show_about()
    add_user_openId(source)
    content+=show_input_my_info()
    return content


@robot.unsubscribe
def unsubscribe(message):
    source = message.source
    print source +' 取消了关注'
    return 'Hello My Friend!'+str(message)


@robot.view
def view(message):
    source = message.source
    print source +' view pages'
    return 'view-Hello My Friend!'+str(message)


@robot.key_click("view_my_info")
def view_my_info(message):
    openId = message.source
    user_info = get_user_info(openId)
    content=build_my_info(user_info)
    if content=="":
        content= "您尚未完善个人信息"
        content+=show_input_my_info()
    return content

@robot.filter("帮助")
def show_help(message):
    return show_about()


@robot.text
def input_text(message, session):
    #set_trace()
    #if 'first' in session:
    #    return '你之前给我发过消息'+str(message.content)
    session['first'] = True
    source = message.source
    openId = source
    #return '你之前没给我发过消息'
    source_content = message.content
    print 'openID:',source,source_content
    session['action'] =''

    keyword = message.content.strip("作者").strip("书名").strip("借阅").strip("预定").strip("信息").strip(" ")
    content = ""
    if source_content.find('书名')>=0:
        
        content = '图书信息如下:\n'
        books = get_books_by_title(keyword)
        content += build_books_info(books)
        content+='\n温馨提示:如需借阅输入 借阅{空格} {图书ID}'
    elif source_content.find('作者')>=0:

        content = '图书信息如下:\n'
        books = get_books_by_author(keyword)
        content += build_books_info(books)
        
        content+='\n温馨提示:如需借阅输入 借阅{空格} {图书ID}'
    
    elif source_content.find('借阅')>=0:
        if not check_user_info(openId):
            return "您尚未完善个人信息,请完善后操作"
        try:
            book_id = int(keyword)
            books = get_books_info(book_id)
            if len(books)==0:
                content = "该书籍暂时不可借阅,请联系管理员"
            else:
                book = books[0]
                if book['book_num']<=0 or book['book_num']==None or book['book_status']==0:
                    content = "该书籍暂时不能借阅,只能预定"

                else:
                    borrows_book = get_my_borrow_books(source,book_id)
                    if len(borrows_book)==0:
                        content = '借阅成功\n借阅信息如下:\n'
                        content+='\n温馨提示:如需预定输入 预定{空格} {图书ID}'
                        save_my_borrow_book(source,book_id,CONST_BORROW_TYPE)
                        update_book_info(book_id,tag="sub")
                        borrows_book = get_my_borrow_books(source,book_id)
                        content += build_my_borrow_book_info(borrows_book)
                    else:
                        content+="您已经借阅此图书,不能再次借阅"

        except Exception,e:
            print 'error:',e
            traceback.print_exc()
            content = "输入book_id有误,请更正后借阅"
    
    elif source_content.find('预定')>=0:
        try:
            book_id = int(keyword)
            books = get_books_info(book_id)
            if len(books)==0:
                content = "该书籍暂时不可操作,请联系管理员"
            else:
                book = books[0]
                if book['book_num']<=0:
                    #content = "该书籍暂时不能借阅,只能预定"

                    order_book = get_my_order_books(source,book_id)
                    if len(order_book)==0:
                        content = '借阅成功\n借阅信息如下:\n'
                        content+='\n温馨提示:如需预定输入 预定{空格} {图书ID}'
                        save_my_borrow_book(source,book_id,CONST_ORDER_TYPE)
                        order_book = get_my_order_books(source,book_id)
                        content += build_my_order_book_info(orders_book)
                    else:
                        content+="您已经预定过次图书,不能再次预定"
                else:
                    content="""
                    该书籍可以直接借阅
                    """
        except Exception,e:
            traceback.print_exc()
            print 'error:',e
            content = "输入book_id有误,请更正后预定"
    
    elif source_content.find('信息')>=0:
        #信息 张三,B13070666,计算机学院,132233100,test@126.com
        infos = keyword.split(',')
        print infos
        try:
            name = infos[0]
            student_id = infos[1]
            college = infos[2]
            phone = infos[3]
            email = infos[4]
            update_my_info(name,student_id,college,phone,email,openId)
            content="更新个人信息成功"
        except Exception,e:
            print 'error:',e
            content = "输入信息有误,请重新输入"

        
    else:
        content = '您输入有误，请重新输入'
    return content




#@robot.handler
#def hello(message):
#    return 'Hello World!'


#@robot.text
#def articles(message):
#    return [
#        [
#            "title",
#            "description",
#            "img",
#            "url"
#        ],
#        [
#            "whtsky",
#            "I wrote WeRoBot",
#            "https://secure.gravatar.com/avatar/0024710771815ef9b74881ab21ba4173?s=420",
#            "http://whouz.com/"
#        ]
#    ]
def test_article():
    articles = [
    {
        "title":"Happy Day",
        "description":"Is Really A Happy Day",
        "url":"URL",
        "picurl":"PIC_URL"
    },
    {
        "title":"Happy Day",
        "description":"Is Really A Happy Day",
        "url":"URL",
        "picurl":"PIC_URL"
    }
    ]
    #client.send_acticle_message("user_id", articles)


if __name__=='__main__':
    init_menu()
    # 让服务器监听在 0.0.0.0:80
    test_article()
    robot.config['HOST'] = '0.0.0.0'
    robot.config['PORT'] = 80
    robot.run()

