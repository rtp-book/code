# __pragma__('skip')
# These are here to quiet the Python linter and are ignored by Transcrypt
require = None
document = None
# __pragma__('noskip')

# Load the React and ReactDOM JavaScript libraries into the local namespace
React = require('react')
ReactDOM = require('react-dom')

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

    document.addEventListener('DOMContentLoaded', main)

