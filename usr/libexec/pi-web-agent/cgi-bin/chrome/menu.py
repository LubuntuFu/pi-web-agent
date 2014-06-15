import sys
import os
if 'MY_HOME' not in os.environ:
    os.environ['MY_HOME']='/usr/libexec/pi-web-agent'
sys.path.append(os.environ['MY_HOME']+'/cgi-bin')
from BlueprintDesigner import *	
class MenuItem(object):
    '''
    MenuItem is an item that has a name and a link.
    '''
    def __init__(self, name, link):
        self.name=name
        self.actionlink='javascript:navigate(\'' + link + '\')'
    
    def __str__(self):
        '''
        Returns an html representation of a MenuItem
        '''        
        return '<li><a href="' + self.actionlink + '">' + self.name + '</a></li>\n'



class DockMenuItem(MenuItem):
    
    def __init__(self, action_item):
        MenuItem.__init__(self, action_item["title"], action_item["url"])
        self.icon = action_item["icon"]
        if (self.icon == None or len(self.icon) == 0):
            self.icon = "applications-other-3.png"
        self.icon = "/icons/" + self.icon
        
    def __str__(self):
        return '''<li><span>''' + self.name + '''</span><a href="''' + self.actionlink + '''"><img id="dock-item" src=" ''' + self.icon + '''"/></a></li>'''




class Menu(object):
    '''
    Menu is a group of MenuItems
    '''
    def __init__(self, items, nav=False):
        self.items = items
        self.span='4 last'
        self.nav=nav
        
    def addItem(self, item):
        '''
        Add a menu item to the list
        '''
        self.items.append(item)
        
    def setSpan(self, span):
        '''
        Sets the span according the the
        Bluepring specification, on where this
        Menu will be placed
        '''
        self.span=str(span)

    def __str__(self):
        '''
        Uses the Blueprint designer createList to pass its
        span and return an html representation of its view
        '''
        if self.nav:
            return createNavListWithDropdown(self.items)
        else:
            return createMenuList(self.items, self.span)

        
class DockMenu(Menu):

    def __init__(self, actions):
        self.items = []
        for action in actions:
            action_obj = actions[action]
            self.items.append(DockMenuItem(action_obj))
                
    def __str__(self):
        div_container = '''
        <div id="dock-container">
        <div id="dock">
            <ul id="dock">'''
        
        for item in self.items:
            div_container += str(item)
            
        div_container += '''
            </ul>
            <div class="base"></div>
            </div>
        </div>

        </div>

        <!-- compatibility -->
        <p id="ua-string" style="margin:2em 0; color:#ddd; font-style:italic; font-size:.8em"></p>
        '''        
        return div_container
