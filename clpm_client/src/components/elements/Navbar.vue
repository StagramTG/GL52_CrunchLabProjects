<template>
    <div class="navbar">
        <span class="brand">C L P M</span>
        <div class="user-actions">
            <span class="username">Bonjour {{ this.username }}</span>
            <a class="logout-btn" href="" @click.prevent="logout()">Déconnexion</a>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from '../../services/api'

export default {
    methods: {
        logout: function() {
            let self = this;
            axios.post('auth/logout/')
                .then(function(response) {
                    self.$store.commit('clearUserData', false);
                    self.$store.commit('setIsAuthenticated', false);
                    self.$router.push({path: '/login'});
                })
        }
    },
    computed: {
        username() {
            return this.$store.state.userData.username;
        }
    }
}
</script>

<style lang="scss">
    .navbar {
        display: flex;
        justify-content: space-between;
        grid-area: nav;
        background-color: darken(#2d2d2d, 3%);
        color: white;

        .brand {
            display: block;
            height: 50px;
            width: 200px;
            text-align: center;
            line-height: 50px;
            font-weight: 600;
        }

        .user-actions {
            display: flex;

            .logout-btn {
                font-size: 0.7em;
                display: block;
                height: 50px;
                margin: 0 20px 0 0;
                text-align: center;
                line-height: 50px;
                text-decoration: none;
                color: white;
            }

            .username {
                display: block;
                height: 50px;
                margin: 0 20px 0 0;
                text-align: center;
                line-height: 50px;
                text-decoration: none;
                color: white;
                font-weight: 400;
            }
        }
    }
</style>
