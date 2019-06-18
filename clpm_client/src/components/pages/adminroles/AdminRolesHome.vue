<template>
    <div class="admin-roles-home">
        <div class="box">
            <div class="space-between">
                <h3>Rôles</h3>
                <div>
                    <router-link to="/app/admin/roles/create" class="button success">+ Créer</router-link> &nbsp;
                    <router-link to="/app/admin" class="button primary">Retour</router-link>
                </div>
            </div>

            <table class="data-table">
                <tbody>
                    <tr v-for="role in rolesList" :key="role.id">
                        <td>{{ role.name }}</td>
                        <td style="text-align: right">
                            <a href="" class="link" @click.prevent="deleteRole(role.id)">Supprimer</a>
                        </td>
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
            rolesList: {}
        }
    },

    mounted() {
        let self = this;
        axios.get('api/project/role/list').then(function(response) {
            self.rolesList = response.data;
        });
    },

    methods: {
        deleteRole(id) {
            let self = this;
            axios.post('api/project/role/delete', { id: id })
                .then(function(response) {
                    return axios.get('api/project/role/list');
                })
                .then(function(response) {
                    self.rolesList = response.data;
                });
        }
    }
}
</script>

<style lang="scss">
    .admin-roles-home {
        padding: 20px;
        overflow-y: auto;
    }
</style>
