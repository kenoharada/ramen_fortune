<template>
  <div class="question">
    しつもん！
    <el-radio v-model="answer" label="2">はい</el-radio>
    <el-radio v-model="answer" label="1">どちらでもない</el-radio>
    <el-radio v-model="answer" label="0">いいえ</el-radio>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      answer: null,
    };
  },
};
</script>

<style lang="scss">
</style>
