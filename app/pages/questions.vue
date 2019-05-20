<template>
  <div class="questions">
    <div
      class="questions__list"
      v-for="(question, index) in questionList"
      :key="qustion"
    >
      <p v-text="question" />
      <el-radio-group v-model="answers[index]">
        <el-radio :label="2">はい</el-radio>
        <el-radio :label="1">どちらでもない</el-radio>
        <el-radio :label="0">いいえ</el-radio>
      </el-radio-group>
    </div>
    {{ answers }}
    <div
      class="questions__toResults"
    >
      <el-button
        type="info"
        @click="sendAnswers"
      >
        結果を見る
      </el-button>
    </div>
  </div>
</template>

<script>
import Question from '~/components/Question.vue';
import axios from 'axios';

export default {
  components: {
    Question,
  },
  data() {
    return {
      questionList: [
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
        '他人には、笑顔で接触するように心がけている。',
      ],
      answers: [
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
      ],
      // answers: {
      //   q1: 0,
      //   q2: 1,
      //   q3: 1,
      //   q4: 1,
      //   q5: 1,
      //   q6: 1,
      //   q7: 1,
      //   q8: 1,
      //   q9: 1,
      //   q10: 1,
      //   q11: 1,
      //   q12: 1,
      //   q13: 1,
      //   q14: 1,
      //   q15: 1,
      // },
    };
  },
  methods: {
    async sendAnswers() {
      await axios.post('/api/answer', JSON.stringify(this.answers)).catch(console.error());
      this.$router.push('/results');
    },
  },
};
</script>

<style lang="scss">
.questions {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
