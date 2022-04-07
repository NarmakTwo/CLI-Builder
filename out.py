import random
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
    cmds = ['echo', 'cat', 'clear', 'fhack', 'help']
    cmds.append('exit')

    termName = 'TestCLI'

    try:
      if cmd == '':
          pass
      elif cmd not in cmds:
          print(f'{termName}: {cmd}: Command not found.')
      elif cmd == 'exit':
          break
      if cmd == 'echo':
          print(' '.join(args))
      if cmd == 'cat':
          print(open(args[0],'r').read())
      if cmd == 'clear':
          os.system('clear')
      if cmd == 'fhack':
          print(f'DIP: {random.randint(100,999)}.{random.randint(10,99)}.1.{random.randint(0,20)} PASSID: {random.randint(1,1000000)}')
      if cmd == 'help':
          print("echo [text]   -Print a string to the shell\ncat [file]   -Read a file line by line\nclear   -Refresh the terminal\nhack   -Refresh the terminal\n")
    except Exception as e:
      print(f'{termName}: {e.__class__.__name__}: {e}')