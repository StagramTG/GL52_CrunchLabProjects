<template>
    <div class="wallet">
        <div class="box">
            <h3>Portefeuille</h3>
            <div class="amount box">
                <h4>Solde : {{this.userData.balance}} €</h4>
                <router-link :to="{name : 'app.supply', params: {id: userData.id}}" class="button success">Ajouter des fonds</router-link>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            userData: {}
        }
    },
    mounted() {
        let self = this;
        axios.get('api/user/details').then(function(response) {
            let userId = response.data.id;
            axios.get('api/account/' + userId + '/details').then(function(response) {
                self.userData = response.data;
            })
        })
    }
}
</script>

<style lang="scss">
    .wallet {
        padding: 20px;
        overflow-y: auto;
    }
</style>