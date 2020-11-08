import time
from pyreact import ReactGA


console = window.console

deepcopy = require('deepcopy')

polyfill = require("@babel/polyfill")  # required by async/await

async def fetch(url, callback):
    t_start = time.time()
    try:
        response = await window.fetch(url)
        if response.status != 200:
            console.error('Fetch error - Status Code: ' + response.status)
        else:
            data = await response.json()
            t_elapsed = time.time() - t_start
            ReactGA.timing({'category': 'API',
                            'variable': 'fetch',
                            'value': int(t_elapsed * 1000),
                            'label': url}
                          )
            callback(data)
    except object as e:
        console.error(e)

