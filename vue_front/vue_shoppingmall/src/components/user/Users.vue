<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- 卡片视图区域 -->
    <el-card>

      <el-row :gutter="20">
        <el-col :span="7">
          <!-- 搜索区域 -->
          <el-input placeholder="请输入内容" v-model="input3" class="input-with-select">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
        <el-col :span="5">
          <el-button type="primary">添加用户</el-button>
        </el-col>
      </el-row>
      <!-- 用户列表区域 -->
      <el-table :data="tableData" style="width: 100%" border>
        <el-table-column type="index">
        </el-table-column>
        <el-table-column prop="id" label="用户编号" width="180">
        </el-table-column>
        <el-table-column prop="username" label="用户名" width="180">
        </el-table-column>
        <el-table-column prop="email" label="邮箱">
        </el-table-column>
        <el-table-column label="操作">
        </el-table-column>
      </el-table>

      <!-- 分页 -->
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage4"
        :page-sizes="[100, 200, 300, 400]" :page-size="100" layout="total, sizes, prev, pager, next, jumper"
        :total="400">
      </el-pagination>
    </el-card>

  </div>
</template>

<script>
export default {
  data () {
    return {
      tableData: [{
        id: '11',
        username: '王小虎',
        email: '1@qq.com'
      }, {
        id: '22',
        username: '李小虎',
        email: '2@qq.com'
      }, {
        id: '33',
        username: '小虎',
        email: '3@qq.com'
      }, {
        id: '44',
        username: '小小虎',
        email: '4@qq.com'
      }]
    }
  }
}

</script>
<style lang="less" scoped>
</style>
