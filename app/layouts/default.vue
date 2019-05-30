<template>
  <div>
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
.app-page {
  width: 100vw;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;

  &__background {
    position: fixed;
    top: 0;
    left: 0;
    filter: blur(10px);
    margin: -10px;
    width: calc(100% + 20px);
    height: calc(100% + 20px);
    z-index: -1;
  }

  &__contents {
    width: 80%;
    min-height: calc(100vh - 160px);
    margin: 80px auto;
    background-color: white;
  }
}

@media screen and (max-width: 768px) {
  .app-page {
    display: flex;
    align-items: center;
    
    &__contents {
      width: 90%;
      min-height: calc(100vh - 60px);
      margin: 30px auto;
    }
  }
}
</style>
