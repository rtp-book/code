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
        return el('li', {'className': 'list-group-item p-1'},
                  el('button',
                     {'onClick': lambda: handleDelete(props['item']),
                      'className': 'btn btn-danger btn-sm mr-2'
                     },
                     "Delete"
                    ),
                  el('button',
                     {'onClick': lambda: handleEdit(props['item']),
                      'className': 'btn btn-primary btn-sm mr-2'
                     },
                     "Edit"
                    ),
                  props['item'],
                 )

    def ListItems():
        return [el(ListItem, {'key': item, 'item': item}) for item in listItems]

    if len(editItem) == 0:
        editClass = 'text-success'
    else:
        editClass = 'text-primary'

    return el('div', {'className': 'container m-1'},
              el('form', {'onSubmit': handleSubmit,
                          'className': 'form-inline col-10 my-2'
                         },
                 el('label',
                    {'htmlFor': 'editBox', 'className': editClass},
                    "Add Item: " if len(editItem) == 0 else "Edit Item: "
                   ),
                 el('input', {'id': 'editBox',
                              'onChange': handleChange,
                              'value': newItem,
                              'className': 'form-control ml-2'
                             }
                   ),
                 el('input', {'type': 'submit',
                              'className': 'btn btn-success ml-2'
                             }
                   ),
                ),
              el('ul', {'className': 'list-group col-10 ml-2'},
                 el(ListItems, None)
                ),
             )

render(App, None, 'root')

