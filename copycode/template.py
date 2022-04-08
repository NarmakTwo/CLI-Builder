# insert startup
import os

while True:
    username = os.environ.get("USERNAME")
    if username == None:
      username = os.environ.get("USER")
    prompt = f'\x1b[38;5;77m{username}@{os.uname().nodename}\x1b[0m:\x1b[38;5;62m{os.getcwd().replace(os.path.expanduser("~"), "~")}\x1b[0m$ '
    def inp():
      try:
        return input(prompt)
      except:
        print()
        return inp()
    fcmd = inp()
    args = fcmd.split(' ')[1:]
    cmd = fcmd.split(' ')[0]
    cmds = None # insert cmds
    cmds.append('exit')

    termName = None # insert $termName

    try:
      if cmd == '':
          pass
      elif cmd not in cmds:
          print(f'{termName}: {cmd}: Command not found.')
      elif cmd == 'exit':
          break
# $commands
    except Exception as e:
      print(f'{termName}: {e.__class__.__name__}: {e}')
