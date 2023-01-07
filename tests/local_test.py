
import os
import sys
import traceback
import multiprocessing
import time

try:
  import net_work
except:
  if not 'ModuleNotFoundError' in traceback.format_exc():
    traceback.print_exc()
  sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'
  )))
  import net_work

WORK_DIR = '/tmp/test_net_work_dir'

def run_server_via_python():
  net_work.run_server(['-req', WORK_DIR])

if __name__ == '__main__':
  # Spawn server in another process
  server_proc = multiprocessing.Process(target=run_server_via_python,args=())
  server_proc.start()

  try:
    nw = net_work.NetWork(WORK_DIR, fatal_timeout_s=5)

    # Submit work request (in this case we just run a shell command, simplest API so far)
    cmd_out_text = nw.run_cmd_sync([
      'sh', '-c', 'echo "This came from the server, $RANDOM!"'
    ])
    print(f'Work from server said: {cmd_out_text}')

  except:
    traceback.print_exc()

  print('Test complete!...')
  time.sleep(2)
  print('Stopping server...')
  server_proc.terminate()


