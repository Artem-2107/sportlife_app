import sys
import os

# Добавляем папку frontend в пути поиска
sys.path.append(os.path.join(os.path.dirname(__file__), 'frontend'))

import flet as ft
from views import (
    login_view, register_view, catalog_view, product_view,
    cart_view, orders_view, profile_view, admin_view, favorites_view
)

class App:
    def __init__(self, page):
        self.page = page
        
    def go(self, name, **kw):
        try:
            self.page.controls.clear()
            
            views = {
                "login": lambda: login_view.build(self),
                "register": lambda: register_view.build(self),
                "catalog": lambda: catalog_view.build(self),
                "product": lambda: product_view.build(self, kw.get("product_id")),
                "cart": lambda: cart_view.build(self),
                "orders": lambda: orders_view.build(self),
                "profile": lambda: profile_view.build(self),
                "admin": lambda: admin_view.build(self),
                "favorites": lambda: favorites_view.build(self),
            }
            
            if name in views:
                control = views[name]()
                if control:
                    self.page.controls.append(control)
                    self.page.update()
                else:
                    self.page.add(ft.Text(f"View {name} returned None"))
            else:
                self.page.add(ft.Text(f"View {name} not found"))
                
        except Exception as e:
            self.page.controls.clear()
            self.page.add(ft.Text(f"Error: {str(e)}", color=ft.colors.RED))
            import traceback
            self.page.add(ft.Text(traceback.format_exc()))

    def ok(self, m):
        s = ft.SnackBar(ft.Text(m, color=ft.colors.WHITE), bgcolor=ft.colors.GREEN)
        self.page.overlay.append(s)
        s.open = True
        self.page.update()

    def error(self, m):
        s = ft.SnackBar(ft.Text(m, color=ft.colors.WHITE), bgcolor=ft.colors.RED)
        self.page.overlay.append(s)
        s.open = True
        self.page.update()

def main(page: ft.Page):
    page.title = "Спорт лайф"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Показываем начальный экран
    try:
        app = App(page)
        app.go("login")
    except Exception as e:
        page.add(ft.Text(f"Ошибка запуска: {str(e)}", color=ft.colors.RED))

if __name__ == "__main__":
    ft.app(target=main)
