from typing import Optional
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page, Playwright
import logging


class BrowserManager:
    def __init__(self) -> None:
        self.p: Optional[Playwright] = None
        self.browser: Optional[Browser] = None
        self._context: Optional[BrowserContext] = None

    def is_alive(self) -> bool:
        try:
            if self.browser and self.browser.is_connected():
                return True
        except Exception:
            pass
        return False

    def start(self) -> None:
        self.stop()
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=True)
        self._context = self.browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

    def new_page(self) -> Page:
        if not self.is_alive():
            logging.warning("Browser morto, reiniciando...")
            self.start()
        return self._context.new_page()

    def stop(self) -> None:
        try:
            if self._context:
                self._context.close()
        except Exception:
            pass
        try:
            if self.browser:
                self.browser.close()
        except Exception:
            pass
        try:
            if self.p:
                self.p.stop()
        except Exception:
            pass
        self.p = None
        self.browser = None
        self._context = None


_manager: Optional[BrowserManager] = None


def _get_manager() -> BrowserManager:
    global _manager
    if _manager is None:
        _manager = BrowserManager()
    return _manager


def get_page() -> Page:
    return _get_manager().new_page()


def stop_browser() -> None:
    if _manager is not None:
        _manager.stop()
