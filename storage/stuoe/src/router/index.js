import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: ()=>import('../views/home')
  },
  {
    path: "/start",
    name: "Start",
    component: ()=>import('../views/Install1')
  },{
    path: "*",
    name: "404",
    component: ()=>import('../views/404')
  }
];

const router = new VueRouter({
  routes
});

export default router;
