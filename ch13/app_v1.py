from pyreact import useState, render, createElement as el

def App():
    newItem, setNewItem = useState("")
    listItems, setListItems = useState([])

    def handleSubmit():
        new_list = list(listItems)  # Make a copy
        new_list.append(newItem)  # Add the new item
        setListItems(new_list)  # Update our state
        setNewItem("")  # Clear the new item value

    def handleChange(event):
        target = event['target']
        setNewItem(target['value'])

    def getListItems():
        items = []
        for item in listItems:
            element = el('li', {'key': item}, item)
            items.append(element)

        return items

    return el('div', None,
              el('label', {'htmlFor': 'editBox'}, "New Item: "),
              el('input', {'id': 'editBox',
                           'onChange': handleChange,
                           'value': newItem
                          }
                ),
              el('button', {'onClick': handleSubmit}, "Submit"),
              el('ol', None, getListItems()),
             )

render(App, None, 'root')

