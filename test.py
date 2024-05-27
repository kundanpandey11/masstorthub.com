import requests 

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

SBR_WEBDRIVER = 'https://brd-customer-hl_5f7bc336-zone-scraping_browser1:uy4101jjayoc@brd.superproxy.io:9515'


def main():
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating to https://optalex.us/privacy-policy/...')
        driver.get('https://optalex.us/privacy-policy/')
        # CAPTCHA handling: If you're expecting a CAPTCHA on the target page, use the following code snippet to check the status of Scraping Browser's automatic CAPTCHA solver
        # print('Waiting captcha to solve...')
        # solve_res = driver.execute('executeCdpCommand', {
        #     'cmd': 'Captcha.waitForSolve',
        #     'params': {'detectTimeout': 10000},
        # })
        # print('Captcha solve status:', solve_res['value']['status'])
        # print('Navigated! Scraping page content...')
        
        html = driver.page_source
        print(html)
        with open("template/privacy_policy.html", "w", encoding="utf-8") as html_file:
            html_file.write(html)
        # driver.quit()
        
if __name__ == "__main__":
    main()

    
    