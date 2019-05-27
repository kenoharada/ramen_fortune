<template>
  <div class="topPage">
    <img
      class="topPage__logo"
      src="~/static/logo.png"
      alt="Ramen Fortune"
    >
    <nuxt-link
      class="topPage__link"
      to="/questions"
    >
      <el-button
        type="info"
        class="topPage__button"
      >
        <i class="el-icon-caret-right topPage__buttonIcon" /> 診断を始める
      </el-button>
    </nuxt-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      questionList: [
        '他人には、絵以上で接触するように心がけている。',
      ],
      answerList: [],
    };
  },
};
</script>

<style lang="scss">
.topPage {
  height: 90vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-family: fantasy;

  &__logo {
    width: 450px;
    height: 450px;
  }

  &__title {
    font-size: 30px;
  }

  &__description {
    font-size: 20px;
  }

  &__link {
    display: block;
    margin-top: 50px;
    font-size: 20px;
  }

  &__button {
    padding: 5px;
    width: 200px;
    height: 50px;
    font-size: 20px;
  }
}
</style>
