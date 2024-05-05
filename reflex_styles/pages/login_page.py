import reflex as rx
from reflex_styles.components.navbar import navbar
from reflex_styles.components.login import login
from reflex_styles.style.styles import Color

def login_page() -> rx.Component:
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
                rx.text('Componente LogIn',
                    size='5',
                    weight='bold'
                    ),
                direction='row',
                spacing='4',
                ),
            login(),

            rx.code_block(
            """
def login() -> rx.Component:
    return (
        rx.flex(
            rx.card(
                rx.heading(
                        'LogIn',
                        padding = '1em'
                        ),
                rx.vstack(
                    rx.input(placeholder='Email',
                        type='email'
                        ),
                    rx.input(placeholder='Password',
                            type='password',
                            ),
                    rx.button('Acceder',
                        on_click = rx.window_alert('LogIn')
                        ),
                    
                    rx.flex(
                        rx.link('Crear cuenta',
                                href = '#'
                                ),
                        rx.link('¿Olvidó su contraseña?',
                                href = '#'
                                ),
                        direction='row',
                        align='baseline',
                        spacing='4',
                        ),

                    spacing='4',
                    align='center',
                    
                    ),
                size='3',
                ),

            direction='column',
            align='center',
            justify='center',
            spacing='4'
            ),
        )
""",
            language = "python",
            auto_height = True,
            can_copy = True,
            width = '100%',
            wrap_long_lines = True,
            ),


            direction='column',
            spacing='4',
            align='center',
            height = '100%',
            width = '100%',
            padding_top = '1em',
            background_color = Color.verde_claro.value
            ),

        
        )