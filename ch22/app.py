from pyreact import render, useState, createElement as el
from pyreact import useContext, createContext
from pymui import Box, TextField

Ctx = createContext()

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
              el(Component3, None)
             )

def Component3(props):
    return el(Box, None,
              el(ROTextField, {'label': 'Row 3', 'value': 'Row Three'}),
              el(Component4, None)
             )

def Component4(props):
    return el(Box, None,
              el(ROTextField, {'label': 'Row 4', 'value': 'Row Four'}),
              el(Component5, None)
             )

def Component5(props):
    ctx = useContext(Ctx)
    testVal = ctx['testVal']
    return el(Box, None,
              el(ROTextField, {'label': 'Copy From Row 1',
                              'value': testVal}
                ),
             )

def App():
    testVal, setTestVal = useState("")

    def handleChange(event):
        target = event['target']
        setTestVal(target['value'])

    return el(Ctx.Provider, {'value': {'testVal': testVal, 'otherVal': 42}},
              el(Box, {'key': 'App', 'style': {'width': '200px'}},
                 el(TextField, {'label': 'Row 1',
                                'value': testVal,
                                'onChange': handleChange}
                   ),
                 el(Component2, None)
                )
             )

render(App, None, 'root')

