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
        self.socket_name = "text=Розетка"
        self.socket_price = "text=Цена: 1000 ₽"
        self.socket_add_button = ":text('В корзину'):near(:text('Розетка'))"
        
        self.switch_name = "text=Выключатель"
        self.switch_price = "text=Цена: 2000 ₽"
        self.switch_add_button = ":text('В корзину'):near(:text('Выключатель'))"
        
        # Селектор футера
        self.footer = "text=© 2024 О нас"

        # Селекторы корзины
        self.cart_empty_title = "text=Корзина пуста"
    
    def navigate_to_main(self):
        """Переход на главную страницу."""
        self.navigate("index.html")    
    
    def is_navigation_visible(self) -> bool:
        """Проверяет видимость элементов навигации."""
        try:
            return (self.page.locator(self.logo).is_visible() and
                   self.page.locator(self.products_link).is_visible() and
                   self.page.locator(self.cart_link).is_visible())
        except:
            return False
    
    def is_socket_product_visible(self) -> bool:
        """Проверяет видимость товара Розетка."""
        try:
            return (self.page.locator(self.socket_name).is_visible() and
                   self.page.locator(self.socket_price).is_visible() and
                   self.page.locator(self.socket_add_button).is_visible())
        except:
            return False
    
    def is_switch_product_visible(self) -> bool:
        """Проверяет видимость товара Выключатель."""
        try:
            return (self.page.locator(self.switch_name).is_visible() and
                   self.page.locator(self.switch_price).is_visible() and
                   self.page.locator(self.switch_add_button).is_visible())
        except:
            return False
    
    def is_footer_visible(self) -> bool:
        """Проверяет видимость футера."""
        try:
            footer = self.page.locator(self.footer)
            return footer.is_visible() and footer.text_content() == "© 2024 О нас"
        except:
            return False
    
    def add_socket_to_cart(self):
        """Добавление розетки в корзину."""
        self.click(self.socket_add_button)
    
    def add_switch_to_cart(self):
        """Добавление выключателя в корзину."""
        self.click(self.switch_add_button)
        
    def navigate_to_cart(self):
        """Переход в корзину."""
        self.click(self.cart_link) 

    def is_cart_emty_title_visible(self) -> bool:
        """Проверяет видимость заголовка пустой корзины."""
        try:
            return self.page.locator(self.cart_empty_title).is_visible()
        except:
            return False