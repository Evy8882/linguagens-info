from flask import Flask
app = Flask(__name__)

pages = {
'redirect_to_home': 'redirect.html',
'homepage': 'home.html',
'pyinfopage': 'pyInfo.html',
'jsinfopage': 'jsInfo.html',
'jvinfopage': 'jvInfo.html',
'tsinfopage': 'tsinfo.html',
}