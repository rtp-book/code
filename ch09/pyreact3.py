# Load React and ReactDOM JavaScript libraries into local namespace
React = __pragma__('js',
    '''
    (function () {{
        var exports = {{}};
        {}  // Puts react in exports and in global window
        return window.React;
    }}) ();
    ''',
    __include__('./node_modules/react/umd/react.development.js')
    )

# returns ReactDOM object
ReactDOM = __pragma__('js',
    '''
    (function () {{
        var exports = {{}};
        {}  // Puts react in exports and in global window
        var abc1 = window.ReactDOM;
        delete window.React;
        delete window.ReactDOM;
        return abc1;
    }}) ();
    ''',
    __include__('./node_modules/react-dom/umd/react-dom.development.js')
    )

# Map React javaScript objects to Python identifiers
createElement = React.createElement
useState = React.useState


def render(root_component, props, container):
    """Loads main react component into DOM"""

    def main():
        ReactDOM.render(
            React.createElement(root_component, props),
            document.getElementById(container)
        )

    document.addEventListener("DOMContentLoaded", main)

