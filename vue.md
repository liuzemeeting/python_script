https://router.vuejs.org/zh/installation.html

一、Vue常用指令
1. v-if 条件渲染指令，根据其后表达式的bool值进行判断是否渲染该元素
2, v-show 与v-if类似，只是会渲染其身后表达式为false的元素，而且会给这样的元素添加css代码：style="display:none";
3, v-else 必须跟在v-if/v-show指令之后，不然不起作用
4. v-for 类似js的遍历，用法为 v-for="item in items" 期中items是数组
5.v-bind 这个指令用于响应地更新html特性，比如绑定某个class元素或者元素的style特性
6. v-on  用于监听指定元素的DOM事件，比如点击事件。
DOM 就是描述html节点关系的图谱
DOM提供获取元素的方法和之间关系属性以及操作元素的方法

二、双向绑定原理
vue数据双向绑定是通过数据劫持结合发布者-订阅者模式的方式来实现的
实现数据的双向绑定，首先要对数据进行劫持监听
Object.defineProperty( )设置了对象Book的name属性，对其get和set进行重写操作
，get就是在读取name属性这个值触发的函数，set就是在设置name属性这个值触发的函数

三、Vue组件实现和传值

1.父组件向子组件传递数据
在vue中，可以使用props向子组件中传递数据

2.子组件向父组件传递数据
子组件主要是通过事件传递数据给父组件

3.子组件向子组件传递数据
vue没有直接子对子传参，建议将需要传递数据的子组件，都合并成为一个组件，如果一定需要子对子传参们可以先传到父组件，再
传到子组件。vue装填管理工具vuex很方便时间组件之间的参数传递

vuex

四、Vue路由
