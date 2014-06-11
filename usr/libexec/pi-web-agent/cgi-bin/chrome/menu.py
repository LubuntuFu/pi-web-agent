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
        return ""
        '''
        Uses the Blueprint designer createList to pass its
        span and return an html representation of its view
        '''
        '''if self.nav:
            return createNavListWithDropdown(self.items)
        else:
            return createMenuList(self.items, self.span)
        '''
        
class DockMenu(Menu):

    def __init__(self, items, nav=False):
        Menu.__init__(self, items, nav)
        
    def __str__(self):
        return '''
        <div id="dock-container">
        <div id="dock">
		    <ul id="dock">
			    <li><span>Firwall</span><a href="http://android.com"><img id="dock-item" src="http://openiconlibrary.sourceforge.net/gallery2/open_icon_library-full/icons/png/128x128/apps/firewall.png"/></a></li>
			    <li><span>Update</span><a href="http://palm.com"><img src="http://openiconlibrary.sourceforge.net/gallery2/open_icon_library-full/icons/png/128x128/apps/system-software-update-3.png"/></a></li>
			    <li><span>Camera</span><a href="http://apple.com/iphone"><img src="http://openiconlibrary.sourceforge.net/gallery2/open_icon_library-full/icons/png/128x128/apps/cheese.png"/></a></li>
			    <li><span>Camera</span><a href="http://apple.com/iphone"><img src="http://openiconlibrary.sourceforge.net/gallery2/open_icon_library-full/icons/png/128x128/apps/mplayer.png"/></a></li>
			    <li><span>Package Management</span><a href="http://microsoft.com/windowsmobile"><img src="http://openiconlibrary.sourceforge.net/gallery2/open_icon_library-full/icons/png/128x128/apps/system-software-installer.png"/></a></li>
			    <li><span>Shutdown</span><a href="http://blackberry.com"><img src="http://openiconlibrary.sourceforge.net/gallery2/open_icon_library-full/icons/png/128x128/apps/system-shutdown-5.png"/></a></li>
		    </ul>
		    <div class="base"></div>
		    </div>
		</div>
	
	</div>
	
	<!-- compatibility -->
	<p id="ua-string" style="margin:2em 0; color:#ddd; font-style:italic; font-size:.8em"></p>
        '''        
