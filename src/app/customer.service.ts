import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Customer } from './customer';

@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  private baseUrl= 'http://localhost:8080/customers/';
  constructor(private httpClient: HttpClient) { }

  getCustomersList(): Observable<Customer[]>{
    return this.httpClient.get<Customer[]>(`${this.baseUrl}`);
  }

  createCustomer(customer: Customer): Observable<Object>{
    return this.httpClient.post(`${this.baseUrl}`, customer);
  }
}
