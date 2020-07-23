<template>
  <div class="Echarts">
    <div class="divisionx">
      <h3>选择图表</h3>
      <el-button
        style="margin-top: 10px"
        @click="selectTag('5')"
        :disabled="this.isShow == '5'"
        >时长</el-button
      >
      <el-button
        style="margin-top: 10px"
        @click="selectTag('6')"
        :disabled="this.isShow == '6'"
        >评分</el-button
      >
      <el-button
        style="margin-top: 10px"
        @click="selectTag('7')"
        :disabled="this.isShow == '7'"
        >实时推荐</el-button
      >
    </div>
    <div id="oo" style="width: 1100px;height:400px;"></div>
  </div>
</template>

<script>
import world from "echarts/map/json/world.json";
import fetch from "../api/fetch";
import movieList from "./movieList";
export default {
  data() {
    return {
      isShow: "0",
      m_name: ["神探夏洛克", "千与千寻", "泰坦尼克号", "海上钢琴师", "寄生虫"],
      m_hot: [1, 2, 3, 4, 5]
    };
  },
  mounted() {
    this.top5();
  },
  name: "Echarts",
  methods: {
    selectTag(tag) {
      this.isShow = tag;
      if (tag == "1") {
        this.myTypes();
      } else if (tag == "2") {
        this.myLanguages();
      } else if (tag == "3") {
        this.myDistricts();
      } else if (tag == "4") {
        this.myYears();
      } else if (tag == "5") {
        this.myLengths();
      } else if (tag == "6") {
        this.myBasics();
      } else if (tag == "7") {
        this.top5();
        this.myTop5();
      }
    },
    top5() {
      console.log(1111111);
      fetch
        .top5({
          num: 5
        })
        .then(res => {
          var movieList = res.data.finalresult;
          for (var i = movieList.length - 1; i >= 0; i--) {
            this.m_name[5 - i - 1] = movieList[i].mname;
            this.m_hot[5 - i - 1] = movieList[i].hot;
          }
        });
    },
    myTop5() {
      // 基于准备好的dom，初始化echarts实例
      var myTop5 = this.$echarts.init(document.getElementById("oo"));
      myTop5.clear();
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: "实时推荐Top5电影",
          subtext: "数据来自用户点击"
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow"
          }
        },
        legend: {
          data: ["热度"]
        },
        grid: {
          top: "20%",
          left: "8%",
          right: "4%",
          bottom: "3%",
          containLabel: true
        },
        xAxis: {
          type: "value",
          boundaryGap: [0, 0.01]
        },
        yAxis: {
          type: "category",
          data: this.m_name,
          axisLabel: {
            textStyle: {
              fontSize: 18
            }
          }
        },
        series: [
          {
            name: "热度",
            type: "bar",
            data: this.m_hot
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myTop5.setOption(option);
    },
    myTypes() {
      // 基于准备好的dom，初始化echarts实例
      //var myType = this.$echarts.init(document.getElementById("oo"));
      myType.clear();
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: "电影类型统计",
          subtext: "",
          x: "center",
          padding: [20, 10, 10, 10]
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c}部 ({d}%)"
        },
        calculable: true,
        series: [
          {
            name: "电影类型统计",
            type: "pie",
            radius: "50%",
            center: ["50%", "55%"],
            data: [
              {
                name: "剧情",
                value: 2376
              },
              {
                name: "喜剧",
                value: 1245
              },
              {
                name: "惊悚",
                value: 1112
              },
              {
                name: "爱情",
                value: 1025
              },
              {
                name: "动作",
                value: 1018
              },
              {
                name: "悬疑",
                value: 693
              },
              {
                name: "犯罪",
                value: 643
              },
              {
                name: "恐怖",
                value: 609
              },
              {
                name: "科幻",
                value: 553
              },
              {
                name: "冒险",
                value: 506
              },
              {
                name: "奇幻",
                value: 419
              },
              {
                name: "家庭",
                value: 266
              },
              {
                name: "动画",
                value: 227
              },
              {
                name: "战争",
                value: 148
              },
              {
                name: "历史",
                value: 132
              },
              {
                name: "其他",
                value: 681
              }
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myType.setOption(option);
    },
    myLanguages() {
      // 基于准备好的dom，初始化echarts实例
      var myLanguage = this.$echarts.init(document.getElementById("oo"));
      myLanguage.clear();
      // 指定图表的配置项和数据
      var option = (option = {
        title: {
          text: "电影语言统计",
          subtext: "",
          x: "center",
          padding: [20, 10, 10, 10]
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c}部 ({d}%)"
        },
        calculable: true,
        series: [
          {
            name: "电影语言统计",
            type: "pie",
            radius: "50%",
            center: ["50%", "55%"],
            data: [
              {
                name: "英语",
                value: 2386
              },
              {
                name: "日语",
                value: 732
              },
              {
                name: "汉语普通话",
                value: 647
              },
              {
                name: "韩语",
                value: 532
              },
              {
                name: "粤语",
                value: 481
              },
              {
                name: "法语",
                value: 339
              },
              {
                name: "西班牙语",
                value: 183
              },
              {
                name: "德语",
                value: 182
              },
              {
                name: "意大利语",
                value: 142
              },
              {
                name: "俄语",
                value: 125
              },
              {
                name: "泰语",
                value: 70
              },
              {
                name: "拉丁语",
                value: 36
              },
              {
                name: "葡萄牙语",
                value: 33
              },
              {
                name: "阿拉伯语",
                value: 31
              },
              {
                name: "瑞典语",
                value: 28
              },
              {
                name: "其他",
                value: 629
              }
            ]
          }
        ]
      });
      // 使用刚指定的配置项和数据显示图表。
      myLanguage.setOption(option);
    },
    myDistricts() {
      // 基于准备好的dom，初始化echarts实例
      var myDistrict = this.$echarts.init(document.getElementById("oo"));
      myDistrict.clear();
      this.$echarts.registerMap("world", world);
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: "不同国家电影产量统计",
          x: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: function(params) {
            return (
              params.seriesName + "<br/>" + params.name + " : " + params.value
            );
          }
        },
        dataRange: {
          min: 0,
          max: 2000,
          text: ["", ""],
          realtime: false,
          calculable: true,
          color: ["red", "orangered", "yellow", "lightgreen", "lightskyblue"]
        },
        series: [
          {
            name: "电影产量",
            type: "map",
            mapType: "world",
            hoverable: false,
            mapLocation: {
              y: 50
            },
            data: [
              {
                name: "United States",
                value: 1891
              },
              {
                name: "China",
                value: 1162
              },
              {
                name: "Japan",
                value: 668
              },
              {
                name: "Korea",
                value: 527
              },
              {
                name: "United Kingdom",
                value: 440
              },
              {
                name: "France",
                value: 348
              },
              {
                name: "Germany",
                value: 248
              },
              {
                name: "Canada",
                value: 141
              },
              {
                name: "Italy",
                value: 101
              },
              {
                name: "Australia",
                value: 70
              },
              {
                name: "Spain",
                value: 68
              },
              {
                name: "Thailand",
                value: 56
              },
              {
                name: "Russia",
                value: 39
              },
              {
                name: "Belgium",
                value: 33
              },
              {
                name: "Sweden",
                value: 30
              },
              {
                name: "Ireland",
                value: 28
              },
              {
                name: "Czech Republic",
                value: 27
              },
              {
                name: "Denmark",
                value: 27
              },
              {
                name: "India",
                value: 26
              },
              {
                name: "Poland",
                value: 24
              },
              {
                name: "Switzerland",
                value: 20
              },
              {
                name: "New Zealand",
                value: 20
              },
              {
                name: "Austria",
                value: 19
              },
              {
                name: "Norway",
                value: 16
              },
              {
                name: "Netherlands",
                value: 15
              },
              {
                name: "Brazil",
                value: 13
              },
              {
                name: "Hungary",
                value: 13
              },
              {
                name: "Slovakia",
                value: 13
              },
              {
                name: "Mexico",
                value: 13
              },
              {
                name: "Iran",
                value: 12
              },
              {
                name: "South Africa",
                value: 12
              },
              {
                name: "Finland",
                value: 10
              },
              {
                name: "Turkey",
                value: 8
              },
              {
                name: "Romania",
                value: 8
              },
              {
                name: "Luxembourg",
                value: 7
              },
              {
                name: "Argentina",
                value: 7
              },
              {
                name: "Iceland",
                value: 7
              },
              {
                name: "Indonesia",
                value: 4
              },
              {
                name: "Israel",
                value: 4
              },
              {
                name: "United Arab Emirates",
                value: 4
              },
              {
                name: "Malaysia",
                value: 4
              },
              {
                name: "Georgia",
                value: 3
              },
              {
                name: "Cuba",
                value: 3
              },
              {
                name: "Kazakhstan",
                value: 3
              },
              {
                name: "Estonia",
                value: 3
              },
              {
                name: "Vietnam",
                value: 3
              },
              {
                name: "Greece",
                value: 3
              },
              {
                name: "Lithuania",
                value: 2
              },
              {
                name: "Chile",
                value: 2
              },
              {
                name: "Ukraine",
                value: 2
              },
              {
                name: "Portugal",
                value: 2
              },
              {
                name: "Bulgaria",
                value: 2
              },
              {
                name: "Botswana",
                value: 2
              },
              {
                name: "The Bahamas",
                value: 1
              },
              {
                name: "Uzbekistan",
                value: 1
              },
              {
                name: "Algeria",
                value: 1
              },
              {
                name: "Puerto Rico",
                value: 1
              },
              {
                name: "Philippines",
                value: 1
              },
              {
                name: "Mauritania",
                value: 1
              },
              {
                name: "Morocco",
                value: 1
              },
              {
                name: "Latvia",
                value: 1
              },
              {
                name: "Egypt",
                value: 1
              },
              {
                name: "Myanmar",
                value: 1
              },
              {
                name: "Tunisia",
                value: 1
              },
              {
                name: "Peru",
                value: 1
              },
              {
                name: "Colombia",
                value: 1
              },
              {
                name: "Tajikistan",
                value: 1
              }
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myDistrict.setOption(option);
    },
    myYears() {
      // 基于准备好的dom，初始化echarts实例
      var myYear = this.$echarts.init(document.getElementById("oo"));
      myYear.clear();
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: "历年电影产量统计",
          x: "center",
          padding: [15, 10, 10, 10]
        },
        tooltip: {
          trigger: "item",
          formatter: function(params) {
            return (
              params.seriesName +
              "<br>" +
              params.value[0] +
              "年：" +
              params.value[1] +
              "部"
            );
          }
        },
        calculable: true,
        xAxis: [
          {
            type: "value",
            min: 1915,
            max: 2020
          }
        ],
        yAxis: [
          {
            type: "value"
          }
        ],
        series: [
          {
            name: "历年电影产量",
            type: "line",
            symbol: "none",
            data: [
              [1920, 1],
              [1921, 1],
              [1922, 3],
              [1923, 2],
              [1924, 3],
              [1925, 2],
              [1926, 2],
              [1927, 1],
              [1928, 2],
              [1929, 1],
              [1931, 2],
              [1932, 5],
              [1933, 2],
              [1934, 3],
              [1935, 3],
              [1936, 2],
              [1937, 1],
              [1938, 3],
              [1939, 1],
              [1940, 3],
              [1941, 4],
              [1942, 3],
              [1943, 5],
              [1944, 3],
              [1945, 4],
              [1946, 4],
              [1947, 2],
              [1948, 6],
              [1949, 5],
              [1950, 3],
              [1951, 6],
              [1952, 8],
              [1953, 10],
              [1954, 6],
              [1955, 10],
              [1956, 6],
              [1957, 8],
              [1958, 10],
              [1959, 14],
              [1960, 9],
              [1961, 9],
              [1962, 15],
              [1963, 8],
              [1964, 13],
              [1965, 8],
              [1966, 12],
              [1967, 9],
              [1968, 12],
              [1969, 11],
              [1970, 10],
              [1971, 9],
              [1972, 9],
              [1973, 17],
              [1974, 16],
              [1975, 13],
              [1976, 12],
              [1977, 12],
              [1978, 12],
              [1979, 14],
              [1980, 16],
              [1981, 17],
              [1982, 15],
              [1983, 12],
              [1984, 24],
              [1985, 24],
              [1986, 17],
              [1987, 27],
              [1988, 33],
              [1989, 32],
              [1990, 37],
              [1991, 43],
              [1992, 44],
              [1993, 53],
              [1994, 61],
              [1995, 68],
              [1996, 50],
              [1997, 80],
              [1998, 70],
              [1999, 92],
              [2000, 75],
              [2001, 101],
              [2002, 111],
              [2003, 123],
              [2004, 159],
              [2005, 172],
              [2006, 176],
              [2007, 222],
              [2008, 193],
              [2009, 229],
              [2010, 224],
              [2011, 255],
              [2012, 268],
              [2013, 292],
              [2014, 499],
              [2015, 258]
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myYear.setOption(option);
    },
    myLengths() {
      // 基于准备好的dom，初始化echarts实例
      var myLength = this.$echarts.init(document.getElementById("oo"));
      myLength.clear();
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: "电影时长统计",
          x: "center",
          padding: [15, 10, 10, 10]
        },
        tooltip: {
          trigger: "item",
          formatter: function(params) {
            return (
              params.seriesName +
              "<br>" +
              params.value[0] +
              "分钟：" +
              params.value[1] +
              "部"
            );
          }
        },
        calculable: true,
        xAxis: [
          {
            type: "value",
            min: 0,
            max: 300
          }
        ],
        yAxis: [
          {
            type: "value"
          }
        ],
        series: [
          {
            name: "电影时长统计",
            type: "line",
            //symbol: "none",
            data: [
              [22, 2][(42, 14)],
              [68, 69],
              [84, 234],
              [94, 497],
              [104, 548],
              [116, 418],
              [127, 315],
              [141, 163],
              [162, 76],
              [188, 37],
              [223, 12],
              [242, 3],
              [267, 1],
              [297, 1]
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myLength.setOption(option);
    },
    myBasics() {
      // 基于准备好的dom，初始化echarts实例
      var myBasic = this.$echarts.init(document.getElementById("oo"));
      myBasic.clear();
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: "电影评分统计",
          x: "center",
          padding: [15, 10, 10, 10]
        },
        tooltip: {
          trigger: "item",
          formatter: function(params) {
            return (
              params.seriesName +
              "<br>" +
              params.value[0] +
              "分：" +
              params.value[1] +
              "部"
            );
          }
        },
        calculable: true,
        xAxis: [
          {
            type: "value",
            min: 2,
            max: 10
          }
        ],
        yAxis: [
          {
            type: "value"
          }
        ],
        series: [
          {
            name: "电影评分统计",
            type: "line",
            data: [
              [3.49, 29],
              [4.09, 72],
              [4.65, 101],
              [5.24, 144],
              [5.8, 149],
              [6.24, 161],
              [6.75, 242],
              [7.35, 305],
              [7.94, 414],
              [8.34, 458],
              [8.73, 233],
              [9.16, 107]
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myBasic.setOption(option);
    }
  }
  // mounted() {
  // 	this.myTypes();
  // 	this.myLanguages();
  // 	this.myDistricts();
  // 	this.myYears();
  // 	this.myLengths();
  // 	this.myBasics();
  // }
};
</script>

<style></style>
<!--myTypes(){-->
<!--		  // 基于准备好的dom，初始化echarts实例-->
<!--		  var myType = this.$echarts.init(document.getElementById('type'));-->
<!--		  // 指定图表的配置项和数据-->
<!--		  var option =-->
<!--		  // 使用刚指定的配置项和数据显示图表。-->
<!--		  myType.setOption(option);-->
<!--		  },-->
