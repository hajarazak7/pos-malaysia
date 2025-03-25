from telnetlib import EC

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait


@given('the user navigates to the rate calculator page')
def step_impl(context):
    service = Service('/usr/local/bin/chromedriver')
    context.driver = webdriver.Chrome(service=service)
    # Maximize the browser window
    context.driver.maximize_window()
    context.driver.get("https://pos.com.my/send/ratecalculator")
    assert "Rate Calculator" in context.driver.page_source

@when('the user enters "{from_postcode}" as the postcode')
def step_impl(context, from_postcode):
    from_postcode_input = context.driver.find_element(By.XPATH, "//input[@formcontrolname='postcodeFrom']")
    from_postcode_input.send_keys(from_postcode)

@when('the user enters "{to_country}" as the "To" country and leaves the postcode empty')
def step_impl(context, to_country):
    to_country_input = context.driver.find_element(By.NAME, "country")
    to_country_input.clear()
    to_country_input.send_keys(to_country)
    to_country_click = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//small[contains(@title, "India - IN")]')))
    to_country_click.click()

@when('the user enters "{weight}" as the "Weight" and presses Calculate')
def step_impl(context, weight):
    weight_input = context.driver.find_element(By.XPATH, "//input[@formcontrolname='itemWeight']")
    weight_input.send_keys(weight)
    calculate_button = context.driver.find_element(By.XPATH,
                                                   '//*[@id="contentBody"]/div/app-static-layout/app-rate-calculator-v2/div/div[3]/div[2]/a')
    calculate_button.click()


@then('the user can see multiple quotes and shipments options available')
def step_impl(context):
    # Use WebDriverWait to ensure the elements are present
    service_type_elements = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'dt.font-medium.text-gray-900'))
    )
    # Initialize a counter for "Service Type" elements
    service_type_count = 0

    # Print only elements with the text "Service Type" and count them
    for service_type in service_type_elements:
        if service_type.text.strip() == "Service Type":
            service_type_count += 1
    if service_type_count > 1:
        print("Multiple quotes and shipment options available.")
    else:
        print("Only single quote and shipment option available.")

    context.driver.quit()