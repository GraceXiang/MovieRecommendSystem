<template>
  <div  style="background-color: #303133">
    <el-card v-if="isShow" class="moviecard">
      <img src="http://www.pqdong.com/wp-content/uploads/2020/03/tip-img.png">
      <p>啊哦，您寻找的演员信息已经被删除了！</p>
    </el-card>
    <div v-if="!isShow">
      <el-card class="moviecard" style="height: 200px;">
        <img :src="person.avatar" class="avatar">
        <div class="introduce">
          <p class="title">{{person.name}}</p>
          <p><span style="font-weight: bolder">性别：</span>{{person.sex}}</p>
          <p><span style="font-weight: bolder">出生日期：</span>{{person.birth}}</p>
          <p><span style="font-weight: bolder">出生地：</span>{{person.birthPlace}}</p>
        </div>
      </el-card>
      <el-card class="moviecard">
        <div class="movieintroduce">演员简介</div>
        <div class="movieintroducet">
          <p><span style="font-weight: bolder">星座：</span>{{person.constellation}}</p>
          <p><span style="font-weight: bolder">中文别名：</span>{{person.nameZn}}</p>
          <p><span style="font-weight: bolder">英文别名：</span>{{person.nameEn}}</p>
          <p><span style="font-weight: bolder">职业：</span>{{person.profession}}</p>
        </div>
      </el-card>
      <el-card class="moviecard" v-show="person.biography">
        <div class="movieintroduce">人物事迹</div>
        <div class="moviecontent">
          <p>{{person.biography}}</p>
        </div>
      </el-card>
      <el-card class="moviecard" v-show="movie">
        <div class="movieintroduce">主演电影</div>
        <div class="newsContain">
          <div class="temp">
            <!--        @click="personDetail(item.id)-->
            <div class="newsItem" v-for="(item, key) in movie" :key="key" @click="getMovieDetail(item.movieId)">
              <div class="picContain" ontouchstart="this.classList.toggle('hover');">
                <meta name="referrer" content="no-referrer"/>
                <img :src=item.cover height="75" width="75">
              </div>
              <div>
                <p style="white-space: pre-wrap;"><span style="font-weight: bolder">名称：</span>{{item.name}}</p>
                <p style="margin-top:10px"><span style="font-weight: bolder">标签：</span>{{item.tags}}</p>
                <p style="margin-top:10px"><span style="font-weight: bolder">评分：</span>{{item.score}}</p>
              </div>
            </div>
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import fetch from '../api/fetch';

export default {
  data() {
    return {
      person: {},
      movie: {},
      isShow: false,
    };
  },
  mounted() {
    this.getPersonDetail();
    this.getPersonMovie();
  },
  computed: {
    isLogin() {
      return !!localStorage.getItem('token');
    },
  },
  methods: {
    getPersonDetail() {
      const personId = localStorage.getItem('personId');
      fetch
        .getPersonInfo(personId)
        .then((res) => {
          if (res.status === 200) {
            if (res.data.data === null) {
              this.isShow = true;
            }
            this.person = res.data.data;
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getMovieDetail(id) {
      localStorage.setItem('movieId', id);
      this.$router.push({ name: 'movieInfo' });
    },
    getPersonMovie() {
      const personName = localStorage.getItem('personName');
      fetch
        .getPersonMovie(personName)
        .then((res) => {
          if (res.status === 200) {
            if (res.data.data === null) {
              this.isShow = true;
            }
            this.movie = res.data.data;
            for(var i=0;i<this.movie.length;i++){
              if(this.movie[i].cover=="https://ydschool-video.nosdn.127.net/1585389729635Snipaste_2020-03-28_18-02-41.png"){
                this.movie[i].cover = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg";
              }
            }
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>


<style>
  * {
    box-sizing: border-box;
  }

  body {
    margin: 0;
    padding: 0;
  }

  div .moviecard {
    width: 1000px;
    margin: 20px auto auto auto;
  }

  .avatar {
    float: left;
    width: 126px;
    height: 140px;
  }

  .title {
    font-size: 21px;
  }

  .introduce {
    margin-left: 140px;
    height: 110px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .movieintroducet {
    /*margin-left: 0px;*/
    margin: 15px auto 15px auto;
    height: 110px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .movieintroducet p {
    margin: 5px;
  }

  .introduce p {
    margin: 8px;
  }

  p span {
    margin: 14px;
  }

  .movieintroduce {
    border-left: 20px solid #888;
    font-size: larger;
    font-weight: bolder;
    text-align: left;
    padding-left: 8px;
  }

  .moviecontent {
    height: 100px;
    margin: 15px auto 15px auto;
    text-align: left;
  }


  .moviebtn {
    float: right;
    margin-bottom: 20px;
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
</style>
