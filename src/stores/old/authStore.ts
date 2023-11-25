import {defineStore} from "pinia";
import {ref} from "vue";
import {DefaultService, OpenAPI} from "@/client";
import router from "@/router";

export const useAuthStore = defineStore('auth',()=>{
    const currentUser = ref("")
    const loading = ref(false)
    const message = ref("")

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    async function register(
        pairing_token: string,
        email:string,
        first_name: string,
        last_name: string,
        password: string,
        password_confirmation: string
    ){
        if (!emailRegex.test(<string>email)){
            return {message: "The provided email is invalid."}
        }
        if (pairing_token !== "" && pairing_token?.length != 8){
            return {message: "Token has wrong length please check your input."}
        }
        if (password !== password_confirmation){
            return {message: "Password and Password Confirmation dont match!"}
        }
        if (<number> password?.length < 8){
            return {message: "Password must have at least 8 characters."}
        }
        loading.value = true
        const response = await DefaultService.registerUserUserRegisterPost(email,password,first_name,last_name, pairing_token == "" ? null : pairing_token);
        //TODO check if register is successful in backend
        loading.value = false
        return response
    }
    async function login(email: string, password: string){
        if (!emailRegex.test(email)){
            return {message: "Invalid email address check your input."}
        }
        if (password === ""){
            return {message: "No Password provided."}
        }
        loading.value = true
        const loginResponse = await DefaultService.loginForAccessTokenAuthTokenPost({username: email, password: password})
        //TODO check if login successful in backend
        localStorage.setItem("access_token", loginResponse.access_token)
        OpenAPI.TOKEN = loginResponse.access_token
        const meResponse = await DefaultService.readUsersMeUserMeGet()
        currentUser.value = meResponse.first_name
        loading.value = false
        return router.push('/dashboard');
    }
    function logout(){
        currentUser.value = ""
        OpenAPI.TOKEN = ""
        localStorage.clear()
    }
    async function applyLocalStorageToken(){
        const access_token = localStorage.getItem("access_token")
        if (access_token !== null) {
            OpenAPI.TOKEN = access_token
            const meResponse = await DefaultService.readUsersMeUserMeGet()
            currentUser.value = meResponse.first_name
            return true
        }
        return false
    }

    return {login, register, currentUser, loading, applyLocalStorageToken}
})