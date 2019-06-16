<template>
    <div class="account">
        <div class="header box">
            <span class="account-name">{{ userData.first_name }} {{ userData.last_name }} <small>({{ userData.username }})</small> </span><br>
            Information sur votre compte
        </div>

        <div class="details box">
            <h3>Détails du compte</h3>
            <table class="data-table">
                <tbody>
                    <tr>
                        <td width="200">Nom d'utilisateur</td>
                        <td>{{ userData.username }}</td>
                    </tr>
                    <tr>
                        <td>Email</td>
                        <td>{{ userData.email }}</td>
                    </tr>
                    <tr>
                        <td>Nom complet</td>
                        <td>{{ userData.first_name }} {{ userData.last_name }}</td>
                    </tr>
                    <tr>
                        <td>Téléphone</td>
                        <td>{{ userData.phone }}</td>
                    </tr>
                    <tr>
                        <td>Adresse</td>
                        <td>{{ userData.location }}</td>
                    </tr>
                </tbody>
            </table>

            <router-link :to="{name: 'app.account.update'}" class="button danger">Modifier</router-link>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from '../../services/api';

export default {
    data() {
        return {
            userData: {}
        }
    },
    computed: {
        username() {
            return this.$store.state.username;
        }
    },
    mounted() {
        let self = this;
        axios.get('api/user/details')
            .then(function(response) {
                self.userData = response.data;
            })
    }
}
</script>

<style lang="scss">
    .account {
        padding: 20px;
        overflow-y: auto;

        .header {
            .account-name {
                font-size: 1.5em;
            }
        }
    }
</style>
