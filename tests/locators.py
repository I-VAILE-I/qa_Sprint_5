class Xpath:
    open_registration_on_login_page = "//a[@class='Auth_link__1fOlj']"
    registration_input_name = "//label[text()='Имя']/following-sibling::input[@name='name']"
    registration_input_email = "//label[text()='Email']/following-sibling::input[@name='name']"
    registration_input_password = "//input[@name='Пароль']"
    click_on_registration_button = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    login_input_email = "//input[@name='name']"
    login_input_password = "//input[@name='Пароль']"
    login_button = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    login_logout_button = "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"
    login_button_on_main_page = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    main_page_logo = "//div[@class='AppHeader_header__logo__2D0X2']"
    login_button_on_registration_page = "//a[@class='Auth_link__1fOlj']"
    login_button_on_recovery_password_page = "//a[@class='Auth_link__1fOlj']"
    forgot_password_button = "//a[@href='/forgot-password']"
    constructor_selection = "//p[@class='AppHeader_header__linkText__3q_va ml-2']"
    error_input = "//p[@class='input__error text_type_main-default']"
    section_sauces = "//span[text()='Соусы']"
    section_fillings = "//span[text()='Начинки']"
    section_rolls = "//span[text()='Булки']"
    active_section = "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"


class LinkText:
    personal_cabinet = "Личный Кабинет"


class Links:
    get_link = "https://stellarburgers.nomoreparties.site"
    login_link = "https://stellarburgers.nomoreparties.site/login"
    main_page = "https://stellarburgers.nomoreparties.site/"
    profile = "https://stellarburgers.nomoreparties.site/account/profile"
    forgot_password = "https://stellarburgers.nomoreparties.site/forgot-password"
