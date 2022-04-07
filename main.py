import os
os.system('python3 build.py cmds.json')
if input('execute file \033[32mout.py\033[0m? [Y/n] ').lower() != 'n':
  if os.path.isfile('out.py'):
    os.system('clear')
    os.system('python3 out.py')
  else: 
    print('error')
else: 
  print('ok')