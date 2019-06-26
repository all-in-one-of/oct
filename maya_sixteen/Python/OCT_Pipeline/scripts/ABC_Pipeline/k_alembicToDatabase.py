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
        """mode为模式，upload为上传模式 返回值为字符串'upload Done'，check为检查模式 返回值为对比后不一致的数据"""

        #获取场景内带有Alembic属性的transform
        AlembicTransform = cc.ls(tr=1, l=1)
        AlembicAttr = [i for i in AlembicTransform if cc.listAttr(i, st='alembic')]
        #获取带有Alembic属性mesh的UV值
        AlembicUVs = {}
        for i in AlembicAttr:
            AlembicUV = cc.polyEditUV('{}.map[0:]'.format(i), query=True)
            AlembicUVs.update({i:'{}'.format(AlembicUV)})


        fileName = cc.file(q=1, sn=1, shn=1)
        contrast_fileName=''
        if   '_rg' in fileName:contrast_fileName = fileName.replace('_rg','_tx')
        elif '_tx' in fileName:contrast_fileName = fileName.replace('_tx','_rg')

        #连接数据库
        ms = MSSQL(driver='{SQL Server}', host='192.168.80.200', user='dengtao', pwd='ceshi1', db='yshubpmTest')

        if mode == 'upload':
            attrAlembicOn = AlembicAttr
            attrAlembicOn_rep = str(attrAlembicOn).replace('\'', '\"')
            AlembicUVs_rep = str(AlembicUVs).replace('\'', '\"')

            add_sql = "insert into k_UploadAssetsData(attrAlembicOn,fileName,AlembicUVs) values('{0}','{1}','{2}')".format(
                attrAlembicOn_rep, fileName,AlembicUVs_rep)
            # 上传内容到数据库

            ms.ExecNonQuery(add_sql)
            return ('upload Done')

        elif mode == 'check':
            #AlembicAttr_sql = self.getData('list', 'attrAlembicOn', contrast_fileName)
            AlembicUVs_sql = self.getData('dict', 'AlembicUVs', contrast_fileName)

            AlembicAttr_dif=[]
            AlembicUVs_difKey=[]
            # 对比数据
            # if AlembicAttr_sql:
            #     AlembicAttr_dif = list(set(AlembicAttr) ^ set(AlembicAttr_sql))

            # 对比 UV  数据
            if AlembicUVs_sql:
                AlembicUVs_dif = list(set(AlembicUVs.items()) ^ set(AlembicUVs_sql.items()))
                for i in AlembicUVs_dif:AlembicUVs_difKey.append(i[0])
                AlembicUVs_difKey = list(set(AlembicUVs_difKey))
            else:raise Exception("没有对比的mb文件数据")

            return (AlembicUVs_difKey)


    def getData(self,type,karg0,karg1):
        """获取数据库信息，type为查找数据的类型，karg为搜索条件 0为条件1, 1为filename"""

        # 连接数据库
        ms = MSSQL(driver='{SQL Server}', host='192.168.80.200', user='dengtao', pwd='ceshi1', db='yshubpmTest')



        find_sql = "select top 1 {0} from k_UploadAssetsData " \
                   "where fileName='{1}' order by id desc".format(karg0,karg1)

        if type == 'dict':
            sql_data = {}
        elif type == 'list':
            sql_data = []

        # 查询数据库的数据
        reslist = ms.ExecQuery(find_sql)

        for reslist_str in reslist:

            try:
                attrAlembic = eval(reslist_str[0])
                for i in attrAlembic:
                    if type == 'dict':
                        sql_data.update({i: attrAlembic[i]})
                    elif type == 'list':
                        sql_data.append(i)
            except Exception as e:
                print (e)

        return (sql_data)

if __name__ == '__main__':
    a=k_alembicToDatabase()
    b = a.do('check')
    #b = a.do('upload')
    print (b)
