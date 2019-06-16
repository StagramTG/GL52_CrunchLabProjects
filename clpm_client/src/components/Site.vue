<template>
    <div class="content">
        <h1>Lol t'es connecté !</h1>
        <p>{{ received }}</p>
        <button @click="logout()">Déconnexion</button>
    </div>
</template>

<script>
/* eslint-disable */
import Cookies from 'js-cookie'
import axios from '@/services/api'

export default {
    data: function() {
        return {
            received: {}
        }
    },

    mounted: function()
    {
        axios.headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': Cookies.get('csrftoken'),
        }

        console.log(axios.headers);

        let self = this;
        axios.get('api/').then(function(response) {
            self.received = response.data;
        }).catch(function(error) { console.log(error) })
    },

    methods: {
        logout: function() {
            console.log("logout");
            let self = this;
            axios.post('auth/logout/').then(function(response) {
                self.$router.push({name: 'login'});
            }).catch(function(error) { console.log(error.data) })
        }
    }
}
</script>

<style lang="scss">

</style>
