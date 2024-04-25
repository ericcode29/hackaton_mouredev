import reflex as rx
from reflex_styles.components.navbar import navbar
from reflex_styles.components.card import card
from reflex_styles.style.styles import Color, Size

def card_page() -> rx.Component:
    return (
        navbar(titulo='Reflex styles by ', 
               text_strong='Ericcode29', 
               ref='/', 
               icon='palette'),
        rx.flex(
            rx.text('Componente Card',
                    color = Color.negro_claro.value,
                    size = '5',
                    weight = 'bold',
                    padding = '1em'
                    ),
            card('Card', '/card.png'),

            rx.code_block(
                """
def card(titulo = '', imagen = '') -> rx.Component:
    return(
        rx.card(
            titulo,
            rx.image(
                src = imagen,
                width = '300px',
                height = '300px',
                border_radius = '10px'   
                ),
            background_color = Color.gris_claro.value,
            color = Color.verde_claro.value,
            _hover = {'color':Color.verde_base.value}
            ),
            
        )
""",

                language = 'python',
                can_copy = True,
                auto_height = True,
                ),

            height = '100%',
            background_color = Color.verde_claro.value,
            direction = 'column',
            align = 'center',
            spacing = '4'
            )
        )