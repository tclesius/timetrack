<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import RegisterView from "@/views/RegisterView.vue";
import { useDark, useToggle } from '@vueuse/core'

import MaterialSymbolsModeNight from "@/components/icons/MaterialSymbolsModeNight.vue";
import MaterialSymbolsLightMode from "@/components/icons/MaterialSymbolsLightMode.vue";
import LoginView from "@/views/LoginView.vue";

const isDark = useDark()
const toggleDark = useToggle(isDark)
const toggleDarkMode = () => {
  toggleDark();
};
</script>

<template>
  <transition name="fade" mode="out-in">
    <div style="padding: 10px; cursor: pointer; display: inline-block;">
      <MaterialSymbolsModeNight @click="toggleDarkMode" v-if="!isDark" style="width: 24px; height: 24px"/>
      <MaterialSymbolsLightMode @click="toggleDarkMode" v-else  style="width: 24px; height: 24px"/>
    </div>
  </transition>
  <RouterView />
</template>

<style scoped>
</style>
