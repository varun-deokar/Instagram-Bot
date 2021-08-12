"""This is a program to automate the process of checking which people don't follow you back on instagram web app
        Don't forget to type in your  username password before using
        Note. This will work only if you turn off 2 step authentication on your instagram.
        Note. This program uses google chrome so you need that installed on your PC.
        Note. Make sure your chrome version matches chromedriver version that is downloaded."""

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from time import sleep

username = input('Enter Username')
password = input('Enter Password')
search = input('Enter username of account to search')

sleep(10)
driver = webdriver.Chrome()  # Opens the homepage using Google Chrome
driver.get("https://www.instagram.com/")  # Opens the instagram page
sleep(4)
# driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/p/a").click()  # Sign in option
# sleep(3)

# Enter username below
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(
    username)  # puts in user name

#Enter password below
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(
    password)  # puts in your password
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]").click()  # clicks the log in button
sleep(4)

# The commented code below is for an old instagram interface

# driver.find_element_by_xpath(
#     "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(
#     "")  # puts in user name
# driver.find_element_by_xpath(
#     "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(
#     "")  # puts in your password
# driver.find_element_by_xpath(
#     "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]").click()  # clicks the sign in button
# sleep(5)


driver.find_element_by_xpath(
    "/html/body/div[4]/div/div/div[3]/button[2]").click()  # presses no to the pop up notification
sleep(4)
# searches the search box, we use css selector as it is an icon, here we should not use xpath
# we type in the user name of the account we want to open


# Type in the account username of person whose followers you want to check
driver.find_element_by_css_selector(
    "#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input").send_keys(search)
sleep(2)
# There are 2 ways to open the profile page of selected user
# Either we can use xpath once you get the search result
driver.find_element_by_xpath(
    "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span").click()
sleep(3)

# If you want to run the commented code below you need to uncomment the import statement that imports Keys
# Or else you can press the enter button (You need to press it twice here, I think thats because we are still in the typing mode)
# driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input").send_keys(Keys.RETURN)
# driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input").send_keys(Keys.RETURN)
driver.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()  # opens up your followers
sleep(3)
scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")  # points to the entire follower section
last_ht, ht = 0, 1  # initialises 2 variables to check if scrolling has ended
while last_ht != ht:
    last_ht = ht  # last_ht is updated to the current ht of scroll_box
    sleep(1.5)
    ht = driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
links = scroll_box.find_elements_by_tag_name(
    'a')  # finds all the elements within scroll_box having hyper-references(users)
names = [name.text for name in links if name.text != '']  # stores the names in a list called names
driver.find_element_by_css_selector(
# clicks the cross icon to shut the followers box
    "body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button > svg").click()
sleep(1)
driver.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()  # opens the following people box
sleep(1)
scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")  # points to the entire following section
last_ht, ht = 0, 1  # last_ht is updated to the current ht of scroll_box
while last_ht != ht:
    last_ht = ht  # last_ht is updated to the current ht of scroll_box
    sleep(1.5)
    ht = driver.execute_script(
        "arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight;", scroll_box)
links2 = scroll_box.find_elements_by_tag_name(
    'a')  # finds all the elements within scroll_box having hyper-references(users)
names2 = [name.text for name in links2 if name.text != '']  # stores the names in a list called names2
driver.close()  # closes Google Chrome browser
c = 0  # initialises counter
for i in names2:  # loops the names in following list
    if i not in names:  # checks if they dont follow back
        print(i)  # prints name of users who dont follow back
        c += 1  # increases count of no. of users who dont follow back
print("\nTotal number of accounts that don't follow you back are ", c) # Prints number of people who don't follow you back
