from rxconfig import config
import reflex as rx
from reflex_styles.style.styles import Color
from reflex_styles.components.form import form
from reflex_styles.components.navbar import navbar
from reflex_styles.components.card import card


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.flex(
        navbar(),
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
                card('Fromulario', '/formulario.png'),
                href='/form'
            ),
            rx.link(
                card('Card'),
                href='#'
            ),
            rx.link(
                card('NavBar'),
                href='#'
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
app.add_page(form, route='/form' )


