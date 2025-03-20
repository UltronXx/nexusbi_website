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
    alignment,
    padding,
    ThemeMode,
    TextAlign,
    ControlEvent,
    alignment
)


from pathlib import Path
assets = f"{Path(__file__).parent}/src/assets"


# TopNavBar
class NavBar(Column):
    def __init__(self):
        super().__init__()

        self.nav_bar_links: list[str] = [
            "Link1", "Link2", "Link3", "Link4", "Link5"
        ]
        self.nav_bar = Row(
            controls=[],
            alignment=MainAxisAlignment.CENTER,
            spacing=50,
        )

        for nav_bar_link in self.nav_bar_links:
            self.nav_bar.controls.append(
                Text(
                    value=f"{nav_bar_link}",
                    color="#f5f5f7", size=13,
                    font_family="regular",
                    # on_tap=lambda e: self.nav_link_tapped(e)
                    on_tap=lambda _: print("Link tapped...")
                )
            )

        self.background = Container(
            height=55, bgcolor="#00215C", content=self.nav_bar
        )
        self.controls = [self.background]


    def nav_link_tapped(self, e: ControlEvent) -> None:
        print(e)


# BottomNavBar
class BottomNavBar(Column):
    def __init__(self):
        super().__init__()

        self.controls = [
            Container(
                bgcolor="#f5f5f7",
                height=220,
                alignment=alignment.center,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text(
                            value="ESB Foundation",
                            size=30, color="black",
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
    def __init__(self, main_page: Page):
        super().__init__()
        self.main_page = main_page

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
                            height=480,
                            alignment=alignment.center,
                            border_radius=30,
                            content=Column(
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Text(
                                        value="Site Under\nConstruction",
                                        font_family="heavy",
                                        size=70,
                                        text_align=TextAlign.CENTER,
                                        style=TextStyle(letter_spacing=-1, height=1),
                                    ),
                                    Column(height=10),
                                    Text(
                                        value="Your patience,\nis everything we need.",
                                        font_family="semibold",
                                        size=15,
                                        style=TextStyle(height=1.2),
                                        text_align=TextAlign.CENTER
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
    page.theme_mode = ThemeMode.LIGHT
    
    page.add(
        NavBar(),
        # ContentBody(),
        BottomNavBar()
    )

if __name__ == "__main__":
    app(target=main)
