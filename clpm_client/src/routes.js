import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '@/components/Login.vue'
import Site from '@/components/Site.vue'

Vue.use(VueRouter);

export const router = new VueRouter({
    routes: [
        { path: '/', component: Login, name: 'login' },
        { path: '/app', component: Site, name: 'app' }
    ]
});