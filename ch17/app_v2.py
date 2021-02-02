from pyreact import useState, render, createElement as el

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

    def ListItem(props):
        return el('li', None,
                  el('button', {
                     'type': 'button',
                     'onClick': lambda: handleDelete(props['item']),
                     'style': {'color': 'darkred',
                               'marginRight': '5px',
                               'width': '60px'
                               }
                     }, "Delete"
                    ),
                  el('button', {
                     'type': 'button',
                     'onClick': lambda: handleEdit(props['item']),
                     'style': {'color': 'blue',
                               'marginRight': '5px',
                               'width': '60px'
                               }
                     }, "Edit"
                    ),
                  props['item'],
                 )

    def ListItems():
        return [el(ListItem, {'key': item, 'item': item}) for item in listItems]

    if len(editItem) == 0:
        editStyle = {'color': 'darkgreen'}
    else:
        editStyle = {'color': 'blue'}

    return el('form', {'onSubmit': handleSubmit,
                       'style': {'fontFamily': 'Arial, sans-serif'}
                      },
              el('label',
                 {'htmlFor': 'editBox', 'style': editStyle},
                 "Add Item: " if len(editItem) == 0 else "Edit Item: "
                ),
              el('input', {'id': 'editBox',
                           'onChange': handleChange,
                           'value': newItem
                          }
                ),
              el('input', {'type': 'submit',
                           'style': {'margin': '10px',
                                     'color': 'darkgreen',
                                     'width': '60px'
                                    }
                          }
                ),
              el('ol', None,
                 el(ListItems, None)
                ),
             )

render(App, None, 'root')

