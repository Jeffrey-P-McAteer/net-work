
import os
import sys
import subprocess
import traceback

def install_twine():
  subprocess.run([
    sys.executable, *('-m pip install --user twine'.split())
  ])

def upload_to_pypi():
  dist_files = []
  for f in os.listdir('dist'):
    if len(f) > 3:
      dist_files.append(
        os.path.join('dist', f)
      )
  dist_files_s = " ".join(dist_files)
  print('Uploading {}'.format(dist_files_s))
  subprocess.run([
    sys.executable, *(f'-m twine upload -r pypi {dist_files_s}'.split())
  ])

def install_build_pkg():
  subprocess.run([
    sys.executable, *('-m pip install --user build'.split())
  ])

def perform_build():
  subprocess.run([
    sys.executable, *('-m build'.split())
  ])


if __name__ == '__main__':
  try:
    perform_build()
  except:
    install_build_pkg()
    perform_build()

  # We now have a dist/ directory with files to publish!
  try:
    import twine
  except:
    install_twine()

  upload_to_pypi()



