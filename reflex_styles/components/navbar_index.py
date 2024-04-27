import reflex as rx
from reflex_styles.style.styles import Color


def navbar_index() -> rx.Component:
    return rx.flex(
            rx.link(
                rx.icon(tag = 'palette'), 
                href = '/',
                color = Color.negro_claro.value,
                _hover = {'color' : Color.verde_medio.value},
                ),
            rx.heading('Reflex components by ',
                       rx.text.strong('Ericcode29', color = Color.verde_medio.value ), 
                       align='center',
                       color = Color.negro_claro.value,
                       ),
            rx.link(
                rx.icon(tag = 'file-stack'),
                href='#',
                color = Color.negro_claro.value,
                _hover = {'color': Color.verde_medio.value},
                is_external=False
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