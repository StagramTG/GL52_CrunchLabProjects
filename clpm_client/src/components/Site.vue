<template>
    <div class="content">
        <h1>Lol t'es connecté !</h1>
        <p>{{ received }}</p>
        <button @click="logout()">Déconnexion</button>
    </div>
</template>

<script>
/* eslint-disable */
import axios from '@/services/api'

export default {
    data: function() {
        return {
            received: {}
        }
    },

    mounted: function()
    {
        let self = this;
        axios.get('api/').then(function(response) {
            self.received = response.data;
        }).catch(function(error) { console.log(error) })
    },

    methods: {
        logout: function() {
            console.log("logout");
            let self = this;
            axios.get('api-auth/logout').then(function(response) {
                self.$router.push({name: 'login'});
            }).catch(function(error) { console.log(error) })
        }
    }
}
</script>

<style lang="scss">

</style>
