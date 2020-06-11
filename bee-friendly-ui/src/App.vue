<template>
  <div id="app">
    <img alt="Bee Friendly banner" src="./assets/azalea_banner.jpg">
    <h1 class="mt-4">Bee Friendly</h1>
    We all need more flowers and pretty insects in our lives. Use this page to assess how best to help our small furry flying friends.
    <GardenQuizz :client-id="clientUUID"></GardenQuizz>
    <NewsletterSignup :client-id="clientUUID"></NewsletterSignup>
    <div>
      client-id: {{ clientUUID }}
    </div>
  </div>
</template>

<script>
import GardenQuizz from './components/GardenQuizz.vue'
import NewsletterSignup from "./components/NewsletterSignup";

export default {
  name: 'App',
  components: {
    NewsletterSignup,
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
