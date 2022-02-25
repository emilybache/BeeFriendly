<script setup>
import NewsletterSignup from "./components/NewsletterSignup.vue";
import GardenQuizz from "./components/GardenQuizz.vue";
</script>

<template>
  <header class="container">
    <img
      alt="Bee Friendly banner"
      src="../public/assets/azalea_banner.jpg"
    />
  </header>

  <main>
    <div class="container">
      <h1 class="mt-4">Bee Friendly</h1>
      We all need more flowers and pretty insects in our lives. Use this page to assess how best to help our small furry flying friends.
    </div>
    <GardenQuizz />
    <NewsletterSignup />
  </main>
</template>

<style>
@import "../public/assets/base.css";

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding-left: 2rem;
  padding-bottom: 2rem;
  padding-right: 2rem;

  font-weight: normal;
}

header {
  line-height: 1.5;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}


</style>
