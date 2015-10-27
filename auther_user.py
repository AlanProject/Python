#-*- coding: utf-8 -*-
__author__ = 'root'
#定义用户字典users
users = {'admin':'passwd','system':'admin123'}
#定义认证函数
def user_auth():
    #定义 追加文件 和 读取文件方法
    f_add = file('lock','a')
    f_read = file('lock','r')
    #获取用户名
    user = raw_input('Please input your name:')
    #将黑名单从lock文件中读取并剔除回车符追加到lock_list
    lock_list = []
    for i in f_read.readlines():
        lock_list.append(i.strip("\n"))
    f_read.close()
    #如果用户在lock_list中则退出并打印出锁定信息
    if user in lock_list:
        print 'User %s lock'%user
        exit()
    else:
        print 'Welcome User Auther System'
        #定义一个长量i为下面错误计数做准备
        i = 0
        if user in users.keys():
            #如果用户认证失败3次则锁定
            while i < 3:
                #获取用户输入的密码
                passwd = raw_input('Please input your passwd:')
                #进行密码对比如果成功则登录成功 否则则失败
                if passwd == users[user]:
                    print 'Login Secuess Welcome'
                    break
                else:
                    #每输错一次密码则失败次数加1
                    i += 1
                    #计算还能尝试次数并打印引用
                    lock_number= 3-i
                    print 'Your password error please try again you can try:%d'%lock_number
            else:
                #错误超过3次将用户加入黑名单 并关闭文件
                f_add.write(user)
                f_add.write("\n")
                f_add.close()
        else:
            pass

if __name__ == '__main__':
    user_auth()
