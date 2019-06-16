export const mutations = {
    setUsername(state, username) {
        state.username = username;
    },

    clearUsername(state) {
        state.username = '';
    }
}