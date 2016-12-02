#from selenium import webdriver

from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('/usr/bin/firefox')
#browser = webdriver.Firefox(firefox_binary=binary)



from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary)

#firefox_capabilities = DesiredCapabilities.FIREFOX
#firefox_capabilities['marionette'] = True

#driver = webdriver.Firefox(capabilities=firefox_capabilities)

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title