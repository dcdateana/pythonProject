import easygui as eui,random,os
# 猜数游戏
# eui.msgbox('让我们来玩一个小游戏')
# secret=random.randint(1,10)
# msg='猜一猜我心中所想的数(1,10)'
# title='猜数小游戏'
# guss=eui.integerbox(msg,title,lowerbound=1,upperbound=10)
# while True:
#     if guss==secret:
#         eui.msgbox('恭喜猜对了')
#         break
#     else:
#         if guss>secret:
#             eui.msgbox('大了')
#         else:
#             eui.msgbox('小了')
#         guss=eui.integerbox(msg,title,lowerbound=1,upperbound=10)
# eui.msgbox('游戏结束')

# 信息填写
# msg='请填写信息'
# title='账号中心'
# filednames=['*用户名','*手机号','地址']
# filedvalues=eui.multenterbox(msg,title,filednames)
# while 1:
#     if filedvalues[0]=='' or filedvalues[1]=='':
#         errmsg='带*号的为必填项'
#     else:
#         break
#     filedvalues=eui.multenterbox(errmsg,title,filednames)
# eui.msgbox(str(filedvalues))

# 文件处理
# fiel_path=eui.fileopenbox(default='*.txt')
# with open(fiel_path) as f:
#     title=os.path.basename(fiel_path)
#     msg=title
#     text=f.read()
#     text_after=eui.textbox(msg,title,text)
# if text_after[:-1]!=text:
#     choice=eui.buttonbox('检测到文件内容发生改变','警告',['覆盖','放弃保存','另存为'])
#     if choice=='覆盖':
#         with open(fiel_path,'w') as f_old:
#             f_old.write(text_after[:-1])
#     elif choice=='放弃保存':
#         pass
#     elif choice=='另存为':
#         new_path=eui.filesavebox(default='.txt')
#         if os.path.splitext(new_path)[1]!='.txt':
#             new_path+='.txt'
#         with open(new_path,'w') as new_file:
#             new_file.write((text_after[:-1]))