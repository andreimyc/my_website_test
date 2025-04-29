from playwright.sync_api import Page, expect
from .base_page import BasePage

class MainPage(BasePage):
    """Класс представляющий главную страницу."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        # Селекторы навигации
        self.logo = "text=LC"
        self.products_link = "text=Продукция"
        self.cart_link = "text=Корзина"
        
        # Селекторы товаров
        self.socket_image = "img:near(:text('Розетка'))"
        self.socket_name = "text=Розетка"
        self.socket_price = "text=Цена: 1000 ₽"
        self.socket_add_button = ":text('В корзину'):near(:text('Розетка'))"
        
        self.switch_image = "img:near(:text('Выключатель'))"
        self.switch_name = "text=Выключатель"
        self.switch_price = "text=Цена: 2000 ₽"
        self.switch_add_button = ":text('В корзину'):near(:text('Выключатель'))"
        
        # Селектор футера
        self.footer = "text=© 2024 О нас"
    
    def navigate_to_main(self):
        """Переход на главную страницу."""
        self.navigate("index.html")
    
    def verify_navigation_elements(self):
        """Проверка элементов навигации."""
        self.expect_visible(self.logo)
        self.expect_visible(self.products_link)
        self.expect_visible(self.cart_link)
    
    def verify_socket_product(self):
        """Проверка отображения товара Розетка."""
        self.expect_visible(self.socket_name)
        self.expect_visible(self.socket_price)
        self.expect_visible(self.socket_add_button)
    
    def verify_switch_product(self):
        """Проверка отображения товара Выключатель."""
        self.expect_visible(self.switch_name)
        self.expect_visible(self.switch_price)
        self.expect_visible(self.switch_add_button)
    
    def verify_footer(self):
        """Проверка отображения футера."""
        self.expect_visible(self.footer)
        self.expect_text(self.footer, "© 2024 О нас")
    
    def add_socket_to_cart(self):
        """Добавление розетки в корзину."""
        self.click(self.socket_add_button)
    
    def add_switch_to_cart(self):
        """Добавление выключателя в корзину."""
        self.click(self.switch_add_button)
        
    def navigate_to_cart(self):
        """Переход в корзину."""
        self.click(self.cart_link) 