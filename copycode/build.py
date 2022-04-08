def main():

  from sys import argv as args
  import json
  from time import sleep as wait


  cmds = json.loads(open(args[1]).read())
  cmds['manual'] = []
  cmdsL = []
  green = '\033[32m'
  reset = '\033[0m'

  def up(): print('\x1b[A',end='')

  def debug(): print(json.dumps(cmds, indent=4))

  def buildHelp():
    if cmds['GenerateHelp'] == True:
      out = ''
      for i in cmds['Cmds']:
        out += f'{i["Usage"]}   -{i["Dis"]}\\n'
      out += 'Type `help` or `?` to see this again.'

      add = {
        'Name':'help',
        'Usage':'help',
        'Dis':'Learn what a command does',
        'Code':f'print("{out}")'
      }
      
      cmds["Cmds"].append(add)

      add = {
        'Name':'?',
        'Usage':'?',
        'Dis':'Learn what a command does',
        'Code':f'print("{out}")'
      }
      
      cmds["Cmds"].append(add)

  def autoToManual():
    for i in cmds['Cmds']:
      print(f'Generating {i["Name"]} command')
      out = ''
      out += f"      if cmd == '{i['Name']}':\n          "
      out += i['Code']
      up()
      print(f'Generating {i["Name"]} command {green}[done]{reset}')

      print(f'Writing {i["Name"]} command')
      cmds['manual'].append(out)
      up()
      print(f'Writing {i["Name"]} command {green}[done]{reset}\n')


  def getCmds():
    for i in cmds['Cmds']:
      cmdsL.append(i['Name'])
  

  def write():
    man = cmds['manual']
    for i in man:
      pass
    rep = {
      'cmds = None # insert cmds':'cmds = '+str(cmdsL),
      'termName = None # insert $termName':'termName = '+f"'{cmds['Name']}'",
      '# $commands':'\n'.join(man),
      '# insert startup':cmds['Startup']
    }
    with open('template.py', 'r') as f:
      tempout = f.read()
      for key in rep:
        tempout = tempout.replace(key,rep[key])
    open('out.py', 'w').write(tempout)
    print(f'Saved as {green}out.py{reset}')
    wait(1)
      
  
  def build():
    print(f'Creating CLI from "{args[1]}"... ')
    wait(1)
    print('\n')

    buildHelp()
    autoToManual()
    getCmds()

    write()

  build()

if __name__ == '__main__':
  main()
