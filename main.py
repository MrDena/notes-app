import flet as ft

def main(page: ft.Page):
    # Делаем приложение полноэкранным
    page.window_full_screen = True
    page.padding = 0
    page.margin = 0

    # Создаём WebView, который загружает ваш макет
    webview = ft.WebView(
        url="https://eject-fond-06364037.figma.site",
        expand=True,
    )

    page.add(webview)

ft.app(target=main)
