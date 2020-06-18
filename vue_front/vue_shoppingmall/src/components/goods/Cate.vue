<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>商品管理</el-breadcrumb-item>
      <el-breadcrumb-item>商品分类</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- 卡片视图区域 -->
    <el-card>
      <el-row>
        <el-col>
          <el-button type="primary">添加分类</el-button>
        </el-col>
      </el-row>
    </el-card>

    <!-- 表格-->
    <tree-table :data="data" :columns="columns" :selection-type="false" :expand-type="false" :show-index="true">
      <!-- 排序 -->
      <template slot="order" slot-scope="scope">
        <el-tag size="mini" v-if="scope.row.cat_level==0">一级</el-tag>
        <el-tag type="success" size="mini" v-else-if="scope.row.cat_level==1">二级</el-tag>
        <el-tag type="warning" size="mini" v-else>三级</el-tag>
      </template>
    </tree-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      data: [
        {
          name: 'Jack',
          sex: 'male',
          likes: ['football', 'basketball'],
          score: 10,
          children: [
            {
              name: 'Ashley',
              sex: 'female',
              likes: ['football', 'basketball'],
              score: 20,
              children: [
                {
                  name: 'Ashley',
                  sex: 'female',
                  likes: ['football', 'basketball'],
                  score: 20
                },
                {
                  name: 'Taki',
                  sex: 'male',
                  likes: ['football', 'basketball'],
                  score: 10,
                  children: [
                    {
                      name: 'Ashley',
                      sex: 'female',
                      likes: ['football', 'basketball'],
                      score: 20
                    },
                    {
                      name: 'Taki',
                      sex: 'male',
                      likes: ['football', 'basketball'],
                      score: 10,
                      children: [
                        {
                          name: 'Ashley',
                          sex: 'female',
                          likes: ['football', 'basketball'],
                          score: 20
                        },
                        {
                          name: 'Taki',
                          sex: 'male',
                          likes: ['football', 'basketball'],
                          score: 10
                        }
                      ]
                    }
                  ]
                }
              ]
            },
            {
              name: 'Taki',
              sex: 'male',
              likes: ['football', 'basketball'],
              score: 10
            }
          ]
        },
        {
          name: 'Tom',
          sex: 'male',
          likes: ['football', 'basketball'],
          score: 20,
          children: [
            {
              name: 'Ashley',
              sex: 'female',
              likes: ['football', 'basketball'],
              score: 20,
              children: [
                {
                  name: 'Ashley',
                  sex: 'female',
                  likes: ['football', 'basketball'],
                  score: 20
                },
                {
                  name: 'Taki',
                  sex: 'male',
                  likes: ['football', 'basketball'],
                  score: 10
                }
              ]
            },
            {
              name: 'Taki',
              sex: 'male',
              likes: ['football', 'basketball'],
              score: 10,
              children: [
                {
                  name: 'Ashley',
                  sex: 'female',
                  likes: ['football', 'basketball'],
                  score: 20
                },
                {
                  name: 'Taki',
                  sex: 'male',
                  likes: ['football', 'basketball'],
                  score: 10
                }
              ]
            }
          ]
        },
        {
          name: 'Tom',
          sex: 'male',
          likes: ['football', 'basketball'],
          score: 20
        },
        {
          name: 'Tom',
          sex: 'male',
          likes: ['football', 'basketball'],
          score: 20,
          children: [
            {
              name: 'Ashley',
              sex: 'female',
              likes: ['football', 'basketball'],
              score: 20
            },
            {
              name: 'Taki',
              sex: 'male',
              likes: ['football', 'basketball'],
              score: 10
            }
          ]
        }
      ],
      columns: [
        {
          label: 'name',
          prop: 'name',
          width: '400px'
        },
        {
          label: 'sex',
          prop: 'sex',
          minWidth: '50px'
        },
        {
          label: 'score',
          prop: 'score'
        },
        {
          label: 'likes',
          prop: 'likes',
          minWidth: '200px',
          type: 'template',
          template: 'likes'
        },
        {
          label: '排序',
          // 将当前列定义为模版列
          type: 'template',
          template: 'order'
        }
      ]
    }
  },
  created () { },
  methods: {}
}

</script>
<style lang="less" scoped>
</style>
