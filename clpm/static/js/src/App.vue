<template>
  <div id="app">
    <top-nav/>
    <side-nav/>
    <main-content/>
  </div>
</template>

<script>
import TopNav from './components/TopNav.vue'
import SideNav from './components/SideNav.vue'
import MainContent from './components/MainContent.vue'

export default {
  name: 'app',
  components: {
    TopNav,
    SideNav,
    MainContent
  }
}
</script>

<style lang="scss">
  $darker: #223843;
  $dark: #41436A;
  $lighter: #EFF1F3;
  $light: #DBD3D8;
  $pink: #D8B4A0;
  $terra: #D77A61;

  body {
      margin: 0;
      padding: 0;

      /** Global style */
      .box {
        padding: 10px;
        background-color: $lighter;
        border-radius: 3px;
        box-shadow: 0px 5px 10px 0px rgba(black, 0.1);

        h1 {
          margin: 0;
        }

        p {
          margin: 0;
        }
      }

      /** App Style */
      #app {
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

          width: 100vw;
          height: 100vh;
          overflow: hidden;
          display: grid;
          grid-template-areas: "top top" "side c";
          grid-template-rows: 50px 1fr;
          grid-template-columns: 200px 1fr;
      }
  }
</style>
