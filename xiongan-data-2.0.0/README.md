# xiongan-data

vue 命令：

```
yarn # 自动安装环境依赖
yarn serve # 运行本地开发服务器
yarn build # 编译静态输出到 dist
yarn lint # 自动代码格式化
```

npm (yarn) 依赖：

* 包管理器: `yarn` https://yarnpkg.com/
* JS 语言： `babel` 新特性支持 `eslint` 格式化
* 前端库：`vue` https://vuejs.org/
* 数据管理：`vuex` https://vuex.vuejs.org/
* 路由：`vue-router` https://router.vuejs.org/

文件结构：(* `.gitignore` 设置不同步的)

* xiongan-data (git 根目录)
    * README.md (本文件)
    * xiongan-data (vue 项目根目录(注意区分))
        * (*) node_modules (node 库目录)
        * (*) dist (编译生成目标)
        * public/ (vue 不控制的静态文件)
        * src/ (编译源文件)
            * assets/ (会经过编译压缩的图片)
            * components/ (组件库, 存放各种可能会反复加以不同参数使用的组件)
            * router/ (vue-router 路由表)
            * store/ (vuex 数据源)
            * views/ (视图，基本等同于一级页面)
            * App.vue (主程序入口组件)
            * main.js (主程序 js 部分)

初始项目结构：

1. main.js 主程序应用 App.vue 主组件
2. App.vue 引用 vue-router 控制内部组件切换
3. About.vue / Home.vue 两个页面视图组件
4. Home.vue 组件提供参数，引用一次可复用的 HelloWorld.vue 组件

vscode settings.json:

```json
{
    "eslint.format.enable": true,
    "eslint.packageManager": "yarn",
    "eslint.validate": [
        "javascript",
        "javascriptreact",
        "vue",
        "html",
    ],
    "editor.formatOnSave": true,
    "[vue]": {
        "editor.defaultFormatter": "octref.vetur"
    },
    "vetur.trace.server": "verbose",
    "vetur.format.defaultFormatter.js": "vscode-typescript",
    "vetur.format.defaultFormatter.html": "js-beautify-html",
    "javascript.format.insertSpaceBeforeFunctionParenthesis": true,
    "vetur.useWorkspaceDependencies": true,
    "editor.codeActionsOnSave": {
        "source.fixAll.eslint": true
    }
}
```