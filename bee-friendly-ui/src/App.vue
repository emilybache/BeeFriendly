<template>
  <div id="app">
    <img alt="Bee Friendly banner" src="./assets/azalea_banner.jpg">
    <HelloWorld msg="Bee Friendly"/>
    <GardenQuizz :client-id="clientUUID"></GardenQuizz>
    <NewsletterSignup></NewsletterSignup>
    <div>
      client-id: {{ clientUUID }}
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import GardenQuizz from './components/GardenQuizz.vue'
import NewsletterSignup from "./components/NewsletterSignup";

export default {
  name: 'App',
  components: {
    NewsletterSignup,
    HelloWorld,
    GardenQuizz
  },
  data: function () {
    return {
      clientUUID: Math.round(Math.random() * 10000)
    }
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
