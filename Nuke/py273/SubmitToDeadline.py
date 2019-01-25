import os, sys
import nuke, nukescripts
def SubmitToDeadline():
    print "1111"
    stdout = None
    if os.path.exists( "/Applications/Deadline/Resources/bin/deadlinecommand" ):
        stdout = os.popen( "/Applications/Deadline/Resources/bin/deadlinecommand GetRepositoryRoot" )
    else:
        stdout = os.popen(" deadlinecommand GetRepositoryRoot" )
    root = stdout.read()
    # Need to strip off the last eol char, it wasn't a '\n'
    root = root[0:-1]
    # Houdini deals with \\ oddly so easier just to use /
    root = root.replace( "\\", "/" )

    submissionScriptLoc = root + "/submission/Nuke"
    if submissionScriptLoc not in sys.path:
        sys.path.append( submissionScriptLoc )

    # sys.path.append("\\\\192.168.80.102\\DeadlineRepository_VFX\\submission\\Nuke")
    sys.path.append("\\\\192.168.80.221\\DeadlineRepository\\submission\\Nuke")

    import SubmitNukeToDeadline
    SubmitNukeToDeadline.SubmitToDeadline( submissionScriptLoc )
