import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Index",
    component: ()=>import('../views/index')
  },
  {
    path: "/start",
    name: "Start",
    component: ()=>import('../views/Install1')
  }
];

const router = new VueRouter({
  routes
});

export default router;
