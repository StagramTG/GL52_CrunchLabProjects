<template>
    <div class="projects">
        <div class="box">
            <div class="space-between">
                <h3>Projects</h3>
                <div>
                    <router-link to="/app/projects/create" class="button success">+ Créer</router-link> &nbsp;
                </div>
            </div>
            <p>Tous vos projets sont listés ci-dessous</p>

            <table class="data-table">
                <tbody>
                    <tr v-for="project in userProjects" :key="project.id">
                        <td>{{ project.name }}</td>
                        <td style="text-align: right">
                            <router-link :to="{ name: 'app.projects.details', params: { id: project.id } }" class="link">Détails</router-link>
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
            userProjects: {}
        }
    },

    mounted() {
        let self = this;
        axios.get('api/user/' + this.$store.state.userData.id + '/projects')
            .then(function(response) {
                self.userProjects = response.data;
            });
    },
}
</script>

<style lang="scss">
    .projects {
        padding: 20px;
        overflow-y: auto;
    }
</style>
