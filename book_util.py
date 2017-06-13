#!/usr/bin/env python
# coding=utf-8
CONST_BORROW_TYPE=1
CONST_ORDER_TYPE=2
def show_menu():
    content ="""
    ***欢迎关注冯泽盛的个人图书馆***
    请选择：
    输入[查询{关键词}],请输入关键词搜索图书,比如输入:查询java
    输入[查询订阅],查看借阅情况
    """
    return content

def show_about():
    content="""
    本系统是基于微信公众号平台的借阅系统
    借书流程如下:
    1)关注公众号
    2)完善基本信息
    3)搜索图书
    4)输入借阅图书编号
    5)有库存则借阅成功，取走书借书成功
    6)无库存则预约图书
    还书流程如下:
    1)携带书籍到图书管理员处还书
    2)管理员检查无误后，通过后台操作数据库归还
    如有使用疑问请留言或联系管理员
    """
    return content

def show_input_my_info():
    content="""
    请先完善个人信息,依次输入: 信息{空格} {姓名} {学号} ,{学院} ,{手机号},{邮箱}
    示例如下: 
    信息 张三,B13070666,计算机学院,13223310011,test@126.com
    """
    return content

def build_my_borrow_book_info(results):
    content = '您的在借图书如下:\n'
    for obj in results:
        content+='book_id:'+obj['book_id']+',书名:'+obj['book_name']+',作者:'+obj['author']+',借阅时间:'+obj['date_borrow']+',归还时间:'+obj['date_return']+'\n'
    content+='\n温馨提示:请记得及时归还'
    return content

def build_my_order_book_info(results):
    content = '您的预约图书如下:\n'
    for obj in results:
        content+='book_id:'+obj['book_id']+','+obj['book_name']+','+obj['author']+'库存数量:'+obj['book_num']+',借阅状态:'+obj['book_status']+'\n'
    content+='\n温馨提示:请及时关注最新状态\n'
    return content

def build_books_info(results):
    content=''
    if len(results)>0:
        for obj in results:
            content+='book_id:'+obj['book_id']+','+obj['book_name']+',作者:'+obj['author']+',出版社:'+obj['publish_com']+',库存数量:'+obj['book_num']+',借阅状态:'+obj['book_status']+'\n'
    else:
        content="\n暂无相关图书\n"
    return content

def build_my_info(user_info):
    content =""
    if user_info and len(user_info)>0:
        content+="姓名:"+user_info['name']+'\n'
        content+="学号:"+user_info['student_id']+'\n'
        content+="学院:"+user_info['college']+'\n'
        content+="电话:"+user_info['phone']+'\n'
        content+="邮箱:"+user_info['email']+'\n'
    return content

def build_about_info():
    content ="""
    
    """
