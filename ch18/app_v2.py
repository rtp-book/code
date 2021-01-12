from appTheme import theme
from pyreact import useState, render, createElement as el
from pymui import Button, List, ListItem, Typography, Box, TextField
from pymui import Paper, Container, AppBar, ThemeProvider, useTheme

def App():
    newItem, setNewItem = useState("")
    editItem, setEditItem = useState("")
    listItems, setListItems = useState([])

    def handleSubmit(event):
        event.preventDefault()
        new_list = list(listItems)  # Make a copy
        if len(editItem) > 0:  # In edit mode
            new_list[new_list.index(editItem)] = newItem
        else:  # In add mode
            new_list.append(newItem)  # Add the new item
        setListItems(new_list)  # Update our state
        setNewItem("")  # Clear the new item value
        setEditItem("")  # Clear the edit item value

    def handleChange(event):
        target = event['target']
        setNewItem(target['value'])

    def handleDelete(item):
        new_list = list(listItems)  # Make a copy
        new_list.remove(item)  # Remove the specified item
        setListItems(new_list)  # Update our state

    def handleEdit(item):
        setNewItem(item)  # Set the new item value
        setEditItem(item)  # Set the edit item value

    def ItemVu(props):
        item = props['item']
        current_theme = useTheme()
        specialColor = current_theme['palette']['special']['main']
        button_style = {'margin': '0 0.5rem 0 0'}

        return el(ListItem, {'dense': True},
                  el(Button,
                     {'color': 'secondary',
                      'style': button_style,
                      'onClick': lambda: handleDelete(item)
                     },
                     el('span', {'className': 'material-icons'}, 'delete'),
                     "Delete"
                    ),
                  el(Button,
                     {'color': 'primary',
                      'style': button_style,
                      'onClick': lambda: handleEdit(item)
                     },
                     el('span', {'className': 'material-icons'}, 'edit'),
                     "Edit"
                    ),
                  el(Typography, {'style': {'color': specialColor}}, item)
                 )

    def ListItemsVu():
        return [el(ItemVu, {'key': item, 'item': item}) for item in listItems]

    if len(editItem) == 0:
        editColor = 'secondary'
        editLabel = "Add Item:"
    else:
        editColor = 'primary'
        editLabel = "Edit Item:"

    return el(ThemeProvider, {'theme': theme},
              el(Container, {'maxWidth': 'sm'},
                 el(AppBar, {'position': 'static',
                             'style': {'marginBottom': '0.5rem'}
                            },
                    el(Box, {'width': '100%', 'marginLeft': '0.5rem'},
                       el(Typography, {'variant': 'h6'}, "React to Python")
                      )
                   ),
                 el(Paper, {'elevation': 2},
                    el('form', {'onSubmit': handleSubmit,
                                'style': {'marginLeft': '1rem'}
                               },
                       el(TextField, {'InputLabelProps': {'color': editColor},
                                      'label': editLabel,
                                      'value': newItem,
                                      'onChange': handleChange,
                                      'autoFocus': True
                                     }
                         ),
                       el(Button, {'type': 'submit',
                                   'size': 'medium'
                                  }, "Submit"),
                      ),
                    el(List, None,
                       el(ListItemsVu, None)
                      ),
                   )
                )
             )

render(App, None, 'root')

