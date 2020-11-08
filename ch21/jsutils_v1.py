console = window.console

def fetch(url, callback):
    def check_response(response):
        if response.status != 200:
            console.error('Fetch error - Status Code: ' + response.status)
            return None
        return response.json()

    try:
        promise = window.fetch(url)
        response = promise.then(check_response)
        response.then(callback)
        promise.catch(console.error)
    except object as e:
        console.error(e)

