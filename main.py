import pytest
from playwright.sync_api import sync_playwright


# choose the short terms courses and create the ouput file "kontrola.txt"
def test_enngeto(page):
    page.goto("https://engeto.cz/prehled-kurzu/")

   # refuse cookies if they show up 
    try:
        btn_refuse = page.locator("#cookiescript_reject")
        btn_refuse.click()
        #page.wait_for_timeout(2000)
    except:
        pass

    page.wait_for_selector("text=Krátkodobé kurzy a školení")
    # finding all of the courses tittles in the short term courses 
    short_courses = page.locator("section:has(h2:has-text('Krátkodobé kurzy a školení')) h3")
    print(short_courses.inner_html())

    count = short_courses.count()
    assert count > 0, "Nebyly nalezeny žádné kurzy."

    h3_list = []
    for i in range(count):
        course_tittle = short_courses.nth(i).inner_text().strip()
        h3_list.append(course_tittle)
        print(course_tittle)

    # finally write it into the file 
    with open("kontrola.txt", mode="w", encoding="utf-8") as txt_kontrola:
        for h3 in h3_list:
            txt_kontrola.write(h3 + "\n") 


"""
# function for testing the FAQ question. 

def test_engeto2(page):
    page.goto("https://engeto.cz/")

    # refuse cookies if they show up 
    try:
        btn_refuse = page.locator("#cookiescript_reject")
        btn_refuse.click()
        page.wait_for_timeout(2000)
    except:
        pass

    # find FAQ click
    faq_test = page.locator("li.area-faq > a")
    faq_test.click()
    page.wait_for_timeout(5000)

    # find and click on "úřad práce - proplácení kurzu"
    faq_topic_test = page.locator("label >> text=Úřad práce")
    faq_topic_test.click()
    page.wait_for_timeout(5000)

    question_elements = page.locator("#urad-prace > div > div")

    # control quantity of elements 
    count = question_elements.count()
    assert count > 0, "Nebyly nalezeny žádné otázky."
    
    # print all of the find questions
    for i in range(count):
        question = question_elements.nth(i)
        print(question.inner_text())

# function for finding the terms of course Python Academy 

def test_engeto3(page):
    page.goto("https://engeto.cz/")

    # refuse cookies if they show up 
    try:
        btn_refuse = page.locator("#cookiescript_reject")
        btn_refuse.click()
        page.wait_for_timeout(2000)
    except:
        pass

    # find and click on "Python Akademie box"
    test_course = page.locator("a:has(h3:has-text('Python Akademie')) >> text=Více informací")
    test_course.click()
    page.wait_for_timeout(5000)

    # find and click on "Zobrazit termíny kurzu"
    test_show_term = page.locator("a:has-text('Zobrazit termíny kurzu')")
    test_show_term.click()
    page.wait_for_timeout(5000)

    # find and click on Python Akademie 
    blocks = page.locator("#terminy a")
    count = blocks.count()

    for i in range(count):
        block = blocks.nth(i)
        text = block.inner_text(timeout=5000)
        if "Python Akademie" in text:
            block.locator("text=Detail termínu").click()
            break
            
    # find box with actual terms
    terms_title = page.locator("span:has-text('Termíny lekcí')")                    # find text "Termíny lekcí"

    terms_box = terms_title.locator("xpath=ancestor::div[contains(@class, 'box')]") # use xPath to find <div> with class "box"

    lesson_dates = terms_box.locator("div.description p")                           # find all <p> elemets inside the div.description
    
    # control that it finds some terms
    count = lesson_dates.count()
    assert count > 0, "Nebyly nalezeny žádné termíny kurzu."

    # create list and print them into the terminal
    dates_list = []
    for i in range(count):
        date_text = lesson_dates.nth(i).inner_text().strip()
        if "/" in date_text:                                                        # prints just the dates 
            dates_list.append(date_text)
            print(date_text)

"""