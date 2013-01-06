import xbmcplugin
import xbmcgui
import xbmcaddon
import urllib2

def printInfo(info):
    print "####: " + info
    
def testLight():
    urllib2.urlopen("http://vera.lan:3480/data_request?id=lu_action&serviceId=urn:micasaverde-com:serviceId:HomeAutomationGateway1&action=RunScene&SceneNum=15")

def runVeraScene(sceneNum):
    verahost = __settings__.getSetting("verahost")
    veraport = __settings__.getSetting("veraport")
    url = "http://"+verahost+":"+veraport+"/data_request?id=lu_action&serviceId=urn:micasaverde-com:serviceId:HomeAutomationGateway1&action=RunScene&SceneNum="+sceneNum
    printInfo("opening URL: "+url)
    urllib2.urlopen(url)
      
class MyPlayer(xbmc.Player) :
    
    def __init__ (self):
        xbmc.Player.__init__(self)
 
    def onPlayBackStarted(self):
        if (VIDEO == 1):
            printInfo("Playback started")
            
    def onPlayBackEnded(self):
        if (VIDEO == 1):
            printInfo("Playback ended")
            
    def onPlayBackStopped(self):
        if (VIDEO == 1):
            printInfo("Playback stopped")
            
    def onPlayBackPaused(self):
        if (VIDEO == 1):
            printInfo("Playback paused")
            runVeraScene(__settings__.getSetting("pauseScene"))
            
    def onPlayBackResumed(self):
        if (VIDEO == 1):
            printInfo("Playback resumed")
            runVeraScene(__settings__.getSetting("unpauseScene"))
            
player = MyPlayer()
 
VIDEO = 0

__settings__ = xbmcaddon.Addon(id='script.movielights')

while(not xbmc.abortRequested):
    if xbmc.Player().isPlaying():
        if xbmc.Player().isPlayingVideo():
            VIDEO = 1
        else:
            VIDEO = 0
    
    printInfo("Tick")
    xbmc.sleep(1000)
