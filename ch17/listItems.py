from pyreact import createElement as el

def ListItem(props):
    item = props['item']
    handleDelete = props['handleDelete']
    handleEdit = props['handleEdit']

    return el('li', None,
              props['item'] + " ",
              el('button', {'type': 'button',
                            'onClick': lambda: handleDelete(item)
                           }, "Delete"
                ),
              el('button', {'type': 'button',
                            'onClick': lambda: handleEdit(item)
                           }, "Edit"
                ),
             )

def ListItems(props):
    return [el(ListItem, {'key': item,
                          'item': item,
                          'handleDelete': props['handleDelete'],
                          'handleEdit': props['handleEdit']
                         }
              ) for item in props['listItems']]

