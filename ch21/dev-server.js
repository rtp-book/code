const { createServer } = require('http');
const { createProxyServer } = require('http-proxy');
const Path = require('path');
const Bundler = require('parcel-bundler');

const flaskServer = {
  protocol: 'http',
  host: 'localhost',
  port: 8000
};

const parcelServer = {
  protocol: 'http',
  host: 'localhost',
  port: 1234
};

// parcel options
const options = {minify:false, cache: false, outDir: 'dist/dev', logLevel: 4};

// point parcel at its entry point
const entryFiles = Path.join(__dirname, '.', 'index.html');

// init the bundler
const bundler = new Bundler(entryFiles, options);
bundler.serve();

// create a proxy server instance
const proxy = createProxyServer();

// web server
const server = createServer((req, res) => {
  if (req.url.startsWith('/api/')) {
    //strip off api prefix if going to app server
    req.url = req.url.slice('/api'.length);
    proxy.web(req, res, {
      // back-end server
      target: flaskServer,
      changeOrigin: true,
      autoRewrite: true
    }, function(e) {
      console.error("ERROR: ", e.message);
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.write('Internal Server Error');
      res.end();
    });
  } else {
    // parcel's dev server
    proxy.web(req, res, {
      target: parcelServer,
      ws: true
    });
  }
});

console.log('dev proxy server operating at: http://localhost:8080/');
server.listen(8080);

