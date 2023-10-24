<script setup lang="ts">

import ButtonComponent from "@/components/ButtonComponent.vue";
import {onBeforeUnmount, onMounted, ref} from "vue";
import {useAuthStore} from "@/stores/authStore";
import {useTimeStore} from "@/stores/timeStore";
import {storeToRefs} from "pinia";

const { currentUser, applyLocalStorageToken } = useAuthStore()
const { refreshTimer, fetchData, stampInOut } = useTimeStore()
const { data, buttonText} = storeToRefs(useTimeStore())

const timerInterval = setInterval(refreshTimer, 1000);

onMounted(()=>{applyLocalStorageToken();fetchData()})
onBeforeUnmount(() => {clearInterval(timerInterval);});
</script>

<template>
  <div class="container">
    <p class="greeting-name">Hello {{ currentUser }}</p>
    <div class="time-container">
      <p class="date">{{ data.current_date }}</p>
      <p class="session-length">{{ data.time_since_start }}</p>
    </div>
    <ButtonComponent class="button" @click.native="stampInOut">{{buttonText}}</ButtonComponent>
  </div>
</template>

<style scoped>
.container {
  text-align: center;
  font-weight: bold;
  margin: 20vh auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  max-width: 350px;
}
.date {
  font-size: 1.3em;
}

.time-container {
  margin: 0;
  padding: 0;
}

.time-container p {
  margin: 0;
  padding: 0;
}

.greeting-name, .session-length {
  font-size: 2em;
}

.button {
  margin-top: 20%;
}
</style>
