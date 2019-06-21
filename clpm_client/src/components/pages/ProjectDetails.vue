<template>
    <div class="project-details">
        <div class="box">
            <div class="space-between">
                <h3>Projet : {{ projectDetails.name }}</h3>
                <router-link :to="{name: 'app.projects'}" class="button primary">Retour</router-link>
            </div>

            <p>{{ projectDetails.description }}</p>
            <hr>

            <div class="space-between">
                <h3>Membres du projet</h3>
                <router-link class="button success" :to="{name: 'app.projects.addmember'}">Ajouter un membre</router-link>
            </div>

            <table class="data-table">
                <tbody>
                    <tr v-for="(member, index) in projectMembers" :key="index">
                        <td>{{ member.user_id.first_name + ' ' + member.user_id.last_name }}</td>
                        <td>{{ member.user_role.name }}</td>
                        <td class="right"><a href="" @click.prevent="removeMember(member.user_id.id)">Supprimer</a></td>
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
            projectDetails: {},
            projectMembers: {}
        }
    },

    mounted() {
        let self = this;
        axios.get('api/project/' + self.$route.params.id + '/details')
            .then(function(response) {
                self.projectDetails = response.data;
                return axios.get('api/project/' + response.data.id + '/users');
            })
            .then(function(response) {
                self.projectMembers = response.data;
            });
    },

    methods: {
        removeMember(id) {
            let self = this;
            axios.post('api/project/deleteuser', {
                userid: id,
                projectid: self.projectDetails.id
            }).then(function(response) {
                return axios.get('api/project/' + self.projectDetails.id + '/users');
            }).then(function(response) {
                self.projectMembers = response.data;
            });
        }
    }
}
</script>

<style lang="scss">
    .project-details {
        padding: 20px;
        overflow-y: auto;
    }
</style>
