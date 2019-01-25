import os, sys, re

try:
	import ConfigParser
except:
	print( "Could not load ConfigParser module, sticky settings will not be loaded/saved" )

import nuke, nukescripts

dialog = None
deadlineCommand = None

class DeadlineDialog( nukescripts.PythonPanel ):
	pools = []
	groups = []
	
	def __init__( self, pools, groups ):
		nukescripts.PythonPanel.__init__( self, "Submit To Deadline", "com.thinkboxsoftware.software.deadlinedialog" )
		
		self.setMinimumSize( 600, 560 )
		
		##########################################################################################
		## Job Description
		##########################################################################################
		
		# Job Name
		self.jobName = nuke.String_Knob( "jobName", "Job Name" )
		self.addKnob( self.jobName )
		self.jobName.setValue( "Untitled" )
		
		# Comment
		self.comment = nuke.String_Knob( "comment", "Comment" )
		self.addKnob( self.comment )
		self.comment.setValue( "" )
		
		# Department
		self.department = nuke.String_Knob( "department", "Department" )
		self.addKnob( self.department )
		self.department.setValue( "" )
		
		# Separator
		self.separator1 = nuke.Text_Knob( "separator1", "" )
		self.addKnob( self.separator1 )
		
		##########################################################################################
		## Job Scheduling
		##########################################################################################
		
		# Pool
		self.pool = nuke.Enumeration_Knob( "pool", "Pool", pools )
		self.addKnob( self.pool )
		self.pool.setValue( "none" )
		
		# Group
		self.group = nuke.Enumeration_Knob( "group", "Group", groups )
		self.addKnob( self.group )
		self.group.setValue( "none" )
		
		# Priority
		self.priority = nuke.Int_Knob( "priority", "Priority" )
		self.addKnob( self.priority )
		self.priority.setValue( 50 )
		
		# Task Timeout
		self.taskTimeout = nuke.Int_Knob( "taskTimeout", "Task Timeout" )
		self.addKnob( self.taskTimeout )
		self.taskTimeout.setValue( 0 )
		
		# Auto Task Timeout
		self.autoTaskTimeout = nuke.Boolean_Knob( "autoTaskTimeout", "Enable Auto Task Timeout" )
		self.addKnob( self.autoTaskTimeout )
		self.autoTaskTimeout.setValue( False )
		
		# Concurrent Tasks
		self.concurrentTasks = nuke.Int_Knob( "concurrentTasks", "Concurrent Tasks" )
		self.addKnob( self.concurrentTasks )
		self.concurrentTasks.setValue( 1 )
		
		# Limit Concurrent Tasks
		self.limitConcurrentTasks = nuke.Boolean_Knob( "limitConcurrentTasks", "Limit Tasks To Slave's Task Limit" )
		self.addKnob( self.limitConcurrentTasks )
		self.limitConcurrentTasks.setValue( False )
		
		# Machine Limit
		# self.machineLimit = nuke.Int_Knob( "machineLimit", "Machine Limit")
		# self.addKnob( self.machineLimit )
		# self.machineLimit.setValue( 0 )

		self.machineLimit = nuke.Enumeration_Knob( "machineLimit", "Machine Limit",['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
		self.addKnob( self.machineLimit)
		self.machineLimit.setValue('10')
		
		# Machine List Is Blacklist
		self.isBlacklist = nuke.Boolean_Knob( "isBlacklist", "Machine List Is A Blacklist" )
		self.addKnob( self.isBlacklist )
		self.isBlacklist.setValue( False )
		
		# Machine List
		self.machineList = nuke.String_Knob( "machineList", "Machine List" )
		self.addKnob( self.machineList )
		self.machineList.setValue( "" )
		
		self.machineListButton = nuke.PyScript_Knob( "machineListButton", "Browse" )
		self.addKnob( self.machineListButton )
		
		# Limit Groups
		self.limitGroups = nuke.String_Knob( "limitGroups", "Limit Groups" )
		self.addKnob( self.limitGroups )
		self.limitGroups.setValue( "" )
		
		self.limitGroupsButton = nuke.PyScript_Knob( "limitGroupsButton", "Browse" )
		self.addKnob( self.limitGroupsButton )
		
		# Dependencies
		self.dependencies = nuke.String_Knob( "dependencies", "Dependencies" )
		self.addKnob( self.dependencies )
		self.dependencies.setValue( "" )
		
		self.dependenciesButton = nuke.PyScript_Knob( "dependenciesButton", "Browse" )
		self.addKnob( self.dependenciesButton )
		
		# On Complete
		self.onComplete = nuke.Enumeration_Knob( "onComplete", "On Job Complete", ("Nothing", "Archive", "Delete") )
		self.addKnob( self.onComplete )
		self.onComplete.setValue( "Nothing" )
		
		# Submit Suspended
		self.submitSuspended = nuke.Boolean_Knob( "submitSuspended", "Submit Job As Suspended" )
		self.addKnob( self.submitSuspended )
		self.submitSuspended.setValue( False )
		
		# Separator
		self.separator1 = nuke.Text_Knob( "separator1", "" )
		self.addKnob( self.separator1 )
		
		##########################################################################################
		## Nuke Options
		##########################################################################################
		
		# Frame List
		self.frameList = nuke.String_Knob( "frameList", "Frame List" )
		self.addKnob( self.frameList )
		self.frameList.setValue( "" )
		
		# Chunk Size
		self.chunkSize = nuke.Int_Knob( "chunkSize", "Frames Per Task" )
		self.addKnob( self.chunkSize )
		self.chunkSize.setValue( 1 )
		
		# Separate Jobs
		self.separateJobs = nuke.Boolean_Knob( "separateJobs", "Submit Each Write Node As A Separate Job" )
		self.addKnob( self.separateJobs )
		self.separateJobs.setValue( False )
		
		# Threads
		self.threads = nuke.Int_Knob( "threads", "Render Threads" )
		self.addKnob( self.threads )
		self.threads.setValue( 0 )
		
		# Only Submit Selected Nodes
		self.selectedOnly = nuke.Boolean_Knob( "selectedOnly", "Only Submit Write Nodes That Are Selected" )
		self.addKnob( self.selectedOnly )
		self.selectedOnly.setValue( False )
		self.selectedOnly.setEnabled( self.separateJobs.value() )
		
		# Memory Usage
		self.memoryUsage = nuke.Int_Knob( "memoryUsage", "Maximum RAM Usage" )
		self.addKnob( self.memoryUsage )
		self.memoryUsage.setValue( 0 )
		
		# Only Submit Read File Nodes
		self.readFileOnly = nuke.Boolean_Knob( "readFileOnly", "Only Submit Write Nodes That Have 'Read File' Enabled" )
		self.addKnob( self.readFileOnly )
		self.readFileOnly.setValue( False )
		self.readFileOnly.setEnabled( self.separateJobs.value() )
		
		# Build
		self.build = nuke.Enumeration_Knob( "build", "Build To Force", ("None", "32bit", "64bit") )
		self.addKnob( self.build )
		self.build.setValue( "None" )
		
		# NukeX
		self.useNukeX = nuke.Boolean_Knob( "useNukeX", "Render With NukeX" )
		self.addKnob( self.useNukeX )
		self.useNukeX.setValue( False )
		
		# Submit Scene
		self.submitScene = nuke.Boolean_Knob( "submitScene", "Submit Nuke Script File With Job" )
		self.addKnob( self.submitScene )
		self.submitScene.setValue( False )
		
		# Separator
		self.separator1 = nuke.Text_Knob( "separator1", "" )
		self.addKnob( self.separator1 )
	
	def knobChanged( self, knob ):
		
		if knob == self.machineListButton:
			GetMachineListFromDeadline()
			
		if knob == self.limitGroupsButton:
			GetLimitGroupsFromDeadline()
		
		if knob == self.dependenciesButton:
			GetDependenciesFromDeadline()
		
		if knob == self.separateJobs:
			self.readFileOnly.setEnabled( self.separateJobs.value() )
			self.selectedOnly.setEnabled( self.separateJobs.value() )
	
	def ShowDialog( self ):
		return nukescripts.PythonPanel.showModalDialog( self )

def GetMachineListFromDeadline():
	global dialog
	global deadlineCommand
	
	# Get the limit groups.
	try:
		stdout = os.popen( deadlineCommand + " -selectmachinelist " + dialog.machineList.value() )
		newMachineList = stdout.read()
		stdout.close()
		dialog.machineList.setValue( newMachineList.replace( "\r", "" ).replace( "\n", "" ) )
	except IOError:
		pass

def GetLimitGroupsFromDeadline():
	global dialog
	global deadlineCommand
	
	# Get the limit groups.
	try:
		stdout = os.popen( deadlineCommand + " -selectlimitgroups " + dialog.limitGroups.value() )
		newLimitGroups = stdout.read()
		stdout.close()
		dialog.limitGroups.setValue( newLimitGroups.replace( "\r", "" ).replace( "\n", "" ) )
	except IOError:
		pass

def GetDependenciesFromDeadline():
	global dialog
	global deadlineCommand
	
	# Get the dependencies
	try:
		stdout = os.popen( deadlineCommand + " -selectdependencies " + dialog.dependencies.value() )
		newDependencies = stdout.read()
		stdout.close()
		dialog.dependencies.setValue( newDependencies.replace( "\r", "" ).replace( "\n", "" ) )
	except IOError:
		pass

# Checks if path is local (c, d, or e drive).
def IsPathLocal( path ):
	lowerPath = path.lower()
	if lowerPath.startswith( "c:" ) or lowerPath.startswith( "d:" ) or lowerPath.startswith( "e:" ):
		return True
	return False

# Checks if the given filename ends with a movie extension
def IsMovie( path ):
	lowerPath = path.lower()
	if lowerPath.endswith( ".mov" ):
		return True
	return False

# Checks if the filename is padded (ie: \\output\path\filename_%04.tga).
def IsPadded( path ):
	paddingRe = re.compile( "%([0-9]+)d", re.IGNORECASE )
	if paddingRe.search( path ) != None:
		return True
	elif path.find( "#" ) > -1:
		return True
	return False

# Parses through the filename looking for the first padded pattern, replaces
# it with the correct number of #'s, and returns the new padded filename.
def GetPaddedPath( path ):
	paddingRe = re.compile( "%([0-9]+)d", re.IGNORECASE )
	
	paddingMatch = paddingRe.search( path )
	if paddingMatch != None:
		paddingSize = int(paddingMatch.group(1))
		
		padding = ""
		while len(padding) < paddingSize:
			padding = padding + "#"
		
		path = paddingRe.sub( padding, path, 1 )
		
	return path

def WriteStickySettings( dialog, configFile ):
	try:
		config = ConfigParser.ConfigParser()
		config.add_section( "Sticky" )
		
		config.set( "Sticky", "Department", dialog.department.value() )
		config.set( "Sticky", "Pool", dialog.pool.value() )
		config.set( "Sticky", "Group", dialog.group.value() )
		config.set( "Sticky", "Priority", str( dialog.priority.value() ) )
		config.set( "Sticky", "MachineLimit", str( dialog.machineLimit.value() ) )
		config.set( "Sticky", "IsBlacklist", str( dialog.isBlacklist.value() ) )
		config.set( "Sticky", "MachineList", dialog.machineList.value() )
		config.set( "Sticky", "LimitGroups", dialog.limitGroups.value() )
		config.set( "Sticky", "SubmitSuspended", str( dialog.submitSuspended.value() ) )
		config.set( "Sticky", "ChunkSize", str( dialog.chunkSize.value() ) )
		config.set( "Sticky", "Threads", str( dialog.threads.value() ) )
		config.set( "Sticky", "SubmitScene", str( dialog.submitScene.value() ) )
		
		fileHandle = open( configFile, "w" )
		config.write( fileHandle )
		fileHandle.close()
	except:
		print( "Could not write sticky settings" )

def SubmitJob( dialog, root, node, writeNodes, deadlineCommand, deadlineTemp, tempJobName, tempFrameList, tempChunkSize  ):
	# Create the submission info file
	jobInfoFile = deadlineTemp + "/nuke_submit_info.job"
	fileHandle = open( jobInfoFile, "w" )
	fileHandle.write( "Plugin=Nuke\n" )
	fileHandle.write( "Name=%s\n" % tempJobName )
	fileHandle.write( "Comment=%s\n" % dialog.comment.value() )
	fileHandle.write( "Department=%s\n" % dialog.department.value() )
	fileHandle.write( "Pool=%s\n" % dialog.pool.value() )
	fileHandle.write( "Group=%s\n" % dialog.group.value() )
	fileHandle.write( "Priority=%s\n" % dialog.priority.value() )
	fileHandle.write( "MachineLimit=%s\n" % dialog.taskTimeout.value() )
	fileHandle.write( "TaskTimeoutMinutes=%s\n" % dialog.taskTimeout.value() )
	fileHandle.write( "EnableAutoTimeout=%s\n" % dialog.autoTaskTimeout.value() )
	fileHandle.write( "ConcurrentTasks=%s\n" % dialog.concurrentTasks.value() )
	fileHandle.write( "LimitConcurrentTasksToNumberOfCpus=%s\n" % dialog.limitConcurrentTasks.value() )
	fileHandle.write( "LimitGroups=%s\n" % dialog.limitGroups.value() )
	fileHandle.write( "JobDependencies=%s\n" % dialog.dependencies.value() )
	fileHandle.write( "OnJobComplete=%s\n" % dialog.onComplete.value() )
	fileHandle.write( "Frames=%s\n" % tempFrameList )
	fileHandle.write( "ChunkSize=%s\n" % tempChunkSize )
	
	if dialog.submitSuspended.value():
		fileHandle.write( "InitialStatus=Suspended\n" )
	
	if dialog.isBlacklist.value():
		fileHandle.write( "Blacklist=%s\n" % dialog.machineList.value() )
	else:
		fileHandle.write( "Whitelist=%s\n" % dialog.machineList.value() )
	
	if not dialog.separateJobs.value():
		index = 0
		for tempNode in writeNodes:
			if not tempNode.knob( 'disable' ).value():
				paddedPath = GetPaddedPath( tempNode.knob( 'file' ).value() )
				fileHandle.write( "OutputFilename%s=%s\n" % (index, paddedPath ) )
				index = index + 1
	else:
		paddedPath = GetPaddedPath( node.knob( 'file' ).value() )
		fileHandle.write( "OutputFilename0=%s\n" % paddedPath )
	
	fileHandle.close()
	
	# Create the plugin info file
	pluginInfoFile = deadlineTemp + "/nuke_plugin_info.job"
	fileHandle = open( pluginInfoFile, "w" )
	if not dialog.submitScene.value():
		fileHandle.write( "SceneFile=%s\n" % root.name() )
	
	fileHandle.write( "Version=%s\n" % nuke.env[ 'NukeVersionMajor' ] )
	fileHandle.write( "Threads=%s\n" % dialog.threads.value() )
	fileHandle.write( "RamUse=%s\n" % dialog.memoryUsage.value() )
	fileHandle.write( "Build=%s\n" % dialog.build.value() )
	
	if dialog.separateJobs.value():
		fileHandle.write( "WriteNode=%s\n" % node.name() )
	
	fileHandle.write( "NukeX=%s\n" % dialog.useNukeX.value() )
	
	fileHandle.close()
			
	# Submit the job to Deadline
	args = "\"" + jobInfoFile + "\" \"" + pluginInfoFile + "\""
	if dialog.submitScene.value():
		args += " \"" + root.name() + "\""
	
	tempResults = ""
	try:
		stdout = os.popen( deadlineCommand + " " + args )
		tempResults = stdout.read()
		stdout.close()
	except IOError:
		tempResults = "An error occurred while submitting the job \"" + tempJobName + "\" to Deadline. Please try again, or if this is a persistent problem, contact Deadline Support."
	
	return tempResults

# The main submission function.
def SubmitToDeadline( nukeScriptPath ):
	global dialog
	global deadlineCommand
	
	# Add the current nuke script path to the system path.
	sys.path.append( nukeScriptPath )
	
	# DeadlineGlobals contains initial values for the submission dialog. These can be modified
	# by an external sanity scheck script.
	import DeadlineGlobals
	
	# Get the root node.
	root = nuke.Root()
	
	# If the Nuke script hasn't been saved, its name will be 'Root' instead of the file name.
	if root.name() == "Root":
		nuke.message( "The Nuke script must be saved before it can be submitted to Deadline." )
		return
	
	# Check if proxy mode is enabled, and warn the user.
	if root.proxy():
		answer = nuke.ask( "Proxy Mode is enabled, which may cause problems when rendering through Deadline. Do you wish to continue?" )
		if not answer:
			return
	
	# If the Nuke script has been modified, then save it.
	if root.modified():
		nuke.scriptSave( root.name() )
	
	# Get the deadlinecommand executable (we try to use the full path on OSX).
	deadlineCommand = "deadlinecommand"
	if os.path.exists( "/Applications/Deadline/Resources/bin/deadlinecommand" ):
		print( "Using full deadline command path" )
		deadlineCommand = "/Applications/Deadline/Resources/bin/deadlinecommand"
	
	# Get the current user Deadline home directory, which we'll use to store settings and temp files.
	deadlineHome = ""
	try:
		stdout = os.popen( deadlineCommand + " -GetCurrentUserHomeDirectory" )
		#deadlineHome = stdout.readline()
		deadlineHome = stdout.read()
		stdout.close()
	except IOError:
		nuke.message( "An error occurred while collecting the user's home directory from Deadline. Please try again, or if this is a persistent problem, contact Deadline Support." )
		return
	
	deadlineHome = deadlineHome.replace( "\n", "" )
	deadlineSettings = deadlineHome + "/settings"
	deadlineTemp = deadlineHome + "/temp"
	
	# Get the pools.
	pools = []
	try:
		stdout = os.popen( deadlineCommand + " -pools" )
		#for line in stdout:
		#	pools.append( line.replace( "\n", "" ) )
		
		output = stdout.read()
		for line in output.splitlines():
			pools.append( line.replace( "\n", "" ) )
		
		stdout.close()
	except IOError:
		nuke.message( "An error occurred while collecting the pools from Deadline. Please try again, or if this is a persistent problem, contact Deadline Support." )
		return
	
	# Get the groups.
	groups = []
	try:
		stdout = os.popen( deadlineCommand + " -groups" )
		
		#for line in stdout:
		#	groups.append( line.replace( "\n", "" ) )
		
		output = stdout.read()
		for line in output.splitlines():
			groups.append( line.replace( "\n", "" ) )
		
		stdout.close()
	except IOError:
		nuke.message( "An error occurred while collecting the groups from Deadline. Please try again, or if this is a persistent problem, contact Deadline Support." )
		return
	
	# Set initial settings for submission dialog.
	DeadlineGlobals.initJobName = os.path.basename( nuke.Root().name() )
	DeadlineGlobals.initComment = ""
	
	startFrame = nuke.Root().firstFrame()
	endFrame = nuke.Root().lastFrame()
	if startFrame == endFrame:
		DeadlineGlobals.initFrameList = str(startFrame)
	else:
		DeadlineGlobals.initFrameList = str(startFrame) + "-" + str(endFrame)
	
	DeadlineGlobals.initDepartment = ""
	DeadlineGlobals.initPool = "none"
	DeadlineGlobals.initGroup = "none"
	DeadlineGlobals.initPriority = 50
	DeadlineGlobals.initTaskTimeout = 0
	DeadlineGlobals.initAutoTaskTimeout = False
	DeadlineGlobals.initConcurrentTasks = 1
	DeadlineGlobals.initLimitConcurrentTasks = True
	#DeadlineGlobals.initMachineLimit = 0
	DeadlineGlobals.initMachineLimit = '10'
	DeadlineGlobals.initIsBlacklist = False
	DeadlineGlobals.initMachineList = ""
	DeadlineGlobals.initLimitGroups = ""
	DeadlineGlobals.initDependencies = ""
	DeadlineGlobals.initOnComplete = "Nothing"
	DeadlineGlobals.initSubmitSuspended = False
	DeadlineGlobals.initChunkSize = 1
	DeadlineGlobals.initThreads = 0
	DeadlineGlobals.initMemoryUsage = 0
	
	DeadlineGlobals.initBuild = "32bit"
	if nuke.env[ '64bit' ]:
		DeadlineGlobals.initBuild = "64bit"
	
	DeadlineGlobals.initSeparateJobs = False
	DeadlineGlobals.initReadFileOnly = False
	DeadlineGlobals.initSelectedOnly = False
	DeadlineGlobals.initSubmitScene = False
	
	DeadlineGlobals.initUseNukeX = False
	if nuke.env[ 'nukex' ]:
		DeadlineGlobals.initUseNukeX = True
	
	# Read In Sticky Settings
	configFile = deadlineSettings + "/nuke_py_submission.ini"
	try:
		if os.path.isfile( configFile ):
			config = ConfigParser.ConfigParser()
			config.read( configFile )
			
			if config.has_section( "Sticky" ):
				if config.has_option( "Sticky", "Department" ):
					DeadlineGlobals.initDepartment = config.get( "Sticky", "Department" )
				if config.has_option( "Sticky", "Pool" ):
					DeadlineGlobals.initPool = config.get( "Sticky", "Pool" )
				if config.has_option( "Sticky", "Group" ):
					DeadlineGlobals.initGroup = config.get( "Sticky", "Group" )
				if config.has_option( "Sticky", "Priority" ):
					DeadlineGlobals.initPriority = config.getint( "Sticky", "Priority" )
				if config.has_option( "Sticky", "MachineLimit" ):
					DeadlineGlobals.initMachineLimit = config.getint( "Sticky", "MachineLimit" )
				if config.has_option( "Sticky", "IsBlacklist" ):
					DeadlineGlobals.initIsBlacklist = config.getboolean( "Sticky", "IsBlacklist" )
				if config.has_option( "Sticky", "MachineList" ):
					DeadlineGlobals.initMachineList = config.get( "Sticky", "MachineList" )
				if config.has_option( "Sticky", "LimitGroups" ):
					DeadlineGlobals.initLimitGroups = config.get( "Sticky", "LimitGroups" )
				if config.has_option( "Sticky", "SubmitSuspended" ):
					DeadlineGlobals.initSubmitSuspended = config.getboolean( "Sticky", "SubmitSuspended" )
				if config.has_option( "Sticky", "ChunkSize" ):
					DeadlineGlobals.initChunkSize = config.getint( "Sticky", "ChunkSize" )
				if config.has_option( "Sticky", "Threads" ):
					DeadlineGlobals.initThreads = config.getint( "Sticky", "Threads" )
				
				if config.has_option( "Sticky", "SubmitScene" ):
					DeadlineGlobals.initSubmitScene = config.getboolean( "Sticky", "SubmitScene" )
	except:
		print( "Could not read sticky settings" )
	
	# Run the sanity check script if it exists, which can be used to set some initial values.
	sanityCheckFile = nukeScriptPath + "/CustomSanityChecks.py"
	if os.path.isfile( sanityCheckFile ):
		print( "Running sanity check script: " + sanityCheckFile )
		try:
			import CustomSanityChecks
			sanityResult = CustomSanityChecks.RunSanityCheck()
			if not sanityResult:
				print( "Sanity check returned false, exiting" )
				return
		except:
			print( "Could not run CustomSanityChecks.py script" )
	
	# Check for potential issues and warn user about any that are found.
	warningMessages = ""
	writeNodes = nuke.allNodes( "Write" )
	
	# AltWriteNodes also contains any Writes that are embedded in groups. This is used just for the write nodes warning.
	altWriteNodes = []
	for node in nuke.allNodes():
		if node.Class() == "Write":
			altWriteNodes.append( node )
		elif node.Class() == "Group":
			for groupNode in nuke.allNodes( "Write", node ):
				altWriteNodes.append( groupNode )
	
	# Warn if there are no write nodes.
	outputCount = 0
	for node in altWriteNodes:
		if not node.knob( 'disable' ).value():
			outputCount = outputCount + 1
	
	if outputCount == 0:
		warningMessages = warningMessages + "No enabled write nodes were detected\n\n"
	
	# Check all the output filenames if they are local or not padded (non-movie files only).
	for node in writeNodes:
		if not node.knob( 'disable' ).value():
			filename = node.knob( 'file' ).value()
			if filename == "":
				warningMessages = warningMessages + "No output path for write node '" + node.name() + "' is defined\n\n"
			else:
				if IsPathLocal( filename ):
					warningMessages = warningMessages + "Output path for write node '" + node.name() + "' is local:\n" + filename + "\n\n"
				if not IsMovie( filename ) and not IsPadded( filename ):
					warningMessages = warningMessages + "Output path for write node '" + node.name() + "' is not padded:\n" + filename + "\n\n"
	
	# If there are any warning messages, show them to the user.
	if warningMessages != "":
		warningMessages = warningMessages + "Do you still wish to submit this job to Deadline?"
		answer = nuke.ask( warningMessages )
		if not answer:
			return
	
	# Create an instance of the submission dialog.
	dialog = DeadlineDialog( pools, groups )
	
	# Set the initial values.
	dialog.jobName.setValue( DeadlineGlobals.initJobName )
	dialog.comment.setValue( DeadlineGlobals.initComment )
	dialog.department.setValue( DeadlineGlobals.initDepartment )
	
	dialog.pool.setValue( DeadlineGlobals.initPool )
	dialog.group.setValue( DeadlineGlobals.initGroup )
	dialog.priority.setValue( DeadlineGlobals.initPriority )
	dialog.taskTimeout.setValue( DeadlineGlobals.initTaskTimeout )
	dialog.autoTaskTimeout.setValue( DeadlineGlobals.initAutoTaskTimeout )
	dialog.concurrentTasks.setValue( DeadlineGlobals.initConcurrentTasks )
	dialog.limitConcurrentTasks.setValue( DeadlineGlobals.initLimitConcurrentTasks )
	dialog.machineLimit.setValue( DeadlineGlobals.initMachineLimit )
	# dialog.machineLimit.setValue('10')
	dialog.isBlacklist.setValue( DeadlineGlobals.initIsBlacklist )
	dialog.machineList.setValue( DeadlineGlobals.initMachineList )
	dialog.limitGroups.setValue( DeadlineGlobals.initLimitGroups )
	dialog.dependencies.setValue( DeadlineGlobals.initDependencies )
	dialog.onComplete.setValue( DeadlineGlobals.initOnComplete )
	dialog.submitSuspended.setValue( DeadlineGlobals.initSubmitSuspended )
	
	dialog.frameList.setValue( DeadlineGlobals.initFrameList )
	dialog.chunkSize.setValue( DeadlineGlobals.initChunkSize )
	dialog.threads.setValue( DeadlineGlobals.initThreads )
	dialog.memoryUsage.setValue( DeadlineGlobals.initMemoryUsage )
	dialog.build.setValue( DeadlineGlobals.initBuild )
	dialog.separateJobs.setValue( DeadlineGlobals.initSeparateJobs )
	dialog.readFileOnly.setValue( DeadlineGlobals.initReadFileOnly )
	dialog.selectedOnly.setValue( DeadlineGlobals.initSelectedOnly )
	dialog.submitScene.setValue( DeadlineGlobals.initSubmitScene )
	dialog.useNukeX.setValue( DeadlineGlobals.initUseNukeX )
	
	dialog.separateJobs.setEnabled( len( writeNodes ) > 0 )
	
	# Show the dialog.
	success = False
	while not success:
		success = dialog.ShowDialog()
		if not success:
			WriteStickySettings( dialog, configFile )
			return
		
		errorMessages = ""
		warningMessages = ""
		
		# Check that frame range is valid.
		if dialog.frameList.value().strip() == "":
			errorMessages = errorMessages + "No frame list has been specified.\n\n"
		
		# If submitting separate write nodes, make sure there are jobs to submit
		if dialog.separateJobs.value():
			validNodeFound = False
			for node in writeNodes:
				if not node.knob( 'disable' ).value():
					validNodeFound = True
					if dialog.readFileOnly.value() and not node.knob( 'reading' ).value():
						validNodeFound = False
					if dialog.selectedOnly.value() and not node.isSelected():
						validNodeFound = False
					
					if validNodeFound:
						break
					
			if not validNodeFound:
				if dialog.readFileOnly.value() and dialog.selectedOnly.value():
					errorMessages = errorMessages + "There are no selected write nodes with 'Read File' enabled, so there are no jobs to submit.\n\n"
				elif dialog.readFileOnly.value():
					errorMessages = errorMessages + "There are no write nodes with 'Read File' enabled, so there are no jobs to submit.\n\n"
				elif dialog.selectedOnly.value():
					errorMessages = errorMessages + "There are no selected write nodes, so there are no jobs to submit.\n\n"
		
		# Check if the script file is local and not being submitted to Deadline.
		if not dialog.submitScene.value():
			if IsPathLocal( root.name() ):
				warningMessages = warningMessages + "Nuke script path is local and is not being submitted to Deadline:\n" + root.name() + "\n\n"
		
		# Alert the user of any errors.
		if errorMessages != "":
			errorMessages = errorMessages + "Please fix these issues and submit again."
			nuke.message( errorMessages )
			success = False
		
		# Alert the user of any warnings.
		if success and warningMessages != "":
			warningMessages = warningMessages + "Do you still wish to submit this job to Deadline?"
			answer = nuke.ask( warningMessages )
			if not answer:
				WriteStickySettings( dialog, configFile )
				return
	
	# Save sticky settings
	WriteStickySettings( dialog, configFile )
	
	# Check if we should be submitting a separate job for each write node.
	resultsString = ""
	tempJobName = dialog.jobName.value()
	tempFrameList = dialog.frameList.value().strip()
	tempChunkSize = dialog.chunkSize.value()
	if not dialog.separateJobs.value():
		for tempNode in writeNodes:
			if not tempNode.knob( 'disable' ).value():
				if IsMovie( tempNode.knob( 'file' ).value() ):
					tempChunkSize = 1000000
					break
		
		resultsString = SubmitJob( dialog, root, None, writeNodes, deadlineCommand, deadlineTemp, tempJobName, tempFrameList, tempChunkSize )
	else:
		for node in writeNodes:
			# Check if we should enter the loop for this node.
			enterLoop = False
			if not node.knob( 'disable' ).value():
				enterLoop = True
				if dialog.readFileOnly.value():
					enterLoop = enterLoop and node.knob( 'reading' ).value()
				if dialog.selectedOnly.value():
					enterLoop = enterLoop and node.isSelected()
			
			if enterLoop:
				tempJobName = tempJobName + " - " + node.name()
				
				# Check if the write node is overriding the frame range
				if node.knob( 'use_limit' ).value():
					tempFrameList = str(int(node.knob('first').value())) + "-" + str(int(node.knob('last').value()))
				
				if IsMovie( node.knob( 'file' ).value() ):
					tempChunkSize = 1000000
				
				tempResults = SubmitJob( dialog, root, node, writeNodes, deadlineCommand, deadlineTemp, tempJobName, tempFrameList, tempChunkSize )
				resultsString = resultsString + tempResults + "\n\n"
	
	nuke.message( resultsString.rstrip( "\n" ) )

################################################################################
## DEBUGGING
################################################################################
#~ # Get the repository root
#~ try:
	#~ stdout = None
	#~ if os.path.exists( "/Applications/Deadline/Resources/bin/deadlinecommand" ):
		#~ stdout = os.popen( "/Applications/Deadline/Resources/bin/deadlinecommand GetRepositoryRoot" )
	#~ else:
		#~ stdout = os.popen(" deadlinecommand GetRepositoryRoot" )
	#~ path = stdout.read()
	#~ stdout.close()
	
	#~ if path == "" or path == None:
		#~ nuke.message( "The SubmitNukeToDeadline.py script could not be found in the Deadline Repository. Please make sure that the Deadline Client has been installed on this machine, that the Deadline Client bin folder is in your PATH, and that the Deadline Client has been configured to point to a valid Repository." )
	#~ else:
		#~ path += "/submission/Nuke"
		#~ path = path.replace("\n","").replace( "\\", "/" )
		
		#~ # Add the path to the system path
		#~ print( "Appending \"" + path + "\" to system path to import SubmitNukeToDeadline module" )
		#~ sys.path.append( path )
		
		#~ # Call the main function to begin job submission.
		#~ SubmitToDeadline( path )
#~ except IOError:
	#~ nuke.message( "An error occurred while getting the repository root from Deadline. Please try again, or if this is a persistent problem, contact Deadline Support." )
	