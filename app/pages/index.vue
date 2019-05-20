<template>
  <div class="topPage">
    <logo />
    <h1　class="topPage__title">
      Ramen Fortune
    </h1>
    <h2 class="topPage__description">
      Find the ramen representing your character.
    </h2>
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
import Logo from '~/components/Logo.vue';

export default {
  components: {
    Logo
  },
  data() {
    return {
      questionList: [
        '他人には、絵以上で接触するように心がけている。',
      ],
      answerList: [],
    };
  },
  head() {
    return {
      title: 'Ramen Fortune',
    };
  },
};
</script>

<style lang="scss">
.topPage {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-family: fantasy;

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
