webpackJsonp([5],{hb18:function(t,e){},nqNz:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=i("HNM5"),s={data:function(){return{movieList:[],count:1,tags:[],isShow:!1}},mounted:function(){this.getMovie()},computed:{isLogin:function(){return!!localStorage.getItem("token")}},methods:{selectTag:function(t){this.tags.push(t),this.getMovie()},resetTag:function(){this.tags=[],this.getMovie()},prePage:function(){this.count>1&&(this.count=this.count-1),this.getMovie()},nextPage:function(){this.count=this.count+1,this.getMovie()},getContent:function(){var t=localStorage.getItem("content");return null!==t?(localStorage.removeItem("content"),t):""},getMovie:function(){var t=this;n.a.getMovieList({page:this.count,size:12,tags:this.tags,content:this.getContent()}).then(function(e){200===e.status&&0===e.data.code&&(t.movieList=e.data.data.movieList)})},getMovieDetail:function(t){localStorage.setItem("movieId",t),this.$router.push({name:"movieInfo"})}}},a={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("div",{staticClass:"divisionx"},[i("h3",[t._v("筛选电影")]),t._v(" "),i("el-button",{staticStyle:{"margin-top":"10px"},attrs:{disabled:-1!==this.tags.indexOf("动作")},on:{click:function(e){return t.selectTag("动作")}}},[t._v("动作")]),t._v(" "),i("el-button",{staticStyle:{"margin-top":"10px"},attrs:{disabled:-1!==this.tags.indexOf("科幻")},on:{click:function(e){return t.selectTag("科幻")}}},[t._v("科幻")]),t._v(" "),i("el-button",{staticStyle:{"margin-top":"10px"},attrs:{disabled:-1!==this.tags.indexOf("爱情")},on:{click:function(e){return t.selectTag("爱情")}}},[t._v("爱情")]),t._v(" "),i("el-button",{staticStyle:{"margin-top":"10px"},attrs:{disabled:-1!==this.tags.indexOf("喜剧")},on:{click:function(e){return t.selectTag("喜剧")}}},[t._v("喜剧")]),t._v(" "),i("el-button",{staticStyle:{"margin-top":"10px"},attrs:{disabled:-1!==this.tags.indexOf("惊悚")},on:{click:function(e){return t.selectTag("惊悚")}}},[t._v("惊悚")]),t._v(" "),i("el-button",{staticStyle:{"margin-top":"10px"},attrs:{disabled:-1!==this.tags.indexOf("犯罪")},on:{click:function(e){return t.selectTag("犯罪")}}},[t._v("犯罪")]),t._v(" "),i("el-button",{staticStyle:{"margin-top":"10px"},attrs:{type:"primary",plain:""},on:{click:function(e){return t.resetTag()}}},[t._v("重置")])],1),t._v(" "),i("div",{staticClass:"cardContain"},[i("div",{staticClass:"wrapper-card"},t._l(t.movieList,function(e,n){return i("div",{key:n,staticClass:"card"},[i("meta",{attrs:{name:"referrer",content:"no-referrer"}}),t._v(" "),i("img",{staticClass:"image",attrs:{src:e.cover},on:{click:function(i){return t.getMovieDetail(e.movieId)}}}),t._v(" "),i("div",[i("p",{staticStyle:{"white-space":"pre-wrap"}},[t._v(t._s(e.name)+"    ")])])])}),0)]),t._v(" "),i("div",[i("el-button",{staticClass:"editt",on:{click:function(e){return t.prePage()}}},[t._v("上一页")]),t._v(" "),i("el-button",{staticClass:"editt",attrs:{type:"primary"}},[t._v(t._s(this.count))]),t._v(" "),i("el-button",{staticClass:"editt"},[t._v(t._s(this.count+1))]),t._v(" "),i("el-button",{staticClass:"editt"},[t._v(t._s(this.count+2))]),t._v(" "),i("el-button",{staticClass:"editt",on:{click:function(e){return t.nextPage()}}},[t._v("下一页")])],1)])},staticRenderFns:[]};var o=i("VU/8")(s,a,!1,function(t){i("hb18")},null,null);e.default=o.exports}});
//# sourceMappingURL=5.ed09e563635ae7e8c254.js.map