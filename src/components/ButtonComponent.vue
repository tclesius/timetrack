<script setup>
import { defineProps, ref } from 'vue';

const { required } = defineProps({
  'required': Boolean,
});

defineEmits(['update:buttonClick'])
</script>


<template>
  <button class="custom-button">
    <slot></slot>
  </button>
</template>

<style scoped>
.custom-button {
  background-color: white;
  color: black;
  border: 1px solid #000;
  border-radius: 4px;
  padding: 10px;
  font-size: 16px;
  font-family: 'Inter', sans-serif;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.custom-button:hover {
  background-color: black !important;
  color: white
}
</style>
