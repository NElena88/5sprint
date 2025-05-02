# 5sprint
# UI-Тесты веб-приложения Stellar Burgers

Автоматизированные UI-тесты для проверки функциональности сайта Stellar Burgers с использованием `Selenium WebDriver` и `pytest`.

## Что покрывают тесты

###  Регистрация
-  `test_successful_registration`: успешная регистрация с валидными данными (имя, email, пароль ≥ 6 символов)
-  `test_registration_error_short_password`: регистрация с ошибкой при коротком пароле (менее 6 символов)

###  Вход в аккаунт
-  `test_login_to_account_button`: вход через кнопку **«Войти в аккаунт»** на главной странице
-  `test_login_to_account_personal_account`: вход через кнопку **«Личный кабинет»**
-  `test_login_to_account_personal_account_form_registration`: вход через ссылку **«Войти»** в форме регистрации
-  `test_login_to_account_forgot_password`: вход через форму восстановления пароля

### ️ Личный кабинет
-  `test_personal_account`: переход в личный кабинет после авторизации
-  `test_personal_account_go_to_constructor`: переход из личного кабинета в раздел **«Конструктор»** по одноимённой кнопке
-  `test_personal_account_go_to_logo`: переход в **«Конструктор»** по нажатию на логотип **Stellar Burgers**
-  `test_personal_account_exit`: выход из аккаунта по кнопке **«Выход»** в личном кабинете

###  Раздел «Конструктор»
-  `test_constructor_tabs_rolls`: переход в раздел **«Булки»**
-  `test_constructor_tabs_sauces`: переход в раздел **«Соусы»**
-  `test_constructor_tabs_toppings`: переход в раздел **«Начинки»**
