import pytest
from playwright.sync_api import sync_playwright

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