import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { AuthService } from '../../../services/auth/auth-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  imports: [ReactiveFormsModule],
  templateUrl: './login.html',
  styles: ``
})
export class Login {

  constructor(private authService: AuthService, private router: Router){}

  formLogin = new FormGroup({
    email: new FormControl<string>(''),
    password: new FormControl<string>(''),
  })

  onLogin(){
    console.log(this.formLogin.value)
    this.authService.login(this.formLogin.value).subscribe({
      next: res => {
        if(res.access){
          localStorage.setItem('access_token', res.access)
          this.router.navigate(['/'])
        }
      }
    })
  }



}
