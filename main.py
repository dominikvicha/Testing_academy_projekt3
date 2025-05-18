import pytest
from playwright.sync_api import sync_playwright

"""
# choose the short terms courses and create the ouput file "kontrola.txt"
def test_enngeto(page):
    page.goto("https://engeto.cz/")

    # refuse cookies 
    btn_refuse = page.locator("#cookiescript_reject")
    btn_refuse.click()
    page.wait_for_timeout(2000)

    # click on the button "Termíny"
    testing_terms = page.locator("#main-header .main-navigation > a[href='/terminy/']")
    testing_terms.click()
    page.wait_for_timeout(2000)

    # find box where are filters of courses 
    filter_box = page.locator(".block-dates-filter__desktop")
    page.wait_for_timeout(2000)

    # find and click on the "Krátkodobé školení"
    checkbox_short_term_courses = filter_box.locator("#type-kratkodobe-skoleni")
    checkbox_short_term_courses.check() 

    # making sure that the page is fully loaded 
    page.wait_for_selector("text=AI od základů s Davidem Šetkem") 

    # finding all of the courses tittles in the short term courses 
    h3_locator = page.locator("div.block-dates-filter-products h3.title")
    h3_list = h3_locator.all_inner_texts()               

    # finally write it into the file 
    with open("kontrola.txt", mode="w", encoding="utf-8") as txt_kontrola:
        for h3 in h3_list:
            txt_kontrola.write(h3 + "\n") 

"""

"""
# function for testing the FAQ question. 

def test_engeto2(page):
    page.goto("https://engeto.cz/")

    # refuse cookies 
    #btn_refuse = page.locator("#cookiescript_reject")
    #btn_refuse.click()
    #page.wait_for_timeout(2000)


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

"""

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
    #lesson_dates = page.locator("div.description.has-text-lg-regular-font-size p")
    lesson_dates = page.locator("#product-12038 > div.block-columns.flex-mobile-column-r.align.wp-block-engeto-columns > div > div:nth-child(1) > div > div:nth-child(1) > div.has-text-lg-regular-font-size.fullwidth > div > div:nth-child(1) > div > p:nth-child(1)")
    
    # control that it finds some terms
    count = lesson_dates.count()
    assert count > 0, "Nebyly nalezeny žádné termíny kurzu."

    # create list and print them into the terminal
    dates_list = []
    for i in range(count):
        date_text = lesson_dates.nth(i).inner_text().strip()
        dates_list.append(date_text)
        print(date_text)
