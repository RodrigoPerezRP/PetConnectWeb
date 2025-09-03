import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../../interfaces/Auth';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = `http://localhost:8000`

  constructor(private http: HttpClient){}

  getUsers(): Observable<User[]>{
    return this.http.get<User[]>(`${this.baseUrl}/api/auth/list/`)
  }

  login(user: any): Observable<any>{
    return this.http.post(`${this.baseUrl}/api/auth/login/`, user)
  }

  register(user: any): Observable<any>{
    return this.http.post(`${this.baseUrl}/api/auth/register/`, user)
  }

  // verify(token: any): Observable<any>{
    
  // }
}
