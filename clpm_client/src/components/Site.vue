<template>
    <div class="content">
        <Navbar/>
        <SideNav/>
        <router-view></router-view>
    </div>
</template>

<script>
import SideNav from './elements/SideNav.vue'
import Navbar from './elements/Navbar.vue'

export default {
    data: function() {
        return {
            received: {}
        }
    },
    components: {
        SideNav,
        Navbar
    },
    /*mounted() {
        let self = this;
        axios.get('api/user/details')
            .then(function(response) {
                self.$store.commit('setUserData', response.data);
                self.$router.push({name: 'app.projects'});
            })
    }*/
}
</script>

<style lang="scss">
    .content {
        height: 100%;
        display: grid;
        grid-template-areas: 
            "nav nav"
            "sidenav content";
        grid-template-columns: 200px 1fr;
        grid-template-rows: 50px 1fr;

        hr {
            border: 1px solid #EEEEEE;
        }

        .box {
            margin: 0 0 20px 0;
            background-color: #fff;
            padding: 10px;
            border-radius: 3px;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
        }

        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin: 0 0 20px 0;
            tbody {
                tr {
                    border-bottom: 1px solid #dedede;

                    &:nth-child(odd) {background-color: #EEEEEE; }

                    td {
                        padding: 5px;

                        &.right {
                            text-align: right;
                        }
                    }
                }
            }
        }
    }
</style>
