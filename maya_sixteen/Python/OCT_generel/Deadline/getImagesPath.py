from System.Collections.Specialized import *
from System.IO import *
from System.Text import *

from Deadline.Scripting import *
from Deadline.Jobs import *


def __main__():
   jobid = RepositoryUtils.GetJobIds()
   serverAddress = RepositoryUtils.GetRootDirectory() + '\n'

   count = 0
   activeStr = ''
   if len(jobid):
      for eachJob in jobid:
         try:
            job = RepositoryUtils.GetJob(eachJob,False)
         except:
            pass
         else:
            if job.JobStatus == 'Active':
            	print job.OutputDirectories
   else:
      print ''
