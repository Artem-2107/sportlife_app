import flet as ft
from views import (
    login_view, register_view, catalog_view, product_view,
    cart_view, orders_view, profile_view, admin_view, favorites_view
)

class App:
    def __init__(self, page):
        self.page = page
        self.page.title = "Спорт лайф"
        self.page.padding = 0
        self.page.theme_mode = ft.ThemeMode.DARK

    def go(self, name, **kw):
        self.page.controls.clear()
        try:
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
            control = views[name]()
            if control:
                self.page.controls.append(control)
            else:
                self.page.controls.append(ft.Text(f"Экран {name} пустой"))
        except Exception as e:
            # Если ошибка — показываем её на экране телефона
            self.page.controls.append(
                ft.Column([
                    ft.Text("ОШИБКА ЗАПУСКА:", color=ft.Colors.RED, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(str(e), color=ft.Colors.WHITE, size=14),
                ], scroll=ft.ScrollMode.AUTO)
            )
        self.page.update()

    def ok(self, m):
        s = ft.SnackBar(ft.Text(m, color=ft.Colors.WHITE), bgcolor=ft.Colors.GREEN)
        self.page.overlay.append(s)
        s.open = True
        self.page.update()

    def error(self, m):
        s = ft.SnackBar(ft.Text(m, color=ft.Colors.WHITE), bgcolor=ft.Colors.RED)
        self.page.overlay.append(s)
        s.open = True
        self.page.update()

def main(page: ft.Page):
    try:
        app = App(page)
        app.go("login")
    except Exception as e:
        page.add(ft.Text(f"КРИТИЧЕСКАЯ ОШИБКА: {str(e)}", color=ft.Colors.RED))

if __name__ == "__main__":
    ft.app(target=main)
