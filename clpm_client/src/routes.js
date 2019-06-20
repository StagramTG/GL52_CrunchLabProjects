/* eslint-disable */

import Vue from 'vue'
import VueRouter from 'vue-router'

import store from './store/index'

import Login from '@/components/Login.vue'
import Site from '@/components/Site.vue'

import Home from '@/components/pages/Home.vue'
import Account from '@/components/pages/Account.vue'
import Wallet from '@/components/pages/Wallet.vue'

import Projects from '@/components/pages/Projects.vue'
import ProjectCreation from '@/components/pages/ProjectCreation.vue'
import ProjectDetails from '@/components/pages/ProjectDetails.vue'

import AccountUpdate from '@/components/pages/AccountUpdate.vue'

import AdminHome from '@/components/pages/AdminHome.vue'
import AdminUserList from '@/components/pages/adminusers/AdminUserList.vue'
import AdminUserCreation from '@/components/pages/adminusers/AdminUserCreation.vue'
import AdminUserModification from '@/components/pages/adminusers/AdminUserModification.vue'

import AdminRolesHome from '@/components/pages/adminroles/AdminRolesHome.vue'
import AdminRolesCreate from '@/components/pages/adminroles/AdminRolesCreate.vue'
import SupplyWallet from "./components/pages/SupplyWallet";

Vue.use(VueRouter);

const router = new VueRouter({
    routes: [{
            path: '/',
            name: 'root',
            redirect: 'app'
        },
        {
            path: '/login',
            component: Login,
            name: 'login'
        },
        {
            path: '/app',
            component: Site,
            meta: { authenticationNeeded: true },
            children: [{
                    path: '',
                    name: 'app',
                    redirect: 'home'
                },
                {
                    path: 'home',
                    component: Home,
                    name: 'app.home',
                    meta: { authenticationNeeded: true },
                },
                {
                    path: 'account',
                    component: Account,
                    name: 'app.account',
                    meta: { authenticationNeeded: true },
                },
                {
                    path: 'account/update',
                    component: AccountUpdate,
                    name: 'app.account.update',
                    meta: { authenticationNeeded: true },
                },
                {
                    path: 'wallet',
                    component: Wallet,
                    name: 'app.wallet',
                    meta: { authenticationNeeded: true },
                },
                {
                    path: 'shop',
                    component: Shop,
                    name: 'app.shop',
                    meta: { authenticationNeeded: true },
                },

                /** PROJECT ROUTES */
                {
                    path: 'supply',
                    component : SupplyWallet,
                    name: 'app.supply',
                    meta: { authenticationNeeded: true },
                },
                {
                    path: 'projects',
                    component: Projects,
                    name: 'app.projects',
                    meta: { authenticationNeeded: true },
                },
                {
                    path: 'projects/create',
                    component: ProjectCreation,
                    name: 'app.projects.create',
                    meta: { authenticationNeeded: true },
                },
                {
                    path: 'projects/:id/details',
                    component: ProjectDetails,
                    name: 'app.projects.details',
                    meta: { authenticationNeeded: true },
                },

                /** ADMINISTRATION ROUTES */
                {
                    path: 'admin',
                    component: AdminHome,
                    name: 'app.admin',
                    meta: { authenticationNeeded: true, adminOnly: true }
                },
                {
                    path: 'admin/users',
                    component: AdminUserList,
                    name: 'app.admin.users',
                    meta: { authenticationNeeded: true, adminOnly: true }
                },
                {
                    path: 'admin/users/create',
                    component: AdminUserCreation,
                    name: 'app.admin.users.create',
                    meta: { authenticationNeeded: true, adminOnly: true }
                },
                {
                    path: 'admin/roles',
                    component: AdminRolesHome,
                    name: 'app.admin.roles',
                    meta: { authenticationNeeded: true, adminOnly: true }
                },
                {
                    path: 'admin/users/modify',
                    component : AdminUserModification,
                    name: 'app.admin.users.modify',
                    meta: {authenticationNeeded: true, adminOnly: true}
                },
                {
                    path: 'admin/roles/create',
                    component: AdminRolesCreate,
                    name: 'app.admin.roles.create',
                    meta: { authenticationNeeded: true, adminOnly: true }
                }
            ]
        }
    ]
});

// A DECOMMENTER EN PROD !!!! --> Ajouter une directive pour la partie admin !!!!
/* router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.authenticationNeeded && !store.state.isAuthenticated)) {
        // You can use store variable here to access globalError or commit mutation 
        next("/Login");
    } else {
        next();
    }
}); */

export default router;