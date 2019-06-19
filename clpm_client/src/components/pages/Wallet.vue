<template>
    <div class="wallet">
        <div class="box">
            <h3>Portefeuille</h3><br>
            <h4>Solde : {{userData.balance}} €</h4>
            <router-link :to="{name : 'app.supply', params: {id: userData.id}}" class="button success">Ajouter des fonds</router-link><br>
            <h4>Dernières transactions :</h4>
            <table class="data-table">
                <tbody>
                    <tr v-for="transaction in userTransactions" :key="transaction.account_id">
                        <td>Transaction du : {{transaction.created_at}}</td>
                        <td style="text-align: right">Montant : {{transaction.amount}} €</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            userData: {},
            userTransactions: {},
        }
    },
    mounted() {
        let self = this;
        axios.get('api/user/details').then(function(response) {
            let userId = response.data.id;
            axios.get('api/account/' + userId + '/details').then(function(response) {
                self.userData = response.data;
            });
            axios.get('api/account/' + userId + '/transaction').then(function(response) {
                self.userTransactions = response.data;
            });
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