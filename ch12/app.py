from pyreact import alert, useState, render, createElement as el

def App():
    newItem, setNewItem = useState("")

    def handleSubmit():
        alert(f"Item is : {newItem}")
        setNewItem("")

    def handleChange(event):
        target = event['target']
        setNewItem(target['value'])

    return el('div', None,
              el('label', {'htmlFor': 'editBox'}, "New Item: "),
              el('input', {'id': 'editBox',
                           'onChange': handleChange,
                           'value': newItem
                          }
                ),
              el('button', {'onClick': handleSubmit}, "Submit"),
             )

render(App, None, 'root')
