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

        .center {
            display: flex;
            justify-content: center;
        }

        .left {
            display: flex;
            justify-content: flex-start;
        }

        .right {
            display: flex;
            justify-content: flex-end;
        }

        .space-between {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .button {
            display: inline-block;
            height: 33px;
            padding: 0 10px 0 10px;
            border-radius: 3px;
            line-height: 33px;
            text-align: center;
            text-decoration: none;

            &.success {
                color: #00A86B;
                background-color: #EEEEEE;
                border: 1px solid #00A86B;

                &:hover {
                    color: #EEEEEE;
                    background-color:#00A86B;
                }
            }

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

        .link {
            text-decoration: none;
            color: #2d2d2d;

            &:hover {
                text-decoration: underline;
            }
        }

        .form-field {
            display: flex;
            flex-direction: column;
            margin: 0 0 20px 0;

            .label {
                margin: 0 0 5px 0;
            }

            input[type='text'], input[type='password'], input[type='email'] {
                height: 33px;
                padding: 0 10px 0 10px;

                border: none;
                border-radius: 5px;

                background-color: #EEEEEE;
                outline: none;

                &.error {
                    border: 1px solid #d64937;
                }

                &.valide {
                    border: 1px solid #00A86B;
                }
            }

            textarea {
                font-family: inherit;
                padding: 10px 10px 10px 10px;

                border: none;
                border-radius: 5px;

                background-color: #EEEEEE;
                outline: none;
                resize: vertical;
            }
        }

        .message {
            margin: 0 0 20px 0;
            padding: 10px;
            border-radius: 3px;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);

            &.danger {
                background-color: #d64937;
                color: white;
            }

            &.success {
                background-color: #00A86B;
                color: white;
            }
        }

        .invisible {
            display: none;
        }
    }
</style>
