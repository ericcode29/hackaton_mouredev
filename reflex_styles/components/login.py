import reflex as rx
from reflex_styles.components.card import card

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
            )

        )