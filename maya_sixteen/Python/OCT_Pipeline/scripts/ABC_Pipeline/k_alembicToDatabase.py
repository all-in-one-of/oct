# -*- coding:utf-8 -*-

import maya.cmds as cc
import pypyodbc

class MSSQL:
    def __init__(self,driver,host,user,pwd,db):
        self.driver = driver
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):

        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pypyodbc.connect(driver=self.driver,server=self.host,uid=self.user,pwd=self.pwd,database=self.db)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


class k_alembicToDatabase:
    def __init__(self):
        pass

    def do(self,mode):
        #获取场景内带有Alembic属性的transform
        AlembicTransform = cc.ls(tr=1, l=1)
        AlembicAttr = [i for i in AlembicTransform if cc.listAttr(i, st='alembic')]
        fileName = cc.file(q=1, sn=1, shn=1)
        contrast_fileName=''
        if   'rg' in fileName:contrast_fileName = fileName.replace('rg','tx')
        elif 'tx' in fileName:contrast_fileName = fileName.replace('tx','rg')

        #连接数据库
        ms = MSSQL(driver='{SQL Server}', host='192.168.80.200', user='dengtao', pwd='ceshi1', db='yshubpmTest')

        if mode == 'upload':
            attrAlembicOn = AlembicAttr
            attrAlembicOn_rep = str(attrAlembicOn).replace('\'', '\"')
            add_sql = "insert into k_UploadAssetsData(attrAlembicOn,fileName) values('{0}','{1}')".format(
                attrAlembicOn_rep, fileName)
            # 上传内容到数据库
            ms.ExecNonQuery(add_sql)
            return ('upload Done')

        elif mode == 'check':
            find_sql = "select top 1 attrAlembicOn from k_UploadAssetsData " \
                       "where fileName='{0}' order by id desc".format(contrast_fileName)

            AlembicAttr_sql = []
            # 查询数据库的数据
            reslist = ms.ExecQuery(find_sql)
            for reslist_str in reslist:
                try:
                    attrAlembic = eval(reslist_str[0])
                    for i in attrAlembic:
                        AlembicAttr_sql.append(i)
                except Exception as e:
                    print (e)

            # 对比数据
            if AlembicAttr_sql:
                k_difference = list(set(AlembicAttr) ^ set(AlembicAttr_sql))
                return (k_difference)
            else:
                raise Exception("没有对比的mb文件数据")

if __name__ == '__main__':
    a=k_alembicToDatabase()
    b = a.do('check')
    #b = a.do('upload')
    print (b)
