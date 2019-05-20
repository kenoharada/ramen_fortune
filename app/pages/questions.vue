<template>
  <div class="questions">
    <div
      class="questions__list"
      v-for="(question, index) in questionList"
      :key="qustion"
    >
      <p v-text="question" />
      <el-radio-group v-model="answers[questionNumber(index)]">
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
      // answers: [
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      //   null,
      // ],
      answers: {
        q1: null,
        q2: null,
        q3: null,
        q4: null,
        q5: null,
        q6: null,
        q7: null,
        q8: null,
        q9: null,
        q10: null,
        q11: null,
        q12: null,
        q13: null,
        q14: null,
        q15: null,
      },
    };
  },
  methods: {
    async sendAnswers() {
      await axios.post('/api/answer', JSON.stringify(this.answers)).catch(console.error());
      this.$router.push('/results');
    },
    questionNumber(number) {
      return `q${number}`;
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
