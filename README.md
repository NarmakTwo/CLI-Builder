# Cli Builder
Soon to be the best way to make a Command-Line Interface
<br><br><br>
## How to use
First things first download the `copycode` folder, then you can change cmds.json to your liking, here's an example:
```json
{
  "Name":"Hsab CLI",
  "GenerateHelp":true,
  "Startup":"import asciiphoyo (not real module)",
  "Cmds":[
    {
      "Name":"echo",
      "Usage":"echo [text]",
      "Dis":"Print a string to the shell",
      "Code":"print(' '.join(args))"
    },
    {
      "Name":"roll",
      "Usage":"roll",
      "Dis":"rickroll :)",
      "Code":"print(asciiphoyo(asciiphoyo.img('8527883465647365847654.rickroll')))"
    },
  ]
}
```
<br><br><br>
## **Heads Up**
**This program will make a new file named out.py.**

<br><br><br>
## **Required Files**
* **`build.py`**
* **`template.py`**
* **`cmds.json`**

If you would like to, you may delete `main.py` and `out.py`

