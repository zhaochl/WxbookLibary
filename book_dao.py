#!/usr/bin/env python
# coding=utf-8
from db_util import *
from pdb import *

def query_user(user_name,password):
    sql="""select user_id,role from users where  user_name='{}'
    and password = '{}' limit 1
    """.format(user_name,password)
    results = db_query(sql)
    user_info = None
    if results and len(results)>0:
        for r in results:
            user_id = int(r[0])
            role = int(r[1])
            user_info = {}
            user_info['user_id'] = user_id
            user_info['role'] = role
    return user_info

def get_user_info_by_user_id(user_id):
    sql="""
    select user_id,`name`,student_id,college,phone,email from users where user_id = '{user_id}'
    """.format(user_id=user_id)
    c,users = convert_results(sql)
    user = users[0]
    return user

def get_user_info(openId):
    sql="""
    select `name`,student_id,college,phone,email from users where openid = '{openid}'
    """.format(openid=openId)
    c,users = convert_results(sql)
    user = users[0]
    return user
def get_books_info(book_id=None):
    sql=""
    if not book_id:
        sql = """
        select bk.book_id,bk.book_name,bk.author,bk.publish_com,bk.book_num, if(bk.`book_num`>0,'可以借阅','不可用借阅') as book_status from books bk where bk.status=1
        """
    else:
        sql = """
        select bk.book_id,bk.book_name,bk.author,bk.publish_com,bk.book_num, if(bk.`book_num`>0,'可以借阅','不可用借阅') as book_status from books bk where book_id = {}
         and bk.status=1 
        """.format(book_id)
    print sql
    columns, books = convert_results(sql)
    return books
def get_books_by_title(keyword):

    sql = """
    select bk.book_id,bk.book_name,bk.author,bk.publish_com,bk.book_num, if(bk.`book_num`>0,'可以借阅','不可用借阅') as book_status from books bk where book_name like '%{}%' and bk.status=1
    """.format(keyword)
    print sql
    columns, books = convert_results(sql)
    return books
def get_books_by_author(keyword):

    sql = """
    select bk.book_id,bk.book_name,bk.author,bk.publish_com,bk.book_num, if(bk.`book_num`>0,'可以借阅','不可用借阅') as book_status from books bk where author like '%{}%' and bk.status=1
    """.format(keyword)
    print sql
    columns, books = convert_results(sql)
    return books

def get_my_borrow_books(openId,book_id=None):
    sql=""
    if not book_id:
        sql="""select bk.book_id,bk.book_name,bk.author,bk.`publish_com`,bk.`publish_date`,bo.`date_borrow`,bo.`date_return` from  borrows bo, users u,books bk
        where bo.`openid` =  u.openid
        and bo.`book_id` = bk.`book_id`
        and u.`openid` = '{}'
        and bo.type=1
        and bo.status=0
        ;
        """.format(openId)
    else:
        sql="""select bk.book_id,bk.book_name,bk.author,bk.`publish_com`,bk.`publish_date`,bo.`date_borrow`,bo.`date_return` from  borrows bo, users u,books bk
        where bo.`openid` =  u.openid
        and bo.`book_id` = bk.`book_id`
        and u.`openid` = '{}'
        and bk.book_id={}
        and bo.type=1
        and bo.status=0
        ;
        """.format(openId,book_id)
    print sql
    columns, books = convert_results(sql)
    return books

def get_my_order_books(openId,book_id=None):
    sql=""
    if not book_id:
        sql="""select bk.book_id,bk.book_name,bk.author,bk.`publish_com`,bk.`publish_date`,bo.`date_borrow`,bo.`date_return`,bk.book_num,
        if(bk.`book_num`>0,'可以借阅','不可用借阅') as book_status  
        from  borrows bo, users u,books bk
        where bo.`user_id` =  u.user_id
        and bo.`book_id` = bk.`book_id`
        and u.`openid` = '{}'
        and bo.type=2
        and bk.status=1
        and bo.status=0
        """.format(openId)
    else:

        sql="""select bk.book_id,bk.book_name,bk.author,bk.`publish_com`,bk.`publish_date`,bo.`date_borrow`,bo.`date_return`,bk.book_num,
        if(bk.`book_num`>0,'可以借阅','不可用借阅') as book_status  
        from  borrows bo, users u,books bk
        where bo.`user_id` =  u.user_id
        and bo.`book_id` = bk.`book_id`
        and u.`openid` = '{}'
        and bo.type=2
        and bo.book_id={}
        """.format(openId,book_id)
    columns, books = convert_results(sql)
    return books
"""
borrow_type=1 borrow,2 order
"""
def save_my_borrow_book(openId,book_id,borrow_type):
    sql="""
    INSERT INTO `borrows` ( `book_id`, `user_id`, `date_borrow`, `date_return`, `status`, `openid`, `type` )
    VALUES
        ({book_id}, 0, now(), date_add(now(),interval 30 DAY), 0, '{openId}', {borrow_type});

    """.format(book_id=book_id,openId=openId,borrow_type=borrow_type)
    print sql

    db_update(sql)

def update_book_info(book_id,tag="add"):
    sql=""
    if tag=="add":
        sql="""
        update books set book_num =book_num+1 
        where book_id ={}
        """.format(book_id)
    else:
        sql="""
        update books set book_num =book_num-1 
        where book_id =1
        """
    print sql
    db_update(sql)

def add_user_openId(openId):
    sql_check = """
    select * from users where openId='{}'
    """.format(openId)
    print sql_check
    results = db_query(sql_check)
    print results
    if not results or len(results)==0:
        sql="""
        INSERT INTO `users` (`openid`,`status`)
        VALUES ('{openId}',1);
        """.format(openId=openId)
        db_update(sql)
def update_my_info(name,student_id,college,phone,email,openId):
    sql="""
    update users set name='{name}',student_id='{student_id}',`college`='{college}',phone='{phone}',email='{email}'
     where openid = '{openid}'
    """.format(name=name,student_id=student_id,college=college,phone=phone,email=email,openid=openId)
    db_update(sql)

def check_user_info(openId):
    check =True
    user_info = get_user_info(openId)
    if user_info['name']=='' or user_info['student_id']=='' or user_info['college']=='' or user_info['phone']==0 or user_info['email']=='':
        check = False
    return check


