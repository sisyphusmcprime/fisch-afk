# fisch-afk
Have you ever wanted to grind on Fisch without setting up a goofy ahh autoclicker or fishing manually *(in the big 26?)* Well, **TOO BAD** cause this IS an autoclicker MWAHAHAHAHAHAHA

All jokes aside, this is a Python script that actively reads your instance of Roblox and adjusts for changes in the location of the fish, even going as far as to land **PERFECT!** catches every time -- essentially fishing as you would. Supported by Linux and macOS, for Windows users js get a better OS lil bro

## Install
As the code is currently in development, binary releases aren't available. However, if you want to you can execute a cloned repo with:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 main.py
```

Details on cloning a repo can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

Keep in mind that this code is **currently under development**, hence main.py may crash or even not work. 

## On OS Support
The code *should* work fine under Linux and macOS (other than the probably 10,000 bugs that I left in it) but Windows is a different beast altogether. Due to the way that Windows handles directories (with a `\`) and the loose support for it with PyWinCtl (what this program uses to access your Roblox window) the code probably won't work. Binary releases also aren't available due to this.

If you'd like, you can try solving the bugs and making a pull request, but unless I need it I'll probably not be adding Windows support. The code should work under something like WSL/Git Bash however.
