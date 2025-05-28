from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv

load_dotenv()
class BasePage:
    """Базовый класс для всех страниц приложения."""
    
    def __init__(self, page: Page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")
        
    def navigate(self, endpoint=""):
        """Переход на указанную страницу."""
        url = f"{self.base_url}/{endpoint}"
        self.page.goto(url)
        
    def get_title(self):
        """Получение заголовка страницы."""
        return self.page.title()
    
    def wait_for_selector(self, selector, state="visible"):
        """Ожидание элемента на странице."""
        return self.page.wait_for_selector(selector, state=state)
    
    def expect_visible(self, selector):
        """Проверка видимости элемента."""
        locator = self.page.locator(selector)
        expect(locator).to_be_visible()
        
    def expect_text(self, selector, text):
        """Проверка текста элемента."""
        locator = self.page.locator(selector)
        expect(locator).to_have_text(text)
        
    def get_text(self, selector):
        """Получение текста элемента."""
        return self.page.locator(selector).inner_text()
    
    def click(self, selector):
        """Клик по элементу."""
        self.page.click(selector)
        
    def fill(self, selector, value):
        """Ввод текста в поле."""
        self.page.fill(selector, value)