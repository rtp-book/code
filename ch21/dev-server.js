const Bundler = require('parcel-bundler');
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');


const app = express();

const apiProxy = createProxyMiddleware('/api', {
  target: 'http://localhost:8000',
  pathRewrite: {'^/api': ''}
});
app.use(apiProxy);

// parcel options
const options = {minify:false, cache: false, outDir: 'dist/dev', logLevel: 4};

const bundler = new Bundler('./index.html', options);
app.use(bundler.middleware());

bundler.on('buildEnd', () => {
  console.log('Parcel proxy server has started at: http://localhost:8080');
});

app.listen(8080);

