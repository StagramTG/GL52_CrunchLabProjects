<template>
    <div class="project-details">
        <div class="box">
            <div class="space-between">
                <h3>Projet : {{ projectDetails.name }}</h3>
                <router-link :to="{name: 'app.projects'}" class="button primary">Retour</router-link>
            </div>

            <p>{{ projectDetails.description }}</p>
            <hr>

            <h3>Membres du projet</h3>

            <table class="data-table">
                <tbody>
                    <tr v-for="member in projectMembers" :key="member.id">
                        <td>{{ member.user_id.first_name + ' ' + member.user_id.last_name }}</td>
                        <td>{{ member.user_role.name }}</td>
                        <td class="right"><a href="">Supprimer</a></td>
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
    }
}
</script>

<style lang="scss">
    .project-details {
        padding: 20px;
        overflow-y: auto;
    }
</style>
