<template>
    <div class="sidenav">
        <ul class="menu">
            <li><router-link to="/app/home">Accueil</router-link></li>
            <li><router-link to="/app/account">Compte</router-link></li>
            <li><router-link to="/app/wallet">Portefeuille</router-link></li>
            <li><router-link to="/app/projects">Projets</router-link></li>
            <li><router-link to="/app/shop">Boutique</router-link></li>
            <div v-if="is_admin">
                <li><router-link to="/app/admin">Administration</router-link></li>
            </div>
        </ul>
    </div>
</template>

<script>
export default {
    computed: {
        is_admin() {
            return this.$store.state.userData.is_admin;
        }
    }
}
</script>

<style lang="scss">
    .sidenav {
        grid-area: sidenav;
        background-color: #2d2d2d;
        color: white;
        height: 100%;

        .menu {
            margin: 50px 0 0 0;
            list-style: none;

            a {
                display: block;
                color: white;
                text-decoration: none;


                height: 33px;
                line-height: 33px;

                &.router-link-active {
                    color: #d64937;
                }

                &:hover {
                    color: #d64937;
                }
            }
        }
    }
</style>
