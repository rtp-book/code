from pymui import createMuiTheme, colors

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

