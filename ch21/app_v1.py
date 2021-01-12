from pyreact import render, useState, createElement as el
from pymui import Box, TextField

def ROTextField(props):
    new_props = {'fullWidth': True,
                 'variant': 'outlined',
                 'InputLabelProps': {'shrink': True},
                 'InputProps': {'margin': 'dense'},
                 'margin': 'dense',
                 'disabled': True
                }

    new_props.update(props)
    return el(TextField, new_props)

def Component2(props):
    return el(Box, None,
              el(ROTextField, {'label': 'Row 2', 'value': 'Row Two'}),
              el(Component3, {'testVal2': props['testVal1']})
             )

def Component3(props):
    return el(Box, None,
              el(ROTextField, {'label': 'Row 3', 'value': 'Row Three'}),
              el(Component4, {'testVal3': props['testVal2']})
             )

def Component4(props):
    return el(Box, None,
              el(ROTextField, {'label': 'Row 4', 'value': 'Row Four'}),
              el(Component5, {'testVal4': props['testVal3']})
             )

def Component5(props):
    return el(Box, None,
              el(ROTextField, {'label': 'Copy From Row 1',
                               'value': props['testVal4']}
                ),
             )

def App():
    testVal, setTestVal = useState("")

    def handleChange(event):
        target = event['target']
        setTestVal(target['value'])

    return el(Box, {'key': 'App', 'style': {'width': '200px'}},
              el(TextField, {'label': 'Row 1',
                             'value': testVal,
                             'onChange': handleChange}
                ),
              el(Component2, {'testVal1': testVal})
             )

render(App, None, 'root')

