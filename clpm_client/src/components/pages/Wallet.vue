<template>
    <div class="wallet">
        <div class="box">
            <h2>Portefeuille</h2><br>
            <h3>Solde : {{new Number(userData.balance).toFixed(2)}} €</h3>
            <router-link :to="{name : 'app.supply', params: {id: userData.id}}" class="button success">Ajouter des fonds</router-link><br><br>
            <table class="data-table">
                <tbody>
                <div class="exchange">
                    <div class="transaction box" style="margin-right: 10px">
                        <h4>Dernières transactions :</h4><br>
                        <tr v-for="transaction in userTransactions" :key="transaction.account_id">
                            <td>Transaction du : {{new Date(transaction.created_at).toLocaleDateString('fr-FR', {year: 'numeric', month: 'numeric', day: 'numeric' })}}</td>
                            <td style="text-align: right">Montant : {{transaction.amount}} €</td>
                        </tr>
                    </div>
                    <div class="reload box">
                        <h4>Derniers rechargements :</h4><br>
                        <tr v-for="reload in userReloads" :key="reload.account_id">
                            <td>Transaction du : {{new Date(reload.created_at).toLocaleDateString('fr-FR', {year: 'numeric', month: 'numeric', day: 'numeric' })}}</td>
                            <td style="text-align: right">Montant : {{reload.amount}} €</td>
                        </tr>
                    </div>
                </div>
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
            userReloads: {},
        }
    },
    mounted() {
        let self = this;
        axios.get('api/user/details').then(function(response) {
            let userId = response.data.id;
            axios.get('api/account/' + userId + '/details').then(function(response) {
                self.userData = response.data;
            });
            axios.get('api/account/' + userId + '/reloadlist').then(function(response) {
                self.userReloads = response.data;
            });
            axios.get('api/account/' + userId + '/transactionlist').then(function(response) {
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
    .exchange {
        display: flex;
    }

</style>