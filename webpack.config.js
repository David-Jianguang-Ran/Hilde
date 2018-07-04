var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    mode:'development',
    context: __dirname,
    entry: './static/scripts/index', // entry point set to index.js
    output: {
        path: path.resolve('./static/bundles'),
        filename: "[name]-[hash].js"
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ],

    module: {
        rules: [
        {
            test: /\.js$/,
            exclude: /(node_modules)/,
            use: {
                loader: 'babel-loader',
                options: {
                    presets: ['react','env'],
                    babelrc: false,
                }
            }
        }
        ]
    }

}
