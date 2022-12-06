from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By


from selenium.webdriver.common.keys import Keys
import time








PATH = "C:/Program Files (x86)/chromedriver_win32/chromedriver.exe"

chrome_options = ChromeOptions()

chrome_options.add_extension('metamask.crx')

driver = webdriver.Chrome(PATH , options=chrome_options)

runner = 1

	

	



driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")



time.sleep(1)



frase = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input")


frase.send_keys(" # YOUR KEY PHRASE # ")
frase.send_keys(Keys.RETURN)

password = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/div[5]/div/input")


password.send_keys(" # YOUR PW # ")
password.send_keys(Keys.RETURN)


password = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/div[6]/div/input")


password.send_keys(" # YOUR PW # ")
password.send_keys(Keys.RETURN)



tick = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/div[7]/div")

tick.click()




importe = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/button")

importe.click()




time.sleep(3)


done = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/button")

done.click()


time.sleep(1)


driver.get("https://opensea.io/")



time.sleep(1)


click = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/nav/ul/div[2]/div/li/a/i")

click.click()



time.sleep(1)


click = driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[2]/ul/li[1]/button/div[2]")

click.click()



time.sleep(4)



driver.switch_to.window(driver.window_handles[1])




click = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]")

click.click()

time.sleep(2)


click = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]")

click.click()







driver.switch_to.window(driver.window_handles[0])


time.sleep(3)



######start opensea######




driver.get("https://opensea.io/account?search[resultModel]=ASSETS&search[sortBy]=EXPIRATION_DATE&search[sortAscending]=true")


time.sleep(2)








element = driver.find_element_by_tag_name('body')





element.send_keys(Keys.PAGE_DOWN);


time.sleep(2)




click = driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[3]/div/article/a/div[2]/div/div[1]/div[2]")

click.click()




time.sleep(2)






click = driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div[1]/div/button")

click.click()



time.sleep(3)



click = driver.find_element(By.XPATH, '//button[text()="Confirm"]')

# click2 = driver.find_element_by_link_text('Confirm')


click.click()



click = driver.find_element(By.XPATH, '//button[text()="Sign"]')


click.click()

time.sleep(2)



driver.switch_to.window(driver.window_handles[1])




click = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[3]/button[2]")

click.click()


driver.switch_to.window(driver.window_handles[0])


time.sleep(2)



sell = driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div[1]/div/span[2]/a")

sell.click()


time.sleep(1)



time.sleep(1)


click = driver.find_element_by_xpath("//input[@name='price']")



click.send_keys("0.02")





# click = driver.find_element_by_id('duration')

# click.click()



element = driver.find_element_by_tag_name('body')





element.send_keys(Keys.ARROW_DOWN);
element.send_keys(Keys.ARROW_DOWN);
element.send_keys(Keys.ARROW_DOWN);

time.sleep(2)


click = driver.find_element(By.XPATH, '//button[text()="Complete listing"]')


click.click()

time.sleep(2)




click = driver.find_element(By.XPATH, '//button[text()="Sign"]')


click.click()

time.sleep(2)




driver.switch_to.window(driver.window_handles[1])




click = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[3]/button[2]")

click.click()


driver.switch_to.window(driver.window_handles[0])


time.sleep(2)



######upload finish#####