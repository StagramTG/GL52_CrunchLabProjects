<template>
    <div class="account-update">
        <div class="box">
            <h3>Modifier vos informations</h3>

            <div class="form-field">
                <span class="label">Nom d'utilisateur</span>
                <input type="text" v-model="username">
            </div>

            <div class="form-field">
                <span class="label">Nom</span>
                <input type="text" v-model="last_name">
            </div>

            <div class="form-field">
                <span class="label">Prénom</span>
                <input type="text" v-model="first_name">
            </div>

            <div class="form-field">
                <span class="label">Email</span>
                <input type="email" v-model="email">
            </div>

            <div class="form-field">
                <span class="label">Téléphone</span>
                <input type="email" v-model="phone">
            </div>

            <div class="form-field">
                <span class="label">Adresse</span>
                <input type="email" v-model="location">
            </div>

            <div class="right">
                <router-link to="/app/account" class="button primary">Retour</router-link> &nbsp;&nbsp;
                <a href="" class="button danger" @click.prevent="updateUserData()">Enregistrer</a>
            </div>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from '../../services/api'

export default {
    data() {
        return {
            username: '',
            last_name: '',
            first_name: '',
            email: '',
            password: '',
            phone: '',
            location: ''
        }
    },

    mounted() {
        this.username = this.$store.state.userData.username;
        this.last_name = this.$store.state.userData.last_name;
        this.first_name = this.$store.state.userData.first_name;
        this.email = this.$store.state.userData.email;
        this.phone = this.$store.state.userData.phone;
        this.location = this.$store.state.userData.location;
    },

    methods: {
        updateUserData() {
            let self = this;
            axios.post('api/user/selfupdate', {
                username: self.username,
                email: self.email,
                first_name: self.first_name,
                last_name: self.last_name,
                phone: self.phone,
                location: self.location
            })
            .then(function(response) {
                self.$router.push({name: 'app.account'});
            });
        }
    }
}
</script>

<style lang="scss">
    .account-update {
        padding: 20px;
        overflow-y: auto;

        .form-field {
            display: flex;
            flex-direction: column;
            margin: 0 0 20px 0;
        }
    }
</style>
