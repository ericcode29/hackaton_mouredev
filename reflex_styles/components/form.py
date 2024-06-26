import reflex as rx
from reflex_styles.components.navbar import navbar
from reflex_styles.style.styles import Color, Size

def form(titulo = 'Formulario') -> rx.Component: 
    return(
        rx.flex(
            rx.text(titulo,
                    size='5',
                    weight='bold'
                    ),
            rx.card(
                rx.heading(text = titulo),
                rx.vstack(
                    rx.input(placeholder='Nombre', type='text', size='2', width = Size.mediano.value),
                    rx.input(placeholder='Apellido', type='text', size='2', width = Size.mediano.value),
                    rx.input(placeholder='Edad', type='number', max_length='3', size='2', width = Size.mediano.value),
                    rx.input(placeholder='Email', type='email', size='2', width = Size.mediano.value),
                    rx.text_area(placeholder='Mensaje', size='2', width = Size.mediano.value, auto_height=True),
                    rx.button('Submit',
                            on_click=rx.window_alert("Formulario enviado"),
                            ),

                    align = 'center',
                    spacing = '4',
                    ),
                    size='3'
                ),
                height = '100%',
                spacing='4',
                direction='column',
                justify='start',
                align='center',
                padding_top = '1em',
                background_color = Color.verde_claro.value
            ),

        )