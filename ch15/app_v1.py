from pyreact import useState, render, createElement as el

def App():
    newItem, setNewItem = useState("")
    listItems, setListItems = useState([])

    def handleSubmit(event):
        event.preventDefault()
        new_list = list(listItems)  # Make a copy
        new_list.append(newItem)  # Add the new item
        setListItems(new_list)  # Update our state
        setNewItem("")  # Clear the new item value

    def handleChange(event):
        target = event['target']
        setNewItem(target['value'])

    def handleDelete(item):
        new_list = list(listItems)  # Make a copy
        new_list.remove(item)  # Remove the specified item
        setListItems(new_list)  # Update our state

    def ListItem(props):
        return el('li', None,
                  props['item'] + " ",
                  el('button', {'type': 'button',
                                'onClick': lambda: handleDelete(props['item'])
                               }, "Delete"),
                  )

    def ListItems():
        items = []
        for item in listItems:
            items.append(el(ListItem, {'key': item, 'item': item}))
        return items

    return el('form', {'onSubmit': handleSubmit},
              el('label', {'htmlFor': 'editBox'}, "New Item: "),
              el('input', {'id': 'editBox',
                           'onChange': handleChange,
                           'value': newItem
                          }
                ),
              el('input', {'type': 'submit'}),
              el('ol', None,
                 el(ListItems, None)
                ),
             )

render(App, None, 'root')

