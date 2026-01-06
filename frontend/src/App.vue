<script setup>
import Navbar from "./components/navbar.vue";
import "./styles/css/main.css"
</script>

<template>
  <Navbar/>
  <div id="app-body">
    <router-view/>
  </div>
</template>

<style scoped></style>
