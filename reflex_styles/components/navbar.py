import reflex as rx
from reflex_styles.style.styles import Color

def navbar()  -> rx.Component:
    return rx.flex(
            rx.link(
                rx.icon(tag = 'palette'),
                href = '/',
                color = Color.negro_claro.value,
                _hover = {'color' : Color.verde_medio.value},
                ),
            rx.heading('Reflex styles by ',
                       rx.text.strong('Ericcode29', color = Color.verde_medio.value), 
                       align='center',
                       color = Color.negro_claro.value,
                       ),
            width = "100%",
            align='center',
            justify='center',
            background_color = Color.verde.value,
            spacing='4',
            padding = '1em',
            position="sticky",
            )
             