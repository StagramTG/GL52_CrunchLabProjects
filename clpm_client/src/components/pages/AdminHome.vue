<template>
    <div class="admin-home">
        <div class="box">
            <h3>Administration</h3>
            <table class="data-table">
                <tbody>
                    <tr>
                        <td><router-link to="/app/admin/users" class="link">Gestion des utilisateurs</router-link></td>
                    </tr>
                    <tr>
                        <td><router-link to="/app/admin/roles" class="link">Gestion des rôles pour les projets</router-link></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style lang="scss">
    .admin-home {
        padding: 20px;
        overflow-y: auto;
    }
</style>
