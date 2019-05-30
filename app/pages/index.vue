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
        <i class="el-icon-caret-right" /> 診断を始める
      </el-button>
    </nuxt-link>
  </div>
</template>

<style scoped lang="scss">
.topPage {
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

.el-button {
  color: white;
  background-color: rgba(76, 175, 80, 1);

  &:hover {
    color: rgba(76, 175, 80, 1);
    background-color: rgba(76, 175, 80, 0.4);
  }
}

@media screen and (max-width: 768px) {
  .topPage {
    margin-top: calc(50vh - 30px - 50%);

    &__logo {
      width: 200px;
      height: 200px;
    }
  }
}
</style>
