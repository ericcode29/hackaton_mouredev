import reflex as rx
from reflex_styles.components import navbar, card
from reflex_styles.style.styles import Color

def components_page() -> rx.Component:
    return(
        navbar.navbar(titulo='Reflex components by ', 
               text_strong='Ericcode29', 
               ref='/', 
               icon='palette'),
        rx.container(
            rx.card(
                rx.grid(
                    rx.link(
                        card.card('Fromulario', '/formulario.png' ),
                        href='/form'
                    ),
                    rx.link(
                        card.card('LogIn', '/login.png' ),
                        href='/login'
                    ),
                    rx.link(
                        card.card('Card', '/card.png' ),
                        href='/card'
                    ),
                    rx.link(
                        card.card('NavBar', '/navbar.png' ),
                        href='/navbar'
                    ),
                    columns='2',
                    align='center',
                    justify='center',
                    spacing='4',
                    ),

                    background_color = Color.verde_base.value,
                    margin = '2em'
            ),
            height = '100%',
            background_color = Color.verde_claro.value
            )
        )