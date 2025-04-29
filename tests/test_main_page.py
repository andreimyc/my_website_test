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
        """Тест проверки элементов навигации."""
        # Переходим на главную страницу
        main_page.navigate_to_main()
        
        # Проверяем элементы навигации
        main_page.verify_navigation_elements()
    
    def test_product_display_socket(self, main_page: MainPage):
        """Тест проверки отображения товара Розетка."""
        # Переходим на главную страницу
        main_page.navigate_to_main()
        
        # Проверяем отображение товара Розетка
        main_page.verify_socket_product()
    
    def test_product_display_switch(self, main_page: MainPage):
        """Тест проверки отображения товара Выключатель."""
        # Переходим на главную страницу
        main_page.navigate_to_main()
        
        # Проверяем отображение товара Выключатель
        main_page.verify_switch_product()
    
    def test_add_product_to_cart(self, main_page: MainPage):
        """Тест добавления товара в корзину."""
        # Переходим на главную страницу
        main_page.navigate_to_main()
        
        # Добавляем товар в корзину
        main_page.add_socket_to_cart()
        
        # Проверяем, что кнопка добавления в корзину все еще видима после нажатия
        main_page.expect_visible(main_page.socket_add_button)
    
    def test_footer_display(self, main_page: MainPage):
        """Тест проверки отображения футера."""
        # Переходим на главную страницу
        main_page.navigate_to_main()
        
        # Проверяем отображение футера
        main_page.verify_footer() 