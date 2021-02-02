from pyreact import setTitle, useEffect, useState, render, createElement as el

def App():
    newTask, setNewTask = useState("")
    editTask, setEditTask = useState(None)
    taskList, setTaskList = useState([])
    taskCount, setTaskCount = useState(0)
    taskFilter, setTaskFilter = useState("all")

    def handleSubmit(event):
        event.preventDefault()
        new_list = list(taskList)  # Make a copy
        if editTask is not None:  # In edit mode
            taskIndex = new_list.index(editTask)  # Get list position
            new_list[taskIndex].update({'name': newTask})  # Update name
        else:  # In add mode
            new_list.append({'name': newTask, 'status': False})  # Add new item
        setTaskList(new_list)  # Update our state
        setNewTask("")  # Clear the new item value
        setEditTask(None)  # Clear the edit item value

    def handleEdit(task):
        setNewTask(task['name'])  # Set the new item value
        setEditTask(task)  # Set the edit item value

    def handleDelete(task):
        new_list = list(taskList)  # Make a copy
        new_list.remove(task)  # Remove the specified item
        setTaskList(new_list)  # Update our state

    def handleChange(event):
        target = event['target']
        if target['name'] == 'taskFilter':
            setTaskFilter(target['value'])
        else:
            setNewTask(target['value'])

    def handleChangeStatus(event, task):
        target = event['target']
        new_list = list(taskList)  # Make a copy
        taskIndex = new_list.index(task)  # Get list position
        new_list[taskIndex].update({'status': target['checked']})  # Update
        setTaskList(new_list)  # Update our state

    def ListItem(props):
        task = props['task']
        if taskFilter == "all" or \
                (taskFilter == "open" and not task['status']) or \
                (taskFilter == "closed" and task['status']):
            return el('li', None,
                      task['name'] + " ",
                      el('button',
                         {'type': 'button',
                          'onClick': lambda: handleDelete(task)
                         }, "Delete"
                        ),
                      el('button',
                         {'type': 'button',
                          'onClick': lambda: handleEdit(task)
                         }, "Edit"
                        ),
                      el('label', {'htmlFor': 'status'}, " Completed:"),
                      el('input',
                         {'type': 'checkbox',
                          'id': 'status',
                          'onChange': lambda e: handleChangeStatus(e, task),
                          'checked': task['status']
                         }
                        ),
                     )
        else:
            return None

    def ListItems():
        return [el(ListItem, {'key': task['name'], 'task': task}) for task in taskList]

    def updateCount():
        if taskFilter == 'open':
            new_list = [task for task in taskList if not task['status']]
        elif taskFilter == 'closed':
            new_list = [task for task in taskList if task['status']]
        else:
            new_list = [task for task in taskList]

        setTaskCount(len(new_list))

    useEffect(lambda: setTitle("ToDo List"), [])
    useEffect(updateCount, [taskList, taskFilter])

    return el('form', {'onSubmit': handleSubmit},
              el('div', None, f"Number of Tasks: {taskCount}"),
              el('div', None,
                 el('label', {'htmlFor': 'all'}, "All Tasks:"),
                 el('input', {'type': 'radio',
                              'name': 'taskFilter',
                              'id': 'all',
                              'value': 'all',
                              'onChange': handleChange,
                              'checked': taskFilter == 'all'
                             }
                   ),
                 el('label', {'htmlFor': 'open'}, " Active:"),
                 el('input', {'type': 'radio',
                              'name': 'taskFilter',
                              'id': 'open',
                              'value': 'open',
                              'onChange': handleChange,
                              'checked': taskFilter == 'open'
                             }
                   ),
                 el('label', {'htmlFor': 'closed'}, " Completed:"),
                 el('input', {'type': 'radio',
                              'name': 'taskFilter',
                              'id': 'closed',
                              'value': 'closed',
                              'onChange': handleChange,
                              'checked': taskFilter == 'closed'
                             }
                   ),
                ),
              el('label', {'htmlFor': 'editBox'},
                 "Edit Task: " if editTask is not None else "Add Task: "
                ),
              el('input', {'id': 'editBox',
                           'onChange': handleChange,
                           'value': newTask
                          }
                ),
              el('input', {'type': 'submit'}),
              el('ol', None,
                 el(ListItems, None)
                ),
             )

render(App, None, 'root')

