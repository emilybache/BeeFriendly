<template>
  <div id="app">
    <img alt="Bee Friendly banner" src="./assets/azalea_banner.jpg">
    <HelloWorld msg="Bee Friendly"/>
    <GardenQuizz></GardenQuizz>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import GardenQuizz from './components/GardenQuizz.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    GardenQuizz
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
