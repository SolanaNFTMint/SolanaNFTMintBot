import os
import json
import me
import monkelabs

def getConfig():
        configFile = open("config.json", 'r')
        return list(json.load(configFile).values())


#gets config
config = getConfig()

#if windows True, else False (mac, linux)
isWindows = True if os.name == 'nt' else False

#if mint on magiceden.io
if "magiceden.io" in config[0]:
    print("Found magiceden.io link")
    me.mint(config, isWindows)
    
#if mint on monkeylabs.io
elif "monkelabs.io" in config[0]:
    print("Found monkelabs.io link")
    ml.mint(config, isWindows)

#if platform not supported
else:
    print("Could not recognize link")

