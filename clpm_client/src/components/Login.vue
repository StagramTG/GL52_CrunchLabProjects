<template>
    <div class="login">
        <div class="login-form">
            <p class="title">Connexion <br><small>Gestion de projet pour le Crunch Lab</small></p>

            <p v-show="loginSuccess">Connecté avec succès !</p>

            <div class="form">
                <div class="form-field">
                    <span class="label">Email</span>
                    <input type="email" name="username" placeholder="ex: example@example.fr" v-model="username" @keyup.enter="login()">
                </div>

                <div class="form-field">
                    <span class="label">Mot de passe</span>
                    <input type="password" name="password" placeholder="************" v-model="password" @keyup.enter="login()">
                </div>

                <div class="center">
                    <a href="" class="button success" @click.prevent="login()">Se connecter</a>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from '@/services/api'

export default {
    data: function() {
        return {
            username: '',
            password: '',
            loginSuccess: false
        }
    },
    methods: {
        login: function() {
            let self = this;

            axios.post('auth/login/', {
                username: this.username,
                password: this.password
            })
            .then(function(response) 
            {
                console.log(response.headers)
                self.loginSuccess = true;
                self.$store.commit('setUserData', response.data);
                self.$store.commit('setIsAuthenticated', true);
                self.$router.push({name: 'app'});
            })
            .catch(function(error) 
            { 
                console.log(error); 
            })
        }
    }
}
</script>

<style lang="scss">
    .login
    {
        padding: 100px 0 0 0;

        .login-form 
        {
            width: 50%;
            margin: auto;

            background-color: #fff;
            border-radius: 5px;
            box-shadow: rgba(0,0,0,0.1) 0px 5px 10px;
            padding: 20px;

            .title
            {
                text-align: center;
                font-size: 42px;

                margin: 20px 0;

                small 
                {
                    font-size: 35%;
                }
            }
        }
    }
</style>
