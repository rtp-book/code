from pyreact import useState, render, createElement as el
from listItems import ListItems

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

    return el('form', {'onSubmit': handleSubmit},
              el('label', {'htmlFor': 'editBox'},
                 "Add Item: " if len(editItem) == 0 else "Edit Item: "
                ),
              el('input', {'id': 'editBox',
                           'onChange': handleChange,
                           'value': newItem
                          }
                ),
              el('input', {'type': 'submit'}),
              el('ol', None,
                 el(ListItems, {'listItems': listItems,
                                'handleDelete': handleDelete,
                                'handleEdit': handleEdit}
                   )
                ),
             )

render(App, None, 'root')

