<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';

const schema = yup.object({
  email: yup.string().required().email("invalid email"),
  password: yup.string().required().min(8),
});
</script>

<template>
  <Form @submit="submit" :validation-schema="schema">
    <Field name="email" />
    <ErrorMessage name="email" />

    <Field name="password" type="password" />
    <ErrorMessage name="password" />

    
    <button>Submit</button>
  </Form>
</template>


<style scoped>

</style>