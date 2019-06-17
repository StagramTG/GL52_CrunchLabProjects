<template>
    <div class="account">
        <div class="header box">
            <span class="account-name">{{ first_name }} {{ last_name }} <small>({{ username }})</small> </span><br>
            Information sur votre compte
        </div>

        <div class="details box">
            <h3>Détails du compte</h3>
            <table class="data-table">
                <tbody>
                    <tr>
                        <td width="200">Nom d'utilisateur</td>
                        <td>{{ username }}</td>
                    </tr>
                    <tr>
                        <td>Email</td>
                        <td>{{ email }}</td>
                    </tr>
                    <tr>
                        <td>Nom complet</td>
                        <td>{{ first_name }} {{ last_name }}</td>
                    </tr>
                    <tr>
                        <td>Téléphone</td>
                        <td>{{ $store.state.userData.phone }}</td>
                    </tr>
                    <tr>
                        <td>Adresse</td>
                        <td>{{ userData.location }}</td>
                    </tr>
                </tbody>
            </table>

            <div class="right">
                <router-link :to="{name: 'app.account.update'}" class="button danger">Modifier</router-link>
            </div>
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
            return this.$store.state.userData.username;
        },

        first_name() {
            return this.$store.state.userData.first_name;
        },

        last_name() {
            return this.$store.state.userData.last_name;
        },

        email() {
            return this.$store.state.userData.email;
        },

        phone() {
            return this.$store.state.userData.phone;
        },

        location() {
            return this.$store.state.userData.location;
        },

        is_admin() {
            return this.$store.state.userData.is_admin;
        },
    },
    mounted() {
        let self = this;
        axios.get('api/user/details')
            .then(function(response) {
                self.$store.commit('setUserData', response.data);
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
