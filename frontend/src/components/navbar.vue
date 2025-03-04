<template>
    <v-app-bar class="main-bg px-10 d-flex main-font" app>
      <router-link
        to="/"
        class="logo logo-font cursor-pointer text-black font-weight-bold "
        style="text-decoration: none"
      >
        <span class="logo-font font-weight-bold">Journalystic.</span>
      </router-link>
  
      <v-spacer></v-spacer>
  
      <!-- <div class="d-none d-md-flex">
        <Button height="45" variant="outlined" to="/create-recipe" class="font-weight-bold rounded-lg">Create Journal</Button>
      </div>
   -->
      <v-btn icon class="d-md-none" @click="drawer = !drawer">
        <v-icon class="text-white">mdi-menu</v-icon>
      </v-btn>
  
      <v-navigation-drawer v-model="drawer" temporary right>
        <v-list>
          <v-list-item to="/projects" @click="drawer = false">
            <v-list-item-title>Projects</v-list-item-title>
          </v-list-item>
          <v-list-item to="/about" @click="drawer = false">
            <v-list-item-title>About</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-app-bar>
  </template>
    <script setup>
  import { ref } from "vue";
  
  const drawer = ref(false); 
  </script>
<style scoped>
  .logo {
    font-size: 1.9rem;
  }
  </style>