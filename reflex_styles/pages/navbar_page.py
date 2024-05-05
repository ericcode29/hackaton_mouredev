import reflex as rx
from reflex_styles.components.navbar import navbar
from reflex_styles.components.card import card
from reflex_styles.style.styles import Color, Size

def navbar_page() -> rx.Component:
    return(
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
                rx.text('Componente NavBar',
                    size='5',
                    weight='bold'
                    ),
                direction='row',
                spacing='4',
                ),
                card(imagen = '/navbar.png'),

            rx.code_block(
                """
def navbar(titulo = '', text_strong = '', ref = '#', icon = '', color = 'white')  -> rx.Component:
    return rx.flex(
            rx.link(
                rx.icon(tag = icon), 
                href = ref,
                _hover = {'color' : color},
                ),
            rx.heading(titulo,
                       rx.text.strong(text_strong), 
                       align='center',
                       ),
            width = "100%",
            align='center',
            justify='center',
            background_color = color,
            spacing='4',
            padding = '1em',
            position="sticky",
            )
""",
                    language='python',
                    can_copy=True,
                    auto_height = True,
                    width = '100%',
                    wrap_long_lines = True,
                    ),

            height = '100%',
            background_color = Color.verde_claro.value,
            align = 'center',
            spacing = '4',
            direction = 'column', 
            padding_top = '1em',
            )
        )