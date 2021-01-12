from pyreact import render, useState, useEffect, createElement as el
from pyreact import ReactGA
from pymui import Box, TextField
from jsutils import fetch


GAID = 'UA-100000000-1'  # Substitute your own GA Tracking ID here
ReactGA.initialize(GAID, {'titleCase': False, 'debug': False,
                          'gaOptions': {'siteSpeedSampleRate': 100}}
                  )


def StyledTextField(props):
    new_props = {'type': 'text',
                 'fullWidth': True,
                 'variant': 'outlined',
                 'InputLabelProps': {'shrink': True},
                 'InputProps': {'margin': 'dense'},
                 'margin': 'dense',
                }

    new_props.update(props)
    return el(TextField, new_props)

def UserVu(props):
    users = props['users'] if props['users'] else []

    def userToRow(user):
        return el('option', {'key': user[0], 'value': user[0]}, user[1])

    return [userToRow(user) for user in users]


def App():
    users, setUsers = useState([])
    userID, setUserID = useState("")
    firstName, setFirstName = useState("")
    lastName, setLastName = useState("")
    username, setUsername = useState("")

    def handleChange(event):
        target = event['target']
        setUserID(target['value'])
        setFirstName("")
        setLastName("")
        setUsername("")

    def getUser():
        def _getUser(data):
            user_info = data if data else {}
            if len(user_info) > 0:
                setFirstName(user_info['FirstName'])
                setLastName(user_info['LastName'])
                setUsername(user_info['Username'])
            else:
                setFirstName("")
                setLastName("")
                setUsername("")

        if len(userID) > 0:
            ReactGA.event({'category': 'User',
                           'action': 'Select',
                           'label': userID}
                         )
            fetch(f"/api/user/{userID}", _getUser)

    def getUsers():
        def _getUsers(data):
            user_list = data if data else []
            user_list.sort(key=lambda user: user[1])
            ReactGA.event({'category': 'App',
                           'action': 'Load',
                           'label': 'Users',
                           'nonInteraction': True}
                         )
            setUsers(user_list)
            setUserID("")

        fetch("/api/users", _getUsers)

    useEffect(getUser, [userID])
    useEffect(getUsers, [])

    return el(Box, {'key': 'App', 'style': {'width': '200px'}},
              el(Box, {'alignItems': 'center'},
                 el(StyledTextField, {'label': "Select User",
                                      'value': userID,
                                      'onChange': handleChange,
                                      'select': True,
                                      'SelectProps': {'native': True},
                                      'autoFocus': True,
                                     },
                    el('option', {'key': '', 'value': ''}),  # Blank row
                    el(UserVu, {'users': users}),
                   ),
                ),
              el(StyledTextField, {'label': 'First Name',
                                   'value': firstName,
                                   'disabled': True,
                                  }
                ),
              el(StyledTextField, {'label': 'Last Name',
                                   'value': lastName,
                                   'disabled': True,
                                  }
                ),
              el(StyledTextField, {'label': 'Username',
                                   'value': username,
                                   'disabled': True,
                                  }
                ),
             ),

render(App, None, 'root')

