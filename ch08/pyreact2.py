# __pragma__('skip')
# These are here to quiet the Python linter and are ignored by Transcrypt
React = None
ReactDOM = None
document = None
# __pragma__('noskip')

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

