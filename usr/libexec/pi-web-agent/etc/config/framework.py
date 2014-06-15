import sys
import os
if 'MY_HOME' not in os.environ:
    os.environ['MY_HOME']='/usr/libexec/pi-web-agent'
sys.path.append(os.environ['MY_HOME']+'/etc/config')
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/chrome')
from pi_web_agent import Configuration
from view import DockView

config=Configuration()
view = DockView(config.system.actions, config.system.cmdactions)

def output(view, form):
    if "type" in form and form["type"].value == "js":
        view.js_output()
    else:
        view.output()

