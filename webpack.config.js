var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  mode:'development',
  watch: true,
  context: __dirname,
  entry : {
    // add name : path pairs below
    
    },
  output: {
    path: path.resolve('./static/bundles'),
    filename: "[name]-dev.gitjs"
    },
  module: {
    rules: [{
            test: /\.jsx$/,
            exclude: /(node_modules)/,
            use: {
                loader: 'babel-loader',
                options: {
                    presets: ['react'],
                    babelrc: false,
                }
            }
        }
        ]
    }

}