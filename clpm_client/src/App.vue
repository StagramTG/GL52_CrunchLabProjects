<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'app',
    components: {
        
    }
}
</script>

<style lang="scss">
    html, body
    {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    #app {
        position: absolute;
        top: 0; left: 0;
        bottom: 0; right: 0;

        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;

        background-color: #EEEEEE;

        .button {
            display: inline-block;
            height: 33px;
            padding: 0 10px 0 10px;
            border-radius: 3px;
            line-height: 33px;
            text-align: center;
            text-decoration: none;

            &.primary {
                color: #2d2d2d;
                background-color: #EEEEEE;
                border: 1px solid #2d2d2d;

                &:hover {
                    color: #EEEEEE;
                    background-color:#2d2d2d;
                }
            }

            &.danger {
                color: #d64937;
                background-color: #EEEEEE;
                border: 1px solid #d64937;

                &:hover {
                    color: #EEEEEE;
                    background-color:#d64937;
                }
            }
        }
    }
</style>
