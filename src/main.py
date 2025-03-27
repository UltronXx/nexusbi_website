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
            "Home", "Ask Me", "About Us", "Contact Us"
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
                        font_family="medium",
                    ),
                    on_hover=self.on_nav_hover,
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

    def on_nav_hover(self, e) -> None:
        print(e.control)


# BottomNavBar
class BottomNavBar(Column):
    def __init__(self):
        super().__init__()

        self.controls = [
            Container(
                bgcolor=guidance,
                height=220,
                alignment=ft.alignment.center,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text(
                            value="Nexus BI Advisory",
                            size=50, color=clarity,
                            font_family="bold",
                        ),
                        Text(
                            value="Copyright 2025",
                            # size=18,
                            color=clarity,
                            font_family="medium",
                        )
                    ]
                )
            )
        ]


# main content
class ContentBody(Column):
    def __init__(self, page: Page):
        super().__init__()

        self.main_page = page
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
                            bgcolor=clarity,
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
                                        font_family="heavy",
                                        size=55, color=guidance,
                                        style=TextStyle(letter_spacing=-1, height=1),
                                    ),
                                    Column(height=10),
                                    Text(
                                        value="We're working hard on something "
                                                "exciting and will be\nlaunching soon. "
                                                "Check back later for updates. "
                                                "We appreciate\nyour patience!",
                                        font_family="medium", color=guidance,
                                        #size=15,
                                        style=TextStyle(height=1.2),
                                    ),
                                ]
                            )
                        ),
                        Column(height=50),
                        # Billboard
                        Container(
                            bgcolor="#F5F5F7",
                            border_radius=30,
                            content=ft.Stack(
                                expand=True,
                                alignment=ft.alignment.center_left,
                                #width=400,
                                controls=[
                                    Image(src="imgs/art.png"),
                                    Container(
                                        #bgcolor="blue",
                                        padding=padding.symmetric(horizontal=60),
                                        content=Column(
                                            controls=[
                                                Text(
                                                    value="Nexus BI\nAdvisory",
                                                    font_family="heavy",
                                                    size=68, color="#F5F5F7",
                                                    style=TextStyle(letter_spacing=-1, height=1),
                                                ),
                                                Column(height=65),
                                                Container(
                                                    width=600,
                                                    content=Text(
                                                        value="Is a trusted business advisory firm "
                                                            "in Ghana specializing in financial and "
                                                            "operational consulting for SMEs and "
                                                            "non-profit organizations. Our expertise "
                                                            "in data-driven decision-making, financial "
                                                            "modelling, and tax advisory has helped "
                                                            "numerous busineses optimize their performance "
                                                            "and achieve sustainable growth.",
                                                        font_family="regular", color="#f5f5f7",
                                                        #size=15,
                                                        style=TextStyle(height=1.2),
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        Column(height=50),
                        # Social media
                        Container(
                            bgcolor=clarity,
                            #height=380,
                            padding=padding.symmetric(vertical=40),
                            border_radius=20,
                            content=Column(
                                controls=[
                                    Container(
                                        alignment=ft.alignment.center,
                                        content=Column(
                                            horizontal_alignment=CrossAxisAlignment.CENTER,
                                            spacing=0,
                                            controls=[
                                                Text(
                                                    value="Connect with Us",
                                                    font_family="bold",
                                                    size=35, color=guidance
                                                    #style=TextStyle(letter_spacing=-1, height=1),
                                                ),
                                                Text(
                                                    value="Let's cross Paths",
                                                    font_family="medium",
                                                    size=15, color=guidance
                                                )
                                            ]
                                        )
                                    ),
                                    Column(height=10),
                                    Row(
                                        alignment=MainAxisAlignment.CENTER,
                                        controls=[
                                            # Facebook
                                            Container(
                                                bgcolor=guidance,
                                                alignment=ft.alignment.center,
                                                height=36, width=120,
                                                border_radius=25,
                                                content=Text(
                                                    value="Facebook",
                                                    color=clarity,
                                                    font_family="medium",
                                                ),
                                                on_click=lambda
                                                    e: self.social_media_button_clicked(e),
                                                on_hover=lambda
                                                    e: self.social_media_g2_hover(e),
                                                scale=1,
                                                animate=ft.animation.Animation(
                                                    duration=200,
                                                    curve=ft.AnimationCurve.EASE_IN
                                                ),
                                                animate_scale=ft.animation.Animation(
                                                    duration=200,
                                                    curve=ft.AnimationCurve.EASE_IN
                                                ),
                                            ),
                                            # LinkedIn
                                            Container(
                                                alignment=ft.alignment.center,
                                                height=36, width=120,
                                                border_radius=25,
                                                border=ft.border.all(
                                                    width=1,
                                                    color=guidance,
                                                ),
                                                content=Text(
                                                    value="LinkedIn",
                                                    color=guidance,
                                                    font_family="semibold",
                                                ),
                                                on_click=lambda
                                                    e: self.social_media_button_clicked(e),
                                                on_hover=lambda
                                                    e: self.social_media_g1_hover(e),
                                                scale=1,
                                                animate=ft.animation.Animation(
                                                    duration=200,
                                                    curve=ft.AnimationCurve.EASE_IN
                                                ),
                                                animate_scale=ft.animation.Animation(
                                                    duration=200,
                                                    curve=ft.AnimationCurve.EASE_IN
                                                ),
                                            ),
                                            # Instagram
                                            Container(
                                                bgcolor=guidance,
                                                alignment=ft.alignment.center,
                                                height=36, width=120,
                                                border_radius=25,
                                                content=Text(
                                                    value="Instagram",
                                                    color=clarity,
                                                    font_family="medium",
                                                ),
                                                on_click=lambda
                                                    e: self.social_media_button_clicked(e),
                                                on_hover=lambda
                                                    e: self.social_media_g2_hover(e),
                                                scale=1,
                                                animate=ft.animation.Animation(
                                                    duration=200,
                                                    curve=ft.AnimationCurve.EASE_IN
                                                ),
                                                animate_scale=ft.animation.Animation(
                                                    duration=200,
                                                    curve=ft.AnimationCurve.EASE_IN
                                                ),
                                            ),
                                            # WhatsApp
                                            Container(
                                                alignment=ft.alignment.center,
                                                height=36, width=120,
                                                border_radius=25,
                                                border=ft.border.all(
                                                    width=1,
                                                    color=guidance,
                                                ),
                                                content=Text(
                                                    value="WhatsApp",
                                                    color=guidance,
                                                    font_family="medium",
                                                ),
                                                on_click=lambda
                                                    e: self.social_media_button_clicked(e),
                                                on_hover=lambda
                                                    e: self.social_media_g1_hover(e),
                                                scale=1,
                                                animate=ft.animation.Animation(
                                                    duration=200,
                                                    curve=ft.AnimationCurve.EASE_IN
                                                ),
                                                animate_scale=ft.animation.Animation(
                                                    duration=200,
                                                    curve=ft.AnimationCurve.EASE_IN
                                                ),
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ),
                        Column(height=50),
                    ]
                )
            )
        ]

    def social_media_g1_hover(self, e: ft.ControlEvent) -> None:
        e.control.bgcolor = guidance if e.control.bgcolor is None else None
        e.control.scale = 1.1 if e.control.scale == 1 else 1
        e.control.content.color = guidance if e.control.content.color == clarity else clarity
        self.update()

    def social_media_g2_hover(self, e: ft.ControlEvent) -> None:
        e.control.bgcolor = guidance if e.control.bgcolor == clarity else clarity
        e.control.scale = 1.1 if e.control.scale == 1 else 1
        e.control.content.color = clarity if e.control.content.color == guidance else guidance
        self.update()

    def social_media_button_clicked(self, e: ft.ControlEvent) -> None:
        button_text: str = e.control.content.value
        if button_text == "Facebook":
            self.main_page.launch_url("https://www.facebook.com/share/1DDxT7Va5A/?mibextid=wwXIfr")
        if button_text == "Instagram":
            self.main_page.launch_url("https://www.instagram.com/nexusbiadvisory/?utm_source=ig_web_button_share_sheet")
        if button_text == "WhatsApp":
            self.main_page.launch_url("https://wa.me/+233556823445")
        if button_text == "LinkedIn":
            self.main_page.launch_url("https://www.linkedin.com/in/nexus-bi-advisory-94789b353?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app")



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
        ContentBody(page),
        BottomNavBar()
    )

    page.update()

if __name__ == "__main__":
    app(target=main, assets_dir=assets)
