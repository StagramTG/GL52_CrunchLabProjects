<template>
    <div class="admin-user-creation">
        <div class="box">
            <h3>Créer un nouvel utilisateur</h3>

            <div class="message danger invisible" id="invalid-empty-msg">
                <span>Veuillez renseigner tous les champs.</span>
            </div>

            <div class="message danger invisible" id="invalid-mail-msg">
                <span>Veuillez saisir une adresse mail valide.</span>
            </div>

            <div class="message danger invisible" id="invalid-pwd-msg">
                <span>Veuillez deux fois le même mot de passe.</span>
            </div>

            <div class="form-field">
                <span class="label">Prénom</span>
                <input type="text" v-model="first_name" id="new-user-fn">
            </div>

            <div class="form-field">
                <span class="label">Nom</span>
                <input type="text" v-model="last_name" id="new-user-ln">
            </div>

            <div class="form-field">
                <span class="label">Email</span>
                <input type="email" v-model.lazy="email" id="new-user-email">
            </div>

            <div class="form-field">
                <span class="label">Mot de passe</span>
                <input type="password" v-model="password" id="new-user-pwd">
            </div>

            <div class="form-field">
                <span class="label">Mot de passe (confirmation)</span>
                <input type="password" v-model="password_conf" id="new-user-pwd-conf">
            </div>

            <div class="right">
                <router-link to="/app/admin/users" class="button primary">Retour</router-link> &nbsp;&nbsp;
                <a href="" class="button success" @click.prevent="create()">Créer</a>
            </div>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from '@/services/api'

export default {
    data() {
        return {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            password_conf: ''
        }
    },

    methods: {
        create() {
            let dataAreValide = true;
            // Check email validity
            if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email))) {
                document.querySelector('#invalid-mail-msg').classList.remove('invisible');
                dataAreValide = false;
            }
            else {
                document.querySelector('#invalid-mail-msg').classList.add('invisible');
            }

            if(this.password_conf != this.password || this.password === "" || this.password_conf === "") {
                document.querySelector('#invalid-pwd-msg').classList.remove('invisible');
                dataAreValide = false;
            }
            else {
                document.querySelector('#invalid-pwd-msg').classList.add('invisible');
            }

            if(this.first_name === "" || this.last_name === "")
            {
                document.querySelector('#invalid-empty-msg').classList.remove('invisible');
                dataAreValide = false;
            }
            else {
                document.querySelector('#invalid-empty-msg').classList.add('invisible');
            }

            if(dataAreValide) {
                // Perform request to create new user
                let self = this;
                axios.post('auth/register/', {
                    email: self.email,
                    first_name: self.first_name,
                    last_name: self.last_name,
                    password: self.password
                }).then(function(response) {
                    if(response.status == 200)
                    {
                        self.$router.push('/app/admin/users');
                    }
                });
            }
        }
    },

    watch: {
        email: function() {
            if(!this.email) {
                document.querySelector('#new-user-email').classList.remove('valide');
                document.querySelector('#new-user-email').classList.remove('error');
                return;
            }

            if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email))){
                document.querySelector('#new-user-email').classList.add('error');
                document.querySelector('#new-user-email').classList.remove('valide');
            }
            else {
                document.querySelector('#new-user-email').classList.remove('error');
                document.querySelector('#new-user-email').classList.add('valide');
            }
        },

        password_conf: function() {
            if(!this.password_conf) {
                document.querySelector('#new-user-pwd-conf').classList.remove('valide');
                document.querySelector('#new-user-pwd-conf').classList.remove('error');
                return;
            }

            if(this.password_conf != this.password){
                document.querySelector('#new-user-pwd-conf').classList.add('error');
                document.querySelector('#new-user-pwd-conf').classList.remove('valide');
            }
            else {
                document.querySelector('#new-user-pwd-conf').classList.remove('error');
                document.querySelector('#new-user-pwd-conf').classList.add('valide');
            }
        }
    }
}
</script>

<style lang="scss">
    .admin-user-creation {
        padding: 20px;
        overflow-y: auto;
    }
</style>
