from org.zaproxy.zap.extension.pscan import PluginPassiveScanner
from org.apache.commons.io import FileUtils
from java.awt import Desktop
from java.io import File
from java.lang import System

def scan(ps, msg, src):
    # Check if the message is a response containing JavaScript
    content_type = msg.getResponseHeader().getHeader("Content-Type")
    if content_type is not None and "javascript" in content_type.lower() and \
        msg.getRequestHeader().getHostName().toString().match(r'^.*?google\..*$'):
        # Save the JavaScript file
        file_name = msg.getRequestHeader().getURI().getPath().replace('/', '_')
        response = msg.getResponseBody().toString()
        try:
            zap_dir = File(System.getProperty("user.home") + "/Desktop/<YOUR>/<DESIRED>/<PATH>")
            zap_dir.mkdirs()
            FileUtils.writeStringToFile(File(zap_dir, file_name), response, "UTF-8")
            print("File saved: " + file_name + "\nFrom Host: " + msg.getRequestHeader().getHostName())
        except Exception as e:
            print(e)

def appliesToHistoryType(history_type):
    return PluginPassiveScanner.getDefaultHistoryTypes().contains(history_type)
