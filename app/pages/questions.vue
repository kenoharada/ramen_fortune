<template>
  <div class="questions">
    <h1　class="questions__heading">らーめん診断</h1>
    <p>よく考えてお答えください。</p>
    <div class="qustions__list">
      <div
        class="questions__item"
        v-for="(question, index) in questionList"
        :key="question.text"
      >
        <div class="questions__sentence">
          <p v-text="`${index + 1}.\t${question.text}`"/>
        </div>
        <div>
          <el-radio-group
            class="questions__radio"
            v-model="answers[index]"
          >
            <el-radio-button :label="{ score: 2, typeId: question.typeId }">
              はい
            </el-radio-button>
            <el-radio-button :label="{ score: 1, typeId: question.typeId }" class="question__radio__middle">
              どちらでもない
            </el-radio-button>
            <el-radio-button :label="{ score: 0, typeId: question.typeId }">
              いいえ
            </el-radio-button>
          </el-radio-group>
        </div>
      </div>
    </div>
    <div
      class="questions__toResults"
    >
      <el-button @click="sendAnswers" >
        結果を見る
      </el-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      questionList: [
        {
          text: '他人には、笑顔で接触するように心がけている。',
          typeId: 1,
        },
        {
          text: '感情に走らないで冷静に判断する方である。',
          typeId: 2,
        },
        {
          text: '何事も素直に受け入れて行動する。',
          typeId: 4,
        },
        {
          text: 'すぐに他人を批判する傾向にある。',
          typeId: 0,
        },
        {
          text: '他人を気にせず、勝手に振る舞ってしまうことがある。',
          typeId: 3,
        },
        {
          text: '社会の規範や規則を厳しく守る方である。',
          typeId: 0,
        },
        {
          text: '他人に対し思いやりが強い方である。',
          typeId: 1,
        },
        {
          text: '後先を考えないで、すぐに行動に移す傾向にある。',
          typeId: 3,
        },
        {
          text: '物事を進めるときは計画を立て、その計画に従って実行することが多い。',
          typeId: 2,
        },
        {
          text: '他人には気に入られたい、良く思われたいという気持ちが強い。',
          typeId: 4,
        },
        {
          text: '正しいこと、よこしまな考えなど、善悪をはっきりさせる方である。',
          typeId: 0,
        },
        {
          text: 'ボランティア活動などには積極的に参加する方である。',
          typeId: 1,
        },
        {
          text: '賛否両論を公平に聴いて結論を出すようにしている。',
          typeId: 2,
        },
        {
          text: '自分が興味を持てるものには熱中して取り組む傾向がある。',
          typeId: 3,
        },
        {
          text: '一人では何事も自信が持てない傾向がある。',
          typeId: 4,
        },
      ],
      answers: [
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
        {
          score: null,
          typeId: null,
        },
      ],
    };
  },
  computed: {
    allAnswered() {
      return this.answers.filter(item => item.score !== null).length === this.answers.length;
    },
    scoreList() {
      const scoreList = [0, 0, 0, 0, 0];
      for (let i = 0; i < 5; i ++) {
        // typeIdごとにスコアを取り出す
        let typeScoreList = this.answers.filter(answer => answer.typeId === i).map(answer => answer.score);
        typeScoreList.forEach(typeScore => scoreList[i] += typeScore);
      }
      return scoreList;
    },
  },
  methods: {
    async sendAnswers() {
      if (this.allAnswered) {
        this.$store.commit('setRawResult', this.scoreList);
        this.$router.push('/results');
      } else {
        // 全ての質問に答えていない場合
        alert('全ての質問にお答えください');
      }
    },
  },
};
</script>

<style lang="scss">
.questions {
  width: 90%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 50px;
  z-index: 1;

  &::before {
    content: '';
    width: 100vh;
    height: calc(100vh - 180px);
    position: fixed;
    top: calc(50% - 50vh + 90px);
    left: calc(50% - 50vh);
    background-image: url('/logo.png');
    background-repeat: no-repeat;
    background-size: 100%;
    z-index: 0;
    opacity: 0.1;
  }

  &__heading {
    margin: 0;
    font-size: 36px;
    font-weight: normal;
    margin-bottom: 15px;
    border-bottom: solid 4px rgba(76, 175, 80, 0.8);
    border-radius: 0px 0px 160px 180px/0px 0px 20px 4px;
  }

  &__item {
    margin: 10px auto;
    text-align: center;
    display: flex;
    justify-content: space-between;
  }

  &__sentence {
    width: 50%;
    text-align: left;
    display: flex;
    align-items: center;
    z-index: 1;
  }

  &__toResults {
    margin-top: 20px;
    z-index: 1;
  }
}

.el-button {
  color: white;
  background-color: rgba(76, 175, 80, 1);

  &:hover {
    color: rgba(76, 175, 80, 1);
    background-color: rgba(76, 175, 80, 0.4);
  }
}

.el-radio-button__inner:hover {
  color: rgba(76, 175, 80, 1);
}

.el-radio-button__orig-radio:checked+.el-radio-button__inner {
  background-color: rgba(76, 175, 80, 1);
  border-color: rgba(76, 175, 80, 1);
  box-shadow: none;
}

@media screen and (max-width: 768px) {
  .questions {
    margin: 30px auto;

    &::before {
      width: 90vw;
      height: calc(90vw - 80px);
      top: calc(50% - 45vw + 40px);
      left: calc(50% - 45vw);
    }

    &__item {
      flex-direction: column;
    }

    &__sentence {
      width: 100%;
    }

    &__radio__middle {
      width: 50%;
    }
  }

  .el-radio-button {
    display: inline;
  }
}
</style>
