from pymui import createMuiTheme, colors, makeStyles, styled, Button
from pyreact import createElement as el

theme = createMuiTheme({
    'palette': {
        'primary': colors['teal'],
        'secondary': colors['pink'],
        'special': {
            'main': colors['deepPurple'][600],
            'contrastText': colors['common']['white'],
        },
    },
    'overrides': {
        'MuiButton': {
            'root': {
                'margin': '0.5rem'
            },
        },
    },
    'props': {
        'MuiButton': {
            'variant': 'contained',
            'size': 'small',
        },
        'MuiTextField': {
            'type': 'text',
            'variant': 'outlined',
            'InputLabelProps': {'shrink': True},
            'InputProps': {'margin': 'dense'},
            'margin': 'dense',
        },
    },
})

StyledButton = styled(Button)({
    'minWidth': '6rem',
    'margin': '0 0.5rem 0 0',
    '&:hover': {'backgroundColor': theme['palette']['special']['main']}
})

useStyle = makeStyles({
    'root': {
        'minWidth': '6rem',
        'margin': '0 0.5rem 0 0',
        '&:hover': {'backgroundColor': lambda props: props['bgcolor']}
    }
})

def ListButton(props):
    new_props = {'style': {'minWidth': '6rem', 'margin': '0 0.5rem 0 0'}}
    new_props.update(props)
    return el(Button, new_props)

