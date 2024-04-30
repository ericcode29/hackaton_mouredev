from rxconfig import config
import reflex as rx
from reflex_styles.style.styles import Color
from reflex_styles.pages.form_page import form_page
from reflex_styles.pages.navbar_page import navbar_page
from reflex_styles.pages.card_page import card_page
from reflex_styles.pages.login_page import login_page
from reflex_styles.pages.components_page import components_page
from reflex_styles.components.card import card
from reflex_styles.components.navbar_index import navbar_index
from reflex_styles.components.footer import footer


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.flex(
        navbar_index(),
        rx.vstack(
        rx.grid(
            rx.flex(
                rx.card(
                    rx.text(
                f"""
Bienvenidos a mi propuesta para la hackaton de MoureDev, una pequeña ayuda para crear tu componentes con Reflex.
La idea es ahorrar tiempo al escribir código, dando unos componentes predefinidos, los cuales puedes adaptar a tu estilo y gusto posteriormente.
Aquí al lado van algunos ejemplos. En la barra superior encontrarás un icono que te llevará a todos los demás componentes que hay por el momento.

 Quizá en un futuro existan más... Quien sabe. 
Espero que los disfruten y les ayuden a ahorrar tiempo al crear sus ideas.
""",
        align='center',
        size='3',
        padding = '1em'
                ),
                padding_y = '4em',
                margin_x = '2em'
                    ),
                width='100%',
                align='center',
                justify='center',
                height = '50%',
                ),
        rx.grid(
            rx.link(
                card('Fromulario', '/formulario.png' ),
                href='/form',
            ),
            rx.link(
                card('LogIn', '/login.png'),
                href='/login',
            ),
            columns='1',
            align='center',
            justify='center',
            spacing='4',
            margin = '2em'
            ),
        align='center',
        justify='center',
        columns='2',
        spacing='4',
            ),
        justify='center',
        align='center',

        ),
        rx.flex(
            footer(),
            width = '100%',
            ),
        height="100%",
        direction='column',
        background_color = Color.verde_claro.value,
        spacing='4',
        align='center',

        
    )


app = rx.App(
    background_color = Color.verde_claro.value,
    theme = rx.theme( 
        has_background = True,
        radius = 'full',
        accent_color = 'lime',
        )
    )
app.add_page(index)
app.add_page(form_page, route='/form' )
app.add_page(card_page, route='/card')
app.add_page(navbar_page, route='/navbar')
app.add_page(login_page, route = '/login')
app.add_page(components_page, route='/components')


