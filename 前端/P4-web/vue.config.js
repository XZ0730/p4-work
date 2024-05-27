const { defineConfig } = require('@vue/cli-service')
const webpack = require("webpack")
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
		plugins: [
			// 配置 jQuery 插件的参数
			new webpack.ProvidePlugin({
				$: 'jquery',
				jQuery: 'jquery',
				'window.jQuery': 'jquery',
				Popper: ['popper.js', 'default']
			})
		]
	},
	devServer: {
		proxy: {
		'/api1': {// 匹配所有以 '/api1'开头的请求路径
		  target: 'http://127.0.0.1:5000',// 代理目标的基础路径
		  changeOrigin: true,//说谎 用于控制请求头的host值
		  pathRewrite: {'^/api': ''},
		  ws:true
		},
		'/api2': {// 匹配所有以 '/api1'开头的请求路径
			target: 'http://192.168.130.167:8081',// 代理目标的基础路径
			changeOrigin: true,//说谎 用于控制请求头的host值
			pathRewrite: {'^/api2': ''},
			ws:true
		  },

	  }
	}
})
