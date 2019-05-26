<template>
    <div class="side-nav">
        <ul class="menu">
            <li class="menu-element" :class="{'active': isActive(0)}">
                <a href="#" v-on:click="navHome">Accueil</a>
            </li>

            <li class="menu-element" :class="{'active': isActive(1)}">
                <a href="#" v-on:click="navAccount">Compte</a>
            </li>

            <li class="menu-element" :class="{'active': isActive(2)}">
                <a href="#" v-on:click="navProjects">Projets</a>
            </li>

            <li class="menu-element" :class="{'active': isActive(3)}">
                <a href="#" v-on:click="navSettings">Paramètres</a>
            </li>
        </ul>
    </div>
</template>

<script>
var HOME     = 0;
var ACCOUNT  = 1;
var PROJECTS = 2;
var SETTINGS = 3;

export default {
    data: function() {
        return {
            activeNav: HOME,
        }
    },

    methods: {
        navHome: function() {
            this.activeNav = HOME;
        },

        navAccount: function() {
            this.activeNav = ACCOUNT;
        },

        navProjects: function() {
            this.activeNav = PROJECTS;
        },

        navSettings: function() {
            this.activeNav = SETTINGS;
        },

        isActive: function(index) {
            return this.activeNav === index;
        }
    },

    computed: {
        
    }
}
</script>

<style lang="scss">
    $darker: #223843;
    $dark: #41436A;
    $lighter: #EFF1F3;
    $light: #DBD3D8;
    $pink: #D8B4A0;
    $terra: #D77A61;

    .side-nav {
        color: $darker;
        background-color: $lighter;
        grid-area: side;

        .menu {
            list-style: none;
            padding: 0;
            margin: 10px 0 0 0;

            .menu-element {
                padding: 0 0 0 20px;

                a {
                    display: block;
                    height: 50px;

                    text-decoration: none;
                    line-height: 50px;
                    color: $darker;

                    &:hover {
                        font-weight: 500;
                    }
                }

                &.active {
                    font-weight: 600;
                    background-color: $light;
                    border-top: 3px solid darken($light, 5);
                    border-radius: 3px 0 0 3px;
                    margin-left: 10px;
                }
            }
        }
    }
</style>
