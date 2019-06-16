<template>
    <div class="login">
        <div class="login-form">
            <p class="title">Connexion <br><small>Gestion de projet pour le Crunch Lab</small></p>

            <p v-show="loginSuccess">Connecté avec succès !</p>

            <div class="form">
                <div class="form-field">
                    <span>Email</span>
                    <input type="email" name="username" placeholder="ex: example@example.fr" v-model="username">
                </div>

                <div class="form-field">
                    <span>Mot de passe</span>
                    <input type="password" name="password" placeholder="************" v-model="password">
                </div>

                <br>
                <input type="button" value="Se connecter" @click="login()">
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

            .form
            {
                display: flex;
                flex-direction: column;

                .form-field
                {
                    display: flex;
                    flex-direction: column;
                    margin: 0 0 20px 0;

                    span
                    {
                        margin: 0 0 5px 0;
                    }

                    input
                    {
                        height: 33px;
                        padding: 0 10px 0 10px;

                        border: none;
                        border-radius: 5px;

                        background-color: #EEEEEE;
                        outline: none;
                    }
                }

                input[type=button]
                {
                    display: block;
                    margin: auto;
                    width: 50%;
                    height: 33px;

                    border: none;
                    border-radius: 5px;
                    outline: none;
                    cursor: pointer;

                    background-color: #029060;
                    color: white;

                    &:hover
                    {
                        background-color: #03b65a;
                    }
                }
            }
        }
    }
</style>
