from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.XPATH, "//div[@id='section1Heading']")
    SECTION_FIRST_CONTENT = (By.XPATH, "//p[contains(text(),'Lorem Ipsum is simply dummy text of the printing a')]")
    SECTION_SECOND = (By.XPATH, "//div[@id='section2Heading']")
    SECTION_SECOND_CONTENT = (By.XPATH, "//p[contains(text(),'Contrary to popular belief, Lorem Ipsum is not sim')]")
    SECTION_THIRD = (By.XPATH, "//div[@id='section3Heading']")
    SECTION_THIRD_CONTENT = (By.XPATH, "//p[contains(text(),'It is a long established fact that a reader will b')]")


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, "input[autocapitalize = 'none'][id = 'autoCompleteMultipleInput']")
    MULTI_VALUE = (By.XPATH, "//div[@class='css-12jo7m5 auto-complete__multi-value__label']")
    MULTI_VALUE_REMOVE = (
    By.CSS_SELECTOR, 'svg[height="14"][width="14"][viewBox="0 0 20 20"][aria-hidden="true"][focusable="false"]')
    SINGLE_CONTAINER = (By.CSS_SELECTOR, 'div[id="autoCompleteSingleContainer"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id = "autoCompleteSingleInput"]')


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.XPATH, "//div[@class = 'react-datepicker__day react-datepicker__day--014']")


class SliderProgressBarPage:
    INPUT_SLIDER = (By.XPATH, "//input[@type='range']")
    SLIDER_VALUE = (By.XPATH, "//input[@id='sliderValue']")
    PROGRESS_BAR_BUTTON = (By.XPATH, "//button[@id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.XPATH, "//div[@role='progressbar']")


class TabsPageLocators:
    TABS_WHAT = (By.XPATH, "//a[@id='demo-tab-what']")
    TABS_WHAT_CONTENT = (By.XPATH, "//p[contains(text(),'Lorem Ipsum is simply dummy text of the printing a')]")
    TABS_ORIGIN = (By.XPATH, "//a[@id='demo-tab-origin']")
    TABS_ORIGIN_CONTENT = (By.XPATH, "//p[contains(text(),'Contrary to popular belief, Lorem Ipsum is not sim')]")
    TABS_USE = (By.XPATH, "//a[@id='demo-tab-use']")
    TABS_USE_CONTENT = (By.XPATH, "//p[contains(text(),'It is a long established fact that a reader will b')]")


class ToolTipsLocators:
    BUTTON = (By.XPATH, "//button[@id='toolTipButton']")
    FIELD = (By.XPATH, "//input[@id='toolTipTextField']")
    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    SECTION_LINK = (By.XPATH, '//*[.="1.10.32"]')
    BUTTON_HOVER_TEXT = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')
    FIELD_HOVER_TEXT = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')
    CONTRARY_HOVER_TEXT = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')
    SECTION_HOVER_TEXT = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')
    TOOL_TIP_INNERS = (By.CSS_SELECTOR, 'div[class = "tooltip-inner"]')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")