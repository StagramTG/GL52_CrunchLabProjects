<template>
    <div class="wallet">
        <div class="box">
            <h3>Portefeuille</h3>
            <div class="amount box">
                <h4>Montant restant sur le compte : {{this.userData.balance}} €</h4>
                <a href="" class="button success">Ajouter des fonds</a>
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