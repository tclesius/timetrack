<script setup>
import { ref, defineProps, computed } from 'vue';

const {label, placeholder, required, type, inputValue, cclass} = defineProps({
  'cclass': String,
  'name': String,
  'label': String,
  'placeholder': String,
  'required': Boolean,
  'type': String,
  'inputValue': String
});

const inputId = `custom-input-${Math.random().toString(36).substring(2, 15)}`;
const inputVisibleStore = ref(type)

function toggleInputVisible() {
  console.log("hier")
  if (type === 'password') {
    if ( inputVisibleStore.value === "password" ){
      inputVisibleStore.value = "text"
    } else {
      inputVisibleStore.value = "password"
    }
  }
}
defineEmits(['update:inputValue'])
</script>

<template>
  <label :for="inputId" class="label-row" v-if="label">{{ label }}<span class="required-star" v-if="required">*</span></label>
  <div class="input-row">
    <Field :id="inputId"
           :name="name"
           :value="inputValue"
           @input="$emit('update:inputValue', $event.target.value)"
           :placeholder="placeholder"
           class="custom-input"
           :type="inputVisibleStore"
           :class="cclass"
    />
    <button style="all: unset;" @click="toggleInputVisible"><slot></slot></button>
  </div>
</template>

<style scoped>
.label-row{
  font-size: 14px;
  font-weight: bold;
}
.input-row {
  display: flex;
  width: 97%;
  align-items: center;
  border: 1px solid #000;
  padding: 5px;
  margin-top: 10px;
  margin-bottom: 10px;
  border-radius: 4px;
}

.custom-input {
  outline: none;
  border: none;
  padding: 5px;
  font-size: 16px;
  width: 100%;
}

.required-star {
  color: red;
  margin-left: 4px;
}
</style>
