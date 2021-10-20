<template>
  <div class="page-sign-up">
      <div class="columns">
          <div class="column is-4 is-offset-4">
              <h1 class="title">Sign Up</h1>
              <form @submit.prevent="submitForm">
                  <div class="field">
                      <label>Fullname</label>
                      <div class="control">
                          <input type="text" class="input" v-model="fullname" />
                      </div>
                  </div>
                  <div class="field">
                      <label>Username</label>
                      <div class="control">
                          <input type="text" class="input" v-model="username" />
                      </div>
                  </div>
                  <div class="field">
                      <label>Email</label>
                      <div class="control">
                          <input type="email" class="input" v-model="email" />
                      </div>
                  </div>
                  <div class="field">
                      <label>Password</label>
                      <div class="control">
                          <input type="password" class="input" v-model="password1" />
                      </div>
                  </div>
                  <div class="field">
                      <label>Confirm Password</label>
                      <div class="control">
                          <input type="password" class="input" v-model="password2" />
                      </div>
                  </div>
                  <div class="notification is-danger" v-if="errors.length">
                      <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                  </div>
                  <div class="field">
                      <div class="control">
                          <button class="button is-black">Sign Up</button>
                      </div>
                  </div>
                  <hr>
                  Or <router-link to="/log-in">Click Here</router-link> to Log in
              </form>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name: 'SignUp',
    data() {
        return {
            fullname: '',
            username: '',
            email: '',
            password1: '',
            password2:  '',
            errors: []
        }
    },
    methods: {
        submitForm(){
            this.errors = []
            if (this.username === ""){
                this.errors.push('Username is missing')
            }
            if (this.password1 === ""){
                this.errors.push("Password Can't be Empty")
            }
            if (this.password1 !== this.password2){
                this.errors.push("Password not Match")
            }
            if (!this.errors.length){
                const formData = {
                    fullname: this.fullname,
                    username: this.username,
                    email: this.email,
                    password: this.password1
                }
                axios.post('/api/v1/users/', formData)
                .then(response => {
                    console.log(response.data);
                    toast({
                        message: 'Account Created',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                    this.$router.push('/log-in')
                })
                .catch(error => {
                    if (error.response){
                        for (const property in error.response.data){
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                        console.log(JSON.stringify(error.response.data));
                    }else if (error.message){
                        this.errors.push("Something went Wrong. Please Try again!!")
                        console.log(JSON.stringify(error))
                    }
                })
            }
        }
    },
}
</script>

<style>

</style>