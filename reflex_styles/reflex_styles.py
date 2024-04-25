from rxconfig import config
import reflex as rx
from reflex_styles.style.styles import Color
from reflex_styles.pages.form_page import form_page
from reflex_styles.pages.navbar_page import navbar_page
from reflex_styles.pages.card_page import card_page
from reflex_styles.components.card import card
from reflex_styles.components.navbar import navbar


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.link(
                rx.icon(tag = 'palette'), 
                href = '/',
                color = Color.negro_claro.value,
                _hover = {'color' : Color.verde_medio.value},
                ),
            rx.heading('Reflex styles by ',
                       rx.text.strong('Ericcode29', color = Color.verde_medio.value ), 
                       align='center',
                       color = Color.negro_claro.value,
                       ),
            rx.link(
                rx.icon(tag = 'github'),
                href='https://github.com/ericcode29/hackaton_mouredev',
                color = Color.negro_claro.value,
                _hover = {'color' : Color.verde_medio.value},
                is_external = True
                ),
            width = "100%",
            align='center',
            justify='center',
            background_color = Color.verde.value,
            spacing='4',
            padding = '1em',
            position="sticky",
            ),
        rx.vstack(
        rx.center(
            rx.text.strong('Selecciona tu componente',
                    color = Color.negro_claro.value,
                    align='center',
                    ),
        align='center',
        justify='center',
            ),

        rx.spacer(),

        rx.flex(
            rx.link(
                card('Fromulario', '/formulario.png' ),
                href='/form'
            ),
            rx.link(
                card('Card', '/card.png'),
                href='/card'
            ),
            rx.link(
                card('NavBar', '/navbar.png'),
                href='/navbar'
            ),
            direction='row',
            justify='center',
            align='center',
            spacing='4',
            ),
        justify='center',
        align='center',

        ),
        height="100vh",
        direction='column',
        background_color = Color.verde_claro.value,
        spacing='4',
        
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


