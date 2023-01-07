
import os
import sys
import subprocess
import time
import traceback

import net_work

def maybe(callback):
  try:
    return callback()
  except:
    return traceback.format_exc()

def run_server(args: list):
  # remove args until we hit the first one beginning with '-'
  while len(args) > 0 and not args[0].startswith('-'):
    args.pop(0)
  # Now turn args (which we assume to be like ['-req', '/path/to/a/dir', '-return', '/path/to/another/dir',])
  # into a dictionary
  args_d = {}
  for arg_flag, arg_value in zip(args[0::2], args[1::2]):
    arg_flag = arg_flag.replace('-', '') # --req and -req both turn into "req" in our argument dictionary.
    args_d[arg_flag] = arg_value

  work_req_dir = args_d['req']
  work_return_dir = work_req_dir
  if 'return' in args_d:
    work_return_dir = args_d['return']

  # TODO parse all other arguments

  nw = net_work.NetWork(work_req_dir, work_return_dir)
  # Poll for incoming work, run, return, etc.
  files_we_must_delete = []
  while True:
    if len(files_we_must_delete) > 0:
      try:
        for file_name in files_we_must_delete:
          net_work.NetWork.safe_del(file_name)
        files_we_must_delete = [] # clear list
      except:
        traceback.print_exc()
    
    try:
      work_d = nw.poll_any_work_req_dicts()
      
      files_we_must_delete.append(
        nw.work_req_file(work_d['job_id']),
      )
      files_we_must_delete.append(
        nw.work_lock_file(work_d['job_id']),
      )

      if 'cmd' in work_d:
        cmd_args = work_d['cmd']
        proc = subprocess.run(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        nw.write_work_return_file(work_d['job_id'], {
          'returncode': proc.returncode,
          'stdout': maybe(lambda: proc.stdout.decode()),
          'stderr': maybe(lambda: proc.stderr.decode()),
        })
        
      else:
        raise Exception(f'Unknown work dictionary={work_d}')
    except:
      traceback.print_exc()
      time.sleep(1)





