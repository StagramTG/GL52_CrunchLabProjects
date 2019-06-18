<template>
    <div class="admin-user-list">
        <div class="box">
            <div class="space-between">
                <h3>Utilisateurs</h3>
                <div>
                    <router-link to="/app/admin/users/create" class="button success">+ Créer</router-link> &nbsp;
                    <router-link to="/app/admin" class="button primary">Retour</router-link>
                </div>
            </div>

            <table class="data-table">
                <tbody>
                    <tr v-for="user in userList" :key="user.id">
                        <td>{{ user.first_name + ' ' + user.last_name + ' (' + user.username + ')' }}</td>
                        <td style="text-align: right"><router-link :to="{name : 'app.admin.users.modify', params: {id: user.id}}">Modifier</router-link></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from '@/services/api'

export default {
    data() {
        return {
            userList: []
        }
    },
    mounted() {
        // Get users list
        let self = this;
        axios.get('api/user/list').then(function(response) {
            self.userList = response.data;
        });
    }
}
</script>

<style lang="scss">
    .admin-user-list {
        padding: 20px;
        overflow-y: auto;
    }
</style>
