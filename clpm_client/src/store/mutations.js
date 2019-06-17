export const mutations = {
    setUserData(state, userData) {
        state.userData = userData;
    },

    clearUserData(state) {
        state.userData = {};
    },

    setIsAuthenticated(state, isAuthenticated) {
        state.isAuthenticated = isAuthenticated;
    }
}