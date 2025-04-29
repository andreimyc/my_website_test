import pytest
from playwright.sync_api import Page, Playwright, Browser, BrowserContext

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Установка параметров браузера для всех тестов."""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1366,
            "height": 768,
        }
    }

@pytest.fixture(scope="function")
def page(page: Page):
    """Фикстура страницы с предварительной настройкой."""
    page.set_default_timeout(10000)
    yield page 