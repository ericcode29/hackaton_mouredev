import reflex as rx
from reflex_styles.components.navbar import navbar
from reflex_styles.components.card import card
from reflex_styles.style.styles import Color, Size

def card_page() -> rx.Component:
    return (
        navbar(titulo='Reflex components by ', 
               text_strong='Ericcode29', 
               ref='/', 
               icon='palette'),
        rx.flex(
            rx.flex(
                rx.link(
                    rx.icon(tag = 'arrow-left'),
                    href='/components',
                    ),
                rx.text('Componente Card',
                    size='5',
                    weight='bold'
                    ),
                direction='row',
                spacing='4',
                ),
            card('Card', '/card.png'),

            rx.code_block(
                """
def card(titulo = '', imagen = '', background = '', color = '') -> rx.Component:
    return(
        rx.card(
            titulo,
            rx.image(
                src = imagen,
                width = '300px',
                height = '300px',
                border_radius = '10px'   
                ),
            background_color = background,
            color = color,
            _hover = {'color': 'white'}
            ),
            
        )
""",

                language = 'python',
                can_copy = True,
                auto_height = True,
                width = '100%',
                wrap_long_lines = True,
                ),

            height = '100%',
            background_color = Color.verde_claro.value,
            direction = 'column',
            align = 'center',
            padding_top = '1em',
            spacing = '4'
            )
        )