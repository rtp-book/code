# __pragma__('skip')
# These are here to quiet the Python linter and are ignored by Transcrypt
window = None
document = None
# __pragma__('noskip')

# Create local references to the React and ReactDOM JavaScript libraries
React = window.React
ReactDOM = window.ReactDOM

# Remove the React and ReactDOM JavaScript libraries from the global namespace
# __pragma__('js', 'delete window.React;')
# __pragma__('js', 'delete window.ReactDOM;')

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

