#coding:utf-8

import maya.cmds as mc
import os
import maya.mel as mm

class BatchRender_Tools():
	def __init__(self):
		self.mayaPath=os.getenv('MAYA_LOCATION')
		self.mayaPath=self.mayaPath+"\\bin\\Render.exe"
		self.mayaPath=self.mayaPath.replace("/","\\")

	def window_Reader(self):
		if mc.window("window_Reader",ex=True):
			mc.deleteUI("window_Reader")
		mc.window("window_Reader",title="window_Reader",sizeable=False)
		mc.rowColumnLayout(numberOfColumns=1)
		mc.frameLayout(u"添加要渲染的maya文件")
		mc.rowColumnLayout(numberOfColumns=2,cw=[(1,370),(2,185)])
		mc.rowColumnLayout(numberOfColumns=1)
		mc.textScrollList("the_mod_list",w=400,h=180,bgc=(0.3,0.3,0.3))
		mc.setParent( '..' ) 
		mc.rowColumnLayout(numberOfColumns=1)
		mc.text(label=u"选择渲染器")
		mc.rowColumnLayout(numberOfColumns=3,cw=[(1,50),(2,50),(3,50)])
		mc.text(label="")
		mc.text(label="")
		mc.text(label="")
		
		mc.checkBox("aronld",label="aronld",v=False)
		mc.text(label="")
		mc.text(label="")
		
		mc.checkBox("vray",label="vray",v=False)
		mc.text(label="")
		mc.text(label="")
		
		mc.checkBox("mr",label="mr",v=False)
		mc.text(label="")
		mc.text(label="")
		
		mc.text(label="")
		mc.text(label="")
		mc.text(label="")
		
		mc.setParent("..")
		mc.rowColumnLayout(numberOfColumns=2,cw=[(1,90),(2,90)])
		mc.button(label=u"载入文件",h=30,c=lambda*args:self.load_file())
		mc.button(label=u"清空列表",c=lambda*args:self.remove_file())
		
		mc.setParent( '..' ) 
		mc.setParent( '..' ) 
		mc.setParent( '..' ) 
		mc.setParent( '..' )
		
		mc.rowColumnLayout(numberOfColumns=4,cw=[(1,120),(2,100),(3,110),(4,100)]) 
		mc.text(label="")
		mc.button(label="OK",h=40,c=lambda*args:self.if_start())
		mc.text(label="")
		mc.button(label="Clase",h=40,c="mc.deleteUI('window_Reader',window=True)")
		mc.showWindow("window_Reader")
		
	def load_file(self):
		render_tool=""
		anrold_Tool= mc.checkBox("aronld",q=True,v=True)
		vray_Tool= mc.checkBox("vray",q=True,v=True)
		mr_Tool= mc.checkBox("mr",q=True,v=True)
		if anrold_Tool and mr_Tool:
			mc.confirmDialog(message=u"只能选择一个渲染器！")
		elif anrold_Tool and vray_Tool:
			mc.confirmDialog(message=u"只能选择一个渲染器！")
		elif vray_Tool and mr_Tool:
			mc.confirmDialog(message=u"只能选择一个渲染器！")
		elif anrold_Tool:
			render_tool="aronld"
		elif vray_Tool:
			render_tool="vray"
		elif mr_Tool:
			render_tool="mentalRay"
		else:
			mc.confirmDialog(message=u"请选择一个渲染器！")
		print render_tool

		getfiles=mc.fileDialog2(fileMode=1,fileFilter="Maya Binary(*.mb);;Maya ASCII(*.ma )",dialogStyle=2)
		getfile_Render=render_tool+" "+getfiles[0]
		mc.textScrollList("the_mod_list",e=True,append=getfile_Render)

	def remove_file(self):
		mc.textScrollList("the_mod_list",e=True,ra=True)

	def if_start(self):
		all_list_file = mc.textScrollList("the_mod_list",q=True,ai=True)
		print all_list_file

		if not os.path.isdir("D:\\Reader"):
			os.makedirs("D:\\Reader")

		if os.path.isfile("D:\\Reader\\render.bat"):
			os.remove("D:\\Reader\\render.bat")

		f=open("D:\\Reader\\render.txt","wt")
		for files in all_list_file:
			getfile_Renders=files.split(" ")
			render_tools=getfile_Renders[0]
			projs =("/".join(getfile_Renders[1].split("/")[0:-2])).replace("/","\\")
			image_save=projs+"\\images"
			if not os.path.isdir(image_save):
				os.makedirs(image_save)
			fi=getfile_Renders[1].replace("/","\\")
			print getfile_Renders[1]
			#写入文件的字符串

			strs="%s -r %s -proj %s -rd %s %s"%(self.mayaPath,render_tools,projs,image_save,fi)
			print strs
			f.write(strs+"\n")

		f.write("pause"+"\n")
		f.close()
		os.rename("D:\\Reader\\render.txt","D:\\Reader\\render.bat")
		os.system('D:\\Reader\\render.bat') 

#BatchRender_Tools().window_Reader()
