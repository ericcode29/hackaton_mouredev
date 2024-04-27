import reflex as rx
from reflex_styles.style.styles import Color, Size

def card(titulo = '', imagen = '') -> rx.Component:
    return(
        rx.card(
            titulo,
            rx.image(
                src = imagen,
                width = '300px',
                height = '300px',
                border_radius = '10px',   
                ),
            background_color = Color.gris_claro.value,
            color = Color.verde_claro.value,
            _hover = {'color':Color.verde_base.value},
            ),
            
        )