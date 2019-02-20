from System.Collections.Specialized import *
from System.IO import *
from System.Text import *

from Deadline.Scripting import *
from Deadline.Jobs import *


def __main__():
   jobid = RepositoryUtils.GetJobIds()
   serverAddress = RepositoryUtils.GetRootDirectory() + '\n'
   
   print serverAddress
   count = 0
   activeStr = ''
   for eachJob in jobid:
      try:
         job = RepositoryUtils.GetJob(eachJob,False)
      except:
         pass
      else:
         if job.JobStatus == 'Active':
            activeStr += 'Name: ' + job.JobName + '\n'
            taskCount = job.JobTaskCount
            rendered = 0
            count += 1
            for eachTask in RepositoryUtils.GetJobTasks(job,False):
               if eachTask.TaskStatus == 'Completed':
                  rendered += 1
            
            activeStr += '\tTask: %d/%d\n' % (rendered, taskCount)
            activeStr += '\tFrames per Task: %d\n\n' % job.JobFramesPerTask
         
   activeJobCount = 'Active Jobs: %d\n' % count
   print activeJobCount
   print activeStr