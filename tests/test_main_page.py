import pytest
from playwright.sync_api import Page, expect
from pages.main_page import MainPage

class TestMainPage:
    """Тесты для главной страницы."""
    
    @pytest.fixture(scope="function")
    def main_page(self, page: Page):
        """Фикстура для создания экземпляра главной страницы."""
        return MainPage(page)
    
    def test_navigation_elements(self, main_page: MainPage):
        """Тест проверки элементов навигации.
        - Логотип LC
        - Ссылка "Продукция"
        - Ссылка "Корзина"
        """
        main_page.navigate_to_main()
        assert main_page.is_navigation_visible(), "Элементы навигации не отображаются"
    
    def test_product_display_socket(self, main_page: MainPage):
        """Тест проверки отображения товара Розетка.
        - Название товара "Розетка"
        - Цена товара "1000 ₽"
        - Кнопка "В корзину"
        """
        main_page.navigate_to_main()
        assert main_page.is_socket_product_visible(), "Элементы товара Розетка не отображаются"
    
    def test_product_display_switch(self, main_page: MainPage):
        """Тест проверки отображения товара Выключатель.
        - Название товара "Выключатель"
        - Цена товара "2000 ₽"
        - Кнопка "В корзину"
        """
        main_page.navigate_to_main()
        assert main_page.is_switch_product_visible(), "Элементы товара Выключатель не отображается"
    
    def test_footer_display(self, main_page: MainPage):
        """Тест проверки отображения футера.
        - Текст копирайта "© 2024 О нас"
        """
        main_page.navigate_to_main()
        assert main_page.is_footer_visible(), "Футер не отображается"

    def test_cart_empty_title_visibility(self, main_page: MainPage):
        """Тест проверки видимости заголовка пустой корзины.
        - Заголовок "Корзина пуста" должен быть виден при переходе в корзину без товара"""
        main_page.navigate_to_main()
        main_page.navigate_to_cart()
        assert main_page.is_cart_emty_title_visible(), "Заголовок пустой корзины не отображается" 