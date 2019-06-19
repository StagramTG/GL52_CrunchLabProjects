<template>
    <div class="project-creation">
        <div class="box">
            <h3>Créer un projet</h3>
            <p>Vous êtes les propriétaires des projets que vous créez.</p>

            <div class="form-field">
                <span class="label">Nom</span>
                <input type="text">
            </div>

            <div class="right">
                <router-link to="/app/projects" class="button primary">Retour</router-link> &nbsp;
                <a href="" class="button success">Enregistrer</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>


<style lang="scss">
    .project-creation {
        padding: 20px;
        overflow-y: auto;
    }
</style>
