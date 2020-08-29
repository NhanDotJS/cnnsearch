from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


class cnnsearch:
    def __init__(self, keyword, pages):
        current_page = 1
        from_post = (current_page - 1) * 10
        bot = webdriver.Chrome(options=chrome_options)
        new_keyword = keyword.replace(' ', '+')
        for x in range(pages):
            bot.get ('https://edition.cnn.com/search?q='+ new_keyword+ '&page=' + str(current_page)+ '&from='+ str(from_post))
            print("\n__________________________________________________________\n")
            print('\nPage:'+ str(current_page)+'\n')
            print("\n__________________________________________________________\n")
            current_page = current_page + 1
            from_post = (current_page - 1) * 10
            time.sleep(10)
            article_list = bot.find_elements_by_class_name('cnn-search__result')
            for article in article_list:
                title = article.find_element_by_class_name('cnn-search__result-headline')
                body = article.find_element_by_class_name('cnn-search__result-body')
                link = article.find_element_by_link_text(title.text)
                print('\nTitle\n')
                print(title.text)
                print(link.get_attribute('href'))
                print('\nBody \n')
                print(body.text[:1000])
                print('\n==========================================================')
                time.sleep(1)


keyword = input('What do you want to search on CNN?\n')
pages = int(input('How many pages do you want to search for?\n'))

cnnsearch(keyword, pages)

