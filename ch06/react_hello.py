def App():
    val, setVal = React.useState("")

    def say_hello():
        setVal("Hello React!")

    def clear_it():
        setVal("")

    return [
        React.createElement('button', {'onClick': say_hello}, "Click Me!"),
        React.createElement('button', {'onClick': clear_it}, "Clear"),
        React.createElement('div', None, val)
    ]

def render():
    ReactDOM.render(
        React.createElement(App, None),
        document.getElementById('root')
    )

document.addEventListener('DOMContentLoaded', render)

