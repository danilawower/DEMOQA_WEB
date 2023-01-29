from selenium.webdriver.common.by import By


class AccordianPageLocators:

    SECTION_FIRST = (By.XPATH, "//div[@id='section1Heading']")
    SECTION_FIRST_CONTENT = (By.XPATH, "//p[contains(text(),'Lorem Ipsum is simply dummy text of the printing a')]")
    SECTION_SECOND = (By.XPATH, "//div[@id='section2Heading']")
    SECTION_SECOND_CONTENT = (By.XPATH, "//p[contains(text(),'Contrary to popular belief, Lorem Ipsum is not sim')]")
    SECTION_THIRD = (By.XPATH, "//div[@id='section3Heading']")
    SECTION_THIRD_CONTENT = (By.XPATH, "//p[contains(text(),'It is a long established fact that a reader will b')]")



