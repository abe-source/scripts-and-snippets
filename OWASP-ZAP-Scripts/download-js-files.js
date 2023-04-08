// passive script to download js files of desired host while navigating through the app

var PluginPassiveScanner = Java.type("org.zaproxy.zap.extension.pscan.PluginPassiveScanner");
var FileUtils = Java.type("org.apache.commons.io.FileUtils");
var Desktop = Java.type("java.awt.Desktop");
var File = Java.type("java.io.File");
var System = Java.type("java.lang.System");

function scan(ps, msg, src) {
    // Check if the message is a response containing JavaScript
    var contentType = msg.getResponseHeader().getHeader("Content-Type");
    if (contentType != null && contentType.contains("javascript") 
	   && msg.getRequestHeader().getHostName().toString().match(/^.*?google\..*$/)) {
        // Save the JavaScript file
        var fileName = msg.getRequestHeader().getURI().getPath().replace(/\//g, "_");
        var response = msg.getResponseBody().toString();
        try {
		  var zapDir = new File(System.getProperty("user.home") + "/Desktop/<YOUR>/<DESIRED>/<PATH>");
            zapDir.mkdirs();
            FileUtils.writeStringToFile(new File(zapDir, fileName), response, "UTF-8");
		  print("File saved: " + fileName + "\nFrom Host: " + msg.getRequestHeader().getHostName())
        } catch (e) {
            print(e)
        }
    }
}

function appliesToHistoryType(historyType) {
    return PluginPassiveScanner.getDefaultHistoryTypes().contains(historyType);
}
