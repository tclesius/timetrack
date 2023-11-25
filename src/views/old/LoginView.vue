<script setup lang="ts">

import InputComponent from "@/components/InputComponent.vue";
import PhPasswordFill from "@/components/icons/PhPasswordFill.vue";
import ButtonComponent from "@/components/ButtonComponent.vue";
import {useAuthStore} from "@/stores/authStore";
import {object, string} from "yup";

const {login} = useAuthStore()

const schema = object({
  email: string().required().email(),
  password: string().required().min(8),
});

</script>

<template>
  <h1 class="login-title">Login</h1>
  <div class="input-wrapper">
    <Form @submit="submit" :validation-schema="schema">
      <InputComponent
          cclass="input-field"
          label="Email:"
          placeholder="Type in your email address"
          name="email"
      />
      <InputComponent
          cclass="input-field"
          label="Password:"
          placeholder="Type in your password"
          type="password"
          name="password"
      >
        <PhPasswordFill style="width: 24px; height: 24px; cursor: pointer"/>
      </InputComponent>
      <div class="link-container" style="font-weight: bold; font-size: 15px; margin-top: 10px">
        <p>Don't have an Account?
          <router-link to="/register">Register</router-link>
        </p>
      </div>
      <ButtonComponent>
        SEND
      </ButtonComponent>
    </Form>
  </div>

</template>

<style scoped>
.login-title {
  margin-top: 10vh; /* Set the top margin to 20% of the viewport height */
  text-align: center; /* Center the title horizontally */
}

.input-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  max-width: 450px;
  margin: 0 auto;
}

.input-field {
  margin-bottom: 9px;
}

/* Ensure input fields take full width on mobile */
@media (max-width: 768px) {
  .input-wrapper {
    width: 97%;
  }
}

/* Center the button horizontally */
ButtonComponent {
  text-align: center;
}
</style>
