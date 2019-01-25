# *-* coding: utf-8 *-*

import nuke, re, os, nukescripts.utils
import pyseq

class OCT_Bulk_Samples_Conversion():
	def __init__(self):
		#要转换的Read节点
		self.myReads=[]
		#{Read节点格式的:素材的宽，高}
		self.myOrangeDict={}
		#{Con与素材连接的类型:[ContactSheet节点类型,[素材节点]]}
		self.myContactReadDict = {}
		self.warning=[]

	#获取nuke中转换素材的节点
	def GetReadNodeAndContactSheet(self):
		self.myReads=nuke.selectedNodes('Read')
		if len(self.myReads)==0:
			self.myReads=nuke.allNodes('Read')
		if not len(self.myReads):
			nuke.message('no Read file ')
			return

		allContactSheet=nuke.allNodes('ContactSheet')
		for Contact in allContactSheet:
			#ContactSheet连接最后一个的节点
			num=Contact.inputs()
			for i in range(num):
				ContactConnNode=Contact.input(i)
				if ContactConnNode in self.myReads:
					if Contact not in self.myContactReadDict.keys():
						self.myContactReadDict.update({Contact: [ContactConnNode]})
					else:
						self.myContactReadDict[Contact].append(ContactConnNode)
				else:
					continue
		#print self.myContactReadDict
		self.ReplaceFilePathUI()

	def invertpath(self,pathname=''):
		pathname=pathname.replace('\\','/')
		if pathname[-1]!='/':
			pathname+='/'
		return pathname

	#转换路径的界面
	def ReplaceFilePathUI(self):
		a = nukescripts.PythonPanel('ReplaceFileRootPath')
		a.addKnob(nuke.File_Knob('OldRootPath:'))
		a.addKnob(nuke.File_Knob('NewRootPath:'))
		reslut = a.showModalDialog()
		if reslut:
			oldfilepath = a.knobs()['OldRootPath:'].getValue()
			newfilepath = a.knobs()['NewRootPath:'].getValue()
			if len(oldfilepath) and len(newfilepath):
				oldfilepath = self.invertpath(oldfilepath)
				newfilepath = self.invertpath(newfilepath)
				self.Bulk_Samples_Conversion(oldfilepath,newfilepath)
			else:
				nuke.message('!!!no something path in OldRootPath:and NewRootPath:!!!')
				return

	def Bulk_Samples_Conversion(self,oldfilepath,newfilepath):
		#print oldfilepath
		#print newfilepath
		j=1
		#print self.myContactReadDict
		for mykey in self.myContactReadDict.keys():
			for myRead in self.myContactReadDict[mykey]:
				self.myReads.remove(myRead)
				readPath=myRead['file'].value()
				filePath = readPath.replace(oldfilepath, newfilepath)
				#print filePath
				readDir=os.path.split(filePath)[0]
				if not os.path.isdir(readDir):
					self.warning.append(myRead.name())
					continue
				Flag=True
				myRead['file'].setValue(filePath)
				formatW=myRead.width()
				formatH = myRead.height()
				#print formatH
				ReadOFormat = myRead['format'].value()
				#print ReadOFormat.width()
				if ReadOFormat.width() != formatW or ReadOFormat.height() != formatH:
					allFormat = nuke.formats()
					if self.myOrangeDict:
						for myOrange in self.myOrangeDict.keys():
							SazeW = self.myOrangeDict[myOrange].split(" ")[0]
							SazeH = self.myOrangeDict[myOrange].split(" ")[1]
							if SazeW == formatW and SazeH == formatH: 
								myRead['format'].setValue(myOrange) 
								Flag = False
								break
					if Flag:
						for eachFormat in allFormat:
							if eachFormat.width() == formatW and eachFormat.height() == formatH:
								#print eachFormat.width()
								#print formatW
								myFormat = eachFormat.name()
								print myFormat
								if myFormat != None:
									#print "sssss"
									myRead['format'].setValue(myFormat)
									Flag = False
									break
						if Flag:
						#键的名字
							while True:
								mySize = ('my_Size%s' % j)
								#print mySize
								if mySize not in [eachFormat.name() for eachFormat in allFormat]:
									break
								else:
									j += 1
							#print j
							widthHeight = str(formatW) + " " + str(formatH)
							self.myOrangeDict.update({mySize:widthHeight})
							square = widthHeight+" "+mySize
							nuke.addFormat(square)
							myRead['format'].setValue(mySize)

				frameOrange=pyseq.getSequences(readDir)
				for frames in frameOrange:
					myPath = frames.path()
					if os.path.isdir(myPath):
						continue
					else:
						if frames.tail():
							if frames.length()==1:
								myRead['origfirst'].setValue(1)
								myRead['origlast'].setValue(1)  
								myRead['first'].setValue(1)
								myRead['last'].setValue(1) 
							else:
								firstFrameName = frames[0]._get_filename()  
								lastFrameName = frames[-1]._get_filename()
								readFileStart=firstFrameName.split(".")[-2] 
								readFileLast=lastFrameName.split(".")[-2]
								myRead['origfirst'].setValue(int(readFileStart))  
								myRead['origlast'].setValue(int(readFileLast))  
								myRead['first'].setValue(int(readFileStart))
								myRead['last'].setValue(int(readFileLast))

			_w=self.myContactReadDict[mykey][0].knob('format').value().width()
			_h=self.myContactReadDict[mykey][0].knob('format').value().height()
			#print _w
			#print _h
			constRows=mykey['rows'].value()
			constColumns=mykey['columns'].value()
			#print constRows
			#print constColumns
			mykey['height'].setValue(constRows*_h)
			mykey['width'].setValue(constColumns*_w)

		if self.myReads:
			for myRead in self.myReads:
				readPath=myRead['file'].value()
				filePath = readPath.replace(oldfilepath, newfilepath)
				Flag=True
				readDir=os.path.split(filePath)[0]
				if not os.path.isdir(readDir):
					self.warning.append(myRead.name())
					continue
				myRead['file'].setValue(filePath)
				formatW=myRead.width()
				formatH = myRead.height()
				#print formatH
				ReadOFormat = myRead['format'].value()
				if ReadOFormat.width() != formatW or ReadOFormat.height() != formatH:
					allFormat = nuke.formats()
					if self.myOrangeDict:
						for myOrange in self.myOrangeDict.keys():
							SazeW = self.myOrangeDict[myOrange].split(" ")[0]
							SazeH = self.myOrangeDict[myOrange].split(" ")[1]
							if SazeW == formatW and SazeH == formatH: 
								myRead['format'].setValue(myOrange) 
								Flag = False
								break
					if Flag:
						for eachFormat in allFormat:
							if eachFormat.width() == formatW and eachFormat.height() == formatH:
								myFormat = eachFormat.name()
								if myFormat != None:
									myRead['format'].setValue(myFormat)
									Flag = False
									break
						if Flag:
						#键的名字
							while True:
								mySize = ('my_Size%s' % j)
								if mySize not in [eachFormat.name() for eachFormat in allFormat]:
									break
								else:
									j += 1
							widthHeight = str(formatW) + " " + str(formatH)
							self.myOrangeDict.update({mySize:widthHeight})
							square = widthHeight+" "+mySize
							nuke.addFormat(square)
							myRead['format'].setValue(mySize)

				frameOrange=pyseq.getSequences(readDir)
				for frames in frameOrange:
					myPath = frames.path()
					if os.path.isdir(myPath):
						continue
					else:
						if frames.tail():
							if frames.length()==1:
								myRead['origfirst'].setValue(1)
								myRead['origlast'].setValue(1)  
								myRead['first'].setValue(1)
								myRead['last'].setValue(1) 
							else:
								firstFrameName = frames[0]._get_filename()  
								lastFrameName = frames[-1]._get_filename()
								readFileStart=firstFrameName.split(".")[-2] 
								readFileLast=lastFrameName.split(".")[-2]
								myRead['origfirst'].setValue(int(readFileStart))  
								myRead['origlast'].setValue(int(readFileLast))  
								myRead['first'].setValue(int(readFileStart))
								myRead['last'].setValue(int(readFileLast))
		if self.warning:
			nuke.message(str(self.warning)+"\xe8\x8a\x82\xe7\x82\xb9\xe6\x96\xb0\xe8\xb7\xaf\xe5\x8a\xb2\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8")


#OCT_Bulk_Samples_Conversion().GetReadNodeAndContactSheet()
