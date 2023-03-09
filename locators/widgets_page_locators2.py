from selenium.webdriver.common.by import By


class AccordianLocators:
    FIRST_SECTION = (By.XPATH, "//div[@id='section1Heading']")
    SECOND_SECTION = (By.XPATH, "//div[@id='section2Heading']")
    THIRD_SECTION = (By.XPATH, "//div[@id='section3Heading']")


class AutocompleteLocators:
    MULTI_COLOR = (By.XPATH, "//input[@autocapitalize = 'none'][@id = 'autoCompleteMultipleInput']")
    SINGLE_COLOR = (By.XPATH, "//input[@autocapitalize = 'none'][@id = 'autoCompleteSingleInput']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, 'svg[height="14"][width="14"][viewBox="0 0 20 20"][aria-hidden="true"][focusable="false"]')


class SliderPageLocators:
    SLIDER = (By.XPATH, "//input[@type='range']")


class ProgressbarPageLocators:
    BAR = (By.XPATH, "//div[@role='progressbar']")
    BUTTON = (By.XPATH, "//button[@id='startStopButton']")


class TabsPageLocators:
    WHAT = (By.XPATH, "//a[@id='demo-tab-what']")
    ORIGIN = (By.XPATH, "//a[@id='demo-tab-origin']")
    USE = (By.XPATH, "//a[@id='demo-tab-use']")


class ToolTipsLocators:
    HOVER_BUTTON = (By.XPATH, "//button[@id='toolTipButton']")
    BUTTON_TOOLTIP = (By.XPATH, "//button[@aria-describedby='buttonToolTip']")
    TOOL_TIP_INNERS = (By.CSS_SELECTOR, 'div[class = "tooltip-inner"]')
