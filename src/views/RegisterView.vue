<script setup lang="ts">
import InputComponent from "@/components/InputComponent.vue";
import MaterialSymbolsContactSupport from "@/components/icons/MaterialSymbolsContactSupport.vue";
import PhPasswordFill from "@/components/icons/PhPasswordFill.vue";
import ButtonComponent from "@/components/ButtonComponent.vue";
import {ref} from "vue";
import {useAuthStore} from "@/stores/authStore";

const { register } = useAuthStore()

const formData = ref({
  pairing_token:"",
  email:"",
  first_name:"",
  last_name:"",
  password:"",
  password_confirmation:""
})

</script>

<template>
  <h1 class="register-title">Register</h1>
  <div class="input-wrapper">
    <InputComponent
        cclass="input-field"
        label="Token:"
        placeholder="Type in your chip token"
        :required="false"
        type="email"
        v-model:input-value="formData.pairing_token"
    >
      <MaterialSymbolsContactSupport style="width: 24px; height: 24px; cursor: pointer"/>
    </InputComponent>
    <InputComponent
        cclass="input-field"
        label="Email:"
        placeholder="Type in your email address"
        :required="true"
        v-model:input-value="formData.email"
    />
    <InputComponent
        cclass="input-field"
        label="First Name:"
        placeholder="Type in your first name"
        :required="true"
        v-model:input-value="formData.first_name"
    />
    <InputComponent
        cclass="input-field"
        label="Last Name:"
        placeholder="Type in your last name"
        :required="true"
        v-model:input-value="formData.last_name"
    />
    <InputComponent
        cclass="input-field"
        label="Password:"
        placeholder="Type in your new password"
        :required="true"
        type="password"
        v-model:input-value="formData.password"
    >
      <PhPasswordFill
          style="width: 24px; height: 24px; cursor: pointer"/>
    </InputComponent>
    <InputComponent
        cclass="input-field"
        label="Password Confirmation:"
        placeholder="Type in your new password again"
        :required="true"
        type="password"
        v-model:input-value="formData.password_confirmation"
    >
      <PhPasswordFill
          style="width: 24px; height: 24px; cursor: pointer"/>
    </InputComponent>
        <div class="link-container"
             style="font-weight: bold; font-size: 15px; margin-top: 10px">
      <p>Already have an Account? <router-link to="/login">Login</router-link></p>
    </div>

    <ButtonComponent @click.native="console.log(register(formData.pairing_token, formData.email, formData.first_name, formData.last_name, formData.password, formData.password_confirmation))">
      SEND
    </ButtonComponent>
  </div>

</template>

<style scoped>
.register-title {
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
