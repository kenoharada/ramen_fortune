<template>
  <div>
    <!-- <div class="header">
      <img
        class="header__logo"
        src="/logo.png"
        alt="Ramen Fortune"
      >
    </div> -->
    <div class="app-page">
      <img
        class="app-page__background"
        src="~/static/background.jpg"
        alt="Ramen Fortune"
      >
      <div class="app-page__contents">
        <nuxt />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: 'Ramen Fortune',
    };
  },
}
</script>

<style scoped lang="scss">
.header {
  position: relative;
  width: 100%;
  height: 100px;
  background-color: rgba(1, 1, 1, 0.5);

  &::before {
    position: absolute;
    content: '';
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 10;
  }

  &__logo {

  }
}


.app-page {
  display: flex;
  justify-content: center;
  align-items: center;

  &__background {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    filter: blur(10px);
    margin: -10px;
    width: calc(100% + 20px);
    height: calc(100% + 20px);
    z-index: -1;
  }

  &__contents {
    width: 90%;
    margin: 50px auto;
    background-color: white;
  }
}
</style>
