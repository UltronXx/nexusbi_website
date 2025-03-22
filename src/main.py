import flet as ft
from flet import (
    Page,
    app,
    Container,
    Column,
    Row,
    ResponsiveRow,
    Image,
    Text,
    TextStyle,
    MainAxisAlignment,
    CrossAxisAlignment,
    padding,
    ThemeMode,
    TextAlign,
    ControlEvent,
    margin,
    alignment
)


from pathlib import Path
from assets.shared.colors import *

assets = f"{Path(__file__).parent}/src/assets"


# TopNavBar
class NavBar(Column):
    def __init__(self):
        super().__init__()

        self.nav_bar_links: list[str] = [
            "nav1", "nav2", "nav3", "nav4"
        ]

        self.nav_bar = Row(
            controls=[],
            spacing=40,
        )

        for nav_bar_link in self.nav_bar_links:
            self.nav_bar.controls.append(
                Container(
                    content=Text(
                        value=f"{nav_bar_link}",
                        color="#f5f5f7", size=13,
                        font_family="regular",
                    ),
                    on_click=lambda e:
                        print(f"<{e.control.content.value}> clicked...")
                )
            )

        self.background = Container(
                #padding=10,
                bgcolor=guidance,
                alignment=ft.alignment.center,
                content=Container(
                    width=800,
                    #bgcolor=guidance,
                    #border_radius=12,
                    padding=padding.symmetric(vertical=15, horizontal=20),
                    content=Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Image(src="imgs/LogO.png", width=90),
                            self.nav_bar
                            ]
                        )
                )
            )
        self.controls = [self.background]


# BottomNavBar
class BottomNavBar(Column):
    def __init__(self):
        super().__init__()

        self.controls = [
            Container(
                bgcolor="#f5f5f7",
                height=220,
                alignment=ft.alignment.center,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text(
                            value="NexusBI Advisory",
                            size=40, color="black",
                            font_family="bold",
                        ),
                        Text(
                            value="Copyright 2025",
                            size=18, color="black",
                            font_family="medium",
                        )
                    ]
                )
            )
        ]


# main content
class ContentBody(Column):
    def __init__(self):
        super().__init__()

        self.width = 780

        self.controls = [
            Container(
                # bgcolor="green",
                content=Column(
                    expand=True,
                    controls=[
                        Column(height=50),
                        # Hero Section
                        Container(
                            bgcolor="pink",
                            height=380,
                            alignment=ft.alignment.center_left,
                            padding=padding.symmetric(horizontal=50),
                            border_radius=30,
                            content=Column(
                                alignment=MainAxisAlignment.CENTER,
                                #horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Text(
                                        value="Site under\nConstruction",
                                        font_family="bold",
                                        size=70,
                                        style=TextStyle(letter_spacing=-1, height=1),
                                    ),
                                    Column(height=10),
                                    Text(
                                        value="We're working hard on something exciting and will be\nlaunching soon. Check back later for updates. We appreciate\nyour patience!",
                                        font_family="medium",
                                        size=15,
                                        style=TextStyle(height=1.2),
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            )
        ]



# main
def main(page: Page) -> None:
    page.title = "NexusBI Page"
    
    page.horizontal_alignment = "center"
    page.window.width = 1200

    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "white"
    page.padding = 0

    page.scroll = ft.ScrollMode.HIDDEN

    page.fonts = {
        "regular": "fonts/SF-Pro-Display-Regular.otf",
        "medium": "fonts/SF-Pro-Display-Medium.otf",
        "semibold": "fonts/SF-Pro-Display-Semibold.otf",
        "bold": "fonts/SF-Pro-Display-Bold.otf",
        "heavy": "fonts/SF-Pro-Display-Heavy.otf",
    }


    page.add(
        NavBar(),
        ContentBody(),
        BottomNavBar()
    )

    page.update()

if __name__ == "__main__":
    app(target=main, assets_dir=assets)
