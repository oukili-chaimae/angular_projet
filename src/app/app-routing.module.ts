import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateCustomerComponent } from './create-customer/create-customer.component';
import { CustomerListComponent } from './customer-list/customer-list.component';

const routes: Routes = [
  {path: '', redirectTo: 'employees', pathMatch: 'full'},
  {path: 'customers', component: CustomerListComponent},
  {path: 'create-customer', component: CreateCustomerComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
