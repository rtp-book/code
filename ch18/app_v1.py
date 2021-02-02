from pyreact import useState, render, createElement as el
from pymui import Button, List, ListItem, Typography, InputLabel, Input, Box

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
        return el(ListItem, {'dense': True},
                  el(Button,
                     {'variant': 'contained',
                      'color': 'secondary',
                      'size': 'small',
                      'style': {'marginRight': '0.5rem'},
                      'onClick': lambda: handleDelete(props['item']),
                     },
                     "Delete"
                    ),
                  el(Button,
                     {'variant': 'contained',
                      'color': 'primary',
                      'size': 'small',
                      'style': {'marginRight': '0.5rem'},
                      'onClick': lambda: handleEdit(props['item']),
                     },
                     "Edit"
                    ),
                  el(Typography, {'variant': 'body1'}, props['item'])
                 )

    def ListItemsVu():
        return [el(ItemVu, {'key': item, 'item': item}) for item in listItems]

    if len(editItem) == 0:
        editColor = 'secondary'
        editLabel = "Add Item:"
    else:
        editColor = 'primary'
        editLabel = "Edit Item:"

    return el(Box, None,
              el('form', {'onSubmit': handleSubmit},
                 el(InputLabel,
                    {'htmlFor': 'editBox', 'color': editColor},
                    editLabel
                   ),
                 el(Input, {'id': 'editBox',
                            'onChange': handleChange,
                            'value': newItem
                           }
                   ),
                 el(Button, {'type': 'submit',
                             'variant': 'contained',
                             'style': {'marginLeft': '0.5rem'}
                            }, "Submit"),
                ),
              el(List, None,
                 el(ListItemsVu, None)
                ),
             )

render(App, None, 'root')

