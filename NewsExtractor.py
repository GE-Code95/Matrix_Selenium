from BaseExtractor import BaseExtractor
class NewsExtractor(BaseExtractor):
    '''options = Options()
    options.headless = True
    options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
    PATH = "C:/Program Files (x86)/geckodriver.exe"
    driver = webdriver.Firefox(executable_path=PATH, options=options)
    driver.maximize_window()
    url = 'https://www.bbc.com/'

    driver.get(url)
    actions = ActionChains(driver)

    bbc_hrefs = []

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.block-link__overlay-link")))
    time.sleep(1)
    media_list = driver.find_elements_by_css_selector("a.block-link__overlay-link")

    for link in media_list:
        bbc_hrefs.append(link.get_attribute('href'))
        print(link.get_attribute('href'))


    def previous():
        driver.execute_script("window.history.go(-1)")


    for idx, url in enumerate(bbc_hrefs):
        if 'sport' not in url and 'news' in url:
            driver.get(url)
            header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "main-heading")))
            data_block = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component='text-block']")))
            print(header.text)
            for block in data_block:
                print(block.text)
            previous()
        else:
            if 'sport' not in url and 'news' not in url:
                driver.get(url)
                header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                    (By.XPATH, "//div[@tabindex='-1']")))

                intro = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='article__intro b-font-family-serif']")))

                body = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//div/div/p")))
                print(header.text)
                print(intro.text)

                for p in body:
                    print(p.text)

    driver.close()
    driver.quit()'''
