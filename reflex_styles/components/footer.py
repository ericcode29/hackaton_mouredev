import reflex as rx
from reflex_styles.components.navbar import navbar

def footer() -> rx.Component:
    return (
        rx.box(
            navbar(
            'Todos los derechos reservados ',
            'Ericcode29',
            'https://github.com/ericcode29/hackaton_mouredev',
            'github',
            
            ),
            bottom = '0',
            width = '100%',
            style={
                "bottom":"0px",               
                }
            )


        
        )