<template>
  <div  style="background-color: #303133">
    <div class="divisionx-movielist"><span  style="font-size: 23px;font-weight: bolder;color: white">筛选电影:</span>
<!--      Tags:[['剧情'],['战争'],['动画'],['历史'],['冒险'],['奇幻'],['传记'],['歌舞'],['动作'],['科幻'],['爱情'],['喜剧'],['惊悚'],['犯罪']],-->
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('剧情')" :disabled="this.tags.indexOf('剧情')!==-1">剧情</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('战争')" :disabled="this.tags.indexOf('战争')!==-1">战争</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('动画')" :disabled="this.tags.indexOf('动画')!==-1">动画</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('历史')" :disabled="this.tags.indexOf('历史')!==-1">历史</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('冒险')" :disabled="this.tags.indexOf('冒险')!==-1">冒险</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('奇幻')" :disabled="this.tags.indexOf('奇幻')!==-1">奇幻</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('传记')" :disabled="this.tags.indexOf('传记')!==-1">传记</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('歌舞')" :disabled="this.tags.indexOf('歌舞')!==-1">歌舞</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('动作')" :disabled="this.tags.indexOf('动作')!==-1">动作</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('科幻')" :disabled="this.tags.indexOf('科幻')!==-1">科幻</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('爱情')" :disabled="this.tags.indexOf('爱情')!==-1">爱情</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('惊悚')" :disabled="this.tags.indexOf('惊悚')!==-1">惊悚</el-button>
      <el-button style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="selectTag('犯罪')" :disabled="this.tags.indexOf('犯罪')!==-1">犯罪</el-button>
      <el-button type="primary" style="margin-top: 10px;border-radius: 20px;font-weight: bolder" @click="resetTag()" plain>重置</el-button>
    </div>
    <div class="cardContain">
      <div class="wrapper-card">
        <div class="card" v-for="(item, key) in movieList" :key="key">
          <!--          引入资源防止403-->
          <meta name="referrer" content="no-referrer"/>
          <img :src="item.cover" class="image" @click="getMovieDetail(item.movieId,item.cover)">
          <div>
            <p style="white-space: pre-wrap;">{{item.name}}    </p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <el-button class="editt" @click="prePage()">上一页</el-button>
      <el-button type="primary" class="editt">{{this.count}}</el-button>
      <el-button class="editt" >{{this.count+1}}</el-button>
      <el-button class="editt" >{{this.count+2}}</el-button>
      <el-button class="editt" @click="nextPage()">下一页</el-button>
    </div>
  </div>
</template>

<script>
import fetch from '../api/fetch';

export default {
  data() {
    return {
      movieList: [],
      count: 1,
      tags: [],
      isShow: false,
    };
  },
  mounted() {
    this.getMovie();
  },
  computed: {
    isLogin() {
      return !!localStorage.getItem('token');
    },
  },
  methods: {
    selectTag(tag) {
      this.tags.push(tag);
      this.count = 1;
      this.getMovie();
    },
    resetTag() {
      this.tags = [];
      this.count = 1;
      this.getMovie();
    },
    prePage() {
      if (this.count > 1) {
        this.count = this.count - 1;
      }
      this.getMovie();
    },
    nextPage() {
      this.count = this.count + 1;
      this.getMovie();
    },
    getContent() {
      // content为从首页电影搜索栏带过来的搜索条件
      const c = localStorage.getItem('content');
      if (c !== null) {
        localStorage.removeItem('content');
        return c;
      }
      return '';
    },
    getMovie() {
        fetch.getMovieByType({
        count: this.count,
        tags: this.tags,
      }).then((res) => {
        this.movieList = JSON.parse(res.data.m_list);
      });
    },
    searchMovie() {
        const content = localStorage.getItem('content');
        console.log(content)
        fetch.searchMovie({
        count: this.count,
        tags: content,
      }).then((res) => {
        this.movieList = JSON.parse(res.data.m_list);
      });
    },
    getMovieDetail(id,cover) {
      localStorage.setItem('movieId', id);
      localStorage.setItem('cover', cover);
      this.$router.push({ name: 'movieInfo' });
    },
  },
};
</script>


<style>
  @import "../assets/Animate/animate.min.css";

  * {
    box-sizing: border-box;
  }

  body {
    background: #ededed;
    padding: 0;
    margin: 0;
  }

  .myMenu {
    position: sticky;
    top: 0;
    z-index: 100;
  }

  .indexContain {
    width: 100%;
    height: 100%;
    border: 1px solid #ededed;
    background: #fff;
  }

  .cardContain {
    width: 100%;
    height: 100%;
    background: #fff;
  }

  .newsContain {
    padding-top: 1px;
    width: 100%;
    height: 100%;
    background: #fff;
  }

  .picContain {
    margin-right: 10px;
    perspective: 1000px;
  }

  .picContain:hover .flipper, .picContain.hover .flipper {
    transform: rotateY(180deg);
  }

  .picContain, .itemPic, .back {
    width: 80px;
    height: 80px;
  }

  .flipper {
    transition: 0.6s;
    transform-style: preserve-3d;
    position: relative;
  }

  .newsItem {
    display: flex;
    justify-content: flex-start;
    width: 1200px;
    margin: auto;
    height: 114px;
    text-align: left;
    color: #5a5a5a;
    font-weight: 500;
    padding-top: 15px;
    border-bottom: 1px solid #ededed;
  }

  .itemPic, .back {
    position: absolute;
    top: 0;
    left: 0;
    backface-visibility: hidden;
    background: #cc0000;
    text-align: center;
    color: white;
    font-weight: 500;
    line-height: 80px;
    white-space: nowrap;
  }

  .itemPic {
    z-index: 2;
  }

  .back {
    transform: rotateY(180deg);
  }

  .footer {
    width: 100%;
    height: 100px;
    background: black;
    padding-top: 20px
  }

  .footer a {
    color: white;
    text-decoration: none;
  }

  .aboutus {
    width: 100%;
    height: 500px;
    background: url("https://ydschool-video.nosdn.127.net/158480509232652112_AaOXxSky.jpg") no-repeat;
    background-size: 100% 100%;
    filter: grayscale(70%);
    opacity: 0.7;
    color: white;
    font-weight: 600;
    padding-top: 60px;
  }

  .aboutus p {
    margin-top: 30px;
    font-size: 18px;
  }

  #aboutusInfo {
    margin-top: 80px;
    animation-delay: 1s
  }

  .cardBox {
    position: relative;
    width: 1200px;
    margin: 20px auto 30px auto;
    box-shadow: 0 10px 15px #888;
    border-radius: 6px;
  }

  .wrapper-card {
    width: 1200px;
    height: 1000px;
    margin: 30px auto auto auto;
    padding-top: 30px;
  }

  .wrapper-card .card {
    color: #07111B;
    font-size: 16px;
    width: 230px;
    height: 243px;
    float: left;
    margin: 30px;
    border-radius: 6px;
  }

  .wrapper-card .card:hover {
    transform: translateY(-5px);
    transition: 3ms;
    box-shadow: 5px 5px 10px #888;
  }

  .wrapper-card .image {
    border-radius: 6px 6px 0 0;
    width: 100%;
    height: 100%;
    margin-bottom: 20px;
    border-radius: 6px;
  }

  .boxImg {
    width: 100%;
    height: 100%;
    border-radius: 6px;
  }

  .divisionx-movielist {
    width: 90%;
    margin: 10px auto;
    text-align: left;
    padding-left: 10px;
    color: #5a5a5a;
  }

  .footer img {
    width: 25px;
    height: 25px;
    margin-right: 10px
  }

  .footer span {
    margin-right: 20px;
  }

  .recommandInfo p {
    margin-bottom: 6px;
  }

  .el-progress__text {
    font-size: 16px !important;
    text-align: center !important;
  }

  .el-carousel-item {
    display: flex;
    justify-content: space-around;
  }

  .el-carousel {
    width: 1200px;
    margin: 0 auto;
  }

  .mytable {
    width: 100%;
    height: 700px;
  }

  .progress2 {
    width: 182px;
    border: 0;
  }

  .editt {
    margin: 0px auto auto 0px;
  }

</style>
