<template>
    <div class="project-add-member">
        <div class="box">
            <h3>Ajouter un membre</h3>

            <div class="form-field">
                <span class="label">Utilisateur</span>
                <div style="display: flex;">
                    <input type="text" v-model="searchUserField" style="flex: 1;" @keydown.enter="searchUser()" @keydown.escape="clearSearchUser()"> &nbsp;&nbsp;
                    <button class="button primary" @click="searchUser()">Chercher</button>
                </div>
            </div>

            <select v-show="searchUserResults.length !== 0" v-model="selectedUserId">
                <option v-for="user in searchUserResults" :key="user.id" :value="user.id">
                    {{ user.first_name + ' ' + user.last_name + ' (' + user.username + ')' }}
                </option>
            </select>

            <p>Rôle du nouveau membre</p>
            <select v-model="selectedRoleId">
                <option v-for="role in roleList" :key="role.id" :value="role.id">
                    {{ role.name }}
                </option>
            </select>

            <div class="right">
                <router-link class="button primary" :to="{name: 'app.projects.details', params: {id: this.$route.params.id }}">Retour</router-link> &nbsp;&nbsp;
                <a href="" class="button success" @click.prevent="addUser()">Ajouter</a>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            searchUserField: '',
            searchUserResults: [],
            selectedUserId: -1,

            roleList: [],
            selectedRoleId: -1
        }
    },

    mounted() {
        let self = this;
        axios.get('api/project/role/list')
            .then(function(response) {
                self.roleList = response.data;
            })
    },

    methods: {
        searchUser() {
            let self = this;
            axios.get('api/user/search/' + self.searchUserField)
                .then(function(response) {
                    self.searchUserResults = response.data;
                });
        },

        clearSearchUser() {
            this.searchUserField = '';
            this.selectedUserId = -1;
            this.searchUserResults = [];
        },

        addUser() {
            let self = this;
            axios.post('api/project/adduser', {
                userid: self.selectedUserId,
                projectid: self.$route.params.id,
                roleid: self.selectedRoleId
            }).then(function(response) {
                self.$router.push({name: 'app.projects.details', params: {id: self.$route.params.id }});
            });
        }
    }
}
</script>

<style lang="scss">
    .project-add-member {
        padding: 20px;
        overflow-y: auto;
    }
</style>
