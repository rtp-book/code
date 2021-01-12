console = window.console

polyfill = require("@babel/polyfill")  # required by async/await

async def fetch(url, callback):
    try:
        response = await window.fetch(url)
        if response.status != 200:
            console.error('Fetch error - Status Code: ' + response.status)
        else:
            data = await response.json()
            callback(data)
    except object as e:
        console.error(e)
