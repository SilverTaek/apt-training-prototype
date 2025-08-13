import { createRouter, createWebHistory } from 'vue-router';

import LoginView from '../views/LoginView.vue';
import DashboardView from '../views/DashboardView.vue';
import UsersView from '../views/UsersView.vue';
import UserCreateView from '../views/UserCreateView.vue';
import SendersView from '../views/SendersView.vue';
import SenderCreateView from '../views/SenderCreateView.vue';
import TestEmailView from '../views/TestEmailView.vue';
import GroupsView from '../views/GroupsView.vue';
import GroupCreateView from '../views/GroupCreateView.vue';
import MailTemplatesView from '../views/MailTemplatesView.vue';
import MailTemplateCreateView from '../views/MailTemplateCreateView.vue';
import PageTemplatesView from '../views/PageTemplatesView.vue';
import PageTemplateCreateView from '../views/PageTemplateCreateView.vue';
import CampaignsView from '../views/CampaignsView.vue';
import ScenarioCreateView from '../views/ScenarioCreateView.vue';
import CampaignDetailView from '../views/CampaignDetailView.vue';

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: LoginView },
  { path: '/dashboard', component: DashboardView },
  { path: '/users', component: UsersView },
  { path: '/users/create', component: UserCreateView },
  { path: '/senders', component: SendersView },
  { path: '/senders/create', component: SenderCreateView },
  { path: '/senders/test-email', component: TestEmailView },
  { path: '/groups', component: GroupsView },
  { path: '/groups/create', component: GroupCreateView },
  { path: '/mail-templates', component: MailTemplatesView },
  { path: '/mail-templates/create', component: MailTemplateCreateView },
  { path: '/page-templates', component: PageTemplatesView },
  { path: '/page-templates/create', component: PageTemplateCreateView },
  { path: '/campaigns', component: CampaignsView },
  { path: '/campaigns/create', component: ScenarioCreateView },
  { path: '/campaigns/:id', component: CampaignDetailView }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
