from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, os
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager


class Driv_option(webdriver.ChromeOptions):
    def __init__(self):
        super().__init__()


class QA_Selenium:

    @staticmethod
    def chrome(mode=None):
        d = DesiredCapabilities.CHROME
        # d['loggingPrefs'] = {'browser': 'ALL'}
        d['goog:loggingPrefs'] = {'browser': 'ALL'}
        sett = Driv_option()
        if mode == 'h5':
            mobile_emulation = {
                'deviceName': 'iPhone X',
            }
            sett.add_experimental_option("mobileEmulation", mobile_emulation)  # 手機模式
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=sett, desired_capabilities=d)

        return driver

    @staticmethod
    def screenshot(driver, picname):
        dir_timeforat = '%Y%m%d%H'
        dir_path = os.path.join('pic', time.strftime(dir_timeforat, time.localtime()))
        if not os.path.exists(dir_path):  # 判斷pic資料夾存不存在
            os.makedirs(dir_path)
        pic_path = os.path.join(dir_path, f'{picname}.png')
        driver.save_screenshot(pic_path)
        return pic_path


if __name__ == '__main__':
    driver = QA_Selenium.chrome(mode="h5")
    driver.get(url="https://www.cathaybk.com.tw/cathaybk/")
    time.sleep(1)
    QA_Selenium.screenshot(driver, '1_首頁截圖')
    driver.find_element_by_css_selector('.cubre-o-header__burger').click()
    for i in driver.find_elements_by_css_selector('.cubre-a-menuSortBtn.-l1'):
        if i.text == "產品介紹":
            i.click()
            break
    for _ in range(10):
        time.sleep(1)
        if driver.find_elements_by_css_selector('.cubre-a-menuSortBtn'):
            break

    for i in driver.find_elements_by_css_selector('.cubre-a-menuSortBtn'):
        if i.text == "信用卡":
            i.click()
            break

    credit_itemm_count = 0
    target_1 = ''
    for i in driver.find_elements_by_css_selector(
            'div.cubre-o-menu__item.is-L1open div.cubre-o-menuLinkList__content a.cubre-a-menuLink'):
        if i.text != '':
            credit_itemm_count += 1
        if i.text == '卡片介紹':
            target_1 = i

    print(f'總共{credit_itemm_count}個項目')
    QA_Selenium.screenshot(driver, '2_個人金融_產品介紹_信用卡列表')
    target_1.click()
    ban_card_count = 0
    for i in driver.find_elements_by_css_selector('.cubre-o-anchorBlock.cubre-o-block.-iconTitle'):
        if i.find_element_by_css_selector('.cubre-a-iconTitle__text').text == '停發卡':
            for ii in i.find_elements_by_css_selector('.swiper-pagination-bullet'):
                ii.click()
                time.sleep(0.5)
                pic_name = i.find_element_by_css_selector(
                    '.cubre-o-slide__item.swiper-slide.swiper-slide-active .cubre-m-compareCard__title').text
                ban_card_count += 1
                QA_Selenium.screenshot(driver, f'3_{ban_card_count}_{pic_name}')
    print(f'總共{credit_itemm_count}張卡停發')
    driver.quit()
